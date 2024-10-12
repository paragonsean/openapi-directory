# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.values_data import ValuesData


pytestmark = pytest.mark.asyncio

async def test_values_in_past_get(client):
    """Test case for values_in_past_get

    Gets all (last) values of a device              The first Value found before the given Date is returned.
    """
    params = [('date', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/ValuesInPast/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

