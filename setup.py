from setuptools import setup, find_packages

setup(
  name='dukedomsplayerbrokerscardservicetests',
  version='0.0.0',
  description='integration tests for player service, card/action broker and card service',
  packages=find_packages(exclude=['swagger_codegen', '&.tests']),
  include_package_data=True
)
