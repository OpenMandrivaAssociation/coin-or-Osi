%global		_disable_ld_no_undefined	1
%global		module		Osi

Name:		coin-or-%{module}

Summary:	COIN-OR Open Solver Interface Library
Version:	0.106.2
Release:	3%{?dist}
License:	EPL
URL:		https://projects.coin-or.org/%{module}
Source0:	http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
Source1:	%{name}.rpmlintrc
BuildRequires:	blas-devel
BuildRequires:	bzip2-devel
BuildRequires:	coin-or-CoinUtils-devel
BuildRequires:	doxygen
BuildRequires:	glpk-devel
BuildRequires:	lapack-devel
BuildRequires:	libatlas-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	zlib-devel

# Properly handle DESTDIR
Patch0:		%{name}-pkgconfig.patch

# Install documentation in standard rpm directory
Patch1:		%{name}-docdir.patch

%description
The COIN-OR Open Solver Interface Library is a collection of solver
interfaces (SIs) that provide a common interface --- the OSI API --- for all
the supported solvers.

%package	devel
Summary:	Development files for %{name}

Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}

Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
make %{?_smp_flags} all doxydoc

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
cp -a doxydoc/html %{buildroot}%{_docdir}/%{name}

%check
make test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/osi_addlibs.txt
%{_libdir}/*.so.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files		doc
%doc %{_docdir}/%{name}/html

%changelog
* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.2-3
- Use proper _smp_flags macro (#894586#c6).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.2-2
- Correct missing bzip2 build requires (#894586#c4).
- Use unversioned docdir (#894586#c4).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.106.2-1
- Update to latest upstream release.

* Wed May 8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.7-2
- Split documentation in a new subpackage.
- Switch to the new upstream tarballs without bundled dependencies.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.7-1
- Update to latest upstream release.

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.5-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.5-2
- Rename package to coin-or-Osi.
- Do not package Thirdy party data or data without clean license.

* Wed Sep 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.105.5-1
- Initial coinor-Osi spec.
