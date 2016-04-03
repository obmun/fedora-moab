MOAB RPM package recipe
=======================

This is the source distribution for the recipe for the creation of a MOAB rpm package.

How to use this source
----------------------

The source package for the current version is already embedded in the repo. In case you want to re-download it, the easiest way of doing it from the spec file is to use `spectool` like this:

    spectool -g moab.spec


Now you have multiple options. If you want to run `rpmbuild` in-place you can do something like this:

1.  Prepare the required `rpmbuild` structure:

        sh rpmbuild_structure.sh

2.  Install the build dependencies:

        dnf builddep SPECS/moab.spec

3.  Build the RPMs from the SPEC file with `rpmbuild`:

        cd SPECS
        rpmbuild --define "_topdir ${PWD}/.." ./moab.spec

Or, you can use `mock` for creating the SRPM that you can import into your normal rpmbuild environment with `rpm -ivh`. Execute the following line in the root folder of this repo:

    mock --buildsrpm --spec ./moab.spec --sources .
