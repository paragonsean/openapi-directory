# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.search_response import SearchResponse


pytestmark = pytest.mark.asyncio

async def test_get_recall_history(client):
    """Test case for get_recall_history

    Recall info by vin
    """
    params = [('api_key', 'api_key_example'),
                    ('page', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/car/recall/{vin}'.format(vin='vin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

