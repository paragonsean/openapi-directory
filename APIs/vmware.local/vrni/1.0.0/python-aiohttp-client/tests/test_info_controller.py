# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.version_response import VersionResponse


pytestmark = pytest.mark.asyncio

async def test_get_version(client):
    """Test case for get_version

    Show version info
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/info/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

