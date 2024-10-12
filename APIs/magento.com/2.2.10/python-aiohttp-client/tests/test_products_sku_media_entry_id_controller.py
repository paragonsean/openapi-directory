# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_media_gallery_entry_interface import CatalogDataProductAttributeMediaGalleryEntryInterface
from openapi_server.models.catalog_product_attribute_media_gallery_management_v1_create_post_request import CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_media_gallery_management_v1_get_get(client):
    """Test case for catalog_product_attribute_media_gallery_management_v1_get_get

    products/{sku}/media/{entryId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/{sku}/media/{entry_id}'.format(sku='sku_example', entry_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_catalog_product_attribute_media_gallery_management_v1_remove_delete(client):
    """Test case for catalog_product_attribute_media_gallery_management_v1_remove_delete

    products/{sku}/media/{entryId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/products/{sku}/media/{entry_id}'.format(sku='sku_example', entry_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_attribute_media_gallery_management_v1_update_put(client):
    """Test case for catalog_product_attribute_media_gallery_management_v1_update_put

    products/{sku}/media/{entryId}
    """
    body = openapi_server.CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/products/{sku}/media/{entry_id}'.format(sku='sku_example', entry_id='entry_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

