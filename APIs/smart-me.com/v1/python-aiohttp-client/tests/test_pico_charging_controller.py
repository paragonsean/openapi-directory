# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pico_charging_data import PicoChargingData


pytestmark = pytest.mark.asyncio

async def test_pico_charging_get(client):
    """Test case for pico_charging_get

    Gets the active charging data of a pico station
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/pico/charging/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

