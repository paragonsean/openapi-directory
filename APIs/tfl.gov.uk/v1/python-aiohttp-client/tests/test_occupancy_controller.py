# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_bike_point_occupancy import TflApiPresentationEntitiesBikePointOccupancy
from openapi_server.models.tfl_api_presentation_entities_car_park_occupancy import TflApiPresentationEntitiesCarParkOccupancy
from openapi_server.models.tfl_api_presentation_entities_charge_connector_occupancy import TflApiPresentationEntitiesChargeConnectorOccupancy


pytestmark = pytest.mark.asyncio

async def test_occupancy_car_park_get(client):
    """Test case for occupancy_car_park_get

    Gets the occupancy for all car parks that have occupancy data
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Occupancy/CarPark',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_occupancy_get(client):
    """Test case for occupancy_get

    Gets the occupancy for a car park with a given id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Occupancy/CarPark/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_occupancy_get_all_charge_connector_status(client):
    """Test case for occupancy_get_all_charge_connector_status

    Gets the occupancy for all charge connectors
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Occupancy/ChargeConnector',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_occupancy_get_bike_points_occupancies(client):
    """Test case for occupancy_get_bike_points_occupancies

    Get the occupancy for bike points.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Occupancy/BikePoints/{ids}'.format(ids=['ids_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_occupancy_get_charge_connector_status(client):
    """Test case for occupancy_get_charge_connector_status

    Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Occupancy/ChargeConnector/{ids}'.format(ids=['ids_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

