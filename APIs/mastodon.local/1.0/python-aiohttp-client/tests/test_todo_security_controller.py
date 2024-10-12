# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v1_accounts_post_request import ApiV1AccountsPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_accounts_post(client):
    """Test case for api_v1_accounts_post

    
    """
    body = openapi_server.ApiV1AccountsPostRequest()
    headers = { 
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

