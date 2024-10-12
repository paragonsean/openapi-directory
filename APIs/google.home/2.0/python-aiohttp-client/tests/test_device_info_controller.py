# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_device_id_request import AppDeviceIDRequest
from openapi_server.models.check_ready_status_request import CheckReadyStatusRequest
from openapi_server.models.example1 import Example1
from openapi_server.models.example11 import Example11
from openapi_server.models.example12 import Example12
from openapi_server.models.example13 import Example13
from openapi_server.models.example14 import Example14
from openapi_server.models.example15 import Example15
from openapi_server.models.example16 import Example16
from openapi_server.models.test_internet_download_speed_request import TestInternetDownloadSpeedRequest


pytestmark = pytest.mark.asyncio

async def test_app_device_id(client):
    """Test case for app_device_id

    App Device ID
    """
    body = {"app_id":"E8C28D3C"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/get_app_device_id',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_ready_status(client):
    """Test case for check_ready_status

    Check Ready Status
    """
    body = {"play_ready_message":True,"user_id":"xxxxx"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/assistant/check_ready_status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eureka_info(client):
    """Test case for eureka_info

    Eureka Info
    """
    params = [('params', 'version,audio,name,build_info,detail,device_info,net,wifi,setup,settings,opt_in,opencast,multizone,proxy,night_mode_params,user_eq,room_equalizer,sign,aogh,ultrasound,mesh'),
                    ('options', 'detail,sign'),
                    ('nonce', 1234512345)]
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/eureka_info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locales(client):
    """Test case for locales

    Locales
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/supported_locales',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer(client):
    """Test case for offer

    Offer
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/offer',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_internet_download_speed(client):
    """Test case for test_internet_download_speed

    Test Internet Download Speed
    """
    body = {"url":"https://storage.googleapis.com/reliability-speedtest/random.txt"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/test_internet_download_speed',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezones(client):
    """Test case for timezones

    Timezones
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/supported_timezones',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

