# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gh_error import GHError
from openapi_server.models.info_response import InfoResponse
from openapi_server.models.route_request import RouteRequest
from openapi_server.models.route_response import RouteResponse
from openapi_server.models.vehicle_profile_id import VehicleProfileId


pytestmark = pytest.mark.asyncio

async def test_get_route(client):
    """Test case for get_route

    GET Route Endpoint
    """
    params = [('point', ['point_example']),
                    ('point_hint', ['point_hint_example']),
                    ('snap_prevention', ['snap_prevention_example']),
                    ('vehicle', car),
                    ('curbside', ['curbside_example']),
                    ('turn_costs', False),
                    ('locale', 'en'),
                    ('elevation', False),
                    ('details', ['details_example']),
                    ('optimize', 'false'),
                    ('instructions', True),
                    ('calc_points', True),
                    ('debug', False),
                    ('points_encoded', True),
                    ('ch.disable', False),
                    ('weighting', 'fastest'),
                    ('heading', [56]),
                    ('heading_penalty', 120),
                    ('pass_through', False),
                    ('block_area', 'block_area_example'),
                    ('avoid', 'avoid_example'),
                    ('algorithm', 'algorithm_example'),
                    ('round_trip.distance', 10000),
                    ('round_trip.seed', 56),
                    ('alternative_route.max_paths', 2),
                    ('alternative_route.max_weight_factor', 1.4),
                    ('alternative_route.max_share_factor', 0.6)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1/route',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_route(client):
    """Test case for post_route

    POST Route Endpoint
    """
    body = {"calc_points":True,"details":["road_class","surface"],"instructions":True,"locale":"en","point_hints":["Lindenschmitstraße","Thalkirchener Str."],"points":[[11.539421,48.118477],[11.559023,48.12228]],"points_encoded":False,"snap_preventions":["motorway","ferry","tunnel"],"vehicle":"bike"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1/route',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_route_info_get(client):
    """Test case for route_info_get

    Coverage information
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1/route/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

