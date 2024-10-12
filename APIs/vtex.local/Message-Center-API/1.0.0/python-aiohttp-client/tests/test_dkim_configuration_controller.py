# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model200_ok import Model200OK
from openapi_server.models.model401_unauthorized import Model401Unauthorized


pytestmark = pytest.mark.asyncio

async def test_create_dkim(client):
    """Test case for create_dkim

    Generate DKIM keys
    """
    headers = { 
        'Accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/mail-service/pvt/providers/{email_provider}/dkim'.format(email_provider='help@valdie.co'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

