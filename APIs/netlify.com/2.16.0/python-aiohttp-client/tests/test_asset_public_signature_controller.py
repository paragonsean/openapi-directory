# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset_public_signature import AssetPublicSignature
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_site_asset_public_signature(client):
    """Test case for get_site_asset_public_signature

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/assets/{asset_id}/public_signature'.format(site_id='site_id_example', asset_id='asset_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

