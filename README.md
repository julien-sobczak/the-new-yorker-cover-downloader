The New Yorker Cover Exporter
=============================

Simple program to download covers from the famous The New Yorker magazine and create a PDF version.

Installation
------------

```
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```

To create PDF from cover images, you need to install [InstallMagick](http://www.imagemagick.org):

```
# apt-get update
# apt-get install imagemagick
```


Running
-------

```
$ mkdir downloads
$ python download.py
```

In the current version, no option could be specified on the command line. To restrict the date range, edit the program file and update the variables in the `main` method.

TODO Add command line options `--from`, `--until`.


To create a PDF, use the following command:

```
$ convert cover-192[56789]-*.jpg ../The_New_Yorker-Covers-1925-1930.pdf
```

This command merges all covers from 1925 (inclusive) to 1930 (exclusive) into a single PDF file (around 100 MB). 
