#!/usr/bin/env python
import io
import re

from setuptools import setup

with io.open('./toga_django.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    version=version,
    install_requires=[
        'django~=3.0',
        'django-environ==0.4.1',
        'toga-web==%s' % version,
    ],
)
