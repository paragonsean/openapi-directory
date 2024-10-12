# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.course_design import CourseDesign
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_coursedesigns_get(client):
    """Test case for coursedesigns_get

    Lists all global course design templates
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/coursedesigns',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

