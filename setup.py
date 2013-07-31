from setuptools import setup, find_packages

#We follow the semver rules for versioning
#http://semver.org

setup(name='aerospike-appdynamics-connector',
      version='0.1.1',
      description='aerospike abstraction library for appdynamics scripts',
      author='Chuka O',
      author_email='dokoye@wsgc.com',
      package_dir={'':'lib'},
      packages=find_packages(where='lib'),)
