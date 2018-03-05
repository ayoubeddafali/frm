FRM
========

CLI tool for bootstraping a Continuous delivery workflow with docker.

**Under development, supports for java based projects.**

Preparing for Development
--------------------------
1. Ensure ``pip``, and ``pipenv`` are installed.
2. Clone the repo: ``https://github.com/ayoubensalem/frm``
3. Fetch development dependencies : ``make install``

Usage
-----

::

  $ frm --info
  $ frm --help
  $ frm --init java

Running Tests :
--------------

::

  $  make


Build :
-------
Build a wheel

::

    $ python setup.py bdist_wheel

Demo:
-------
DEMO_.


.. _DEMO: https://asciinema.org/a/k1ZSB5Pz4zhf8yrxsQxa9S9O2
