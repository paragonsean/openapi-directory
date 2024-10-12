# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.patch_assets200_response_inner import PatchAssets200ResponseInner
from openapi_server.models.patch_assets_request_inner import PatchAssetsRequestInner
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_delete_assets_code(client):
    """Test case for delete_assets_code

    Delete an asset
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/asset-families/{asset_family_code}/assets/{code}'.format(asset_family_code='asset_family_code_example', code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_assets(client):
    """Test case for get_assets

    Get the list of the assets of a given asset family
    """
    params = [('search', 'search_example'),
                    ('channel', 'channel_example'),
                    ('locales', 'locales_example'),
                    ('search_after', 'cursor to the first page')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-families/{asset_family_code}/assets'.format(asset_family_code='asset_family_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_assets_code(client):
    """Test case for get_assets_code

    Get an asset of a given asset family
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-families/{asset_family_code}/assets/{code}'.format(asset_family_code='asset_family_code_example', code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_asset_code(client):
    """Test case for patch_asset_code

    Update/create an asset
    """
    body = openapi_server.PatchAssetsRequestInner()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/asset-families/{asset_family_code}/assets/{code}'.format(asset_family_code='asset_family_code_example', code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_assets(client):
    """Test case for patch_assets

    Update/create several assets
    """
    body = [openapi_server.PatchAssetsRequestInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/asset-families/{asset_family_code}/assets'.format(asset_family_code='asset_family_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

