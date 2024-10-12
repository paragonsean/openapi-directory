# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster_code_versions_list_result import ClusterCodeVersionsListResult


pytestmark = pytest.mark.asyncio

async def test_cluster_versions_get(client):
    """Test case for cluster_versions_get

    Gets information about a Service Fabric cluster code version available in the specified location.
    """
    params = [('api-version', 2019-06-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions/{cluster_version}'.format(location='location_example', subscription_id='subscription_id_example', cluster_version='cluster_version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_versions_get_by_environment(client):
    """Test case for cluster_versions_get_by_environment

    Gets information about a Service Fabric cluster code version available for the specified environment.
    """
    params = [('api-version', 2019-06-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions/{cluster_version}'.format(location='location_example', environment='environment_example', subscription_id='subscription_id_example', cluster_version='cluster_version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_versions_list(client):
    """Test case for cluster_versions_list

    Gets the list of Service Fabric cluster code versions available for the specified location.
    """
    params = [('api-version', 2019-06-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cluster_versions_list_by_environment(client):
    """Test case for cluster_versions_list_by_environment

    Gets the list of Service Fabric cluster code versions available for the specified environment.
    """
    params = [('api-version', 2019-06-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions'.format(location='location_example', environment='environment_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

