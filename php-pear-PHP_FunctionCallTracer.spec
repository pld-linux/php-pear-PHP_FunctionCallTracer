%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	FunctionCallTracer
%define		_status		stable
%define		_pearname	PHP_FunctionCallTracer
Summary:	%{_pearname} - Function Call Tracer
Summary(pl.UTF-8):	%{_pearname} - śledzenie wywołań funkcji
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	2
License:	The BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ca727faf817b20a3e5de7296800f276c
URL:		http://pear.php.net/package/PHP_FunctionCallTracer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-PHP_FunctionCallTracer-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creates a function calls debug trace. Functions arguments, returned
parameters and watched variables are reported in the same section for
each function call. The trace is available as an array, or can be
displayed or written in a file. Traced variables can be processed by
provided user functions for displaying purposes.

This package is not a replacement for full fledged PHP debuggers. It
is useful for:
- remote debugging,
- to debug a complex sequence of function calls,
- to display non text variables in a user readable format.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa tworzy ślady diagnostyczne wywołań funkcji. Argumenty
funkcji, zwracane parametry i podglądane zmienne są zwracane w tej
samej sekcji dla każdego wywołania funkcji. Ślad jest dostępny jako
tablica lub może być wyświetlany albo zapisywany do pliku. Śledzone
zmienne mogą być przetwarzane do wyświetlenia przez funkcje
dostarczone przez użytkownika.

Ten pakiet nie jest zamiennikiem pełnych debuggerów PHP. Jest
natomiast przydatny do:
- zdalnej diagnostyki,
- śledzenia złożonej sekwencji wywołań funkcji,
- wyświetlania zmiennych nietekstowych w formacie czytelnym dla
  użytkownika.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/PHP_FunctionCallTracer/docs/examples/
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/FunctionCallTracer.php
