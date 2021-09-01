import pytest


@pytest.mark.parametrize("name", [
    ("containerd.io"),
    ("iptables-services"),
    ("docker-ce"),
    ("docker-ce-cli"),
    ("python3-pip"),
    ("unzip"),
    ("wget"),
    ("curl"),
    ("bind-utils"),
])
def test_packages(host, name):
    package = host.package(name)

    assert package.is_installed


@pytest.mark.parametrize("name", [
    ("docker"),
    ("docker-compose"),
])
def test_pip_packages(host, name):
    packages = host.pip.get_packages()

    assert name in packages


def test_container(host):
    container = host.docker(name="nginx")

    assert container != None


@pytest.mark.parametrize("path", [
    ("/opt/test/apps/nginx/docker-compose.override.yml"),
])
def test_files_creation(host, path):
    file = host.file(path)

    assert file.exists


@pytest.mark.parametrize("path", [
    ("/lib/systemd/system/nginx.service"),
])
def test_no_files_creation(host, path):
    file = host.file(path)

    assert file.exists == False


@pytest.mark.parametrize("path", [("/opt/test/apps/nginx/volumes/test")])
def test_named_volumes_creation(host, path):
    file = host.file(path)

    assert file.exists


@pytest.mark.parametrize("path", [("/opt/test/apps/nginx/volumes/test1")])
def test_named_volumes_no_creation(host, path):
    file = host.file(path)

    assert file.exists == False


@pytest.mark.parametrize("path", [("/root/test.txt"), ("/root/test")])
def test_bind_volumes_creation(host, path):
    file = host.file(path)

    assert file.exists


@pytest.mark.parametrize("actual_file, expected_file", [
    ("/opt/test/apps/nginx/docker-compose.override.yml",
     "/root/test/resources/docker-compose-expected.override.yml"),
])
def test_generated_file_content(host, actual_file, expected_file):
    expected_file_content = host.file(expected_file).content
    actual_file_content = host.file(actual_file).content

    assert actual_file_content == expected_file_content
