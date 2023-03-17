from setuptools import setup
import pypkg
import sys

DESCRIPTION = "onecmd: Python pyproject.toml Genelator"
NAME = 'onecmd'
AUTHOR = 'sonyakun'
AUTHOR_EMAIL = 'sonyakun217@gmail.com'
URL = 'https://github.com/sakurapkg/onecmd'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/sakurapkg/onecmd/releases'
PYTHON_REQUIRES = ">=3.10"

INSTALL_REQUIRES = [
    'cleo',
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3 :: Only',
]

long_description_content_type = "https://github.com/sakurapkg/onecmd"

setup(
    name=NAME,
      version="1.0.0",
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description_content_type,
      license=LICENSE,
      url=URL,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      classifiers=CLASSIFIERS,
    entry_points={
        "console_scripts": [
            "onecmd=onecmd_sys.app:main".format(sys.version_info[0]),
        ]
    },
)
