# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset_families import AssetFamilies
from openapi_server.models.get_asset_family_code200_response import GetAssetFamilyCode200Response
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_asset_families(client):
    """Test case for get_asset_families

    Get list of asset families
    """
    params = [('search_after', 'cursor to the first page')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-families',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_family_code(client):
    """Test case for get_asset_family_code

    Get an asset family
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-families/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_asset_family_code(client):
    """Test case for patch_asset_family_code

    Update/create an asset family
    """
    body = openapi_server.GetAssetFamilyCode200Response()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/asset-families/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

