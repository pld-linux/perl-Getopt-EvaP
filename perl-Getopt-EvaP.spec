#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Getopt
%define		pnam	EvaP
Summary:	Getopt::EvaP - evaluate Perl command line parameters
Summary(pl.UTF-8):	Getopt::EvaP - przetwarzanie parametrów linii poleceń Perla
Name:		perl-Getopt-EvaP
Version:	2.3.5
Release:	14
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Getopt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	edc3fd2fbb0070e4d4ce954d6e715443
URL:		http://search.cpan.org/dist/Getopt-EvaP/
BuildRequires:	perl-Tk
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
W skrócie, EvaP() jest opartym na tablicy procesorem argumentów linii
poleceń, który sprawdza typy wartości i zapewnia do trzech poziomów
pomocy online odnośnie polecenia i jego argumentów. Podaje się tablica
opisu parametrów (Parameter Description Table, PDT) oraz, opcjonalnie,
pomocniczy moduł komunikacyjny (Message Module, MM), a następnie
wywołuje EvaP() ze wskaźnikami do tych informacji, otrzymując jako
wynik hasza opcji zawierającego wartości z linii polecenia indeksowane
nazwami argumentów. Gdy użytkownik poprosi o pomoc, EvaP() korzysta z
PDT i MM dla przedstawienia informacji pomocy i kończy. Wszystko
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
