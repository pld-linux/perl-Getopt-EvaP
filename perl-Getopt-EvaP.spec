%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	EvaP
Summary:	Getopt-EvaP perl module
Summary(pl):	Modu³ perla Getopt-EvaP
Name:		perl-Getopt-EvaP
Version:	2.3.5
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Getopt-EvaP perl module.

%description -l pl
Modu³ perla Getopt-EvaP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/genpTk
%{perl_sitelib}/Getopt/DisU.pl
%{perl_sitelib}/Getopt/EvaP.pm
%{_mandir}/man3/*
