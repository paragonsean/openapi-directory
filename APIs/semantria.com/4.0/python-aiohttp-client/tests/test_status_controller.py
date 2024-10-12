# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.status import Status


pytestmark = pytest.mark.asyncio

async def test_get_status(client):
    """Test case for get_status

    Retrieve API status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/status.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

