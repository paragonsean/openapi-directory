# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activation import Activation
from openapi_server.models.activation_resource import ActivationResource
from openapi_server.models.activation_resources_page import ActivationResourcesPage


pytestmark = pytest.mark.asyncio

async def test_activations_create_or_update(client):
    """Test case for activations_create_or_update

    
    """
    activation = {"marketplaceSyndicationEnabled":True,"azureRegistrationResourceIdentifier":"azureRegistrationResourceIdentifier","displayName":"displayName","expiration":"expiration","provisioningState":"Stopped","usageReportingEnabled":True}
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example'),
        headers=headers,
        json=activation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activations_delete(client):
    """Test case for activations_delete

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activations_get(client):
    """Test case for activations_get

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations/{activation_name}'.format(subscription_id='subscription_id_example', resource_group='resource_group_example', activation_name='activation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activations_list(client):
    """Test case for activations_list

    
    """
    params = [('api-version', '2016-01-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group}/providers/Microsoft.AzureBridge.Admin/activations'.format(subscription_id='subscription_id_example', resource_group='resource_group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

