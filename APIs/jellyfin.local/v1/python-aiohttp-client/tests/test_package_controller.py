# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.package_info import PackageInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.repository_info import RepositoryInfo


pytestmark = pytest.mark.asyncio

async def test_cancel_package_installation(client):
    """Test case for cancel_package_installation

    Cancels a package installation.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Packages/Installing/{package_id}'.format(package_id='package_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_package_info(client):
    """Test case for get_package_info

    Gets a package by name or assembly GUID.
    """
    params = [('assemblyGuid', 'assembly_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Packages/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_packages(client):
    """Test case for get_packages

    Gets available packages.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Packages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_repositories(client):
    """Test case for get_repositories

    Gets all package repositories.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Repositories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_install_package(client):
    """Test case for install_package

    Installs a package.
    """
    params = [('assemblyGuid', 'assembly_guid_example'),
                    ('version', 'version_example'),
                    ('repositoryUrl', 'repository_url_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Packages/Installed/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_repositories(client):
    """Test case for set_repositories

    Sets the enabled and existing package repositories.
    """
    body = {"Enabled":True,"Url":"Url","Name":"Name"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Repositories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

