FRM
========

CLI tool for bootstraping a Continuous delivery workflow.

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
