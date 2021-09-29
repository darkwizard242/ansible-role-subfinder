[![build-test](https://github.com/darkwizard242/ansible-role-subfinder/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-subfinder/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-subfinder/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-subfinder/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47867?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47867?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47867?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subfinder&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-subfinder) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subfinder&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subfinder) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subfinder&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subfinder) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-subfinder&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-subfinder) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-subfinder?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-subfinder?color=orange&style=flat-square)

# Ansible Role: Subfinder

Role to install (_by default_) extended [subfinder](https://github.com/projectdiscovery/subfinder) on **Debian/Ubuntu** and **EL** systems. Subfinder is a subdomain discovery tool.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
subfinder_app: subfinder
subfinder_version: 2.4.8
subfinder_app_owner: root
subfinder_app_group: root
subfinder_osarch: linux_amd64
subfinder_dl_url: "https://github.com/projectdiscovery/{{ subfinder_app }}/releases/download/v{{ subfinder_version }}/{{ subfinder_app }}_{{ subfinder_version }}_{{ subfinder_osarch }}.tar.gz"
subfinder_bin_path: /usr/local/bin
```

### Variables table:

Variable            | Value (default)                                                                                                                                                                  | Description
------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------
subfinder_app       | subfinder                                                                                                                                                                        | Defines the app to install i.e. **subfinder**
subfinder_version   | 2.4.5                                                                                                                                                                            | Defined to dynamically fetch the desired version to install. Defaults to: **2.4.8**
subfinder_app_owner | root                                                                                                                                                                             | Defined to dynamically set the owner for the file..
subfinder_app_group | root                                                                                                                                                                             | Defined to dynamically set the primary group for the file.
subfinder_osarch    | linux_amd64                                                                                                                                                                      | Defines os architecture.
subfinder_dl_url    | "<https://github.com/projectdiscovery/{{> subfinder_app }}/releases/download/v{{ subfinder_version }}/{{ subfinder_app }}_{{ subfinder_version }}_{{ subfinder_osarch }}.tar.gz" | Defines URL to download the subfinder binary from.
subfinder_bin_path  | /usr/local/bin                                                                                                                                                                   | Defined to dynamically set the appropriate path to store subfinder binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
