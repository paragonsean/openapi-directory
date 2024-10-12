# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.set_depth_external_payload import SetDepthExternalPayload
from openapi_server.models.set_master_external_payload import SetMasterExternalPayload
from openapi_server.models.set_orientation_external_payload import SetOrientationExternalPayload
from openapi_server.models.set_vehicle_imu_external_payload import SetVehicleIMUExternalPayload
from openapi_server.models.waterlinked_operation_response import WaterlinkedOperationResponse
from openapi_server.models.wl_external_locator_orientation import WlExternalLocatorOrientation
from openapi_server.models.wl_external_vehicle_imu import WlExternalVehicleImu


pytestmark = pytest.mark.asyncio

async def test_external_get_orientation(client):
    """Test case for external_get_orientation

    GetOrientation external
    """
    headers = { 
        'Accept': 'application/vnd.wl.external.locator.orientation+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/external/orientation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_get_vehicle_imu(client):
    """Test case for external_get_vehicle_imu

    GetVehicleIMU external
    """
    headers = { 
        'Accept': 'application/vnd.wl.external.vehicle.imu+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/external/imu',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_set_depth(client):
    """Test case for external_set_depth

    SetDepth external
    """
    payload = {"depth":3.2,"temp":11.2}
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/external/depth',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_set_master(client):
    """Test case for external_set_master

    SetMaster external
    """
    payload = {"cog":42,"fix_quality":1,"hdop":1.9,"lat":63.422,"lon":10.424,"numsats":11,"orientation":42,"sog":0.5}
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/external/master',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_set_orientation(client):
    """Test case for external_set_orientation

    SetOrientation external
    """
    payload = {"orientation":42}
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/external/orientation',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_external_set_vehicle_imu(client):
    """Test case for external_set_vehicle_imu

    SetVehicleIMU external
    """
    payload = {"pitch":30,"roll":-30,"x":10,"y":-10,"yaw":30,"z":5}
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/external/imu',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

