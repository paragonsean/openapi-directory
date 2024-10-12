# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_group_input_model import ServiceGroupInputModel
from openapi_server.models.service_group_list_view_model import ServiceGroupListViewModel
from openapi_server.models.service_group_view_model import ServiceGroupViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_servicegroups_get(client):
    """Test case for setup_v1_servicegroups_get

    List Service Groups
    """
    params = [('locationId', 'location_id_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/servicegroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_servicegroups_id_delete(client):
    """Test case for setup_v1_servicegroups_id_delete

    Delete Service Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/servicegroups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_servicegroups_id_get(client):
    """Test case for setup_v1_servicegroups_id_get

    Get Service Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/servicegroups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_servicegroups_id_put(client):
    """Test case for setup_v1_servicegroups_id_put

    Update Service Group
    """
    body = {"locationId":"locationId","name":"name","description":"description","type":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/servicegroups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_servicegroups_id_recover_put(client):
    """Test case for setup_v1_servicegroups_id_recover_put

    Recover Service Group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/servicegroups/{id}/recover'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_servicegroups_post(client):
    """Test case for setup_v1_servicegroups_post

    Create Service Group
    """
    body = {"locationId":"locationId","name":"name","description":"description","type":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/servicegroups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

