# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_tariffs_of_folder import VirtualTariffsOfFolder


pytestmark = pytest.mark.asyncio

async def test_virtual_tariffs_for_property_get(client):
    """Test case for virtual_tariffs_for_property_get

    Gets all Virtual Tariffs for a property (folder)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/VirtualTariffsForProperty/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

