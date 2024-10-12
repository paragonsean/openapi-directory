# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_item_wrapped import MediaItemWrapped


pytestmark = pytest.mark.asyncio

async def test_resources_user_media_lists_id_json_get(client):
    """Test case for resources_user_media_lists_id_json_get

    Get UserMediaList by ID
    """
    params = [('displayMethod', 'display_method_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/userMediaLists/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

