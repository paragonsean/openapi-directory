# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.values_data import ValuesData


pytestmark = pytest.mark.asyncio

async def test_values_in_past_multiple_get(client):
    """Test case for values_in_past_multiple_get

    Gets multiple values of a device. This call needs a smart-me professional licence.
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('interval', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/ValuesInPastMultiple/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

