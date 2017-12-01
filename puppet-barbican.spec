%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:                   puppet-barbican
Version:                11.3.1
Release:                1%{?dist}
Summary:                Puppet module for OpenStack Barbican
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-barbican

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-stdlib
Requires:               puppet-keystone
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet >= 2.7.0

%description
Puppet module which installs and configures OpenStack Barbican.

%prep
%setup -q -n openstack-barbican-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/barbican/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/barbican/



%files
%{_datadir}/openstack-puppet/modules/barbican/


%changelog
* Fri Dec 01 2017 RDO <dev@lists.rdoproject.org> 11.3.1-1
- Update to 11.3.1

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 11.3.0-1
- Update to 11.3.0



