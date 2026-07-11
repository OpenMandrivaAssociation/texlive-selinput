%global tl_name selinput
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Semi-automatic detection of input encoding
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/selinput
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/selinput.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/selinput.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/selinput.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package selects the input encoding by specifying pairs of input
characters and their glyph names.

