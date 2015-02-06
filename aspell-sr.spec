%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.02
%define languageenglazy Serbian
%define languagecode sr
%define lc_ctype sr_YU

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.60.0
Release:       6
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




%changelog
* Tue Sep 01 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.60.0-5mdv2010.0
+ Revision: 423966
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.60.0-4mdv2009.0
+ Revision: 226181
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.60.0-3mdv2008.1
+ Revision: 182654
- provide enchant-dictionary

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.60.0-2mdv2008.1
+ Revision: 140690
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/


* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-2mdv2007.0
+ Revision: 132949
- Import aspell-sr

* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Mon Nov 28 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.60.0-1mdk
- first version

