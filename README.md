node-exporter
=========
  [![Build Status](https://travis-ci.org/coaxial/ansible-role-node-exporter.svg?branch=master)](https://travis-ci.org/coaxial/ansible-role-node-exporter)

Install Prometheus' node_exporter and run it as a service.

Role Variables
--------------

Name | Default | Possible values | Description
---|---|---|---
`ne__pkg_checksum` | SHA256 sum for version | Verify the downloaded archive | any valid checksum as per the [`get_url` module](https://docs.ansible.com/ansible/2.5/modules/get_url_module.html?highlight=get_url).
`ne__pkg_version` | cf. [here](defaults/main.yml) | Select which node_exporter version to install | string like `0.0.0`
`ne__exporter_dir` | `/opt/prometheus/exporters` | Where to put the node_exporter binary | Any valid path (will be created if it doesn't exist)


Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - node-exporter
```

License
-------

MIT

Author Information
------------------

Coaxial ([64b.it](https://64b.it))
