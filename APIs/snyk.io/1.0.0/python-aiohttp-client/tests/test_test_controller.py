# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.test_composer_json_composer_lock_file_request import TestComposerJsonComposerLockFileRequest
from openapi_server.models.test_dep_graph_request import TestDepGraphRequest
from openapi_server.models.test_gemfile_lock_file_request import TestGemfileLockFileRequest
from openapi_server.models.test_gopkg_toml_gopkg_lock_file_request import TestGopkgTomlGopkgLockFileRequest
from openapi_server.models.test_gradle_file_request import TestGradleFileRequest
from openapi_server.models.test_maven_file_request import TestMavenFileRequest
from openapi_server.models.test_package_json_package_lock_json_file_request import TestPackageJsonPackageLockJsonFileRequest
from openapi_server.models.test_package_json_yarn_lock_file_request import TestPackageJsonYarnLockFileRequest
from openapi_server.models.test_requirements_txt_file_request import TestRequirementsTxtFileRequest
from openapi_server.models.test_sbt_file_request import TestSbtFileRequest
from openapi_server.models.test_vendor_json_file_request import TestVendorJsonFileRequest


pytestmark = pytest.mark.asyncio

async def test_test_composer_json_composer_lock_file(client):
    """Test case for test_composer_json_composer_lock_file

    Test composer.json & composer.lock file
    """
    body = openapi_server.TestComposerJsonComposerLockFileRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/composer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_dep_graph(client):
    """Test case for test_dep_graph

    Test Dep Graph
    """
    body = openapi_server.TestDepGraphRequest()
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/dep-graph',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_for_issues_in_a_public_gem_by_name_and_version(client):
    """Test case for test_for_issues_in_a_public_gem_by_name_and_version

    Test for issues in a public gem by name and version
    """
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/test/rubygems/{gem_name}/{version}'.format(gem_name='rails-html-sanitizer', version='1.0.3'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_for_issues_in_a_public_package_by_group_id_artifact_id_and_version(client):
    """Test case for test_for_issues_in_a_public_package_by_group_id_artifact_id_and_version

    Test for issues in a public package by group id, artifact id and version
    """
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7'),
                    ('repository', 'https://repo1.maven.org/maven2')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/test/maven/{group_id}/{artifact_id}/{version}'.format(group_id='org.apache.flex.blazeds', artifact_id='blazeds', version='4.7.2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_for_issues_in_a_public_package_by_group_name_and_version(client):
    """Test case for test_for_issues_in_a_public_package_by_group_name_and_version

    Test for issues in a public package by group, name and version
    """
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7'),
                    ('repository', 'https://repo1.maven.org/maven2')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/test/gradle/{group}/{name}/{version}'.format(group='org.apache.flex.blazeds', name='blazeds', version='4.7.2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_for_issues_in_a_public_package_by_name_and_version(client):
    """Test case for test_for_issues_in_a_public_package_by_name_and_version

    Test for issues in a public package by name and version
    """
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/test/npm/{package_name}/{version}'.format(package_name='ms', version='0.7.0'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gemfile_lock_file(client):
    """Test case for test_gemfile_lock_file

    Test gemfile.lock file
    """
    body = openapi_server.TestGemfileLockFileRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/rubygems',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gopkg_toml_gopkg_lock_file(client):
    """Test case for test_gopkg_toml_gopkg_lock_file

    Test Gopkg.toml & Gopkg.lock File
    """
    body = openapi_server.TestGopkgTomlGopkgLockFileRequest()
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/golangdep',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_gradle_file(client):
    """Test case for test_gradle_file

    Test gradle file
    """
    body = openapi_server.TestGradleFileRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/gradle',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_maven_file(client):
    """Test case for test_maven_file

    Test maven file
    """
    body = openapi_server.TestMavenFileRequest()
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7'),
                    ('repository', 'https://repo1.maven.org/maven2')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/maven',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_package_json_package_lock_json_file(client):
    """Test case for test_package_json_package_lock_json_file

    Test package.json & package-lock.json File
    """
    body = openapi_server.TestPackageJsonPackageLockJsonFileRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/npm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_package_json_yarn_lock_file(client):
    """Test case for test_package_json_yarn_lock_file

    Test package.json & yarn.lock File
    """
    body = openapi_server.TestPackageJsonYarnLockFileRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/yarn',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_pip_package_name_version_get(client):
    """Test case for test_pip_package_name_version_get

    Test for issues in a public package by name and version
    """
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/test/pip/{package_name}/{version}'.format(package_name='rsa', version='3.3'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_requirements_txt_file(client):
    """Test case for test_requirements_txt_file

    Test requirements.txt file
    """
    body = openapi_server.TestRequirementsTxtFileRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/pip',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_sbt_file(client):
    """Test case for test_sbt_file

    Test sbt file
    """
    body = openapi_server.TestSbtFileRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/sbt',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_sbt_group_id_artifact_id_version_get(client):
    """Test case for test_sbt_group_id_artifact_id_version_get

    Test for issues in a public package by group id, artifact id and version
    """
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7'),
                    ('repository', 'https://repo1.maven.org/maven2')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
    }
    response = await client.request(
        method='GET',
        path='/v1/test/sbt/{group_id}/{artifact_id}/{version}'.format(group_id='org.apache.flex.blazeds', artifact_id='blazeds', version='4.7.2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_vendor_json_file(client):
    """Test case for test_vendor_json_file

    Test vendor.json File
    """
    body = openapi_server.TestVendorJsonFileRequest()
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/test/govendor',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

