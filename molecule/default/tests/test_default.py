import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_node_exporter_running(host):
    s = host.service("node_exporter")

    assert s.is_running
    assert s.is_enabled


def test_metrics_endpoint(host):
    metrics = host.check_output('curl -sfL http://localhost:9100/metrics')

    assert 'go_gc_duration_seconds_sum' in metrics
