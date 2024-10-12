# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_tariff_consumption_data import VirtualTariffConsumptionData


pytestmark = pytest.mark.asyncio

async def test_virtual_tariff_consumption_get(client):
    """Test case for virtual_tariff_consumption_get

    Gets the consumption of a folder with a virtuall tariffs.
    """
    params = [('folderId', 'folder_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/VirtualTariffConsumption',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

