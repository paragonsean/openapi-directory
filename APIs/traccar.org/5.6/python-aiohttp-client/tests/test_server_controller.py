# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server import Server


pytestmark = pytest.mark.asyncio

async def test_server_get(client):
    """Test case for server_get

    Fetch Server information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/server',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_server_put(client):
    """Test case for server_put

    Update Server information
    """
    body = {"deviceReadonly":True,"poiLayer":"poiLayer","latitude":6.027456183070403,"zoom":5,"version":"version","coordinateFormat":"coordinateFormat","bingKey":"bingKey","readonly":True,"limitCommands":True,"twelveHourFormat":True,"forceSettings":True,"mapUrl":"mapUrl","attributes":"{}","registration":True,"id":0,"map":"map","longitude":1.4658129805029452}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/server',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

