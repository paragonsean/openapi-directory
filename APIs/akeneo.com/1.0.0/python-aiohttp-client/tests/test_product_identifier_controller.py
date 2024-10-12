# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_products_request import PatchProductsRequest
from openapi_server.models.post_products_request import PostProductsRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.products1 import Products1


pytestmark = pytest.mark.asyncio

async def test_delete_products_code(client):
    """Test case for delete_products_code

    Delete a product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/products/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_draft_code(client):
    """Test case for get_draft_code

    Get a draft
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/products/{code}/draft'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products(client):
    """Test case for get_products

    Get list of products
    """
    params = [('search', 'search_example'),
                    ('scope', 'scope_example'),
                    ('locales', 'locales_example'),
                    ('attributes', 'attributes_example'),
                    ('pagination_type', page),
                    ('page', 1),
                    ('search_after', 'cursor to the first page'),
                    ('limit', 10),
                    ('with_count', False),
                    ('with_attribute_options', False),
                    ('with_quality_scores', False),
                    ('with_completenesses', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_code(client):
    """Test case for get_products_code

    Get a product
    """
    params = [('with_attribute_options', False),
                    ('with_quality_scores', False),
                    ('with_completenesses', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/products/{code}'.format(code='code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_products(client):
    """Test case for patch_products

    Update/create several products
    """
    body = openapi_server.PatchProductsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_products_code(client):
    """Test case for patch_products_code

    Update/create a product
    """
    body = openapi_server.PostProductsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/products/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_products(client):
    """Test case for post_products

    Create a new product
    """
    body = openapi_server.PostProductsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_proposal(client):
    """Test case for post_proposal

    Submit a draft for approval
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/products/{code}/proposal'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

