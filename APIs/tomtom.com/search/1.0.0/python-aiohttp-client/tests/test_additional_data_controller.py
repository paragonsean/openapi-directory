# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_version_number_additional_data_ext_get(client):
    """Test case for search_version_number_additional_data_ext_get

    Additional Data
    """
    params = [('geometries', '00004631-3400-3c00-0000-0000673c4d2e,00004631-3400-3c00-0000-0000673c42fe'),
                    ('geometriesZoom', 56)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/additionalData.{ext}'.format(version_number=56, ext='ext_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

