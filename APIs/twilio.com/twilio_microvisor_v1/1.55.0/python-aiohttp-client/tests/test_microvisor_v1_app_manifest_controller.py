# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.microvisor_v1_app_app_manifest import MicrovisorV1AppAppManifest


pytestmark = pytest.mark.asyncio

async def test_fetch_app_manifest(client):
    """Test case for fetch_app_manifest

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Apps/{app_sid}/Manifest'.format(app_sid='app_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

