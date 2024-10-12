# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_product_models_request import PatchProductModelsRequest
from openapi_server.models.post_product_models_request import PostProductModelsRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.product_models import ProductModels


pytestmark = pytest.mark.asyncio

async def test_delete_product_models_code(client):
    """Test case for delete_product_models_code

    Delete a product model
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/product-models/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_model_draft_code(client):
    """Test case for get_product_model_draft_code

    Get a draft
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/product-models/{code}/draft'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_models(client):
    """Test case for get_product_models

    Get list of product models
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
                    ('with_quality_scores', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/product-models',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_models_code(client):
    """Test case for get_product_models_code

    Get a product model
    """
    params = [('with_quality_scores', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/product-models/{code}'.format(code='code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_product_models(client):
    """Test case for patch_product_models

    Update/create several product models
    """
    body = openapi_server.PatchProductModelsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/product-models',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_product_models_code(client):
    """Test case for patch_product_models_code

    Update/create a product model
    """
    body = openapi_server.PostProductModelsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/product-models/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_product_model_proposal(client):
    """Test case for post_product_model_proposal

    Submit a draft for approval
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/product-models/{code}/proposal'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_product_models(client):
    """Test case for post_product_models

    Create a new product model
    """
    body = openapi_server.PostProductModelsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/product-models',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

