# TODO: optflags
Summary:	Loki C++ Library
Summary(pl.UTF-8):   Biblioteka Loki C++
Name:		loki
Version:	0.1.5
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/loki-lib/%{name}-%{version}.tar.gz
# Source0-md5:	f246e9e91b46d4e55ce36193984697e6
URL:		http://sourceforge.net/projects/loki-lib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++ library of designs, containing flexible implementations of
common design patterns and idioms.

%description -l pl.UTF-8
Biblioteka projektów C++, zawierająca elastyczne implementacje
popularnych szablonów projektów i idiomów.

%package devel
Summary:	The Loki C++ headers
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki Loki C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers, shared object symlink for the Loki C++ Library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dowiązanie symboliczne dla biblioteki Loki C++.

%package static
Summary:	The Loki C++ static library
Summary(pl.UTF-8):   Statyczna biblioteka Loki C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Loki C++ Library.

%description static -l pl.UTF-8
Statyczna biblioteka Loki C++.

%package doc
Summary:	The Loki C++ HTML docs
Summary(pl.UTF-8):   Dokumentacja HTML do biblioteki Loki C++
Group:		Documentation

%description doc
HTML documentation files for the Loki C++ Library.

%description doc -l pl.UTF-8
Dokumentacja HTML do biblioteki Loki C++.

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
%attr(755,root,root) %{_libdir}/libloki.so
%{_includedir}/loki

%files static
%defattr(644,root,root,755)
%{_libdir}/libloki.a
