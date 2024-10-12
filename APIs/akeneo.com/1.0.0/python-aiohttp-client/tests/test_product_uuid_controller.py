# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_products_uuid200_response import PatchProductsUuid200Response
from openapi_server.models.patch_products_uuid_request import PatchProductsUuidRequest
from openapi_server.models.post_products_uuid_request import PostProductsUuidRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.products2 import Products2


pytestmark = pytest.mark.asyncio

async def test_delete_products_uuid_uuid(client):
    """Test case for delete_products_uuid_uuid

    Delete a product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/products-uuid/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_draft_uuid_uuid(client):
    """Test case for get_draft_uuid_uuid

    Get a draft
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/products-uuid/{uuid}/draft'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_uuid(client):
    """Test case for get_products_uuid

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
        path='/api/rest/v1/products-uuid',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_products_uuid_uuid(client):
    """Test case for get_products_uuid_uuid

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
        path='/api/rest/v1/products-uuid/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_products_uuid(client):
    """Test case for patch_products_uuid

    Update/create several products
    """
    body = openapi_server.PatchProductsUuidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/products-uuid',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_products_uuid_uuid(client):
    """Test case for patch_products_uuid_uuid

    Update/create a product
    """
    body = openapi_server.PostProductsUuidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/products-uuid/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_products_uuid(client):
    """Test case for post_products_uuid

    Create a new product
    """
    body = openapi_server.PostProductsUuidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/products-uuid',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_proposal_uuid(client):
    """Test case for post_proposal_uuid

    Submit a draft for approval
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/products-uuid/{uuid}/proposal'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

