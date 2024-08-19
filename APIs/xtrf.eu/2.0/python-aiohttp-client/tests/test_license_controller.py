# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_license_result import GetLicenseResult


pytestmark = pytest.mark.asyncio

async def test_get_license(client):
    """Test case for get_license

    Returns license content.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/license',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh(client):
    """Test case for refresh

    Refreshes license content.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/license/refresh',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

