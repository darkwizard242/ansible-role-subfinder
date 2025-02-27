[![build-test](https://github.com/darkwizard242/ansible-role-subfinder/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-subfinder/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-subfinder/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-subfinder/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/subfinder) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subfinder&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subfinder) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subfinder&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subfinder) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subfinder&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subfinder) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-subfinder?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-subfinder?color=orange&style=flat-square)

# Ansible Role: Subfinder

Role to install (_by default_) extended [subfinder](https://github.com/projectdiscovery/subfinder) on **Debian/Ubuntu** and **EL** systems. Subfinder is a subdomain discovery tool.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
subfinder_app: subfinder
subfinder_version: 2.6.8
subfinder_os: "{{ ansible_system | lower }}"
subfinder_architecture_map:
  amd64: amd64
  arm: arm64
  x86_64: amd64
  armv6l: armv6
  armv7l: armv7
  aarch64: arm64
  32-bit: "386"
  64-bit: amd64
subfinder_dl_url: "https://github.com/projectdiscovery/{{ subfinder_app }}/releases/download/v{{ subfinder_version }}/{{ subfinder_app }}_{{ subfinder_version }}_{{ subfinder_os}}_{{ subfinder_architecture_map[ansible_architecture] }}.zip"
subfinder_bin_path: /usr/local/bin
subfinder_file_owner: root
subfinder_file_group: root
subfinder_file_mode: '0755'
```

### Variables table:

Variable                   | Description
-------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------
subfinder_app              | Defines the app to install i.e. **subfinder**
subfinder_version          | Defined to dynamically fetch the desired version to install. Defaults to: **2.6.8**
subfinder_os               | Defines os type. Used for obtaining the correct type of binaries based on OS type.
subfinder_architecture_map | Defines os architecture. Used to set the correct type of binaries based on OS System Architecture.
subfinder_dl_url           | Defines URL to download the subfinder binary from.
subfinder_bin_path         | Defined to dynamically set the appropriate path to store subfinder binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
subfinder_file_owner       | Owner for the binary file of subfinder.
subfinder_file_group       | Group for the binary file of subfinder.
subfinder_file_mode        | Mode for the binary file of subfinder.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **subfinder**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.subfinder
```

For customizing behavior of role (i.e. specifying the desired **subfinder** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.subfinder
  vars:
    subfinder_version: 2.3.1
```

For customizing behavior of role (i.e. placing binary of **subfinder** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.subfinder
  vars:
    subfinder_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-subfinder/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
