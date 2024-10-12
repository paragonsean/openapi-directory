# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.app_info_presentation import AppInfoPresentation


pytestmark = pytest.mark.asyncio

async def test_application_info(client):
    """Test case for application_info

    Retrieve version information about ID4i
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

