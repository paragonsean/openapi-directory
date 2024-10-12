# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.screenshot_payload import ScreenshotPayload
from openapi_server.models.start_screenshot_bad_request import StartScreenshotBadRequest
from openapi_server.models.start_screenshot_success import StartScreenshotSuccess


pytestmark = pytest.mark.asyncio

async def test_start_screenshot_test(client):
    """Test case for start_screenshot_test

    Start Screenshot Test
    """
    body = openapi_server.ScreenshotPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/screenshots/v1/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

