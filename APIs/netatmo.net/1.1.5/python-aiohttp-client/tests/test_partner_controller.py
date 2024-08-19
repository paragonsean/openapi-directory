# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.na_measure_response import NAMeasureResponse
from openapi_server.models.na_partner_devices_response import NAPartnerDevicesResponse


pytestmark = pytest.mark.asyncio

async def test_getmeasure_1(client):
    """Test case for getmeasure_1

    
    """
    params = [('device_id', 'device_id_example'),
                    ('module_id', 'module_id_example'),
                    ('scale', 'scale_example'),
                    ('type', ['type_example']),
                    ('date_begin', 56),
                    ('date_end', 'date_end_example'),
                    ('limit', 56),
                    ('optimize', True),
                    ('real_time', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/getmeasure',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partnerdevices(client):
    """Test case for partnerdevices

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/partnerdevices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

