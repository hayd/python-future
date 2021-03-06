"""
future: Easy, safe support for Python 3/2 compatibility
=======================================================

``future`` is the missing compatibility layer between Python 3 and Python
2. It allows you to use a single, clean Python 3.x-compatible codebase to
support both Python 3 and Python 2 with minimal overhead.

Notable projects that use ``future`` for Python 2/3 compatibility are `Mezzanine <http://mezzanine.jupo.org/>`_ and `xlwt-future <https://pypi.python.org/pypi/xlwt-future>`_.

It is designed to be used as follows::

    from __future__ import (absolute_import, division,
                            print_function, unicode_literals)
    from future import *

or explicitly as::

    from future.builtins import (bytes, int, range, round, str, super,
                                 ascii, chr, hex, input, oct, open,
                                 filter, map, zip)

followed by predominantly standard, idiomatic Python 3 code that then runs
similarly on Python 2.6/2.7 and Python 3.3+.

The imports have no effect on Python 3. On Python 2, they shadow the
corresponding builtins, which normally have different semantics on Python 3
versus 2, to provide their Python 3 semantics.


Standard library reorganization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``from future import standard_library`` provides a context-manager called
``enable_hooks`` that installs import hooks (PEP 3108) to allow renamed and
moved standard library modules to be imported from their new Py3 locations.


Automatic conversion
--------------------
An included script called `futurize
<http://python-future.org/automatic_conversion.html>`_ aids in converting
code (from either Python 2 or Python 3) to code compatible with both
platforms. It is similar to ``python-modernize`` but goes further in
providing Python 3 compatibility through the use of the backported types
and builtin functions in ``future``.


Documentation
-------------

See: http://python-future.org

Also see the docstrings for each of these modules for more info::

- future.standard_library
- future.builtins
- future.utils


Credits
-------

:Author:  Ed Schofield
:Sponsor: Python Charmers Pty Ltd, Australia, and Python Charmers Pte
          Ltd, Singapore. http://pythoncharmers.com
:Others:  - The backported ``super()`` and ``range()`` functions are
            derived from Ryan Kelly's ``magicsuper`` module and Dan
            Crosta's ``xrange`` module.
          - The ``futurize`` script uses ``lib2to3`` and fixers from
            Joe Amenta's ``lib3to2`` and Armin Ronacher's ``python-modernize``.
          - The ``python_2_unicode_compatible`` decorator is from
            Django. The ``implements_iterator`` and ``with_metaclass``
            decorators are from Jinja2.
          - Documentation is generated using ``sphinx`` and styled using
            ``sphinx-bootstrap-theme``.


Licensing
---------
Copyright 2013 Python Charmers Pty Ltd, Australia.
The software is distributed under an MIT licence. See LICENSE.txt.

"""

from future import standard_library, utils
from future.builtins import *

__title__ = 'future'
__author__ = 'Ed Schofield'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Python Charmers Pty Ltd'
__ver_major__ = 0
__ver_minor__ = 11
__ver_patch__ = 0
__ver_sub__ = '-dev'
__version__ = "%d.%d.%d%s" % (__ver_major__, __ver_minor__,
                              __ver_patch__, __ver_sub__)
