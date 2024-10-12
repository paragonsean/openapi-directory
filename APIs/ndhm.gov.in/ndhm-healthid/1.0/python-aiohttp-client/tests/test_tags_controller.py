# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tag_request import TagRequest


pytestmark = pytest.mark.asyncio

async def test_add_tag_using_post(client):
    """Test case for add_tag_using_post

    Add tag against HealthId.
    """
    tag_request = {"healthId":"healthId","tags":{"key":"tags"}}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/ha/tags',
        headers=headers,
        json=tag_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_tag_using_delete(client):
    """Test case for delete_tag_using_delete

    Delete tag against HealthId.
    """
    tag_request = openapi_server.TagRequest()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/ha/tags',
        headers=headers,
        json=tag_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_using_get(client):
    """Test case for get_tags_using_get

    Get list of Tags against HealthID.
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/ha/tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

