# revision 15878
# category Package
# catalog-ctan /macros/xmltex/contrib/passivetex
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-passivetex
Version:	20080420
Release:	3
Summary:	Support package for XML/SGML typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xmltex/contrib/passivetex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/passivetex.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Packages providing XML parsing, UTF-8 parsing, Unicode
entities, and common formatting object definitions for jadetex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080420-2
+ Revision: 754656
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080420-1
+ Revision: 719201
- texlive-passivetex
- texlive-passivetex
- texlive-passivetex
- texlive-passivetex

