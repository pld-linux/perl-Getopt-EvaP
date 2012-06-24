#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Getopt
%define		pnam	EvaP
Summary:	Getopt::EvaP - evaluate Perl command line parameters
Summary(pl):	Getopt::EvaP - przetwarzanie parametr�w linii polece� Perla
Name:		perl-Getopt-EvaP
Version:	2.3.5
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	edc3fd2fbb0070e4d4ce954d6e715443
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Tk
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Briefly, EvaP() is a table driven command line argument processor that
type checks values and provides up to three levels of online help on
the comamnd and its parameters.  You provide the Parameter Description
Table (PDT), and, optionally, a help Message Module (MM), and call
EvaP() with pointers to this information, and get in return an option
hash with command line values indexed by argument name.  When users
request help, EvaP() uses the PDT and MM to present the help data and
exits, all automatically.

%description -l pl
W skr�cie, EvaP() jest opartym na tablicy procesorem argument�w linii
polece�, kt�ry sprawdza typy warto�ci i zapewnia do trzech poziom�w
pomocy online odno�nie polecenia i jego argument�w. Podaje si� tablica
opisu parametr�w (Parameter Description Table, PDT) oraz, opcjonalnie,
pomocniczy modu� komunikacyjny (Message Module, MM), a nast�pnie
wywo�uje EvaP() ze wska�nikami do tych informacji, otrzymuj�c jako
wynik hasza opcji zawieraj�cego warto�ci z linii polecenia indeksowane
nazwami argument�w. Gdy u�ytkownik poprosi o pomoc, EvaP() korzysta z
PDT i MM dla przedstawienia informacji pomocy i ko�czy. Wszystko
automatycznie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/genpTk
%{perl_vendorlib}/Getopt/DisU.pl
%{perl_vendorlib}/Getopt/EvaP.pm
%{_mandir}/man3/*
