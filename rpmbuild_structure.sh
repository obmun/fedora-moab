mkdir -p SPECS
ln -s ../moab.spec SPECS/moab.spec
mkdir -p SOURCES
SOURCE_PKG=$(ls *.tar*)
ln -s ../$SOURCE_PKG SOURCES/$SOURCE_PKG
PATCHES=$(ls *.patch)
for file in $PATCHES; do ln -s ../$file SOURCES/$file; done
