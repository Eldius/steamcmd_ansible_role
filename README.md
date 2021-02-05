steamcmd_ansible_role
=========

![Molecule](https://github.com/Eldius/steamcmd_ansible_role/workflows/Molecule/badge.svg)

Requirements
------------

None

Role Variables
--------------

- `steamcmd_login_user`: User to login into Steam servers (default to 'anonymous')
- `steamcmd_login_pass`: Pass to login into Steam servers (default to '')
- `steamcmd_user`: OS username to run SteamCMD on (default to 'steam')
- `steamcmd_home`: Steam OS user home folder (default to '/home/steam')
- `steamcmd_installation_folder`: SteamCMD install folder (default to '/home/steam/Steam')
- `steamcmd_command`: SteamCMD script name, `don't touch this, please` (fefault to './steamcmd.sh')
- `steamcmd_download_link`: SteamCMD download link, `don't touch this too, please` (default to 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz')
- `steamcmd_debug`: downloads the SteamCMD install folder as a `.tar.bz2` package (default to 'False')

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, steamcmd_login_user: user, steamcmd_login_pass: pass }

License
-------

GPL-2.0-or-later

Author Information
------------------

My Github profile [Eldius](https://github.com/Eldius)
