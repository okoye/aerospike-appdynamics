aerospike-appdynamics
=====================
Custom monitors for aerospike to integrate with app dynamics.

==============================
Installing:
==============================
Before you install ensure a compatible sqlite3 lib is installed. For CentOS5.x
systems that ship with python2.4, you can install python-sqlite2 from the
rpmforge repository.

To install as a python package, simply run:
  python setup.py install

You could also install this module as an rpm by first generating the rpm
package via:
  python setup.py bdist_rpm
Then installing via rpm or yum as appropriate.

==============================
Testing:
==============================
python setup.py test

=============================
Notes
=============================
Versioning on this module follows the semantic versioning scheme. More
information can be found here: http://semver.org/
