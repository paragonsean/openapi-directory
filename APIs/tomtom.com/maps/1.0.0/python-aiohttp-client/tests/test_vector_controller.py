# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_map_version_number_tile_layer_style_zoom_xy_pbf_get(client):
    """Test case for map_version_number_tile_layer_style_zoom_xy_pbf_get

    Tile
    """
    params = [('view', 'Unified'),
                    ('language', 'NGT')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/tile/{layer}/{style}/{zoom}/{x}/{y_pb}'.format(version_number=56, layer='basic', style='main', zoom=0, x=0, y=0),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

