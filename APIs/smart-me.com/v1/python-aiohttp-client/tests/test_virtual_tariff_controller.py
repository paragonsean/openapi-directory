# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_tariffs_of_folder import VirtualTariffsOfFolder


pytestmark = pytest.mark.asyncio

async def test_api_virtual_tariff_id_get(client):
    """Test case for api_virtual_tariff_id_get

    Gets all virtual tariffs of a folder
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/VirtualTariff/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_tariff_get(client):
    """Test case for virtual_tariff_get

    Gets all Virtual Tariffs of a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/VirtualTariff',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

