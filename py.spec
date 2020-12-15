#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : py
Version  : 1.10.0
Release  : 78
URL      : https://files.pythonhosted.org/packages/0d/8c/50e9f3999419bb7d9639c37e83fa9cdcf0f601a9d407162d6c37ad60be71/py-1.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/8c/50e9f3999419bb7d9639c37e83fa9cdcf0f601a9d407162d6c37ad60be71/py-1.10.0.tar.gz
Summary  : library with cross-python path, ini-parsing, io, code, log facilities
Group    : Development/Tools
License  : MIT
Requires: py-license = %{version}-%{release}
Requires: py-python = %{version}-%{release}
Requires: py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : setuptools-python
BuildRequires : setuptools_scm

%description
.. image:: https://img.shields.io/pypi/v/py.svg
:target: https://pypi.org/project/py

%package license
Summary: license components for the py package.
Group: Default

%description license
license components for the py package.


%package python
Summary: python components for the py package.
Group: Default
Requires: py-python3 = %{version}-%{release}

%description python
python components for the py package.


%package python3
Summary: python3 components for the py package.
Group: Default
Requires: python3-core
Provides: pypi(py)

%description python3
python3 components for the py package.


%prep
%setup -q -n py-1.10.0
cd %{_builddir}/py-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607929342
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest --verbose || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/py
cp %{_builddir}/py-1.10.0/LICENSE %{buildroot}/usr/share/package-licenses/py/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
cp %{_builddir}/py-1.10.0/py/_vendored_packages/iniconfig-1.1.1.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/py/cf3eaf29116a37a7d9ba773e776104c067c8e5fc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/py/cf3eaf29116a37a7d9ba773e776104c067c8e5fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
