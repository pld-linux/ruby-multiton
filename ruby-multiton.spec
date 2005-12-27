Summary:	Ruby implementation of the Multiton pattern
Summary(pl):	Implementacja wzorca Multiton dla jêzyka Ruby
Name:		ruby-Multiton
Version:	1.0.2
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.codeforpeople.com/lib/ruby/multiton/multiton-%{version}.tgz
# Source0-md5:	15c7e51021825782f1713b4db36f466f
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
BuildRequires:	ruby-devel
Requires:	ruby-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby implementation of the Multiton pattern.

%description -l pl
Implementacja wzorca Multiton dla jêzyka Ruby.

%prep
%setup -q -n multiton-%{version}

%build
rdoc -o rdoc/ --main README README lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
install lib/multiton.rb $RPM_BUILD_ROOT%{ruby_rubylibdir}/multiton.rb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/* README
%{ruby_rubylibdir}/multiton.rb
