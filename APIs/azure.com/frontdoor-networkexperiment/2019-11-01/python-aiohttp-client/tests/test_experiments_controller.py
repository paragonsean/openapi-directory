# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.experiment import Experiment
from openapi_server.models.experiment_list import ExperimentList
from openapi_server.models.experiment_update_model import ExperimentUpdateModel


pytestmark = pytest.mark.asyncio

async def test_experiments_create_or_update(client):
    """Test case for experiments_create_or_update

    Creates or updates an Experiment
    """
    parameters = {"name":"name","properties":{"endpointA":{"endpoint":"endpoint","name":"name"},"endpointB":{"endpoint":"endpoint","name":"name"},"enabledState":"Enabled","scriptFileUri":"scriptFileUri","description":"description","resourceState":"Creating","status":"status"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}/Experiments/{experiment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_experiments_delete(client):
    """Test case for experiments_delete

    Deletes an Experiment
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}/Experiments/{experiment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_experiments_get(client):
    """Test case for experiments_get

    Gets an Experiment by ExperimentName
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}/Experiments/{experiment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_experiments_list_by_profile(client):
    """Test case for experiments_list_by_profile

    Gets a list of Experiments
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}/Experiments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_experiments_update(client):
    """Test case for experiments_update

    Updates an Experiment by Experiment id
    """
    parameters = {"properties":{"enabledState":"Enabled","description":"description"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/NetworkExperimentProfiles/{profile_name}/Experiments/{experiment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example', experiment_name='experiment_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

