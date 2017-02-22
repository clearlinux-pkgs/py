#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : py
Version  : 1.4.32
Release  : 24
URL      : https://pypi.python.org/packages/93/bd/8a90834a287e0c1682eab8e20ada672e4f4cf7d5b99f2833ddbf31ed1a6d/py-1.4.32.tar.gz
Source0  : https://pypi.python.org/packages/93/bd/8a90834a287e0c1682eab8e20ada672e4f4cf7d5b99f2833ddbf31ed1a6d/py-1.4.32.tar.gz
Summary  : library with cross-python path, ini-parsing, io, code, log facilities
Group    : Development/Tools
License  : MIT
Requires: py-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/pypi/pyversions/pytest.svg
:target: https://pypi.org/project/py
.. image:: https://img.shields.io/travis/pytest-dev/py.svg
:target: https://travis-ci.org/pytest-dev/py

%package python
Summary: python components for the py package.
Group: Default

%description python
python components for the py package.


%prep
%setup -q -n py-1.4.32

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487782813
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test --verbose ||:
%install
export SOURCE_DATE_EPOCH=1487782813
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
