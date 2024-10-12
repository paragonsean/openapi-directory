# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token_info_response import AccessTokenInfoResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_oauth_v1_access_tokens_token_get(client):
    """Test case for get_oauth_v1_access_tokens_token_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/oauth/v1/access-tokens/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

