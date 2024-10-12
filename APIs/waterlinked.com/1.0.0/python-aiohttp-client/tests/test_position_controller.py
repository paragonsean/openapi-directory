# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.waterlinked_accoustic_position import WaterlinkedAccousticPosition
from openapi_server.models.wl_satellite_position import WlSatellitePosition


pytestmark = pytest.mark.asyncio

async def test_position_acoustic_filtered(client):
    """Test case for position_acoustic_filtered

    AcousticFiltered position
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.accoustic.position+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/position/acoustic/filtered',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_position_acoustic_raw(client):
    """Test case for position_acoustic_raw

    AcousticRaw position
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.accoustic.position+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/position/acoustic/raw',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_position_get(client):
    """Test case for position_get

    Get position
    """
    headers = { 
        'Accept': 'application/vnd.wl.satellite.position+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/position/global',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_position_get_master(client):
    """Test case for position_get_master

    GetMaster position
    """
    headers = { 
        'Accept': 'application/vnd.wl.satellite.position+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/position/master',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

