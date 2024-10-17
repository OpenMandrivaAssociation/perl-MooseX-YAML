%define upstream_name    MooseX-YAML
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	DWIM loading of Moose objects from YAML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(MooseX::Blessed::Reconstruct)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(YAML)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This module provides DWIM loading of the Moose manpage based objects from
YAML documents.

Any hashes blessed into a the Moose manpage class will be replaced with a
properly constructed instance (respecting init args, 'BUILDALL', and the
meta instance type).

This is similar to the YAML::Active manpage in that certain nodes in the
loaded YAML documented are treated specially.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 655604
- rebuild for updated spec-helper

* Wed Jul 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 562772
- import perl-MooseX-YAML


* Wed Jul 14 2010 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
