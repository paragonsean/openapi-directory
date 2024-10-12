# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.example17 import Example17
from openapi_server.models.night_modesettings_request import NightModesettingsRequest
from openapi_server.models.rebootand_factory_reset_request import RebootandFactoryResetRequest
from openapi_server.models.set_eureka_info_request import SetEurekaInfoRequest


pytestmark = pytest.mark.asyncio

async def test_night_modesettings(client):
    """Test case for night_modesettings

    Night Mode settings
    """
    body = {"demo_to_user":True,"do_not_disturb":True,"enabled":False,"led_brightness":0.44999998807907104,"volume":0.46000000834465027,"windows":[{"days":[0,1,2,3,4,5,6],"length_hours":8,"start_hour":22}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/assistant/set_night_mode_params',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rebootand_factory_reset(client):
    """Test case for rebootand_factory_reset

    Reboot and Factory Reset
    """
    body = {"params":"now"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/reboot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_eureka_info(client):
    """Test case for set_eureka_info

    Set Eureka Info
    """
    body = {"name":"Living Room","opt_in":{"opencast":True,"preview_channel":True,"remote_ducking":True,"stats":True},"settings":{"control_notifications":2}}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/set_eureka_info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

