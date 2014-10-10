%define upstream_name 	 XML-QL
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl-libwww-perl
BuildArch:	noarch

%description
%{upstream_name} - An XML query language.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%doc README MANIFEST Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML

%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 408244
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-11mdv2009.0
+ Revision: 242256
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.07-9mdv2008.0
+ Revision: 23502
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-8mdk
- Fix According to perl Policy
	- BuildRequires
	- URL
	- Source URL
- use mkrel

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.07-7mdk
- Own dir

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.07-6mdk
- rebuild for new auto{prov,req}

