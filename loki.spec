Summary:	Loki C++ Library
Name:		loki
Version:	0.1.5
Release:	0.1
License:	MIT License
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/loki-lib/%{name}-%{version}.tar.gz
# Source0-md5:	f246e9e91b46d4e55ce36193984697e6
URL:		http://sourceforge.net/projects/loki-lib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ library of designs, containing flexible implementations of
common design patterns and idioms.

%package devel
Summary:	The Loki C++ headers and development libraries
Group:		Libraries

%description devel
Headers, shared object symlinks for the Loki C++ Library

%package static
Summary:	The Loki C++ development libraries
Group:		Libraries

%description static
static libraries for the Loki C++ Library

%package doc
Summary:	The Loki C++ html docs
Group:		Libraries

%description doc
HTML documentation files for the Loki C++ Library

%prep
%setup -q

%build
%{__make} build-static build-shared \
	CC="%{__cc}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_libdir}/libloki.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/loki
%{_libdir}/libloki.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libloki.a
