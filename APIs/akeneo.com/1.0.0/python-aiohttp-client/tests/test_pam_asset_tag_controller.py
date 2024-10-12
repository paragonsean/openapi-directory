# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_asset_tags_code200_response import GetAssetTagsCode200Response
from openapi_server.models.pam_asset_tags import PAMAssetTags
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_asset_tags(client):
    """Test case for get_asset_tags

    Get list of PAM asset tags
    """
    params = [('page', 1),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_tags_code(client):
    """Test case for get_asset_tags_code

    Get a PAM asset tag
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-tags/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_asset_tags_code(client):
    """Test case for patch_asset_tags_code

    Update/create a PAM asset tag
    """
    body = openapi_server.GetAssetTagsCode200Response()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/asset-tags/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

