import os
from setuptools import setup, find_packages
from wagtailmenus import __version__, stable_branch_name

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

base_url = "https://github.com/jazzband/wagtailmenus/"
download_url = '%starball/v%s' % (base_url, __version__)
branch_url = "%stree/stable/%s" % (base_url, stable_branch_name)

# Essential dependencies
requires = [
    'wagtail>=5.2',
    'django-cogwheels==0.3',
]

testing_extras = [
    'beautifulsoup4>=4.8,<4.10',
    'coverage>=4.5',
    'django-webtest>=1.9,<1.10',
]

development_extras = [
    'wagtail>=5.2',
    'django-debug-toolbar',
    'django-extensions',
    'ipdb',
    'werkzeug',
]

documentation_extras = [
    'pyenchant>=2.0',
    'Sphinx>=1.7.4',
    'sphinxcontrib-spelling>=1.4',
    'sphinx_rtd_theme>=0.3',
]

deployment_extras = []

setup(
    name="wagtailmenus",
    version=__version__,
    author="Andy Babic",
    author_email="ababic@rkh.co.uk",
    description=("An app to help you manage menus in your Wagtail projects "
                 "more consistently."),
    long_description=README,
    packages=find_packages(),
    license="MIT",
    keywords="wagtail cms model utility",
    download_url=download_url,
    url=branch_url,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Framework :: Wagtail :: 5',
        'Framework :: Wagtail :: 6',
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=requires,
    python_requires='>=3.9',
    extras_require={
        'testing': testing_extras,
        'docs': documentation_extras,
        'development': development_extras + testing_extras,
        'deployment': deployment_extras,
    },
)
