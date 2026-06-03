#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="pipelinewise-singer-python",
      version='2.0.2',
      description="Singer.io utility library - PipelineWise compatible",
      python_requires=">=3.7.0",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="TransferWise",
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
      ],
      url="https://github.com/transferwise/pipelinewise-singer-python",
      install_requires=[
          'pytz',
          'jsonschema>=4.16.0',
          'orjson>=3.9.0,<4',
          'python-dateutil>=2.6.0',
          'backoff==2.2.1',
          'ciso8601',
          'pycryptodome',
          'pycryptodomex',
      ],
      extras_require={
          'dev': [
              'pylint==2.11.1',
              'pytest==7.1.2',
              'coverage[toml]~=6.3',
              'ipython',
              'ipdb',
              'unify==0.5'
          ]
      },
      packages=['singer'],
      package_data={
          'singer': [
              'logging.conf'
          ]
      },
      include_package_data=True
      )
