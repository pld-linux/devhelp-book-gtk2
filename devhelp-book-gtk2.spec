Summary:	DevHelp book: GTK+ 2.0
Summary(pl):	Ksi±¿ka do DevHelpa o GTK+ 2.0
Name:		devhelp-book-gtk2
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gtk-2.0.tar.gz
# Source0-md5:	795dd5a42ee2a3624d8b8bffab7694ad
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about GTK+ 2.0.

%description -l pl
Ksi±¿ka do DevHelpa o GTK+ 2.0.

%prep
%setup -q -c -n gtk-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/gtk-%{version},specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/gtk-%{version}.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/gtk-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
