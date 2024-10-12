# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gallery_item import GalleryItem
from openapi_server.models.gallery_item_list import GalleryItemList
from openapi_server.models.gallery_item_uri_payload import GalleryItemUriPayload


pytestmark = pytest.mark.asyncio

async def test_gallery_items_create(client):
    """Test case for gallery_items_create

    Uploads a provider gallery item to the storage.
    """
    gallery_item_uri_payload = {"galleryItemUri":"galleryItemUri"}
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/microsoft.gallery.admin/galleryItems'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=gallery_item_uri_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_items_delete(client):
    """Test case for gallery_items_delete

    Delete a specific gallery item.
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/microsoft.gallery.admin/galleryItems/{gallery_item_name}'.format(subscription_id='subscription_id_example', gallery_item_name='gallery_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_items_get(client):
    """Test case for gallery_items_get

    Get a specific gallery item.
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.gallery.admin/galleryItems/{gallery_item_name}'.format(subscription_id='subscription_id_example', gallery_item_name='gallery_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gallery_items_list(client):
    """Test case for gallery_items_list

    Lists gallery items.
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.gallery.admin/galleryItems'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

