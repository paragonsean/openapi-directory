# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server.models.device_to_post import DeviceToPost


pytestmark = pytest.mark.asyncio

async def test_api_devices_id_get(client):
    """Test case for api_devices_id_get

    Gets a Device by it's ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Devices/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_get(client):
    """Test case for devices_get

    Gets all Devices
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Devices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_devices_post(client):
    """Test case for devices_post

    Creates or updates a Device or updates it's values.
    """
    body = {"Temperature":7.457744773683766,"Name":"Name","ActivePower":0.8008281904610115,"CounterReadingExportT2":5.637376656633329,"CounterReadingExportT1":5.962133916683182,"Voltage":1.1730742509559433,"ValueDate":"2000-01-23T04:56:07.000+00:00","VoltageL1":4.965218492984954,"CurrentL1":3.616076749251911,"CurrentL2":2.027123023002322,"VoltageL2":5.025004791520295,"CounterReadingExport":1.4658129805029452,"VoltageL3":9.965781217890562,"PowerFactor":7.386281948385884,"DeviceEnergyType":"MeterTypeUnknown","CurrentL3":4.145608029883936,"CounterReadingT2":7.061401241503109,"DigitalInput1":True,"PowerFactorL1":1.2315135367772556,"PowerFactorL2":1.0246457001441578,"CounterReadingT1":2.3021358869347655,"PowerFactorL3":1.4894159098541704,"CounterReading":6.027456183070403,"Serial":6,"Id":"Id","Current":9.301444243932576,"MeterSubType":"MeterSubTypeUnknown"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/Devices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_devices_put(client):
    """Test case for devices_put

    Updates the On/Off Switch on a device.               For new implementations please use the \"actions\" command
    """
    params = [('switchState', True),
                    ('switchNumber', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/Devices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

