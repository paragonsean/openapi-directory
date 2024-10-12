# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pico_charging_history_data import PicoChargingHistoryData


pytestmark = pytest.mark.asyncio

async def test_pico_charging_history_get(client):
    """Test case for pico_charging_history_get

    Gets the last charging history for a pico station
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/pico/history/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

