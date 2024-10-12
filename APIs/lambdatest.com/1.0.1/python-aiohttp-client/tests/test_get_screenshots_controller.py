# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.screenshot_not_found import ScreenshotNotFound
from openapi_server.models.screenshot_test_response import ScreenshotTestResponse


pytestmark = pytest.mark.asyncio

async def test_screenshots(client):
    """Test case for screenshots

    Fetch specified screenshot details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/screenshots/v1/{test_id}'.format(test_id='test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

