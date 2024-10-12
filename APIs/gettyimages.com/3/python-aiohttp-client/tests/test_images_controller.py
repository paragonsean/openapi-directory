# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset_download_history_results import AssetDownloadHistoryResults
from openapi_server.models.image_detail_field_values import ImageDetailFieldValues
from openapi_server.models.image_search_item_search_results import ImageSearchItemSearchResults
from openapi_server.models.images_detail_results import ImagesDetailResults
from openapi_server.models.images_field_values import ImagesFieldValues


pytestmark = pytest.mark.asyncio

async def test_v3_images_get(client):
    """Test case for v3_images_get

    Get metadata for multiple images by supplying multiple image ids
    """
    params = [('ids', ['ids_example']),
                    ('fields', [openapi_server.ImageDetailFieldValues()])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_images_id_downloadhistory_get(client):
    """Test case for v3_images_id_downloadhistory_get

    Returns information about a customer's download history for a specific asset
    """
    params = [('company_downloads', True)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/images/{id}/downloadhistory'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_images_id_get(client):
    """Test case for v3_images_id_get

    Get metadata for a single image by supplying one image id
    """
    params = [('fields', [openapi_server.ImageDetailFieldValues()])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/images/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_images_id_same_series_get(client):
    """Test case for v3_images_id_same_series_get

    Retrieve creative images from the same series
    """
    params = [('fields', [openapi_server.ImagesFieldValues()]),
                    ('page', 1),
                    ('page_size', 30)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/images/{id}/same-series'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_images_id_similar_get(client):
    """Test case for v3_images_id_similar_get

    Retrieve similar images
    """
    params = [('fields', [openapi_server.ImagesFieldValues()]),
                    ('page', 1),
                    ('page_size', 30)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/images/{id}/similar'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

