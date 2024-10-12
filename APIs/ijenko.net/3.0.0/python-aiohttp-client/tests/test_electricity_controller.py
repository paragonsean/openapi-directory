# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error import DefaultError
from openapi_server.models.electricity_autonomy import ElectricityAutonomy
from openapi_server.models.electricity_flows import ElectricityFlows
from openapi_server.models.electricity_flows_setup import ElectricityFlowsSetup
from openapi_server.models.electricity_self_consumption import ElectricitySelfConsumption


pytestmark = pytest.mark.asyncio

async def test_place_electricity_autonomy(client):
    """Test case for place_electricity_autonomy

    Get autonomy rate of the place
    """
    params = [('when', '2013-10-20T19:20:30+01:00'),
                    ('span', 'span_example')]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/electricity/autonomy'.format(place_id='place_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_electricity_get_flows(client):
    """Test case for place_electricity_get_flows

    Get electricity virtual flows
    """
    params = [('flows', ['flows_example'])]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/electricity/flows'.format(place_id='place_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_electricity_get_flows_setup(client):
    """Test case for place_electricity_get_flows_setup

    Get electricity flows setup
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/electricity/flows/setup'.format(place_id='place_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_electricity_self_consumption(client):
    """Test case for place_electricity_self_consumption

    Get self-consumption rate of the place
    """
    params = [('when', '2013-10-20T19:20:30+01:00'),
                    ('span', 'span_example')]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/electricity/self-consumption'.format(place_id='place_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

