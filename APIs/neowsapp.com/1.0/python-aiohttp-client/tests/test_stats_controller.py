# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.statistics import Statistics


pytestmark = pytest.mark.asyncio

async def test_retrieve_current_neo_statistics(client):
    """Test case for retrieve_current_neo_statistics

    Get the Near Earth Object data set totals
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1/stats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

