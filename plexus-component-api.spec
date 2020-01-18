%define project_version 1.0-alpha-15

Name:           plexus-component-api
Version:        1.0
Release:        0.16.alpha15%{?dist}
Summary:        Plexus Component API

License:        ASL 2.0
URL:            http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/
#svn export http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/ plexus-component-api-1.0-alpha-15
#tar zcf plexus-component-api-1.0-alpha-15.tar.gz plexus-component-api-1.0-alpha-15/
Source0:        plexus-component-api-1.0-alpha-15.tar.gz

BuildArch: noarch

BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers

%description
Plexus Component API

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{project_version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-0.16.alpha15
- Mass rebuild 2013-12-27

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.alpha15
- Remove workaround for rpm bug #646523
- Add BR on plexus-containers

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.14.alpha15
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Mar 20 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.13.alpha15
- Update to latest guidelines

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.12.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.11.alpha15
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Aug  7 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.10.alpha15
- Move jar to original name format to improve compatibility

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.8.alpha15
- Cleanup spec
- Use maven-3.x to build

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.alpha15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 26 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.5.alpha15
- Add R: plexus-digest

* Thu May 20 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.4.alpha15
- Fix JPP pom name

* Thu May 20 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.3.alpha15
- Add BR:  plexus-digest

* Thu May 20 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.2.alpha15
- Change JPP pom name to prefix JPP-

* Tue May 04 2010 Yong Yang <yyang@redhat.com> - 0:1.0-0.1.alpha15
- Initial build
