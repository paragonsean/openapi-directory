# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_geomarks_geomark_id_feature_file_format_extension_get(client):
    """Test case for geomarks_geomark_id_feature_file_format_extension_get

    Get the feature and attribution of the geomark
    """
    params = [('srid', 4326)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pub/geomark/geomarks/{geomark_id}/feature.{fileFormatExtension}'.format(geomark_id='gm-abcdefghijklmnopqrstuv0bcislands', file_format_extension='json'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

