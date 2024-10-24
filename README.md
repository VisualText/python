# Python Class for NLP++

This is a simple class that calls the NLP Engine as a command line executable. This is suitable for tasks that are not meant for production.

If you are wanting to use python to call the NLP++ engine in production mode, please use the NLPPlus Python package in our [NLPPlus Python Package Repository](https://github.com/VisualText/py-package-nlpengine).

## NLP Engine Command Line Executable
For this python class to work, you must have the NLP Engine command line executable somewhere on your system. These are found in separate repositories for each operating system:

* [Linux NLP Executable](https://github.com/VisualText/nlp-engine-linux)
* [Windows NLP Executable](https://github.com/VisualText/nlp-engine-windows)
* [MacOS NLP Executable](https://github.com/VisualText/nlp-engine-mac)

## Files in This Repository

1. **nlpengine.py**: the NLPEngine python class that calls nlp.exe to run NLP++ text analyzers
2. **gethTMLHighlights.py**: an example of how to use the NLP Engine class running various NLP++ analyzers.
