# **Changelog**

All notable changes to this project will be documented in this file.

## **[2.02]**

- **Added**
  - Docker networks and labels feature

## **[2.01]**

- **Changed**
  - Fix docker installation enabling docker-ce oficial repository
  - Update python version from `3.8.11` to `3.8.12`

## **[2.0]**

- **Changed**
  - Migrate to latest `ansible`, `molecule`, and `testinfra` packages

## **[1.2]**

- **Added**
  - `docker-command`, `docker-entrypoint` to `docker-compose.yml`
  - Able to specify if a volume is a new one or if is an existing one

- **Changed**
  - Environment variables schema

## **[1.1]**

- **Added**
  - Python virtual environment
  - Workspace application

- **Changed**
  - Pipeline definition

## **[1.0]**

- **Added**
  - Creation of generic docker application which supports:
    - Volumes: `volume` and `bind` types
    - Ports
    - Extra Hosts
    - Environment Variables
    - Private/Public Docker Registry
  - System unit creation to run docker container as a system's service
