Name:		texlive-bibarts
Version:	2.2
Release:	1
Summary:	"Arts"-style bibliographical information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibarts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibarts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibarts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibarts.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bibarts package assists in making bibliographical lists in
the way that is common in the arts; it requires an auxiliary
program, for which source and a DOS executable are provided.
(Documentation is in German, though bibarts.sty does contain a
brief introduction in English, as a comment.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibarts
%doc %{_texmfdistdir}/doc/latex/bibarts
#- source
%doc %{_texmfdistdir}/source/latex/bibarts

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
