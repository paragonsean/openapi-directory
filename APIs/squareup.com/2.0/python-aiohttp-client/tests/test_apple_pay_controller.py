# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.register_domain_request import RegisterDomainRequest
from openapi_server.models.register_domain_response import RegisterDomainResponse


pytestmark = pytest.mark.asyncio

async def test_register_domain(client):
    """Test case for register_domain

    RegisterDomain
    """
    body = {"request_body":{"domain_name":"example.com"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/apple-pay/domains',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

