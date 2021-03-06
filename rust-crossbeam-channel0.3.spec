# Generated by rust2rpm 10
%bcond_with check
%global debug_package %{nil}

%global crate crossbeam-channel

Name:           rust-%{crate}0.3
Version:        0.3.9
Release:        2%{?dist}
Summary:        Multi-producer multi-consumer channels for message passing

# Upstream license specification: MIT/Apache-2.0 AND BSD-2-Clause
License:        (MIT or ASL 2.0) and BSD
URL:            https://crates.io/crates/crossbeam-channel
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Multi-producer multi-consumer channels for message passing.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE LICENSE-THIRD-PARTY
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 11:25:36 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.9-1
- Initial package
