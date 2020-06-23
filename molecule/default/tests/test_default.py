import pytest


@pytest.mark.parametrize("name", [
    ("containerd.io-1.2.6-3.3.el7.x86_64"),
    ("docker-ce"),
    ("docker-ce-cli"),
    ("python3-pip"),
])
def test_packages(host, name):
    package = host.package(name)

    assert package.is_installed


@pytest.mark.parametrize("name", [
    ("docker"),
    ("docker-compose"),
])
def test_pip_packages(host, name):
    packages = host.pip_package.get_packages()

    assert name in packages


def test_container(host):
    container = host.docker(name="nginx")

    assert container != None


@pytest.mark.parametrize("path", [
    ("/opt/apps/nginx/docker-compose.yml"),
    ("/opt/apps/nginx/docker-compose.override.yml"),
    ("/lib/systemd/system/nginx.service")
])
def test_files_creation(host, path):
    file = host.file(path)

    assert file.exists


@pytest.mark.parametrize("path", [
    ("/opt/apps/nginx/volumes/test")
])
def test_named_volumes_creation(host, path):
    file = host.file(path)

    assert file.exists


@pytest.mark.parametrize("path", [
    ("/root/test.txt"),
    ("/root/test")
])
def test_bind_volumes_creation(host, path):
    file = host.file(path)

    assert file.exists


@pytest.mark.parametrize("actual_file, expected_file", [
    ("/opt/apps/nginx/docker-compose.yml", "/root/test/resources/docker-compose-expected.yml"),
    ("/opt/apps/nginx/docker-compose.override.yml", "/root/test/resources/docker-compose-expected.override.yml"),
    ("/lib/systemd/system/nginx.service", "/root/test/resources/nginx-expected.service"),

])
def test_generated_file_content(host, actual_file, expected_file):
    expected_file_content = host.file(expected_file).content
    actual_file_content = host.file(actual_file).content

    assert actual_file_content == expected_file_content
