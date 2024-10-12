# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activation_key_result import ActivationKeyResult
from openapi_server.models.registration import Registration
from openapi_server.models.registration_list import RegistrationList
from openapi_server.models.registration_parameter import RegistrationParameter
from openapi_server.models.registrations_list_default_response import RegistrationsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_registrations_create_or_update(client):
    """Test case for registrations_create_or_update

    
    """
    token = {"location":"global","properties":{"registrationToken":"registrationToken"}}
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example'),
        headers=headers,
        json=token,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_delete(client):
    """Test case for registrations_delete

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_get(client):
    """Test case for registrations_get

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_get_activation_key(client):
    """Test case for registrations_get_activation_key

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}/getactivationkey'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_list(client):
    """Test case for registrations_list

    
    """
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations'.format(subscription_id='subscription_id_example', resource_group='resource_group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_update(client):
    """Test case for registrations_update

    
    """
    token = {"location":"global","properties":{"registrationToken":"registrationToken"}}
    params = [('api-version', '2017-06-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.AzureStack/registrations/{registration_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', registration_name='registration_name_example'),
        headers=headers,
        json=token,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

