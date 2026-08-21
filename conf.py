project = 'FCC Tutorials'
copyright = '2026, CERN'
html_logo = '_static/img/fcc-logo-light.png'
html_favicon = '_static/img/favicon.ico'

exclude_patterns = [
    'venv',
    '.github',
    'README.md',
    'archive'
]

html_theme = 'sphinx_book_theme'

html_theme_options = {
    'repository_url': 'https://github.com/HEP-FCC/fcc-tutorials',
    'repository_branch': 'main',
    'path_to_docs': '',
    'use_repository_button': True,
    'use_edit_page_button': True,
    'use_issues_button': True,
    # sphinx-multiversion version dropdown (renders only in multiversion builds)
    'primary_sidebar_end': ['version-switcher'],
}

html_context = {
    'github_user': 'HEP-FCC',
    'github_repo': 'fcc-tutorials',
    'github_version': 'main',
    'doc_path': '',
}

extensions = [
    'myst_parser',
    'sphinx_togglebutton',
    'sphinx_copybutton',
    'sphinx_multiversion',
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    'colon_fence',
    'html_admonition'
]

myst_heading_anchors = 3

html_static_path = [
    '_static'
]

html_css_files = [
    'css/custom-admonitions.css'
]

templates_path = [
    '_templates',
]

smv_tag_whitelist = r'^(?!(v0.1.0|v0.2.0))$'
smv_branch_whitelist = r'^(?!(HEAD|vvolkl-patch-|starterkit|gh-pages)).*$'
smv_remote_whitelist = r'^(origin)$'

linkcheck_ignore = [
    # FIXME: The URLs have changed
    r'https://research\.cs\.wisc\.edu/htcondor/.*',
]
