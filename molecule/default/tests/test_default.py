import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_user_is_present(host):
    u = host.user('steam')

    assert u.exists
    assert u.name == 'steam'
    assert u.group == 'steam'


def test_install_folder_is_present(host):
    f = host.file('/home/steam/Steam')

    assert f.exists
    assert f.user == 'steam'
    assert f.group == 'steam'
    assert f.is_directory


def test_steamcmd_script_is_present(host):
    f = host.file('/home/steam/Steam/steamcmd.sh')

    assert f.exists
    assert f.user == 'steam'
    assert f.group == 'steam'
    assert f.is_file


def test_package_folder_is_present(host):
    f = host.file('/home/steam/Steam/package')

    assert f.exists
    assert f.user == 'steam'
    assert f.group == 'steam'
    assert f.is_directory


def test_userdata_is_present(host):
    f = host.file('/home/steam/Steam/userdata/anonymous/config')

    assert f.exists
    assert f.user == 'steam'
    assert f.group == 'steam'
    assert f.is_directory
