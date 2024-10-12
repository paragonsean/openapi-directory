# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_interface import CatalogDataProductInterface
from openapi_server.models.catalog_product_repository_v1_save_post_request import CatalogProductRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_repository_v1_delete_by_id_delete(client):
    """Test case for catalog_product_repository_v1_delete_by_id_delete

    products/{sku}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/{sku}'.format(sku='sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_product_repository_v1_get_get(client):
    """Test case for catalog_product_repository_v1_get_get

    products/{sku}
    """
    params = [('editMode', True),
                    ('storeId', 56),
                    ('forceReload', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/{sku}'.format(sku='sku_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_repository_v1_save_put(client):
    """Test case for catalog_product_repository_v1_save_put

    products/{sku}
    """
    body = openapi_server.CatalogProductRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/products/{sku}'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

