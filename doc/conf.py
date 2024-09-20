# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-paramlinks-sphinx-autoapi-compat'
copyright = '2024, SH'
author = 'SH'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "sphinx.ext.autodoc",
  "sphinx_paramlinks",
  "autoapi.extension",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Set default role so `stuff` is enough to reference something:
default_role = "any"

# sphinx-paramlinks settings:
paramlinks_hyperlink_param='name'

# For autodoc:
import sys, os
sys.path.insert(0, os.path.abspath('../src'))

# For sphinx-autoapi:
autoapi_dirs = ['../src/auto']
