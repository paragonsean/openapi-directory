# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.performance_results_api_response import PerformanceResultsAPIResponse
from openapi_server.models.performance_spec import PerformanceSpec
from openapi_server.models.performance_test_config import PerformanceTestConfig


pytestmark = pytest.mark.asyncio

async def test_id_get_all_perf_results(client):
    """Test case for id_get_all_perf_results

    Handles GET requests for perf results
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/perf/profile/result',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_single_perf_result(client):
    """Test case for id_get_single_perf_result

    Handles GET requests for perf result
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/perf/profile/result/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_id_run_perf_test(client):
    """Test case for id_run_perf_test

    Handle GET request to run a test
    """
    body = {"duration":"duration","clients":[{"headers":{"key":"headers"},"internal":True,"protocol":6,"content_type":"content_type","rps":1,"endpoint_urls":["endpoint_urls","endpoint_urls"],"load_generator":"load_generator","body":"body","connections":0,"cookies":{"key":"cookies"}},{"headers":{"key":"headers"},"internal":True,"protocol":6,"content_type":"content_type","rps":1,"endpoint_urls":["endpoint_urls","endpoint_urls"],"load_generator":"load_generator","body":"body","connections":0,"cookies":{"key":"cookies"}}],"name":"name","smp_version":"smp_version","id":"id","labels":{"key":"labels"}}
    headers = { 
        'Content-Type': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/perf/profile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

