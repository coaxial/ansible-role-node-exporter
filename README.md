node-exporter Ansible role
=========

Install Prometheus' node_exporter and runs it as a service (Ubuntu/Debian only)

Requirements
------------

- Python 2 on host (see the [raw-python role](https://github.com/coaxial/ansible-role-raw-python) to set it up)

Role Variables
--------------

Name | Default | Purpose | Possible values
---|---|---|---
`ne__pkg_checksum` | SHA256 sum for version | Verify the downloaded archive | any valid checksum as per the [`get_url` module](https://docs.ansible.com/ansible/2.5/modules/get_url_module.html?highlight=get_url).
`ne__pkg_version` | cf. [here](defaults/main.yml) | Select which node_exporter version to install | string like `0.0.0`
`ne__exporter_dir` | `/opt/prometheus/exporters` | Where to put the node_exporter binary | Any valid path (will be created if it doesn't exist)

Dependencies
------------

N/A

Example Playbook
----------------

    ---
    - hosts: all
      roles:
        - coaxial.node-exporter

License
-------

MIT

Author Information
------------------

coaxial<[64b.it](https://64b.it)>
