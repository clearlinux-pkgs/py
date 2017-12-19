#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : py
Version  : 1.5.2
Release  : 36
URL      : http://pypi.debian.net/py/py-1.5.2.tar.gz
Source0  : http://pypi.debian.net/py/py-1.5.2.tar.gz
Summary  : library with cross-python path, ini-parsing, io, code, log facilities
Group    : Development/Tools
License  : MIT
Requires: py-legacypython
Requires: py-python3
Requires: py-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/pypi/v/py.svg
:target: https://pypi.org/project/py

%package legacypython
Summary: legacypython components for the py package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the py package.


%package python
Summary: python components for the py package.
Group: Default
Requires: py-legacypython
Requires: py-python3

%description python
python components for the py package.


%package python3
Summary: python3 components for the py package.
Group: Default
Requires: python3-core

%description python3
python3 components for the py package.


%prep
%setup -q -n py-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511277589
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose ||:
%install
export SOURCE_DATE_EPOCH=1511277589
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
