# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_list_response import MediaListResponse


pytestmark = pytest.mark.asyncio

async def test_geographies_geo_id_media_recent_get(client):
    """Test case for geographies_geo_id_media_recent_get

    Get recent media from a custom geo-id.
    """
    params = [('count', 56),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geographies/{geo_id}/media/recent'.format(geo_id='geo_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

