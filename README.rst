Mkdocutils
==========

MkDocs fork with Docutils as core renderer.

Feel free to play around:

.. code:: shell

   git clone https://gitlab.com/notpushkin/mkdocutils
   cd mkdocutils
   poetry install
   cd docs
   poetry run mkdocs build
   cd site
   python3 -m http.server 8999
   # Visit http://localhost:8999/

.. _things-that-work--things-that-are-broken:

Things that work / things that are broken
-----------------------------------------

-  basic reST rendering works

   -  code highlighting is there but classnames are wrong
   -  admonitions work
   -  text roles (e. g. :literal:`:func:`foo\``) don't work

-  VERY basic MyST rendering

   -  many things are broken (e. g. code blocks are just ``<pre>``)
   -  many things would crash the build process


-  basic Recommonmark rendering

   -  to use, replace the parser in ``mkdocutils.docutils`` to ``recommonmark.parser.CommonMarkParser``
