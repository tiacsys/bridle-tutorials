# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import git
import semver
import sphinx
from datetime import date


# -- Variable setup ----------------------------------------------------------

bridle_release = '3.7'
zephyr_release = '3.7'
zephyr_us_version = '3.7.0'

online_ide_entry = 'https://coder.meetup.mp-labs.de/'

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# sys.path.insert(0, os.path.abspath('.'))

logcfg = sphinx.util.logging.getLogger(__name__)
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_windows = sys.platform.startswith('win')

if 'DOCSRC' not in os.environ:
    DOCSRC = os.path.abspath(os.getcwd())
else:
    DOCSRC = os.path.abspath(os.environ['DOCSRC'])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

docstat = 'preliminary'
docnumb = 'MPNX-TST-240119'
doctype = 'Tutorial'
category = 'Learning'
project = 'Cytron Maker RP2040 Tutorials'
publisher = 'Navimatix GmbH, inovex GmbH, SIS by UL Solutions'
author = 'TiaC Systems Team'
contactaddr = 'Jena / Erlangen, Germany'
contactemail = 'info@tiac-systems.net'
contactweb = 'https://tiac-systems.net/'
copyright = f'2019‒{date.today().year}, ' + publisher + ' and individual contributors'
about = category + ' – ' + project + '.'
keywords: str = docnumb
keywords += ',' + doctype
keywords += ',' + category
keywords += ',' + project
keywords += ',Zephyr'
keywords += ',Bridle'
keywords += ',Cytron'

# Define basic strings that will be used in the dictionary of external sites.
# gxp/GXP stands for GitX (Hub/Lab) Pages
gxp_base = 'https://github.com/tiacsys/bridle-tutorials'
gxp_slug = 'bridle-tutorials'
gxp_name = publisher + ', ' + doctype + ', ' + project

if on_rtd:
    git_describe = ('--dirty=+RTDS', '--broken=+broken')
else:
    git_describe = ('--dirty=+dirty', '--broken=+broken')

try:
    repo = git.Repo(search_parent_directories=True)
    semv = semver.VersionInfo.parse(repo.git.describe(git_describe))
    sha1 = repo.head.object.hexsha.lower()
except:
    # fallback to unknown version / release
    semv = semver.VersionInfo.parse('0.0.0-invalid+unknown')
    sha1 = '0000000000000000000000000000000000000000'

# The short SHA1 for identification
identify = repo.git.rev_parse(sha1, short=8)

# The short X.Y.Z version
version = str(semv.finalize_version())
genvers = str(semv.major)

# The full version, including alpha/beta/rc tags
release = str(semv)

# Combined document title and subtitle
# title = project + ' ' + version
title = project
subtitle = doctype

# Single target file names
basename: str = 'bridle-tutorial'
namespace: str = 'net.tiac-systems.doc.learning.tutorial.cytron-maker-rp2040.'
namespace += version + '.'

# Overview ---------------------------------------------------------------------

logcfg.info(project + ' ' + release, color='yellow')
logcfg.info('With Bridle {}'.format(bridle_release), color='green')
logcfg.info('With Zephyr {} (upstream: {})'.format(zephyr_release, zephyr_us_version), color='green')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

build_sphinx = sphinx.__version__

needs_sphinx = '8.1.3'
needs_extensions = {
    'sphinx.ext.extlinks':          needs_sphinx,
    'sphinx.ext.ifconfig':          needs_sphinx,
    'sphinx.ext.intersphinx':       needs_sphinx,
    'sphinx.ext.todo':              needs_sphinx,
#   'sphinx_immaterial':            '0.12.4',
    'sphinxcontrib.spelling':       '8.0.0',
}

extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_immaterial',
    'sphinxcontrib.spelling',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

rst_prolog = '''
.. include:: /roles.txt
.. include:: /shortcuts.txt
.. |docsrc| replace:: {docsrc}
.. |docstat| replace:: {docstat}
.. |docnumb| replace:: {docnumb}
.. |genvers| replace:: {genvers}
.. |identify| replace:: {identify}
.. |title| replace:: {title}
.. |subtitle| replace:: {subtitle}
.. |publisher| replace:: {publisher}
.. |copyright| replace:: {copyright}
.. |project| replace:: {project}
.. |author| replace:: {author}
.. |about| replace:: {about}
.. |contactaddr| replace:: {contactaddr}
.. |contactemail| replace:: {contactemail}
.. |contactweb| replace:: {contactweb}
.. |gxp_name| replace:: {gxp_name}
.. |gxp_name_e| replace:: :emphasis:`{gxp_name}`
.. |gxp_name_s| replace:: :strong:`{gxp_name}`
.. meta::
   :keywords: {keywords}
.. |bridle_release| replace:: v{bridle_release}
.. |bridle_release_tt| replace:: ``v{bridle_release}``
.. |bridle_release_em| replace:: *v{bridle_release}*
.. |bridle_release_number| replace:: {bridle_release}
.. |bridle_release_number_tt| replace:: ``{bridle_release}``
.. |bridle_release_number_em| replace:: *{bridle_release}*
.. |bridle_branch| replace:: ``v{bridle_release}-branch``
.. |bridle_shell_cmd_hello_c| replace::
   https://github.com/tiacsys/bridle/blob/v{bridle_release}-branch/subsys/shell/modules/cmd_hello.c
.. |zephyr_release| replace:: v{zephyr_release}
.. |zephyr_release_tt| replace:: ``v{zephyr_release}``
.. |zephyr_release_em| replace:: *v{zephyr_release}*
.. |zephyr_release_number| replace:: {zephyr_release}
.. |zephyr_release_number_tt| replace:: ``{zephyr_release}``
.. |zephyr_release_number_em| replace:: *{zephyr_release}*
.. |zephyr_branch| replace:: ``tiacsys/v{zephyr_release}-branch``
.. |zephyr_us_version| replace:: v{zephyr_us_version}
.. |zephyr_us_version_tt| replace:: ``v{zephyr_us_version}``
.. |zephyr_us_version_em| replace:: *v{zephyr_us_version}*
.. |zephyr_us_version_number| replace:: {zephyr_us_version}
.. |zephyr_us_version_number_tt| replace:: ``{zephyr_us_version}``
.. |zephyr_us_version_number_em| replace:: *{zephyr_us_version}*
.. |zephyr_us_branch| replace:: ``v{zephyr_release}-branch``
.. |online_ide_entry| replace:: https://coder.meetup.mp-labs.de/
'''.format(
    docsrc = DOCSRC,
    docstat = docstat,
    docnumb = docnumb,
    genvers = genvers,
    identify = identify,
    title = title,
    subtitle = subtitle,
    publisher = publisher,
    copyright = copyright,
    project = project,
    author = author,
    about = about,
    contactaddr = contactaddr,
    contactemail = contactemail,
    contactweb = contactweb,
    gxp_name = gxp_name,
    keywords = keywords,
    bridle_release = bridle_release,
    zephyr_release = zephyr_release,
    zephyr_us_version = zephyr_us_version,
    online_ide_entry = online_ide_entry,
)

rst_epilog = '''
.. include:: /unicode.txt
'''.format()

numfig = True
numfig_format = {
    'code-block': 'Listing %s',
    'section': 'Abschnitt %s',
    'figure': 'Abbildung %s',
    'table': 'Tabelle %s',
}

# -- Options for linkcheck builder -------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

user_agent = 'Mozilla/5.0 AppleWebKit/537.36 Chrome/87.0.4280.88 Safari/537.36'
linkcheck_retries = 10
linkcheck_timeout = 60
linkcheck_workers = 10
linkcheck_anchors = False
linkcheck_ignore = [
    'http://localhost:\d+/',
    'https://www.raspberrypi.com/.*',
    online_ide_entry,
]
linkcheck_allowed_redirects = {
    'https://www.cytron.io/p-maker-pi-rp2040': 'https://www.cytron.io/p-maker-pi-rp2040-simplifying-robotics-with-raspberry-pi-rp2040',
    'https://rptl.io/debug-spec': 'https://datasheets.raspberrypi.com/debug/debug-connector-specification.pdf',
    'https://github.com/raspberrypi/picoprobe': 'https://github.com/raspberrypi/debugprobe',
    'https://de.wikipedia\.org/wiki/.*': r'https://de.wikipedia\.org/wiki/.*',
    'https://raspberrypi\.com/.*': r'https://www.raspberrypi\.com/.*',
}

# -- Options for PDF output --------------------------------------------------
# https://www.mos6581.org/rinohtype/master/quickstart.html#sphinx-quickstart

rinoh_documents = [
    dict(doc = 'index', target = basename,
         title = project, author = author,
         template = '_styles/rinohtype/bridle-book-de.rtt',
         logo = '_static/images/bridle_text.pdf',
    ),
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project
html_favicon = '_static/images/bridle.ico'
html_logo = '_static/images/bridle.svg'

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']
html_css_files = [
    'css/common.css',
    'css/colors.css',
    'css/bold.css',
    'css/strikethrough.css',
    'css/underline.css',
    'css/italic.css',
    'css/hwftlbl.css',
    'css/rpipico.css',
    'css/tweaks-sphinx_immaterial_theme.css',
]
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
    },
    "repo_url": "https://github.com/tiacsys/bridle-tutorials/",
    "repo_name": "TiaCSys/Bridle-Tutorials",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "indigo",
            "accent": "amber",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "In den dunklen Modus wechseln",
                # "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "indigo",
            "accent": "amber",
            "toggle": {
                "icon": "material/weather-night",
                "name": "In den hellen Modus wechseln",
                # "name": "Switch to light mode",
            },
        },
    ],
}

# -- Options for extlinks extension ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#configuration

extlinks_detect_hardcoded_links = True
extlinks = {
    'wiki': ('https://de.wikipedia.org/wiki/%s', '[Wiki: %s]'),
    'bridle': ('https://bridle.tiac-systems.net/doc/{}/bridle/%s'.format(bridle_release), '[Bridle: %s]'),
    'zephyr': ('https://bridle.tiac-systems.net/doc/{}/zephyr/%s'.format(zephyr_release), '[Zephyr: %s]'),
    'zephyr-us': ('https://docs.zephyrproject.org/{}/%s'.format(zephyr_us_version), '[Zephyr (upstream): %s]'),
}

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'bridle': ('https://bridle.tiac-systems.net/doc/{}/bridle'.format(bridle_release), None),
    'zephyr': ('https://bridle.tiac-systems.net/doc/{}/zephyr'.format(zephyr_release), None),
    'zephyr-us': ('https://docs.zephyrproject.org/{}'.format(zephyr_us_version), None),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- Options for spelling extension ------------------------------------------
# https://sphinxcontrib-spelling.readthedocs.io/en/stable/customize.html

spelling_lang = 'de_DE'
spelling_warning = True
spelling_show_suggestions = True

spelling_word_list_filename = [
    '{}/companies'.format(os.path.join(DOCSRC, '_dicts')),
    '{}/electronics'.format(os.path.join(DOCSRC, '_dicts')),
    '{}/missing-de'.format(os.path.join(DOCSRC, '_dicts')),
    '{}/missing-en'.format(os.path.join(DOCSRC, '_dicts')),
    '{}/proper-nouns'.format(os.path.join(DOCSRC, '_dicts')),
]

spelling_exclude_patterns = [
    'todo.rst',
]
