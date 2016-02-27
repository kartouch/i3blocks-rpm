Name:           i3blocks
Version:        1.4
Release:        1%{?dist}
Summary:        i3blocks is a highly flexible status line for the i3 window manager.

License:        GPLv3
URL:            https://github.com/vivien/i3blocks
Source0:        https://github.com/vivien/i3blocks/releases/download/1.4/i3blocks-1.4.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  rubygem-ronn
Requires: i3 > 4.10
%description
i3blocks is a highly flexible status line for the i3 window manager. It handles clicks, signals and language-agnostic user scripts.
The content of each block (e.g. time, battery status, network state, ...) is the output of a command provided by the user. Blocks are updated on click, at a given interval of time or on a given signal, also specified by the user. It aims to respect the i3bar protocol, providing customization such as text alignment, urgency, color, and more.

%prep
%setup -q


%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/usr/local/libexec/i3blocks/ /usr/local/libexec/i3blocks

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(755,root,root)
/usr/local/bin/i3blocks
/usr/local/libexec/i3blocks
%defattr(644,root,root)
%config(noreplace) /usr/local/etc/i3blocks.conf
%doc /usr/local/share/man/man1/i3blocks.1

%changelog
* Thu Sep 24 2015 Christophe Augello <christophe@augello.be> 1.4-1
- Initial build
