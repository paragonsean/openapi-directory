# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_provisioning_status import FlexV1ProvisioningStatus


pytestmark = pytest.mark.asyncio

async def test_fetch_provisioning_status(client):
    """Test case for fetch_provisioning_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/provision/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

