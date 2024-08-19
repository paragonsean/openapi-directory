# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_patch import KeyPatch
from openapi_server.models.key_post import KeyPost
from openapi_server.models.key_response import KeyResponse


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_keys_get(client):
    """Test case for apps_app_id_keys_get

    Lists app keys
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{app_id}/keys'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_keys_key_id_patch(client):
    """Test case for apps_app_id_keys_key_id_patch

    Updates a key
    """
    body = openapi_server.KeyPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/apps/{app_id}/keys/{key_id}'.format(app_id='app_id_example', key_id='key_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_keys_key_id_revoke_post(client):
    """Test case for apps_app_id_keys_key_id_revoke_post

    Revokes a key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/apps/{app_id}/keys/{key_id}/revoke'.format(app_id='app_id_example', key_id='key_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_keys_post(client):
    """Test case for apps_app_id_keys_post

    Creates a key
    """
    body = openapi_server.KeyPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/apps/{app_id}/keys'.format(app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

