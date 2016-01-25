%{?scl:%scl_package nodejs-spdx-exceptions}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-spdx-exceptions

%global npm_name spdx-exceptions
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-spdx-exceptions
Version:	1.0.4
Release:	1%{?dist}
Summary:	list of SPDX standard license exceptions
Url:		https://github.com/kemitchell/spdx-exceptions.json#readme
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	CC-BY-3.0

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
%endif

%description
list of SPDX standard license exceptions

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.json \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/spdx-exceptions

%doc README.md

%changelog
* Mon Nov 23 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build
