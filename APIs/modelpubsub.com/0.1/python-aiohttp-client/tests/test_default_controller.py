# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apiv10_safe_unsafe_image_with_tags_body import Apiv10SafeUnsafeImageWithTagsBody
from openapi_server.models.inline_response200 import InlineResponse200


pytestmark = pytest.mark.asyncio

async def test_api_v10_safe_unsafe_image_with_tags_post(client):
    """Test case for api_v10_safe_unsafe_image_with_tags_post

    
    """
    body = openapi_server.Apiv10SafeUnsafeImageWithTagsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api-v1.0/SafeUnsafeImageWithTags',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

