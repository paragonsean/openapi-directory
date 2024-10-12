# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pico_settings_dto import PicoSettingsDto


pytestmark = pytest.mark.asyncio

async def test_pico_settings_get(client):
    """Test case for pico_settings_get

    GET: api/pico/settings                            Returns the settings of a pico charging station.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/pico/settings/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

