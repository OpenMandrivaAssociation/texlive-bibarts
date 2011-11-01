Name:		texlive-bibarts
Version:	20061229
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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bibarts package assists in making bibliographical lists in
the way that is common in the arts; it requires an auxiliary
program, for which source and a DOS executable are provided.
(Documentation is in German, though bibarts.sty does contain a
brief introduction in English, as a comment.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/bibarts/gbibarts.ist
%{_texmfdistdir}/tex/latex/bibarts/bibarts.sty
%doc %{_texmfdistdir}/doc/latex/bibarts/bibarts.pdf
%doc %{_texmfdistdir}/doc/latex/bibarts/bibarts.tex
%doc %{_texmfdistdir}/doc/latex/bibarts/gbib209.bat
%doc %{_texmfdistdir}/doc/latex/bibarts/gbib2e.bat
%doc %{_texmfdistdir}/doc/latex/bibarts/gbibsort.exe
#- source
%doc %{_texmfdistdir}/source/latex/bibarts/gbibsort.c

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
