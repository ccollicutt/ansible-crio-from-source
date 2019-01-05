import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_running_and_enabled(host):
    crio = host.service("crio")
    assert crio.is_running
    assert crio.is_enabled
