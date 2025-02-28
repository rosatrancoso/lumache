import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lumache'
copyright = '2025, Graziella'
author = 'Graziella'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',  # support for MyST markdown
    'sphinx.ext.duration',
    'sphinx.ext.doctest',  # include code snippets in the documentation
    'sphinx.ext.autodoc',  # include docstrings in the documentation
    'sphinx.ext.autosummary',  # include summaries of modules and classes
    # 'sphinx.ext.intersphinx',  # link to other Sphinx documentation
    # 'sphinx.ext.viewcode',  # add links to highlighted source code
    # 'sphinx.ext.napoleon',  # parse Google-style docstrings
    # 'sphinx.ext.todo',  # include to-do items
    # 'sphinx.ext.coverage',  # include coverage information   
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_theme = 'furo'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
