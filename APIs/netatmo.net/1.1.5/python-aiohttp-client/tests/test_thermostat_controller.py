# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.na_measure_response import NAMeasureResponse
from openapi_server.models.na_new_schedule_response import NANewScheduleResponse
from openapi_server.models.naok_response import NAOkResponse
from openapi_server.models.na_therm_program import NAThermProgram
from openapi_server.models.na_thermostat_data_response import NAThermostatDataResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_createnewschedule(client):
    """Test case for createnewschedule

    
    """
    body = openapi_server.NAThermProgram()
    params = [('device_id', 'device_id_example'),
                    ('module_id', 'module_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/createnewschedule',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getmeasure_0(client):
    """Test case for getmeasure_0

    
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

async def test_getthermostatsdata(client):
    """Test case for getthermostatsdata

    
    """
    params = [('device_id', 'device_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/getthermostatsdata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setthermpoint(client):
    """Test case for setthermpoint

    
    """
    params = [('device_id', 'device_id_example'),
                    ('module_id', 'module_id_example'),
                    ('setpoint_mode', 'setpoint_mode_example'),
                    ('setpoint_endtime', 56),
                    ('setpoint_temp', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/setthermpoint',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_switchschedule(client):
    """Test case for switchschedule

    
    """
    params = [('device_id', 'device_id_example'),
                    ('module_id', 'module_id_example'),
                    ('schedule_id', 'schedule_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/switchschedule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_syncschedule(client):
    """Test case for syncschedule

    
    """
    body = openapi_server.NAThermProgram()
    params = [('device_id', 'device_id_example'),
                    ('module_id', 'module_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/syncschedule',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

