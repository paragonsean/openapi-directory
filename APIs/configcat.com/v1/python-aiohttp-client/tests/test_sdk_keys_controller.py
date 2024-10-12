# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sdk_keys_model import SdkKeysModel


pytestmark = pytest.mark.asyncio

async def test_get_sdk_keys(client):
    """Test case for get_sdk_keys

    Get SDK Key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/configs/{config_id}/environments/{environment_id}'.format(config_id='config_id_example', environment_id='environment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

