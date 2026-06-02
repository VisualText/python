import shutil
import subprocess
import os

class NLPEngine:

    def __init__(self, engineDir, analyzersDir ):
        self.engineDir = engineDir
        self.analyzersDir = analyzersDir

    def analyzerPath(self, analyzerFolder):
        return os.path.join(self.analyzersDir, analyzerFolder)
    
    def kbPath(self, analyzerFolder):    
        return os.path.join(self.analyzerPath(analyzerFolder), "kb", "user")
    
    def specPath(self, analyzerFolder):
        return os.path.join(self.analyzerPath(analyzerFolder), "spec")
    
    def outputDir(self, analyzerFolder, textPath):    
        return os.path.join(self.analyzerPath(analyzerFolder), "input", textPath+"_log")
    
    def outputFileContents(self, analyzerFolder, filename, outputFile):
        outputPath = os.path.join(self.outputDir(analyzerFolder, filename), outputFile)
        with open(outputPath, "r") as file:
            contents = file.read()
        return contents
    
    def inputFileDir(self, analyzerFolder, textPath):    
        return os.path.join(self.analyzerPath(analyzerFolder), "input", textPath)

    def analyzeFile(self, analyzerFolder, textPath, dev=False, compiled=False):
        """Run nlp.exe over textPath using the analyzer at analyzerFolder.

        If compiled=True, passes -COMPILED so the engine loads the
        analyzer's pre-built shared libraries (bin/run.<ext> + bin/kb.<ext>)
        instead of running interpreted from the .nlp source. Build
        those libraries first via compileAnalyzer() / compileLocal() or
        by running the platform's scripts/compile-analyzer.{sh,ps1}
        directly.
        """
        self.clearLogFiles(analyzerFolder)
        analyzerPath = os.path.join(self.analyzersDir, analyzerFolder)
        textPath = os.path.join(analyzerPath, "input", textPath)
        try:
            executable_path = os.path.join(self.engineDir, "nlp.exe")
            args = [executable_path, "-ANA", analyzerPath, "-WORK", self.engineDir, textPath]
            if dev:
                args.append("-DEV")
            if compiled:
                args.append("-COMPILED")

            with open("output.txt", "w") as output_file, open("errors.txt", "w") as error_file:
                subprocess.run(args, stdout=output_file, stderr=error_file, text=True)

        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            return

    def compileAnalyzer(self, analyzerFolder, inputTextPath=None, kbOnly=False):
        """Generate the C++ source trees for the named analyzer.

        Runs nlp.exe in -COMPILE mode (or -COMPILEKB if kbOnly=True),
        which emits <analyzer>/run/*.cpp + <analyzer>/kb/*.cpp (or just
        <analyzer>/kb/*.cpp for KB-only). The resulting trees still
        need to be built into shared libraries before analyzeFile
        with compiled=True will work — use compileLocal() to drive the
        local cmake build via scripts/compile-analyzer.sh.

        inputTextPath: any input text file path; -COMPILE requires one
        but doesn't actually analyze the text. If None, defaults to the
        analyzer's input/ directory's first text file (if any).
        """
        analyzerPath = os.path.join(self.analyzersDir, analyzerFolder)
        if inputTextPath is None:
            inputDir = os.path.join(analyzerPath, "input")
            if os.path.isdir(inputDir):
                for entry in sorted(os.listdir(inputDir)):
                    candidate = os.path.join(inputDir, entry)
                    if os.path.isfile(candidate):
                        inputTextPath = candidate
                        break
        if inputTextPath is None or not os.path.isfile(inputTextPath):
            raise FileNotFoundError(
                "compileAnalyzer needs an input text file path "
                "(none provided and analyzer's input/ has no files)"
            )
        try:
            executable_path = os.path.join(self.engineDir, "nlp.exe")
            flag = "-COMPILEKB" if kbOnly else "-COMPILE"
            args = [executable_path, flag, "-ANA", analyzerPath,
                    "-WORK", self.engineDir, inputTextPath]
            subprocess.run(args, check=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"compileAnalyzer failed: {e}")
            raise
        return analyzerPath

    def compileLocal(self, analyzerFolder, inputTextPath, kbOnly=False,
                     ubuntu="ubuntu-latest"):
        """Run scripts/compile-analyzer.sh to build the analyzer's
        compiled shared libraries locally via cmake.

        Calls into the shell script in the engine repo's scripts/ dir,
        which runs nlp.exe -COMPILE first then drives cmake against the
        engine's bundled compile-libs. On success, drops
        <analyzer>/bin/run.so + bin/runu.so + bin/kb.so + bin/kbu.so
        (or just bin/kb.so + bin/kbu.so for kbOnly).

        After this returns, analyzeFile(..., compiled=True) will load
        the staged libraries.
        """
        analyzerPath = os.path.join(self.analyzersDir, analyzerFolder)
        script = os.path.join(self.engineDir, "scripts", "compile-analyzer.sh")
        if not os.path.isfile(script):
            raise FileNotFoundError(
                f"compile-analyzer.sh not found at {script}"
            )
        args = ["bash", script]
        if kbOnly:
            args.append("--kb-only")
        args.extend([analyzerPath, inputTextPath, ubuntu])
        subprocess.run(args, check=True, text=True)
        return os.path.join(analyzerPath, "bin")
    
    def analyzeStr(self, analyzerFolder, filename, textStr):
        inputPath = self.inputFileDir(analyzerFolder,filename)
        with open(inputPath, "w") as input_file:
            input_file.write(textStr)
        self.analyzeFile(analyzerFolder, filename, False)
        
    def isAnalyzerFolder(self, analyzerFolder):
        required_folders = ['spec', 'input', 'kb/user']
        for folder in required_folders:
            if not os.path.isdir(os.path.join(self.analyzersDir, analyzerFolder, folder)):
                return False
        return True
    
    def clearLogFiles(self, analyzerFolder):
        logPath = os.path.join(os.path.join(self.analyzersDir,analyzerFolder), "input")
        for root, dirs, files in os.walk(logPath):
            for dir in dirs:
                if dir.endswith("_log"):
                    shutil.rmtree(os.path.join(root, dir))

    def createInputDir(self, analyzer, inputFolder, clearFolder=True):
        inputPath = os.path.join(self.analyzerPath(analyzer), "input", inputFolder)
        if clearFolder and os.path.exists(inputPath):
            shutil.rmtree(inputPath)
            shutil.os.makedirs(inputPath)
        if not os.path.exists(inputPath):
            os.makedirs(inputPath)
        return inputPath