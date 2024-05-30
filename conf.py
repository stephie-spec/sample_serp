# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('.'))  # Add project root to path

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '4.4.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions shipped with Sphinx, or your own custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',  # For improved docstrings on functions, classes, etc.
]

# Add any paths that contain templates.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Your Project Name'
copyright = '2024, Your Name'
author = 'Your Name'

# The version info for the project doc ( genellikle requirements.txt den alınır)
version = '0.1.0'
release = version


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  
# See https://www.sphinx-doc.org/en/master/usage/themes.html for available themes.
html_theme = 'sphinx_rtd_theme'  # Make sure this theme is installed (pip install sphinx-rtd-theme)

# Add any paths that contain custom static files (such as style sheets, scripts,
# images) for HTML output.
html_static_path = ['_static']

# -- Options for intersphinx extension ---------------------------------------

# #  The list of other projects with intersphinx links.
# #  Used by sphinx.ext.intersphinx to link to other project's documentation.
# intersphinx_mapping = {'https://docs.python.org/3/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for Napoleon extension -------------------------------------------

# Napoleon settings for improved docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_rtype = False  # Set to True if your function has a return type
