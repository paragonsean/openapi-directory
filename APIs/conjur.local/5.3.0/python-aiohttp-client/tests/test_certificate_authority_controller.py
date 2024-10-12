# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sign201_response import Sign201Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_sign(client):
    """Test case for sign

    Gets a signed certificate from the configured Certificate Authority service.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
        'accept': 'application/x-pem-file',
        'conjurAuth': 'special-key',
    }
    data = {
        'csr': 'csr_example',
        'ttl': 'ttl_example'
        }
    response = await client.request(
        method='POST',
        path='/ca/{account}/{service_id}/sign'.format(account='account_example', service_id='ca-service'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

