# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_product_link_management_v1_set_product_links_post_request import CatalogProductLinkManagementV1SetProductLinksPostRequest
from openapi_server.models.catalog_product_link_repository_v1_save_put_request import CatalogProductLinkRepositoryV1SavePutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_link_management_v1_set_product_links_post(client):
    """Test case for catalog_product_link_management_v1_set_product_links_post

    products/{sku}/links
    """
    body = openapi_server.CatalogProductLinkManagementV1SetProductLinksPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/{sku}/links'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_link_repository_v1_save_put(client):
    """Test case for catalog_product_link_repository_v1_save_put

    products/{sku}/links
    """
    body = openapi_server.CatalogProductLinkRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/products/{sku}/links'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

