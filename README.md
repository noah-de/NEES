# NEES
taking the [Konno/Omachi Smoothing implemenation](http://www.eq.db.shibaura-it.ac.jp/papers/Konno&Ohmachi1998.pdf) by https://github.com/arkottke/ and implement it for processing in the [EEG Data Portal](http://nees.ucsb.edu/data-portal)

Referring to [other Konno/Omachi implementations](https://github.com/jsh9/fast-konno-ohmachi) may be helpful.

Check syntax with **pycodestyle** and debug with either **spyder** or **pudb** (python -m pudb.run utils.py)

This project was built using [Anaconda distribution of Python](https://www.anaconda.com/download/).

To set up a similar environment you can start a new 2.7 envrionment:
 - `conda create -n py27 python=2.7 ipykernel`
 - `conda env create -f environment.yml` from the code directory
