# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_map_version_number_copyrights_caption_format_get(client):
    """Test case for map_version_number_copyrights_caption_format_get

    Captions
    """
    params = [('callback', 'param_callback_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/copyrights/caption.{format}'.format(version_number=56, format=xml),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_map_version_number_copyrights_format_get(client):
    """Test case for map_version_number_copyrights_format_get

    Copyrights whole world
    """
    params = [('callback', 'param_callback_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/copyrights.{format}'.format(version_number=56, format=xml),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_map_version_number_copyrights_min_lon_min_lat_max_lon_max_lat_format_get(client):
    """Test case for map_version_number_copyrights_min_lon_min_lat_max_lon_max_lat_format_get

    Copyrights bounding box
    """
    params = [('callback', 'param_callback_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/copyrights/{min_lon}/{min_lat}/{max_lon}/{max_lat_format}'.format(version_number=56, format=xml, min_lon=-179.1506, min_lat=18.9117, max_lon=-66.9406, max_lat=71.441),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_map_version_number_copyrights_zoom_xy_format_get(client):
    """Test case for map_version_number_copyrights_zoom_xy_format_get

    Copyrights tile
    """
    params = [('callback', 'param_callback_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/copyrights/{zoom}/{x}/{y_format}'.format(version_number=56, format=xml, zoom=0, x=0, y=0),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

