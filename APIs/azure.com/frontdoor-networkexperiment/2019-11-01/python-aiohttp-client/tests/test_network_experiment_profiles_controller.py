# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.profile import Profile
from openapi_server.models.profile_list import ProfileList
from openapi_server.models.profile_update_model import ProfileUpdateModel


pytestmark = pytest.mark.asyncio

async def test_network_experiment_profiles_create_or_update(client):
    """Test case for network_experiment_profiles_create_or_update

    Creates an NetworkExperiment Profile
    """
    parameters = {"name":"name","etag":"etag","properties":{"enabledState":"Enabled","resourceState":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}'.format(profile_name='profile_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_experiment_profiles_delete(client):
    """Test case for network_experiment_profiles_delete

    Deletes an NetworkExperiment Profile by ProfileName
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_experiment_profiles_get(client):
    """Test case for network_experiment_profiles_get

    Gets an NetworkExperiment Profile by ProfileName
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_experiment_profiles_list(client):
    """Test case for network_experiment_profiles_list

    Gets a list of Network Experiment Profiles under a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/NetworkExperimentProfiles'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_experiment_profiles_list_by_resource_group(client):
    """Test case for network_experiment_profiles_list_by_resource_group

    Gets a list of Network Experiment Profiles within a resource group under a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_experiment_profiles_update(client):
    """Test case for network_experiment_profiles_update

    Updates an NetworkExperimentProfiles by NetworkExperimentProfile name
    """
    parameters = {"properties":{"enabledState":"Enabled"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

