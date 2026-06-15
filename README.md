# Python for NLP++

You will find python scripts that allow you to call the NLP++ engine in a variety of ways.

## Files in This Repository

1. **[nlpengine.py](https://github.com/VisualText/python/blob/main/nlpengine.py)**: the NLPEngine python class that calls nlp.exe to run NLP++ text analyzers
1. **[nlpengine-example.py](https://github.com/VisualText/python/blob/main/nlpengine-example.py)**: an example using the NLPEngine python class in nlpengine.py.
1. **[nlpplus.py](https://github.com/VisualText/python/blob/main/nlpplus.py)**: a python script that uses the native NLPPlus python package.
1. **[deaccent.py](https://github.com/VisualText/python/blob/main/deaccent.py)**: a script to deaccent a file (does not call NLP++).

## Python Class for NLP++

This is a simple class that calls the NLP Engine as a command line executable. This is suitable for tasks that are not meant for production.

- **[nlpengine.py](https://github.com/VisualText/python/blob/main/nlpengine.py)**: the NLPEngine python class that calls nlp.exe to run NLP++ text analyzers
- **[nlpengine-example.py](https://github.com/VisualText/python/blob/main/nlpengine-example.py)**: an example using the NLPEngine python class in nlpengine.py.

### NLP Engine Command Line Executable
For this python class to work, you must have the NLP Engine command line executable somewhere on your system. These are found in separate repositories for each operating system:

* [Linux NLP Executable](https://github.com/VisualText/nlp-engine-linux)
* [Windows NLP Executable](https://github.com/VisualText/nlp-engine-windows)
* [MacOS NLP Executable](https://github.com/VisualText/nlp-engine-mac)

### API

#### `analyzeFile(analyzerFolder, textPath, dev=False, compiled=False)`

Run the named analyzer over the input text. When `compiled=True`,
passes `-COMPILED` to `nlp.exe` so the engine loads the analyzer's
pre-built `bin/run.<ext>` + `bin/kb.<ext>` shared libraries instead
of running interpreted from the `.nlp` source. Build those libraries
first via `compileLocal()` or by running the platform's
`scripts/compile-analyzer.{sh,ps1}` directly.

#### `compileAnalyzer(analyzerFolder, inputTextPath=None, kbOnly=False, analyzerOnly=False)`

Shell out to `nlp.exe -COMPILE` (or `-COMPILEKB` if `kbOnly=True`, or
`-COMPILEANA` if `analyzerOnly=True`) to generate the analyzer's C++
source trees: `-COMPILE` emits both `<analyzer>/run/*.cpp` and
`<analyzer>/kb/*.cpp`; `-COMPILEKB` emits just `kb/*.cpp`; `-COMPILEANA`
emits just `run/*.cpp`. The trees still need to be built into shared
libraries before `analyzeFile(..., compiled=True)` will work — see
`compileLocal()`.

Use `analyzerOnly=True` when only the rules changed and the KB is
already compiled. `kbOnly` and `analyzerOnly` are mutually exclusive.

If `inputTextPath` is `None`, the function picks the first text file
it finds under the analyzer's `input/` directory. The engine
requires an input file at compile time but doesn't actually analyze
it for `-COMPILE`.

#### `compileLocal(analyzerFolder, inputTextPath, kbOnly=False, analyzerOnly=False, ubuntu="ubuntu-latest")`

Drive the platform's `scripts/compile-analyzer.{sh,ps1}` to do the
full local build end-to-end: `-COMPILE` step, cmake configure +
build, and stage the resulting library into `<analyzer>/bin/` under
every name the engine's load paths look for (`run.<ext>` /
`runu.<ext>` / `kb.<ext>` / `kbu.<ext>`, or just `kb.<ext>` /
`kbu.<ext>` for `kbOnly`, or just `run.<ext>` / `runu.<ext>` for
`analyzerOnly`).

After `compileLocal()` returns, `analyzeFile(..., compiled=True)`
will load the staged libraries instead of running interpreted.

The `ubuntu` argument is ignored on Windows and macOS; on Linux it
selects which set of bundled `nlp.exe` + `compile-libs/<ubuntu>` to
use (the Linux distribution ships multiple Ubuntu variants).

## NLPPlus Python Package Now Released

The NLPPlus Python Package is released and can be found at https://pypi.org/project/NLPPlus/, or you can install it via pip:

```python
pip install NLPPlus
```


Here you will find a script for using the [NLPPlus Python Package](https://github.com/VisualText/py-package-nlpengine). This is a native C++ package for Python. The Python script nlpplus.py explains how to [download](https://github.com/VisualText/py-package-nlpengine/releases/latest), install, and use the package.

- **[nlpplus.py](https://github.com/VisualText/python/blob/main/nlpplus.py)**: a python script that uses the native NLPPlus python package.
