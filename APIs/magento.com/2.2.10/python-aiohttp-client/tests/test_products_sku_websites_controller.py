# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_product_website_link_repository_v1_save_put_request import CatalogProductWebsiteLinkRepositoryV1SavePutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_website_link_repository_v1_save_post(client):
    """Test case for catalog_product_website_link_repository_v1_save_post

    products/{sku}/websites
    """
    body = openapi_server.CatalogProductWebsiteLinkRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/{sku}/websites'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_website_link_repository_v1_save_put(client):
    """Test case for catalog_product_website_link_repository_v1_save_put

    products/{sku}/websites
    """
    body = openapi_server.CatalogProductWebsiteLinkRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/products/{sku}/websites'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

