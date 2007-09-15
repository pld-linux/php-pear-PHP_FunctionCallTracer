%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	FunctionCallTracer
%define		_status		stable
%define		_pearname	PHP_FunctionCallTracer
Summary:	%{_pearname} - Function Call Tracer
#Summary(pl.UTF-8):	%{_pearname} - 
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	The BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ca727faf817b20a3e5de7296800f276c
URL:		http://pear.php.net/package/PHP_FunctionCallTracer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creates a function calls debug trace. Functions arguments, returned
parameters and watched variables are reported in the same section for
each function call.
The trace is available as an array, or can be displayed or written in
a file.
Traced variables can be processed by provided user functions for
displaying purposes.

This package is not a replacement for full fledged PHP debuggers. It
is useful for (1) remote debugging, (2) to debug a complex sequence of
function calls, (3) to display non text variables in a user readable
format.

(1) Remote debugging is sometimes the only option to debug a package
that works fine on your system, e.g. a 32-bit OS, but breaks on a
different system, e.g. a 64-bit OS, which you have no access to. A
remote user who has the latter OS could run the package, then send you
the trace for analysis.

(2) It is sometimes difficult not to loose track of functions calls
in some live debugging sessions even with top notch PHP
editor/debuggers. The trace produced by this package may come handy
and is easy to use in combination with the source code to track calls
and variables.

(3) Some variables native format does not always display well,
typically:
packed data and UTF-8 strings. They can be converted as they are
being traced to a readable format by provided user functions. For
example: converting binary strings to hexadecimal, or UTF-8 string to
Unicode.

Fully tested with phpUnit. Code coverage test close to 100%.

Usage including trace examples is fully documented in docs/examples
files.

In PEAR status of this package is: %{_status}.

#%description -l pl.UTF-8
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/PHP_FunctionCallTracer
