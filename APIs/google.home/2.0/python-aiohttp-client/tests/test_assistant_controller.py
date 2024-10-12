# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accessibility_request import AccessibilityRequest
from openapi_server.models.alarm_volume_request import AlarmVolumeRequest
from openapi_server.models.delete_alarmsand_timers_request import DeleteAlarmsandTimersRequest
from openapi_server.models.example18 import Example18
from openapi_server.models.example19 import Example19
from openapi_server.models.getcurrentstate import Getcurrentstate
from openapi_server.models.getcurrentvalues import Getcurrentvalues
from openapi_server.models.getvolume import Getvolume
from openapi_server.models.set_equalizer_values_request import SetEqualizerValuesRequest


pytestmark = pytest.mark.asyncio

async def test_accessibility(client):
    """Test case for accessibility

    Accessibility
    """
    body = {"endpoint_enabled":False,"hotword_enabled":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/assistant/a11y_mode',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alarm_volume(client):
    """Test case for alarm_volume

    Alarm Volume
    """
    body = {"volume":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/assistant/alarms/volume',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_alarmsand_timers(client):
    """Test case for delete_alarmsand_timers

    Delete Alarms and Timers
    """
    body = {"ids":["timer/xxx","alarm/xxx"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/assistant/alarms/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_do_not_disturb(client):
    """Test case for do_not_disturb

    Do Not Disturb
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/assistant/notifications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_alarmsand_timers(client):
    """Test case for get_alarmsand_timers

    Get Alarms and Timers
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/assistant/alarms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_equalizer_values(client):
    """Test case for set_equalizer_values

    Set Equalizer Values
    """
    body = {"high_shelf":{"gain_db":0},"low_shelf":{"gain_db":0}}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/user_eq/set_equalizer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

