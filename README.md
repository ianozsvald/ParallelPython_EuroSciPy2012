ParallelPython_EuroSciPy2012
============================

Starting code &amp; solutions for EuroSciPy Paralllel Python 2 hour tutorial
http://www.euroscipy.org/talk/6612

I'm using CPython ('normal' python) 2.7. We'll use:
* multiprocessing
* parallelpython
* picloud
* gearman
* ipython cluster
* PIL (Python Imaging Library) - optional but used for visualisation of Mandelbrot set

multiprocessing
---------------
The multiprocessing module is built into CPython.

```>>> import multiprocessing

parallelpython
--------------

Parallel Python 1.6.2 via: http://www.parallelpython.com/ and test the Python bindings using:

```>>> import pp
```>>> pp.version
```'1.6.1' # the latest version is 1.6.1

Recent version of gearman 2.x, I'm using
gearman 0.14-1 # on ubuntu 11.04
with Python bindings
>>> import gearman
>>> gearman.__version__
'2.0.2'
and at the command line test:
terminal1$ gearman -w -f test wc # will run this worker forever
terminal2$ gearman -f test "Hello World" # posts a 'test' job which returns
      0       2      11 # this is the wc (word-count) output for the test string
now you can close these two terminals - this has tested that gearman is running ok




picloud:
>>> import cloud
>>> cloud.__version__
>>> '2.5.5'

For picloud I have made an account but you ought to make your own:
u:ianozsvald+euroscipy2012@gmail.com
p:euroscipy2012
Note that there's a limit of 20 computer hours for free per month (and there's no Credit Card on file!), we're unlikely to run out in the class but it makes sense to register for a free account. Setup notes:
http://docs.picloud.com/quickstart.html
If you use my login then just use the existing 4569 API key (it won't matter if we have redundant keys in this test account).

IPython with cluster support:
$ ipython
Python 2.7.3 (default, Apr 20 2012, 22:39:59) 
Type "copyright", "credits" or "license" for more information.
IPython 0.13 -- An enhanced Interactive Python.

$ ipcluster
-> shows help message
