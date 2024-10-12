# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_virtual_tariffs_status_for_property_get(client):
    """Test case for virtual_tariffs_status_for_property_get

    Gets the calculation status for a virtual tariff property
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/VirtualTariffsStatusForProperty/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

