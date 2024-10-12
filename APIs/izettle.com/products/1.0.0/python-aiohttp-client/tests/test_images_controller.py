# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.library_images_response import LibraryImagesResponse


pytestmark = pytest.mark.asyncio

async def test_get_all_image_urls(client):
    """Test case for get_all_image_urls

    Retrieve all library item images
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/organizations/{organization_uuid}/images'.format(organization_uuid='organization_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

