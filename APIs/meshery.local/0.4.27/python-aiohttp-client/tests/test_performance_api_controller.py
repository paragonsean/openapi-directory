# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.performance_profile import PerformanceProfile
from openapi_server.models.performance_profile_parameters import PerformanceProfileParameters
from openapi_server.models.performance_profiles_api_response import PerformanceProfilesAPIResponse
from openapi_server.models.performance_results_api_response import PerformanceResultsAPIResponse


pytestmark = pytest.mark.asyncio

async def test_id_delete_performance_profile(client):
    """Test case for id_delete_performance_profile

    Handle Delete requests for performance profiles
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/user/performance/profiles/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_all_performance_results(client):
    """Test case for id_get_all_performance_results

    Handles GET requests for performance results
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/performance/profiles/results',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_performance_profiles(client):
    """Test case for id_get_performance_profiles

    Handle GET requests for performance profiles
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/performance/profiles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_profile_results(client):
    """Test case for id_get_profile_results

    Handle GET request for results of a profile
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/performance/profiles/{id}/results'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_single_performance_profile(client):
    """Test case for id_get_single_performance_profile

    Handle GET requests for performance results of a profile
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/performance/profiles/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_run_performance_test(client):
    """Test case for id_run_performance_test

    Handle GET request to run a performance test
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/user/performance/profiles/{id}/run'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_id_save_performance_profile(client):
    """Test case for id_save_performance_profile

    Handle POST requests for saving performance profile
    """
    body = {"duration":"duration","endpoints":["endpoints","endpoints"],"concurrent_request":0,"load_generators":["load_generators","load_generators"],"qps":6,"service_mesh":"service_mesh","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/user/performance/profiles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

