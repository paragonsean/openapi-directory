# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.kyc_response import KycResponse


pytestmark = pytest.mark.asyncio

async def test_get_kyc(client):
    """Test case for get_kyc

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/kyc',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

