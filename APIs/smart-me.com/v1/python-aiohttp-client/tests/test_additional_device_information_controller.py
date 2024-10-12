# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.additional_device_information import AdditionalDeviceInformation


pytestmark = pytest.mark.asyncio

async def test_additional_device_information_get(client):
    """Test case for additional_device_information_get

    Gets the additional information (e.g. Firmware Version) about a device.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/AdditionalDeviceInformation/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

