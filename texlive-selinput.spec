Name:		texlive-selinput
Version:	53098
Release:	2
Summary:	Semi-automatic detection of input encoding
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/selinput
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selinput.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selinput.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/selinput.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package selects the input encoding by specifying pairs of
input characters and their glyph names.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/selinput
%{_texmfdistdir}/tex/latex/selinput
%doc %{_texmfdistdir}/doc/latex/selinput

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
