# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_map_version_number_staticimage_get(client):
    """Test case for map_version_number_staticimage_get

    Static Image
    """
    params = [('layer', basic),
                    ('style', main),
                    ('format', png),
                    ('zoom', 12),
                    ('center', '4.899886, 52.379031'),
                    ('width', 512),
                    ('height', 512),
                    ('bbox', 'bbox_example'),
                    ('view', 'Unified')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/staticimage'.format(version_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_map_version_number_tile_layer_style_zoom_xy_format_get(client):
    """Test case for map_version_number_tile_layer_style_zoom_xy_format_get

    Tile
    """
    params = [('tileSize', 256),
                    ('view', 'Unified')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/tile/{layer}/{style}/{zoom}/{x}/{y_format}'.format(version_number=56, layer='basic', style='main', zoom=0, x=0, y=0, format='png'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

