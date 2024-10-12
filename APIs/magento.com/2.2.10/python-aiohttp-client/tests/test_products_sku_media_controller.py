# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_media_gallery_entry_interface import CatalogDataProductAttributeMediaGalleryEntryInterface
from openapi_server.models.catalog_product_attribute_media_gallery_management_v1_create_post_request import CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_attribute_media_gallery_management_v1_create_post(client):
    """Test case for catalog_product_attribute_media_gallery_management_v1_create_post

    products/{sku}/media
    """
    body = openapi_server.CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/{sku}/media'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_media_gallery_management_v1_get_list_get(client):
    """Test case for catalog_product_attribute_media_gallery_management_v1_get_list_get

    products/{sku}/media
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/{sku}/media'.format(sku='sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

