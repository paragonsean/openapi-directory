# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError


pytestmark = pytest.mark.asyncio

async def test_resolve_image_using_get(client):
    """Test case for resolve_image_using_get

    Resolve image
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/public/image/{image_id}'.format(image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

