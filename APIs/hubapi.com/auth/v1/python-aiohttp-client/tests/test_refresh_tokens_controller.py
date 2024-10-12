# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.refresh_token_info_response import RefreshTokenInfoResponse


pytestmark = pytest.mark.asyncio

async def test_delete_oauth_v1_refresh_tokens_token_archive(client):
    """Test case for delete_oauth_v1_refresh_tokens_token_archive

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/oauth/v1/refresh-tokens/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_oauth_v1_refresh_tokens_token_get(client):
    """Test case for get_oauth_v1_refresh_tokens_token_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/oauth/v1/refresh-tokens/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

