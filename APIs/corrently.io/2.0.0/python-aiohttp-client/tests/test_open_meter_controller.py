# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ommeters import Ommeters


pytestmark = pytest.mark.asyncio

async def test_om_activities(client):
    """Test case for om_activities

    Public shared smart meters installed in Germany and available for subservices and exploration.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/alternative/openmeter/activities',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_om_meters(client):
    """Test case for om_meters

    Public shared smart meters installed in Germany and available for subservices and exploration.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/alternative/openmeter/meters',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_om_readings(client):
    """Test case for om_readings

    Public shared smart meters installed in Germany and available for subservices and exploration.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/alternative/openmeter/readings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

