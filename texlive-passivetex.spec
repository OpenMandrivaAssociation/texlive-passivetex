%global tl_name passivetex
%global tl_revision 69742

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support package for XML/SGML typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/formats/xmltex/contrib/passivetex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/passivetex.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Packages providing XML parsing, UTF-8 parsing, Unicode entities, and
common formatting object definitions for jadetex.

