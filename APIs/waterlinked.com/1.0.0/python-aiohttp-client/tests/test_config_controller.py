# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.modify_antenna_config_config_payload import ModifyAntennaConfigConfigPayload
from openapi_server.models.modify_config_payload import ModifyConfigPayload
from openapi_server.models.modify_ip_config_payload import ModifyIPConfigPayload
from openapi_server.models.modify_receiver_config_payload import ModifyReceiverConfigPayload
from openapi_server.models.modify_wifi_config_payload import ModifyWIFIConfigPayload
from openapi_server.models.waterlinked_antenna_config import WaterlinkedAntennaConfig
from openapi_server.models.waterlinked_configuration import WaterlinkedConfiguration
from openapi_server.models.waterlinked_ip_config import WaterlinkedIpConfig
from openapi_server.models.waterlinked_operation_response import WaterlinkedOperationResponse
from openapi_server.models.waterlinked_receiver import WaterlinkedReceiver
from openapi_server.models.waterlinked_wifi_config import WaterlinkedWifiConfig


pytestmark = pytest.mark.asyncio

async def test_config_get(client):
    """Test case for config_get

    Get config
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config/generic',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_get_antenna_config(client):
    """Test case for config_get_antenna_config

    GetAntennaConfig config
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.antenna_config+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config/antenna',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_get_ip(client):
    """Test case for config_get_ip

    GetIP config
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.ip_config+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config/ip',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_get_wifi(client):
    """Test case for config_get_wifi

    GetWIFI config
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.wifi_config+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config/wifi',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_list_receiver(client):
    """Test case for config_list_receiver

    ListReceiver config
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.receiver+json; type=collection',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config/receivers/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_modify(client):
    """Test case for config_modify

    Modify config
    """
    payload = {"antenna_enabled":True,"channel":13,"compass":"external","environment":"openwater","external_pps_enabled":False,"gps":"external","imu_vehicle_enabled":True,"locator_type":"a1","range_max_x":50,"range_max_y":50,"range_max_z":50,"range_min_x":-50,"range_min_y":-50,"search_direction":30,"search_radius":150,"search_sector":90,"speed_of_sound":1475,"static_lat":63.422,"static_lon":10.424,"static_orientation":42}
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/config/generic',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_modify_antenna_config(client):
    """Test case for config_modify_antenna_config

    ModifyAntennaConfig config
    """
    payload = {"antenna_rotation":90,"depth":2,"x":-2,"y":2}
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/config/antenna',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_modify_ip(client):
    """Test case for config_modify_ip

    ModifyIP config
    """
    payload = {"address":"10.11.12.94","dhcp":True,"dns":"10.11.12.1","gateway":"10.11.12.1","prefix":24}
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/config/ip',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_modify_receiver(client):
    """Test case for config_modify_receiver

    ModifyReceiver config
    """
    payload = {"id":2339264502380679700,"x":0.0158212572962501,"y":0.08142596921667565,"z":0.34617068793186784}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/config/receivers/{id}'.format(id=56),
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_modify_wifi(client):
    """Test case for config_modify_wifi

    ModifyWIFI config
    """
    payload = {"mode":"ap","password":"10.11.12.1","ssid":"10.11.12.94"}
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/config/wifi',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_show_receiver(client):
    """Test case for config_show_receiver

    ShowReceiver config
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.receiver+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config/receivers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

