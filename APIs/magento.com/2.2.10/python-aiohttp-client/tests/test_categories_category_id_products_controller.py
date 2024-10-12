# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_category_link_repository_v1_save_put_request import CatalogCategoryLinkRepositoryV1SavePutRequest
from openapi_server.models.catalog_data_category_product_link_interface import CatalogDataCategoryProductLinkInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_category_link_management_v1_get_assigned_products_get(client):
    """Test case for catalog_category_link_management_v1_get_assigned_products_get

    categories/{categoryId}/products
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/categories/{category_id}/products'.format(category_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_category_link_repository_v1_save_post(client):
    """Test case for catalog_category_link_repository_v1_save_post

    categories/{categoryId}/products
    """
    body = openapi_server.CatalogCategoryLinkRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/categories/{category_id}/products'.format(category_id='category_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_category_link_repository_v1_save_put(client):
    """Test case for catalog_category_link_repository_v1_save_put

    categories/{categoryId}/products
    """
    body = openapi_server.CatalogCategoryLinkRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/categories/{category_id}/products'.format(category_id='category_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

