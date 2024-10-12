# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.anchore_image_tag_summary import AnchoreImageTagSummary
from openapi_server.models.api_error_response import ApiErrorResponse


pytestmark = pytest.mark.asyncio

async def test_list_imagetags(client):
    """Test case for list_imagetags

    List all visible image digests and tags
    """
    params = [('image_status', ["active"])]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/summaries/imagetags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

