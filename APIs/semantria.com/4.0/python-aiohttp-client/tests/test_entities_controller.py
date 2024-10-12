# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_response_version import EntityResponseVersion


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_entities(client):
    """Test case for add_entities

    Add user entities
    """
    user_entities = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/entities.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=user_entities,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_entities(client):
    """Test case for delete_entities

    Remove user entities
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/entities.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_entities(client):
    """Test case for get_entities

    Retrieve user entities
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/entities.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_entities(client):
    """Test case for update_entities

    Update user entities
    """
    user_entities = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/entities.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=user_entities,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

