# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'arg_sphinx'
copyright = '2025 Eviden'
author = 'jbc'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
    "sphinx_multiversion",
]


autoclass_content = 'both'

templates_path = ['_templates']

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/versions.html",
        "sidebar/scroll-end.html",
    ],
}


# -- Sphinx Multiversion config--------------------------------------------
# https://holzhaus.github.io/sphinx-multiversion/master/configuration.html#
smv_tag_whitelist = r'^.*$'         # include all tags
#smv_branch_whitelist = r'^.*$'      # include all branches
smv_branch_whitelist = r'^(?!HEAD$).*$' 
# Accept all branches except HEAD (detached head in CI) and temp branches
smv_remote_whitelist = r'^origin$'  # build only origin branches
smv_released_pattern = r'^refs/tags/.*$'

# Optional: Label format
smv_label_format = '{ref.name}'  # e.g., "main", "v1.0"

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_theme = 'classic'
html_theme = 'furo'   #PyPI Theme
html_static_path = ['_static']

html_favicon = "_static/favicon.ico"


# Optional: HTML context for versions
html_context = {
    'display_github': True,
    'github_user': 'Eviden',
    'github_repo': 'your-repo',
    'github_version': 'main/docs/',
    'versions': []
}

