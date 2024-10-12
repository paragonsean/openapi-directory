# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_result import ActionResult
from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_gateway_unreachable import ErrorGatewayUnreachable


pytestmark = pytest.mark.asyncio

async def test_device_run(client):
    """Test case for device_run

    Run actions
    """
    arguments = None
    params = [('functionalities', 'functionalities_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/devices/{device_id}/run/{action}'.format(device_id='device_id_example', action='action_example'),
        headers=headers,
        json=arguments,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functionality_run(client):
    """Test case for functionality_run

    Run an action
    """
    arguments = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/functionalities/{functionality_id}/run/{action}'.format(functionality_id='functionality_id_example', action='action_example'),
        headers=headers,
        json=arguments,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_run(client):
    """Test case for place_run

    Run actions
    """
    arguments = None
    params = [('devices', 'devices_example'),
                    ('functionalities', 'functionalities_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/places/{place_id}/run/{action}'.format(place_id='place_id_example', action='action_example'),
        headers=headers,
        json=arguments,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

