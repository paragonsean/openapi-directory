# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_resource_description import ApplicationResourceDescription
from openapi_server.models.application_resource_upgrade_progress_info import ApplicationResourceUpgradeProgressInfo
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_application_resource_description_list import PagedApplicationResourceDescriptionList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_mesh_application_create_or_update(client):
    """Test case for mesh_application_create_or_update

    Creates or updates a Application resource.
    """
    application_resource_description = openapi_server.ApplicationResourceDescription()
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/Resources/Applications/{application_resource_name}'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        json=application_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_application_delete(client):
    """Test case for mesh_application_delete

    Deletes the Application resource.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/Resources/Applications/{application_resource_name}'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_application_get(client):
    """Test case for mesh_application_get

    Gets the Application resource with the given name.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_application_get_upgrade_progress(client):
    """Test case for mesh_application_get_upgrade_progress

    Gets the progress of the latest upgrade performed on this application resource.
    """
    params = [('api-version', 7.0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications/{application_resource_name}/$/GetUpgradeProgress'.format(application_resource_name='application_resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh_application_list(client):
    """Test case for mesh_application_list

    Lists all the application resources.
    """
    params = [('api-version', 6.4-preview)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Resources/Applications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

