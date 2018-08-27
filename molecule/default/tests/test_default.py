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
    # Install curl because Debian doesn't come with either curl or wget
    host.ansible('package', 'name=curl state=present', check=False)

    metrics = host.check_output('curl -sfL http://localhost:9100/metrics || ' +
                                'wget -q http://localhost:9100/metrics -O -')

    # And remove it when we're done
    host.ansible('package', 'name=curl state=absent', check=False)

    assert 'go_gc_duration_seconds_sum' in metrics
