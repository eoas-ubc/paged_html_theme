# -*- coding: utf-8 -*-
#
# -- Project information -----------------------------------------------------

project = "Numeric course"
copyright = "Numeric project"
author = "Numeric Project"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = "0.1"


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
     "nbsphinx",
     "sphinx.ext.mathjax",
]


extensions = [
    "nbsphinx",
    "sphinx.ext.mathjax",
]
extensions = [
    "myst_nb",
    "sphinx.ext.mathjax",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst','.md']
# source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "paged_html_theme"
#html_theme = "sphinx_rtd_theme"
html_style = None
html_static_path = ["_static"]



# -- Extension configuration -------------------------------------------------
nbsphinx_allow_errors = True
jupyter_execute_notebooks = "cache"
