# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.get_cluster_solution404_response import GetClusterSolution404Response
from openapi_server.models.internal_error_message import InternalErrorMessage
from openapi_server.models.job_id import JobId
from openapi_server.models.request import Request
from openapi_server.models.response import Response


pytestmark = pytest.mark.asyncio

async def test_async_vrp(client):
    """Test case for async_vrp

    POST route optimization problem (batch mode)
    """
    body = {"configuration":{"routing":{"calc_points":True,"snap_preventions":["motorway","trunk","tunnel","bridge","ferry"]}},"objectives":[{"type":"min","value":"vehicles"},{"type":"min","value":"completion_time"}],"services":[{"address":{"lat":52.537338,"location_id":"13.375854_52.537338","lon":13.375854},"id":"s-1","name":"visit-Joe","size":[1],"time_windows":[{"earliest":1554805329,"latest":1554806329}]},{"address":{"lat":52.525851,"location_id":"13.393364_52.525851","lon":13.393364},"id":"s-2","name":"serve-Peter","size":[1]},{"address":{"lat":52.523543,"location_id":"13.416882_52.523543","lon":13.416882},"id":"s-3","name":"visit-Michael","size":[1]},{"address":{"lat":52.514038,"location_id":"13.395767_52.514038","lon":13.395767},"id":"s-4","name":"do nothing","size":[1]}],"shipments":[{"delivery":{"address":{"lat":52.513614,"location_id":"13.380575_52.513614","lon":13.380575}},"id":"7fe77504-7df8-4497-843c-02d70b6490ce","name":"pickup and deliver pizza to Peter","pickup":{"address":{"lat":52.529961,"location_id":"13.387613_52.529961","lon":13.387613}},"priority":1,"required_skills":["physical strength"],"size":[1]}],"vehicle_types":[{"capacity":[10],"profile":"bike","type_id":"cargo-bike"}],"vehicles":[{"earliest_start":1554804329,"latest_end":1554808329,"max_jobs":3,"start_address":{"lat":52.537,"location_id":"berlin","lon":13.406},"type_id":"cargo-bike","vehicle_id":"vehicle-1"},{"earliest_start":1554804329,"latest_end":1554808329,"max_jobs":3,"skills":["physical strength"],"start_address":{"lat":52.537,"location_id":"berlin","lon":13.406},"type_id":"cargo-bike","vehicle_id":"vehicle-2"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1/vrp/optimize',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_solution(client):
    """Test case for get_solution

    GET the solution (batch mode)
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1/vrp/solution/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solve_vrp(client):
    """Test case for solve_vrp

    POST route optimization problem
    """
    body = {"configuration":{"routing":{"calc_points":True,"snap_preventions":["motorway","trunk","tunnel","bridge","ferry"]}},"objectives":[{"type":"min","value":"vehicles"},{"type":"min","value":"completion_time"}],"services":[{"address":{"lat":52.537338,"location_id":"13.375854_52.537338","lon":13.375854},"id":"s-1","name":"visit-Joe","size":[1],"time_windows":[{"earliest":1554805329,"latest":1554806329}]},{"address":{"lat":52.525851,"location_id":"13.393364_52.525851","lon":13.393364},"id":"s-2","name":"serve-Peter","size":[1]},{"address":{"lat":52.523543,"location_id":"13.416882_52.523543","lon":13.416882},"id":"s-3","name":"visit-Michael","size":[1]},{"address":{"lat":52.514038,"location_id":"13.395767_52.514038","lon":13.395767},"id":"s-4","name":"do nothing","size":[1]}],"shipments":[{"delivery":{"address":{"lat":52.513614,"location_id":"13.380575_52.513614","lon":13.380575}},"id":"7fe77504-7df8-4497-843c-02d70b6490ce","name":"pickup and deliver pizza to Peter","pickup":{"address":{"lat":52.529961,"location_id":"13.387613_52.529961","lon":13.387613}},"priority":1,"required_skills":["physical strength"],"size":[1]}],"vehicle_types":[{"capacity":[10],"profile":"bike","type_id":"cargo-bike"}],"vehicles":[{"earliest_start":1554804329,"latest_end":1554808329,"max_jobs":3,"start_address":{"lat":52.537,"location_id":"berlin","lon":13.406},"type_id":"cargo-bike","vehicle_id":"vehicle-1"},{"earliest_start":1554804329,"latest_end":1554808329,"max_jobs":3,"skills":["physical strength"],"start_address":{"lat":52.537,"location_id":"berlin","lon":13.406},"type_id":"cargo-bike","vehicle_id":"vehicle-2"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1/vrp',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

