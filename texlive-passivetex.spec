Name:		texlive-passivetex
Version:	20080420
Release:	1
Summary:	Support package for XML/SGML typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xmltex/contrib/passivetex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/passivetex.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Packages providing XML parsing, UTF-8 parsing, Unicode
entities, and common formatting object definitions for jadetex.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xmltex/passivetex/dummyels.sty
%{_texmfdistdir}/tex/xmltex/passivetex/fotex.sty
%{_texmfdistdir}/tex/xmltex/passivetex/fotex.xmt
%{_texmfdistdir}/tex/xmltex/passivetex/mlnames.sty
%{_texmfdistdir}/tex/xmltex/passivetex/tei.xmt
%{_texmfdistdir}/tex/xmltex/passivetex/teiprintslides.xmt
%{_texmfdistdir}/tex/xmltex/passivetex/teislides.xmt
%{_texmfdistdir}/tex/xmltex/passivetex/teixml.sty
%{_texmfdistdir}/tex/xmltex/passivetex/teixmlslides.sty
%{_texmfdistdir}/tex/xmltex/passivetex/ucharacters.sty
%{_texmfdistdir}/tex/xmltex/passivetex/unicode.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
