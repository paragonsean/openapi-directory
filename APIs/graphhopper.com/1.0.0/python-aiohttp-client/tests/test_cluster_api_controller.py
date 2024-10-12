# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.cluster_request import ClusterRequest
from openapi_server.models.cluster_response import ClusterResponse
from openapi_server.models.get_cluster_solution404_response import GetClusterSolution404Response
from openapi_server.models.internal_error_message import InternalErrorMessage
from openapi_server.models.job_id import JobId


pytestmark = pytest.mark.asyncio

async def test_async_clustering_problem(client):
    """Test case for async_clustering_problem

    Batch Cluster Endpoint
    """
    body = {"configuration":{"routing":{"profile":"car","cost_per_meter":0,"cost_per_second":1},"response_type":"json","clustering":{"max_quantity":50,"min_quantity":30,"num_clusters":10}},"customers":[{"address":{"street_hint":"Lindenschmitstraße 52","lon":11.53941,"lat":48.118434},"quantity":10,"id":"GraphHopper GmbH"},{"address":{"street_hint":"Lindenschmitstraße 52","lon":11.53941,"lat":48.118434},"quantity":10,"id":"GraphHopper GmbH"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1/cluster/calculate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cluster_solution(client):
    """Test case for get_cluster_solution

    GET Batch Solution Endpoint
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1/cluster/solution/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_solve_clustering_problem(client):
    """Test case for solve_clustering_problem

    POST Cluster Endpoint
    """
    body = {"configuration":{"routing":{"profile":"car","cost_per_meter":0,"cost_per_second":1},"response_type":"json","clustering":{"max_quantity":50,"min_quantity":30,"num_clusters":10}},"customers":[{"address":{"street_hint":"Lindenschmitstraße 52","lon":11.53941,"lat":48.118434},"quantity":10,"id":"GraphHopper GmbH"},{"address":{"street_hint":"Lindenschmitstraße 52","lon":11.53941,"lat":48.118434},"quantity":10,"id":"GraphHopper GmbH"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1/cluster',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

