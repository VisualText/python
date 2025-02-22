# Python for NLP++

You will find python scripts that allow you to call the NLP++ engine in a variety of ways.

## Files in This Repository

1. **[nlpengine.py](https://github.com/VisualText/python/blob/main/nlpengine.py)**: the NLPEngine python class that calls nlp.exe to run NLP++ text analyzers
1. **[nlpengine-example.py](https://github.com/VisualText/python/blob/main/nlpengine-example.py)**: an example using the NLPEngine python class in nlpengine.py.
1. **[nlpplus.py](https://github.com/VisualText/python/blob/main/nlpplus.py)**: a python script that uses the native NLPPlus python package.
1. **[deaccent.py](https://github.com/VisualText/python/blob/main/deaccent.py)**: a script to deaccent a file (does not call NLP++).

## NLPPlus Python Package

Here you will find a script for using the [NLPPlus Python Package](https://github.com/VisualText/py-package-nlpengine). This is a native C++ package for Python. The Python script nlpplus.py explains how to [download](https://github.com/VisualText/py-package-nlpengine/releases/latest), install, and use the package.

- **[nlpplus.py](https://github.com/VisualText/python/blob/main/nlpplus.py)**: a python script that uses the native NLPPlus python package.

## Python Class for NLP++

This is a simple class that calls the NLP Engine as a command line executable. This is suitable for tasks that are not meant for production.

- **[nlpengine.py](https://github.com/VisualText/python/blob/main/nlpengine.py)**: the NLPEngine python class that calls nlp.exe to run NLP++ text analyzers
- **[nlpengine-example.py](https://github.com/VisualText/python/blob/main/nlpengine-example.py)**: an example using the NLPEngine python class in nlpengine.py.

If you are wanting to use python to call the NLP++ engine in production mode, please use the NLPPlus Python package in our [NLPPlus Python Package Repository](https://github.com/VisualText/py-package-nlpengine).

### NLP Engine Command Line Executable
For this python class to work, you must have the NLP Engine command line executable somewhere on your system. These are found in separate repositories for each operating system:

* [Linux NLP Executable](https://github.com/VisualText/nlp-engine-linux)
* [Windows NLP Executable](https://github.com/VisualText/nlp-engine-windows)
* [MacOS NLP Executable](https://github.com/VisualText/nlp-engine-mac)
