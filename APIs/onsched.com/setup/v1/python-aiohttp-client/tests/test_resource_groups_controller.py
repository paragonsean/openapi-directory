# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_group_input_model import ResourceGroupInputModel
from openapi_server.models.resource_group_list_view_model import ResourceGroupListViewModel
from openapi_server.models.resource_group_update_model import ResourceGroupUpdateModel
from openapi_server.models.resource_group_view_model import ResourceGroupViewModel
from openapi_server.models.resource_view_model import ResourceViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resourcegroups_get(client):
    """Test case for setup_v1_resourcegroups_get

    List Resource Groups
    """
    params = [('locationId', 'location_id_example'),
                    ('deleted', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resourcegroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resourcegroups_id_delete(client):
    """Test case for setup_v1_resourcegroups_id_delete

    Delete Resource Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/resourcegroups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resourcegroups_id_get(client):
    """Test case for setup_v1_resourcegroups_id_get

    Get Resource Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resourcegroups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resourcegroups_id_put(client):
    """Test case for setup_v1_resourcegroups_id_put

    Update Resource Group
    """
    body = {"name":"name","description":"description","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resourcegroups/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resourcegroups_id_recover_put(client):
    """Test case for setup_v1_resourcegroups_id_recover_put

    Recover Resource Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resourcegroups/{id}/recover'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resourcegroups_post(client):
    """Test case for setup_v1_resourcegroups_post

    Create Resource Group
    """
    body = {"locationId":"locationId","name":"name","description":"description","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/resourcegroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

