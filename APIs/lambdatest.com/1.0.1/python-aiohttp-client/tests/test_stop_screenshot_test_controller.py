# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.forbidden import Forbidden
from openapi_server.models.stop_screenshot_not_found import StopScreenshotNotFound
from openapi_server.models.stop_screenshot_success import StopScreenshotSuccess


pytestmark = pytest.mark.asyncio

async def test_stop_screenshots_test(client):
    """Test case for stop_screenshots_test

    Stop specified screenshot test
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/screenshots/v1/stop/{test_id}'.format(test_id='test_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

