Summary:	DevHelp book: gtk 2.0
Summary(pl):	Ksi±¿ka do DevHelpa o gtk 2.0
Name:		devhelp-book-gtk2
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/gtk-2.0.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
DevHelp book about gtk 2.0.

%description -l pl
Ksi±¿ka do DevHelpa o gtk 2.0.

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
