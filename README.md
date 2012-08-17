ParallelPython_EuroSciPy2012
============================

Starting code &amp; solutions for EuroSciPy Paralllel Python 2 hour tutorial
http://www.euroscipy.org/talk/6612

If you run into difficulties installing these prerequisites then get in contact with me (ian AT ianozsvald COM) and I'll try to help. I can't offer support (except in the moral sense) with Windows & Mac, I'm an Ubuntu user. If you have trouble I strongly suggest you use VirtualBox to setup a virtual Ubuntu 12.04 (or 11.04 like mine) environment. I'll attempt to bring a VirtualBox environment on a USB stick but it'll be over 5GB and hard to transfer before the class.

You are responsible for having a working environment in time for the class, we won't be installing anything once the class starts.

If you don't have a working environment then you can buddy-up with someone else.

NOTE in the class we'll start with ````serial_python.py```` and ````multiproce.py```` and adapt the code to cover the following tools. I've included a ````solutions\```` directory but don't go peeking - that's only in case we run out of time or you need to catch-up.

I'm using CPython 2.7 ('normal' python). We'll use:
* multiprocessing
* parallelpython
* picloud
* gearman
* ipython cluster
* PIL (Python Imaging Library) - optional but used for visualisation of Mandelbrot set

multiprocessing
---------------
The multiprocessing module is built into CPython.

    $ python
    Python 2.7.2+ (default, Oct  4 2011, 20:06:09) 
    [GCC 4.6.1] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import multiprocessing

PIL (python imaging library)
----------------------------

You probably have the Python Imaging Library already, if not you can get it here for Windows and Linux http://www.pythonware.com/products/pil/ and try the Mac-friendly fork here http://pypi.python.org/pypi/Pillow/

    >>>> import Image # if it impo
    >>>> im=Image.new('RGB', (100,100))
    >>>> im.show() # pops up a 100x100 pixel empty image

parallelpython
--------------

Parallel Python 1.6.2 via: http://www.parallelpython.com/ and test the Python bindings using:

    >>> import pp
    >>> pp.version
    '1.6.1' # the latest version is 1.6.1

gearman
-------

Recent version of gearman 2.x, via http://gearman.org/ I'm using

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

picloud
-------

Install the cloud Python binding via: http://docs.picloud.com/quickstart.html

    >>> import cloud
    >>> cloud.__version__
    >>> '2.5.5'

For picloud I have made an account which you can share but you ought to make your own:

    u:ianozsvald+euroscipy2012@gmail.com
    p:euroscipy2012

Note that there's a limit of 20 computer hours for free per month (and there's no Credit Card on file!), we're unlikely to run out in the class but it makes sense to register for a free account. If you use my login then just use the existing 4569 API key (it won't matter if we have redundant keys in this test account).

ipython cluster
---------------

IPython with cluster support http://ipython.org/ , I installed mine via apt-get in Ubuntu. As long as the ```ipcluster``` command works then you should be fine:

    $ ipython
    Python 2.7.3 (default, Apr 20 2012, 22:39:59) 
    Type "copyright", "credits" or "license" for more information.
    IPython 0.13 -- An enhanced Interactive Python.

    $ ipcluster
    -> shows help message
