# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.create_access_token_request import CreateAccessTokenRequest
from openapi_server.models.error import Error
from openapi_server.models.get_access_tokens_response import GetAccessTokensResponse
from openapi_server.models.patch_access_token_request import PatchAccessTokenRequest
from openapi_server.models.v2_access_tokens_uuid_get200_response import V2AccessTokensUuidGet200Response
from openapi_server.models.value_error import ValueError


pytestmark = pytest.mark.asyncio

async def test_v2_access_tokens_get(client):
    """Test case for v2_access_tokens_get

    Get a list of personal access tokens
    """
    params = [('page', 1),
                    ('page_size', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/access-tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_access_tokens_post(client):
    """Test case for v2_access_tokens_post

    Create a personal access token
    """
    body = openapi_server.CreateAccessTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/access-tokens',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_access_tokens_uuid_delete(client):
    """Test case for v2_access_tokens_uuid_delete

    Delete a personal access token
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/access-tokens/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_access_tokens_uuid_get(client):
    """Test case for v2_access_tokens_uuid_get

    Get a personal access token
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/access-tokens/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_access_tokens_uuid_patch(client):
    """Test case for v2_access_tokens_uuid_patch

    Update a personal access token
    """
    body = openapi_server.PatchAccessTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/access-tokens/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

