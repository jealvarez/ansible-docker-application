# **Docker Application Template**

[![actions-workflow-test][actions-workflow-test-badge]][actions-workflow-test]

Provides the configuration to run any application in a docker container.

## **Author**

Jorge Alvarez <alvarez.jeap@gmail.com>

## **Requirements**

- Ansible 2.6+
- Python 3+
- Pip3

## **Setting Up the Environment**

- Set python virtual environment

```sh
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## **Testing**

- Run molecule test scenario

```sh
molecule test --all
```

## **Role**

### **Variables**

```text
application_name: application
auto_startup: y
docker_registry_url:
docker_registry_username:
docker_registry_password:
docker_registry_private: n
docker_image_name:
docker_image_tag:
docker_user:
docker_ports: []
docker_volumes: []
docker_environment_variables: []
docker_extra_hosts: []
```

#### **Variables Description**

- **docker_ports**. It will define the ports available for the docker container.

```text
docker_ports:
  - 5555:5555
  - 5551:551
```

- **docker_volumes**. It will define a docker volume for the docker container.

  ```text
  docker_volumes:
    - type:
      source:
      destination:
      directory:
      file:
      external:
  ```

  - Volume types:
    - **volume**. It will create a docker volume and a directory under `/opt/apps/${application}/volumes` to hold on all files from the container
      - type. `volume`
      - source. name of the `named` docker volume
      - destination. path inside of the container
      - directory. always `true`

      ```text
      docker_volumes: 
        - type: volume
          source: pg-data
          destination: /var/lib/postgresql/data
          directory: true
      ```

    - **bind**. It will mount in the container a directory that already exists
      - type. `bind`
      - source. path from the host
      - destination. path inside of the container
      - directory. `true` or `false`
      - file. name of the file to mount
      - external. `false` if it's inside of the `/opt/apps/${application}` or `true` if is outside

      ```text
      docker_volumes:
        - type: bind
          source: conf
          destination: /etc/nginx/nginx.conf:ro
          directory: false
          external: false
          file: nginx.conf
      ```

- **docker_environment_variables**. It will define environment variables for the docker container.

```text
docker_environment_variables:
  - "VAR1: VALUE1"
  - "VAR2: VALUE2"
```

- **docker_extra_hosts**. It will define extra hosts for the docker container.

```text
docker_extra_hosts:
  - HOST1:IP1
  - HOST2:IP2
```

## **Playbook**

```text
---
- name: configure docker application
  hosts: localhost
  roles:
    - docker-application
  vars:
    application_name: nginx
    auto_startup: y
    docker_registry_url: https://docker-registry.private.com/
    docker_registry_username: username
    docker_registry_password: password
    docker_registry_private: y
    docker_image_name: nginx
    docker_image_tag: latest
    docker_user: root
    docker_ports:
      - 80:80
    docker_volumes:
      - type: bind
        source: conf
        destination: /etc/nginx/nginx.conf:ro
        directory: false
        external: false
        file: nginx.conf
    docker_environment_variables:
      - "VAR1: VALUE1"
    docker_extra_hosts:
      - HOST1:IP1
```
