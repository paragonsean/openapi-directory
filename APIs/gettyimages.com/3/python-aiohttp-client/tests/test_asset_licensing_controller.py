# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.acquire_asset_licenses_request import AcquireAssetLicensesRequest
from openapi_server.models.asset_licensing_response import AssetLicensingResponse


pytestmark = pytest.mark.asyncio

async def test_v3_asset_licensing_asset_id_post(client):
    """Test case for v3_asset_licensing_asset_id_post

    Endpoint for acquiring extended licenses with iStock credits for an asset.
    """
    body = {"extended_licenses":["multiseat","multiseat"],"use_team_credits":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/asset-licensing/{asset_id}'.format(asset_id='asset_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

