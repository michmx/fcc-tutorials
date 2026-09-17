project = 'FCC Tutorials'
copyright = '2026, CERN'
html_favicon = '_static/img/favicon.ico'

exclude_patterns = [
    'venv',
    '.github',
    'README.md',
    'archive'
]

html_theme = 'furo'

html_theme_options = {
    # Dark-text logo on the light theme, light-text logo on the dark theme
    'light_logo': 'img/fcc-logo-dark.png',
    'dark_logo': 'img/fcc-logo-light.png',
    # "Edit this page" button
    'source_repository': 'https://github.com/HEP-FCC/fcc-tutorials',
    'source_branch': 'main',
    'source_directory': '',
}

# Furo's default sidebar plus the sphinx-multiversion switcher
# (_templates/sidebar/versions.html, rendered only in multiversion builds)
html_sidebars = {
    '**': [
        'sidebar/brand.html',
        'sidebar/search.html',
        'sidebar/scroll-start.html',
        'sidebar/navigation.html',
        'sidebar/versions.html',
        'sidebar/scroll-end.html',
        'sidebar/variant-selector.html',
    ]
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
