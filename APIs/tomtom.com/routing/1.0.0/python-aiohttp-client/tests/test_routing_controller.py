# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calculate_reachable_range_post_data_parameters import CalculateReachableRangePostDataParameters
from openapi_server.models.calculate_route_post_data_parameters import CalculateRoutePostDataParameters


pytestmark = pytest.mark.asyncio

async def test_routing_version_number_calculate_reachable_range_origin_content_type_get(client):
    """Test case for routing_version_number_calculate_reachable_range_origin_content_type_get

    Reachable Range
    """
    params = [('fuelBudgetInLiters', 3.4),
                    ('energyBudgetInkWh', 43),
                    ('timeBudgetInSec', 3.4),
                    ('callback', 'callback'),
                    ('report', 'report_example'),
                    ('departAt', 'now'),
                    ('arriveAt', 'arrive_at_example'),
                    ('routeType', fastest),
                    ('traffic', True),
                    ('avoid', 'unpavedRoads'),
                    ('travelMode', car),
                    ('hilliness', normal),
                    ('windingness', normal),
                    ('vehicleMaxSpeed', 0),
                    ('vehicleWeight', 0),
                    ('vehicleAxleWeight', 0),
                    ('vehicleLength', 0),
                    ('vehicleWidth', 0),
                    ('vehicleHeight', 0),
                    ('vehicleCommercial', False),
                    ('vehicleLoadType', 'vehicle_load_type_example'),
                    ('constantSpeedConsumptionInLitersPerHundredkm', 'constant_speed_consumption_in_liters_per_hundredkm_example'),
                    ('currentFuelInLiters', 3.4),
                    ('auxiliaryPowerInLitersPerHour', 3.4),
                    ('fuelEnergyDensityInMJoulesPerLiter', 3.4),
                    ('accelerationEfficiency', 3.4),
                    ('decelerationEfficiency', 3.4),
                    ('uphillEfficiency', 3.4),
                    ('downhillEfficiency', 3.4),
                    ('vehicleEngineType', combustion),
                    ('constantSpeedConsumptionInkWhPerHundredkm', '50,8.2:130,21.3')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/routing/{version_number}/calculateReachableRange/{origin}/{content_type}'.format(version_number=56, origin='52.50931,13.42936', content_type=xml),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_routing_version_number_calculate_reachable_range_origin_content_type_post(client):
    """Test case for routing_version_number_calculate_reachable_range_origin_content_type_post

    Reachable Range
    """
    body = openapi_server.CalculateReachableRangePostDataParameters()
    params = [('fuelBudgetInLiters', 3.4),
                    ('energyBudgetInkWh', 43),
                    ('timeBudgetInSec', 3.4),
                    ('callback', 'callback'),
                    ('report', 'report_example'),
                    ('departAt', 'now'),
                    ('arriveAt', 'arrive_at_example'),
                    ('routeType', fastest),
                    ('traffic', True),
                    ('avoid', 'unpavedRoads'),
                    ('travelMode', car),
                    ('hilliness', normal),
                    ('windingness', normal),
                    ('vehicleMaxSpeed', 0),
                    ('vehicleWeight', 0),
                    ('vehicleAxleWeight', 0),
                    ('vehicleLength', 0),
                    ('vehicleWidth', 0),
                    ('vehicleHeight', 0),
                    ('vehicleCommercial', False),
                    ('vehicleLoadType', 'vehicle_load_type_example'),
                    ('constantSpeedConsumptionInLitersPerHundredkm', 'constant_speed_consumption_in_liters_per_hundredkm_example'),
                    ('currentFuelInLiters', 3.4),
                    ('auxiliaryPowerInLitersPerHour', 3.4),
                    ('fuelEnergyDensityInMJoulesPerLiter', 3.4),
                    ('accelerationEfficiency', 3.4),
                    ('decelerationEfficiency', 3.4),
                    ('uphillEfficiency', 3.4),
                    ('downhillEfficiency', 3.4),
                    ('vehicleEngineType', combustion),
                    ('constantSpeedConsumptionInkWhPerHundredkm', '50,8.2:130,21.3')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/routing/{version_number}/calculateReachableRange/{origin}/{content_type}'.format(version_number=56, origin='52.50931,13.42936', content_type=xml),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_routing_version_number_calculate_route_locations_content_type_get(client):
    """Test case for routing_version_number_calculate_route_locations_content_type_get

    Calculate Route
    """
    params = [('maxAlternatives', 0),
                    ('alternativeType', anyRoute),
                    ('minDeviationDistance', 0),
                    ('minDeviationTime', 0),
                    ('instructionsType', 'instructions_type_example'),
                    ('language', 'en-GB'),
                    ('computeBestOrder', False),
                    ('routeRepresentation', polyline),
                    ('computeTravelTimeFor', none),
                    ('vehicleHeading', 56),
                    ('sectionType', 'travelMode'),
                    ('callback', 'callback'),
                    ('report', 'report_example'),
                    ('departAt', 'now'),
                    ('arriveAt', 'arrive_at_example'),
                    ('routeType', fastest),
                    ('traffic', True),
                    ('avoid', 'unpavedRoads'),
                    ('travelMode', car),
                    ('hilliness', normal),
                    ('windingness', normal),
                    ('vehicleMaxSpeed', 0),
                    ('vehicleWeight', 0),
                    ('vehicleAxleWeight', 0),
                    ('vehicleLength', 0),
                    ('vehicleWidth', 0),
                    ('vehicleHeight', 0),
                    ('vehicleCommercial', False),
                    ('vehicleLoadType', 'vehicle_load_type_example'),
                    ('vehicleEngineType', combustion),
                    ('constantSpeedConsumptionInLitersPerHundredkm', 'constant_speed_consumption_in_liters_per_hundredkm_example'),
                    ('currentFuelInLiters', 3.4),
                    ('auxiliaryPowerInLitersPerHour', 3.4),
                    ('fuelEnergyDensityInMJoulesPerLiter', 3.4),
                    ('accelerationEfficiency', 3.4),
                    ('decelerationEfficiency', 3.4),
                    ('uphillEfficiency', 3.4),
                    ('downhillEfficiency', 3.4),
                    ('constantSpeedConsumptionInkWhPerHundredkm', 'constant_speed_consumption_ink_wh_per_hundredkm_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/routing/{version_number}/calculateRoute/{locations}/{content_type}'.format(version_number=56, locations='52.50931,13.42936:52.50274,13.43872', content_type=xml),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_routing_version_number_calculate_route_locations_content_type_post(client):
    """Test case for routing_version_number_calculate_route_locations_content_type_post

    Calculate Route
    """
    body = openapi_server.CalculateRoutePostDataParameters()
    params = [('maxAlternatives', 0),
                    ('alternativeType', anyRoute),
                    ('minDeviationDistance', 0),
                    ('minDeviationTime', 0),
                    ('instructionsType', 'instructions_type_example'),
                    ('language', 'en-GB'),
                    ('computeBestOrder', False),
                    ('routeRepresentation', polyline),
                    ('computeTravelTimeFor', none),
                    ('vehicleHeading', 56),
                    ('sectionType', 'travelMode'),
                    ('callback', 'callback'),
                    ('report', 'report_example'),
                    ('departAt', 'now'),
                    ('arriveAt', 'arrive_at_example'),
                    ('routeType', fastest),
                    ('traffic', True),
                    ('avoid', 'unpavedRoads'),
                    ('travelMode', car),
                    ('hilliness', normal),
                    ('windingness', normal),
                    ('vehicleMaxSpeed', 0),
                    ('vehicleWeight', 0),
                    ('vehicleAxleWeight', 0),
                    ('vehicleLength', 0),
                    ('vehicleWidth', 0),
                    ('vehicleHeight', 0),
                    ('vehicleCommercial', False),
                    ('vehicleLoadType', 'vehicle_load_type_example'),
                    ('vehicleEngineType', combustion),
                    ('constantSpeedConsumptionInLitersPerHundredkm', 'constant_speed_consumption_in_liters_per_hundredkm_example'),
                    ('currentFuelInLiters', 3.4),
                    ('auxiliaryPowerInLitersPerHour', 3.4),
                    ('fuelEnergyDensityInMJoulesPerLiter', 3.4),
                    ('accelerationEfficiency', 3.4),
                    ('decelerationEfficiency', 3.4),
                    ('uphillEfficiency', 3.4),
                    ('downhillEfficiency', 3.4),
                    ('constantSpeedConsumptionInkWhPerHundredkm', 'constant_speed_consumption_ink_wh_per_hundredkm_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/routing/{version_number}/calculateRoute/{locations}/{content_type}'.format(version_number=56, locations='52.50931,13.42936:52.50274,13.43872', content_type=xml),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

