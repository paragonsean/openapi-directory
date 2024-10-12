# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verify_request_with_psd2200_response import VerifyRequestWithPSD2200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_verify_request(client):
    """Test case for verify_request

    Request a Verification
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'api_secret': 'api_secret_example',
        'brand': 'brand_example',
        'code_length': 4,
        'country': 'country_example',
        'lg': en-us,
        'next_event_wait': 300,
        'number': 'number_example',
        'pin_code': 'pin_code_example',
        'pin_expiry': 300,
        'sender_id': 'VERIFY',
        'workflow_id': 1
        }
    response = await client.request(
        method='POST',
        path='/verify/{format}'.format(format='json'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

