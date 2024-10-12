# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.instance_read import InstanceRead
from openapi_server.models.instance_write import InstanceWrite


pytestmark = pytest.mark.asyncio

async def test_get_instance_collection(client):
    """Test case for get_instance_collection

    Retrieves the collection of Instance resources.
    """
    params = [('projectId', 'project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/instances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instance_item(client):
    """Test case for get_instance_item

    Retrieves a Instance resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/instances/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_live_instance_item(client):
    """Test case for live_instance_item

    Replaces the Instance resource.
    """
    instance = openapi_server.InstanceWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/instances/{id}/live'.format(id='id_example'),
        headers=headers,
        json=instance,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_logging_instance_item(client):
    """Test case for logging_instance_item

    Replaces the Instance resource.
    """
    instance = openapi_server.InstanceWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/instances/{id}'.format(id='id_example'),
        headers=headers,
        json=instance,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_instance_collection(client):
    """Test case for post_instance_collection

    Creates a Instance resource.
    """
    instance = openapi_server.InstanceWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/agent-instance-updates',
        headers=headers,
        json=instance,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_instance_item(client):
    """Test case for put_instance_item

    Replaces the Instance resource.
    """
    instance = openapi_server.InstanceWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/agent-instance-updates/{id}'.format(id='id_example'),
        headers=headers,
        json=instance,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

