import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = "subfinder"
PACKAGE_BINARY = "/usr/local/bin/subfinder"


def test_subfinder_binary_exists(host):
    """
    Tests if subfinder binary file exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_subfinder_binary_file(host):
    """
    Tests if subfinder binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_subfinder_binary_which(host):
    """
    Tests the output to confirm subfinder's binary location.
    """
    assert host.check_output('which subfinder') == PACKAGE_BINARY
