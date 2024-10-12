# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.values_data import ValuesData


pytestmark = pytest.mark.asyncio

async def test_values_get(client):
    """Test case for values_get

    Gets all (last) values of a device
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Values/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

