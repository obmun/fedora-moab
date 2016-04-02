MOAB RPM package recipe
=======================

This is the source distribution for the recipes for the creation of a MOAB rpm package.

How to use this source
----------------------

1.  Install the build dependencies:

        dnf builddep SPECS/moab.spec

2.  Download the package

3.  Create the RPMs from the SPEC file with `rpmbuild`:

        cd SPECS
        rpmbuild --define "_topdir ${PWD}/.." ./moab.spec
