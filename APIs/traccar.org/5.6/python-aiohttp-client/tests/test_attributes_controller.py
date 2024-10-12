# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute import Attribute


pytestmark = pytest.mark.asyncio

async def test_attributes_computed_get(client):
    """Test case for attributes_computed_get

    Fetch a list of Attributes
    """
    params = [('all', True),
                    ('userId', 56),
                    ('deviceId', 56),
                    ('groupId', 56),
                    ('refresh', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/attributes/computed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attributes_computed_id_delete(client):
    """Test case for attributes_computed_id_delete

    Delete an Attribute
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/attributes/computed/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attributes_computed_id_put(client):
    """Test case for attributes_computed_id_put

    Update an Attribute
    """
    body = {"expression":"expression","description":"description","attribute":"attribute","id":0,"type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/attributes/computed/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attributes_computed_post(client):
    """Test case for attributes_computed_post

    Create an Attribute
    """
    body = {"expression":"expression","description":"description","attribute":"attribute","id":0,"type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/attributes/computed',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

