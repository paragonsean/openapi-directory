# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.servicepack import Servicepack


pytestmark = pytest.mark.asyncio

async def test_servicepacks(client):
    """Test case for servicepacks

    Overview of service packs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/servicepacks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

