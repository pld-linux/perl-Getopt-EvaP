%include	/usr/lib/rpm/macros.perl
%define	pdir	Getopt
%define	pnam	EvaP
Summary:	Getopt::EvaP - evaluate Perl command line parameters
Summary(pl):	Modu³ Getopt::EvaP - przekszta³caj±cy parametry z linii poleceñ
Name:		perl-Getopt-EvaP
Version:	2.3.5
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
@PDT is the Parameter Description Table, which is a reference to a
list of strings describing the command line parameters, aliases, types
and default values. @MM is the Message Module, which is also a
reference to a list of strings describing the command and it's
parameters. %%OPT is an optional hash reference where Evaluate
Parameters should place its results. If specified, the historical
behaviour of modifying the calling routines' namespace by storing
option values in %%Options, %%options and $opt* is disabled.

%description -l pl
@PDT to tablica opisu parametrów (Parameter Description Table), która
jest referencj± do listy ³añcuchów opisuj±cych parametry dla linii
poleceñ, aliasy, typy i warto¶ci domy¶lne. @MM to modu³ komunikacyjny
(Message Module), który jest tak¿e referencj± do listy ³añcuchów -
opisuj±cych polecenie i jego parametry. %%OPT to opcjonalna referencja
do hasza, w którym modu³ powinien umie¶ciæ wyniki. Je¶li jest podana,
wy³±czane jest stare zachowanie polegaj±ce na modyfikowaniu przstrzeni
nazw funkcji wywo³uj±cych poprzez zapisywanie warto¶ci opcji w
%%Options, %%options oraz $opt*.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/genpTk
%{perl_sitelib}/Getopt/DisU.pl
%{perl_sitelib}/Getopt/EvaP.pm
%{_mandir}/man3/*
