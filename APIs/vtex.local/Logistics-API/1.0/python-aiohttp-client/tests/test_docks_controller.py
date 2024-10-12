# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.all_docks200_response_inner import AllDocks200ResponseInner
from openapi_server.models.create_update_dock_request import CreateUpdateDockRequest
from openapi_server.models.dock_by_id200_response import DockById200Response


pytestmark = pytest.mark.asyncio

async def test_activate_dock(client):
    """Test case for activate_dock

    Activate dock
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/docks/{dock_id}/activation'.format(dock_id='dock_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_all_docks(client):
    """Test case for all_docks

    List all  docks
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/docks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_create_update_dock(client):
    """Test case for create_update_dock

    Create/update dock
    """
    body = {"address":{"city":"Rio de Janeiro","complement":"","coordinates":[[-43.18228090000002,-22.9460398]],"country":{"acronym":"BRA","name":"Brazil"},"neighborhood":"Catete","number":"100","postalCode":"22220070","state":"RJ","street":"Artur Bernardes Street"},"dockTimeFake":"00:00:00","freightTableIds":[],"id":"catete","name":"Loja Catete","priority":0,"salesChannel":null,"salesChannels":["1"],"timeFakeOverhead":"00:00:00","wmsEndPoint":""}
    headers = { 
        'Content-Type': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/docks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate_dock(client):
    """Test case for deactivate_dock

    Deactivate dock
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/configuration/docks/{dock_id}/deactivation'.format(dock_id='dock_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dock(client):
    """Test case for dock

    Delete dock
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/logistics/pvt/configuration/docks/{dock_id}'.format(dock_id='dock_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dock_by_id(client):
    """Test case for dock_by_id

    List dock by ID
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/configuration/docks/{dock_id}'.format(dock_id='dock_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

