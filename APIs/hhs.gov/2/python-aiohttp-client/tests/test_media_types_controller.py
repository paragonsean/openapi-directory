# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.media_type_holder_wrapped import MediaTypeHolderWrapped


pytestmark = pytest.mark.asyncio

async def test_resources_media_types_format_get(client):
    """Test case for resources_media_types_format_get

    Get MediaTypes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/mediaTypes.{format}'.format(format='format_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

