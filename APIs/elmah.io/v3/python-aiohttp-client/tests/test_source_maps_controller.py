# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_source_maps_create_or_update(client):
    """Test case for source_maps_create_or_update

    Create or update a translation between a minified JavaScript path to the minified JavaScript and source map files.
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'api_key': 'special-key',
    }
    data = FormData()
    data.add_field('minified_java_script', '/path/to/file')
    data.add_field('path', 'path_example')
    data.add_field('source_map', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v3/sourcemaps/{log_id}'.format(log_id='log_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

