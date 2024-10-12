# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.gh_error import GHError
from openapi_server.models.job_id import JobId
from openapi_server.models.matrix_response import MatrixResponse
from openapi_server.models.post_matrix_request import PostMatrixRequest
from openapi_server.models.vehicle_profile_id import VehicleProfileId


pytestmark = pytest.mark.asyncio

async def test_calculate_matrix(client):
    """Test case for calculate_matrix

    Batch Matrix Endpoint
    """
    body = openapi_server.PostMatrixRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1/matrix/calculate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_matrix(client):
    """Test case for get_matrix

    GET Matrix Endpoint
    """
    params = [('point', ['point_example']),
                    ('from_point', ['from_point_example']),
                    ('to_point', ['to_point_example']),
                    ('point_hint', ['point_hint_example']),
                    ('from_point_hint', ['from_point_hint_example']),
                    ('to_point_hint', ['to_point_hint_example']),
                    ('snap_prevention', ['snap_prevention_example']),
                    ('curbside', ['curbside_example']),
                    ('from_curbside', ['from_curbside_example']),
                    ('to_curbside', ['to_curbside_example']),
                    ('out_array', ['out_array_example']),
                    ('vehicle', car),
                    ('fail_fast', True),
                    ('turn_costs', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1/matrix',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_matrix_solution(client):
    """Test case for get_matrix_solution

    GET Batch Matrix Endpoint
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1/matrix/solution/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_matrix(client):
    """Test case for post_matrix

    POST Matrix Endpoint
    """
    body = openapi_server.PostMatrixRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1/matrix',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

