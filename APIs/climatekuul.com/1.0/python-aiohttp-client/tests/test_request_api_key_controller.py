# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_request_api_key(client):
    """Test case for request_api_key

    requestApiKey
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key_l1': 'api_key_l1_example',
        'api_key_l2': 'api_key_l2_example',
        'email': 'email_example',
        'password': 56,
        'user_first_name': 'user_first_name_example',
        'user_last_name': 'user_last_name_example'
        }
    response = await client.request(
        method='POST',
        path='/footprint/requestApiKey',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

