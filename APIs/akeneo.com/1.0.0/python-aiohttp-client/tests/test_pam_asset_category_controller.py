# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pam_asset_categories import PAMAssetCategories
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_asset_categories_request import PatchAssetCategoriesRequest
from openapi_server.models.post_asset_categories_request import PostAssetCategoriesRequest
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_asset_categories(client):
    """Test case for get_asset_categories

    Get list of PAM asset categories
    """
    params = [('page', 1),
                    ('limit', 10),
                    ('with_count', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_asset_categories_code(client):
    """Test case for get_asset_categories_code

    Get a PAM asset category
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-categories/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_asset_categories(client):
    """Test case for patch_asset_categories

    Update/create several PAM asset categories
    """
    body = openapi_server.PatchAssetCategoriesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/asset-categories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_asset_categories_code(client):
    """Test case for patch_asset_categories_code

    Update/create a PAM asset category
    """
    body = openapi_server.PostAssetCategoriesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/asset-categories/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_asset_categories(client):
    """Test case for post_asset_categories

    Create a new PAM asset category
    """
    body = openapi_server.PostAssetCategoriesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/asset-categories',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

