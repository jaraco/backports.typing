backports.typing
================

`Backport <https://pypi.python.org/pypi/backports>`_ of the typing module
as found in Python 3.5, but made available for Python 3.3 and later.

Since the inception of this package, a new, more authoritative backport
has been released as `typing <https://pypi.io/project/typing>`_. This
project selectively installs that package on the relevant platforms.

Usage
-----

Simply import the typing module as you would on Python 3.5+.

    import typing

This module additionally bundles late versions of the module as
published in the ``typing`` package as backports.typing, such that
later releases of ``typing`` can be loaded on earlier versions
of Python 3.5 and later by importing from the backports namespace.

    from backports import typing

Note that the bundled version currently only supports Python 3.2+.

License
-------

This package is licensed under the OSI MIT License, but the bundled
typing module is licensed under the Python Software Foundation License.
