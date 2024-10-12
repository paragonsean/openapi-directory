# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_v1_configuration import FlexV1Configuration


pytestmark = pytest.mark.asyncio

async def test_fetch_configuration(client):
    """Test case for fetch_configuration

    
    """
    params = [('UiVersion', 'ui_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Configuration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

