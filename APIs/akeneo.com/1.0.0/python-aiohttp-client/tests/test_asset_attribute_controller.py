# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_asset_families_code_attributes200_response_inner import GetAssetFamiliesCodeAttributes200ResponseInner
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_asset_families_code_attributes(client):
    """Test case for get_asset_families_code_attributes

    Get the list of attributes of a given asset family
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-families/{asset_family_code}/attributes'.format(asset_family_code='asset_family_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_family_attributes_code(client):
    """Test case for get_asset_family_attributes_code

    Get an attribute of a given asset family
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-families/{asset_family_code}/attributes/{code}'.format(asset_family_code='asset_family_code_example', code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_asset_family_attributes_code(client):
    """Test case for patch_asset_family_attributes_code

    Update/create an attribute of a given asset family
    """
    body = openapi_server.GetAssetFamiliesCodeAttributes200ResponseInner()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/asset-families/{asset_family_code}/attributes/{code}'.format(asset_family_code='asset_family_code_example', code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

