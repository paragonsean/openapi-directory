# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deletechargingschedule_request import DeletechargingscheduleRequest
from openapi_server.models.setchargingschedule201_response import Setchargingschedule201Response
from openapi_server.models.setchargingschedule_request import SetchargingscheduleRequest


pytestmark = pytest.mark.asyncio

async def test_deletechargingschedule(client):
    """Test case for deletechargingschedule

    
    """
    body = openapi_server.DeletechargingscheduleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/commands/chargingschedule',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setchargingschedule(client):
    """Test case for setchargingschedule

    
    """
    body = openapi_server.SetchargingscheduleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/commands/chargingschedule',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

