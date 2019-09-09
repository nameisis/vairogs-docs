# -*- coding: utf-8 -*-

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# adding PhpLexer
from sphinx.highlighting import lexers
from pygments.lexers.compiled import CLexer
from pygments.lexers.special import TextLexer
from pygments.lexers.text import RstLexer
from pygments.lexers.web import PhpLexer

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
    'sensio.sphinx.refinclude', 'sensio.sphinx.configurationblock', 'sensio.sphinx.phpcode', 'sensio.sphinx.codeblock'
]

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Vairogs / Nameisis / RavenFlux'
copyright = 'k0d3r1s'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '2.2'
# The full version, including alpha/beta/rc tags.
release = '0.0.1'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# enable highlighting for PHP code not between ``<?php ... ?>`` by default
lexers['markdown'] = TextLexer()
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
lexers['php-standalone'] = PhpLexer(startinline=True)
lexers['php-symfony'] = PhpLexer(startinline=True)
lexers['rst'] = RstLexer()
lexers['varnish3'] = CLexer()
lexers['varnish4'] = CLexer()

config_block = {
    'apache': 'Apache',
    'markdown': 'Markdown',
    'nginx': 'Nginx',
    'rst': 'reStructuredText',
    'varnish3': 'Varnish 3',
    'varnish4': 'Varnish 4'
}

# use PHP as the primary domain
primary_domain = 'php'

html_favicon = 'favicon.ico'

# set url for API links
api_url = 'http://github.com/vairogs/vairogs-docs/master/%s'


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'VairogsDoc'
