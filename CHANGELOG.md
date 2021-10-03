# **Changelog**

All notable changes to this project will be documented in this file.

## **[2.01]**

- **Changed**
  - Fix docker installation enabling docker-ce oficial repository

## **[2.0]**

- **Changed**
  - Migrate to latest `ansible`, `molecule`, and `testinfra` packages

## **[1.0]**

- **Added**
  - Creation of generic docker application which supports:
    - Volumes: `volume` and `bind` types
    - Ports
    - Extra Hosts
    - Environment Variables
    - Private/Public Docker Registry
  - System unit creation to run docker container as a system's service
