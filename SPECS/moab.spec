# TODO:
# - Create Doxygen documentation and pack it
#   See doc/README in src
Name: moab
Version: 4.9.0
Release: 0
Summary: The Mesh-Oriented datABase (MOAB), a component for representing and evaluating mesh data
Group: System Environment/Libraries
License: GPL
URL: http://sigma.mcs.anl.gov/moab-library/
Vendor: Fathom Team
Source: ftp://ftp.mcs.anl.gov/pub/fathom/%{name}-%{version}.tar.gz
Prefix: %{_prefix}
Packager: Obmun
BuildRoot: %{_tmppath}/%{name}-root
# As the package already includes a generated ./configure script, even without libtool an autoreconf call should not fail
BuildRequires: autoconf
BuildRequires: chrpath
BuildRequires: gcc-c++
BuildRequires: netcdf-devel
BuildRequires: hdf5-devel
Patch0: moab-4.9.0-netcdf_config.patch

%description
MOAB can store structured and unstructured mesh, consisting of elements in the finite element "zoo" plus polygons and polyhedra. The functional interface to MOAB is simple yet powerful, allowing the representation of many types of metadata commonly found on the mesh. MOAB is optimized for efficiency in space and time, based on access to mesh in chunks rather than through individual entities, while also versatile enough to support individual entity access.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1


%build
# Patches touch some of the autoconf .m4 scripts
autoreconf
%configure --with-hdf5 --with-netcdf --enable-shared --enable-static=no
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# Gather list of libraries
ls %{buildroot}%{_libdir}/*.so.* > libs.list
# Gather list of tools
ls %{buildroot}%{_bindir}/* > tools.list

# Remove any remnants of rpaths
#   MOAB includes the std RPATHS in its binaries and libs
#   These don't add anything, and rpmbuild does not like them
for file in `cat libs.list tools.list`; do
  chrpath -d $file
done

# Move examples files into a MOAB specfic dir
mv %{buildroot}%{_datarootdir}/examples %{buildroot}%{_datarootdir}/moab_examples

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README README.IMESH README.IO RELEASE_NOTES LICENSE KNOWN_ISSUES
%doc %{_docdir}/moab/ANNOUNCE
%{_libdir}/*.so.0.0.0
%{_libdir}/*.la
# Do not include the symlinks
%exclude %{_libdir}/*.so
%exclude %{_libdir}/*.so.0
# Exclude some additional files
%exclude %{_libdir}/iMesh-Defs.inc
%exclude %{_libdir}/moab.config
%exclude %{_libdir}/moab.make


%package tools
Summary: The MOAB tools
Requires: moab = %{version}-%{release}
Group: Applications/Engineering


%description tools
Set of tools for working with the file formats supported by MOAB.


%files tools
%{_bindir}/*
%{_mandir}/man1/mbconvert.1.gz
%doc %{_docdir}/moab/README.hexmodops
%doc %{_docdir}/moab/README.mbconvert
%doc %{_docdir}/moab/README.mbsize
%doc %{_docdir}/moab/README.mbskin
%doc %{_docdir}/moab/README.mbsurfplot
%doc %{_docdir}/moab/README.mbtagprop
%doc %{_docdir}/moab/README.spheredecomp


%package devel
Summary: MOAB header files for building C++ code
Requires: moab = %{version}-%{release}
Group: Development/Libraries


%description devel
This provides the VTK header files required to compile C++ programs that
use VTK to do 3D visualisation.


%files devel
%defattr(-,root,root,-)
%{_includedir}/moab
%{_includedir}/MBCN.h
%{_includedir}/MBCN_protos.h
%{_includedir}/MBEntityType.h
%{_includedir}/MBTagConventions.hpp
%{_includedir}/MBiMesh.hpp
%{_includedir}/MOAB_FCDefs.h
%{_includedir}/iBase.h
%{_includedir}/iBase_f.h
%{_includedir}/iMesh.h
%{_includedir}/iMesh_extensions.h
%{_includedir}/iMesh_extensions_protos.h
%{_includedir}/iMesh_f.h
%{_includedir}/iMesh_protos.h
%{_libdir}/*.cmake


%package examples
Summary: Examples for MOAB
Requires: moab = %{version}-%{release}
Group: Applications/Engineering


%description examples
Examples of how to use MOAB distributed with the library source package.

%files examples
%doc %{_datarootdir}/moab_examples


%changelog
* Sat Apr 2 2016 Jacobo Cabaleiro <obmun.h@gmail.com> - 4.9.0-0
- First creation


