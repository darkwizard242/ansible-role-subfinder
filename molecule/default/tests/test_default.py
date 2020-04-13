import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_subfinder_binary_exists(host):
    assert host.file('/usr/local/bin/subfinder').exists


def test_subfinder_binary_file(host):
    assert host.file('/usr/local/bin/subfinder').is_file


def test_subfinder_binary_which(host):
    assert host.check_output('which subfinder') == '/usr/local/bin/subfinder'
