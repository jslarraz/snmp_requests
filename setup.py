from setuptools import setup, find_packages
setup(
  name = 'pysnmplib',
  version='0.0.1',
  description = 'SNMP library developed for Network Management classes at University of Zaragoza. This library has been developed with teaching purposes and relies on based on pySNMP library.',
  author = 'Jorge Sancho',
  author_email = 'jslarraz@gmail.com',
  url = 'https://github.com/jslarraz/pysnmplib', # use the URL to the github repo

  packages=find_packages(),
  package_data={
    '': ['schemas/*.schema.json'],
  },
  include_package_data=True,
  install_requires=[
    'pysnmp',
  ],

  #download_url = 'https://github.com/jslarraz/fhirtools/tarball/0.1',
  keywords = ['snmp', 'development'],
  classifiers = [],
)
