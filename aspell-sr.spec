%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.02
%define languageenglazy Serbian
%define languagecode sr
%define lc_ctype sr_YU

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.60.0
Release:       %mkrel 6
Group:         System/Internationalization
Source:	       http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell6-%{languagecode}-%{src_ver}.tar.bz2
URL:		   http://aspell.net/
License:	   LGPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n aspell6-%{languagecode}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright 
%{_libdir}/aspell-*/*


