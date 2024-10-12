# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.experience_response import ExperienceResponse


pytestmark = pytest.mark.asyncio

async def test_get_experience_homepage(client):
    """Test case for get_experience_homepage

    Homepage Experience
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/experience/homepage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

