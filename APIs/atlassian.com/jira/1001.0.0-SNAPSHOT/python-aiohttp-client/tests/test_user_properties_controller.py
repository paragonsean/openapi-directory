# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.property_keys import PropertyKeys


pytestmark = pytest.mark.asyncio

async def test_delete_user_property(client):
    """Test case for delete_user_property

    Delete user property
    """
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('userKey', 'user_key_example'),
                    ('username', 'username_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/user/properties/{property_key}'.format(property_key='property_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_property(client):
    """Test case for get_user_property

    Get user property
    """
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('userKey', 'user_key_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/properties/{property_key}'.format(property_key='property_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_property_keys(client):
    """Test case for get_user_property_keys

    Get user property keys
    """
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('userKey', 'user_key_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/user/properties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_user_property(client):
    """Test case for set_user_property

    Set user property
    """
    body = None
    params = [('accountId', '5b10ac8d82e05b22cc7d4ef5'),
                    ('userKey', 'user_key_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/user/properties/{property_key}'.format(property_key='property_key_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

