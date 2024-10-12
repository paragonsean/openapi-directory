# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.smart_me_device_configuration_container import SmartMeDeviceConfigurationContainer


pytestmark = pytest.mark.asyncio

async def test_smart_me_device_configuration_get(client):
    """Test case for smart_me_device_configuration_get

    Gets the configuration of a smart-me device.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/SmartMeDeviceConfiguration/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_smart_me_device_configuration_post(client):
    """Test case for smart_me_device_configuration_post

    Sets the configuration of a smart-me device. The device needs to be online.
    """
    body = {"ShowReactiveEnergy":True,"DevicePinCode":"DevicePinCode","EnableModbusTcp":True,"OutputConfiguration":[{"Type":"ImpulseOutputActiveEnergy","DigitalOutputNoConnectionAction":"Nothing","Number":6,"S0PulseValue":"PulseValue1000Kwh","Name":"Name"},{"Type":"ImpulseOutputActiveEnergy","DigitalOutputNoConnectionAction":"Nothing","Number":6,"S0PulseValue":"PulseValue1000Kwh","Name":"Name"}],"DeviceEncryptionKey":"DeviceEncryptionKey","DnsUpdateState":"NoUpdate","Id":"Id","SwitchConfiguration":[{"Number":1,"CanSwitchOff":True},{"Number":1,"CanSwitchOff":True}],"InputConfiguration":[{"Type":"TariffInput","OffText":"OffText","Number":0,"OnText":"OnText","Name":"Name"},{"Type":"TariffInput","OffText":"OffText","Number":0,"OnText":"OnText","Name":"Name"}],"UploadInterval":"UploadInterval_1s"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/SmartMeDeviceConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

