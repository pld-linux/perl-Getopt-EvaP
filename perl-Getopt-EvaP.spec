%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Getopt-EvaP perl module
Summary(pl):	Modu³ perla Getopt-EvaP
Name:		perl-Getopt-EvaP
Version:	2.3.5
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Getopt/Getopt-EvaP-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Getopt-EvaP perl module.

%description -l pl
Modu³ perla Getopt-EvaP.

%prep
%setup -q -n Getopt-EvaP-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Getopt/EvaP
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/genpTk

%{perl_sitelib}/Getopt/DisU.pl
%{perl_sitelib}/Getopt/EvaP.pm
%{perl_sitearch}/auto/Getopt/EvaP

%{_mandir}/man3/*
