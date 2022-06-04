#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Taint-Util
Version  : 0.08
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/A/AV/AVAR/Taint-Util-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AV/AVAR/Taint-Util-0.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtaint-util-perl/libtaint-util-perl_0.08-3.debian.tar.xz
Summary  : 'Test for and flip the taint flag without regex matches or C<eval>'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Taint-Util-license = %{version}-%{release}
Requires: perl-Taint-Util-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Taint::Util - Test for and flip the taint flag without regex matches or
"eval"

%package dev
Summary: dev components for the perl-Taint-Util package.
Group: Development
Provides: perl-Taint-Util-devel = %{version}-%{release}
Requires: perl-Taint-Util = %{version}-%{release}

%description dev
dev components for the perl-Taint-Util package.


%package license
Summary: license components for the perl-Taint-Util package.
Group: Default

%description license
license components for the perl-Taint-Util package.


%package perl
Summary: perl components for the perl-Taint-Util package.
Group: Default
Requires: perl-Taint-Util = %{version}-%{release}

%description perl
perl components for the perl-Taint-Util package.


%prep
%setup -q -n Taint-Util-0.08
cd %{_builddir}
tar xf %{_sourcedir}/libtaint-util-perl_0.08-3.debian.tar.xz
cd %{_builddir}/Taint-Util-0.08
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Taint-Util-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Taint-Util
cp %{_builddir}/Taint-Util-0.08/LICENSE %{buildroot}/usr/share/package-licenses/perl-Taint-Util/39dbbbcc6f04dd00e367be10852bff7a6eae0744
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Taint::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Taint-Util/39dbbbcc6f04dd00e367be10852bff7a6eae0744

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
