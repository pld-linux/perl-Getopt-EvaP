%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	EvaP
Summary:	Getopt::EvaP - evaluate Perl command line parameters.
Name:		perl-Getopt-EvaP
Version:	2.3.5
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
B<@PDT> is the Parameter Description Table, which is a reference to
a list of strings describing the command line parameters, aliases,
types and default values.  B<@MM> is the Message Module, which is also a
reference to a list of strings describing the command and it's parameters.
B<%OPT> is an optional hash reference where Evaluate Parameters should
place its results.  If specified, the historical behaviour of modifying
the calling routines' namespace by storing option values in B<%Options>,
B<%options> and B<$opt*> is disabled.

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
