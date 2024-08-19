# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancelreservation_request import CancelreservationRequest
from openapi_server.models.patch_charge_station200_response import PatchChargeStation200Response
from openapi_server.models.patch_charge_station_variable_request import PatchChargeStationVariableRequest
from openapi_server.models.remotestart_request import RemotestartRequest
from openapi_server.models.remotestop_request import RemotestopRequest
from openapi_server.models.reserve_request import ReserveRequest
from openapi_server.models.reset_request import ResetRequest
from openapi_server.models.setchargingschedule201_response import Setchargingschedule201Response
from openapi_server.models.unlockconnector_request import UnlockconnectorRequest


pytestmark = pytest.mark.asyncio

async def test_cancelreservation(client):
    """Test case for cancelreservation

    
    """
    body = openapi_server.CancelreservationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/commands/cancelreservation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commands(client):
    """Test case for get_commands

    
    """
    params = [('paginate_limit', 20),
                    ('paginate_page', 'paginate_page_example'),
                    ('paginate_enabled', True),
                    ('sort_by', 'createdAt'),
                    ('sort_order', desc),
                    ('createdAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('createdAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$gte]', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt[$lte]', '2013-10-20T19:20:30+01:00'),
                    ('include_chargestation', True),
                    ('include_driver', True),
                    ('include_transaction', True),
                    ('include_organization', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/commands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variables(client):
    """Test case for get_variables

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/commands/{id}/variables'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_charge_station_variable(client):
    """Test case for patch_charge_station_variable

    
    """
    body = openapi_server.PatchChargeStationVariableRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/commands/{id}/variables'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotestart(client):
    """Test case for remotestart

    
    """
    body = openapi_server.RemotestartRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/commands/remotestart',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotestop(client):
    """Test case for remotestop

    
    """
    body = openapi_server.RemotestopRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/commands/remotestop',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reserve(client):
    """Test case for reserve

    
    """
    body = openapi_server.ReserveRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/commands/reserve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset(client):
    """Test case for reset

    
    """
    body = openapi_server.ResetRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/commands/reset',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlockconnector(client):
    """Test case for unlockconnector

    
    """
    body = openapi_server.UnlockconnectorRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/commands/unlockconnector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

