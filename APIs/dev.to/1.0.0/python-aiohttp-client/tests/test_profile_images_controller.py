# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.profile_image import ProfileImage


pytestmark = pytest.mark.asyncio

async def test_get_profile_image(client):
    """Test case for get_profile_image

    A Users or organizations profile image
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/profile_images/{username}'.format(username='janedoe'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

