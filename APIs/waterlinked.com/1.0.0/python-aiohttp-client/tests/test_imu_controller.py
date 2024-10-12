# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calibrate_imu_payload import CalibrateImuPayload
from openapi_server.models.set_north_imu_payload import SetNorthImuPayload
from openapi_server.models.waterlinked_imu import WaterlinkedImu


pytestmark = pytest.mark.asyncio

async def test_imu_calibrate(client):
    """Test case for imu_calibrate

    Calibrate imu
    """
    payload = {"action":"start"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/imu/calibrate',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_imu_get(client):
    """Test case for imu_get

    Get imu
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.imu+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/imu/calibrate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_imu_reset_gyro(client):
    """Test case for imu_reset_gyro

    ResetGyro imu
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/v1/imu/resetgyros',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_imu_set_north(client):
    """Test case for imu_set_north

    SetNorth imu
    """
    payload = {"heading":50}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/imu/setnorth',
        headers=headers,
        json=payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

