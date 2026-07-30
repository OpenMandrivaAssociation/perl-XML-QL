%define upstream_name 	 XML-QL
%define upstream_version 0.07
Name:		perl-%{upstream_name}
Version:	0.07
Release:	1

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-QL
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSERGEANT/XML-QL-0.07.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl-libwww-perl
BuildArch:	noarch

%description
%{upstream_name} - An XML query language.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%doc README MANIFEST Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML

