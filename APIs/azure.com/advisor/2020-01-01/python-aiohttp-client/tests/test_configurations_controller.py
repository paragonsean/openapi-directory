# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.arm_error_response import ArmErrorResponse
from openapi_server.models.config_data import ConfigData
from openapi_server.models.configuration_list_result import ConfigurationListResult


pytestmark = pytest.mark.asyncio

async def test_configurations_create_in_resource_group(client):
    """Test case for configurations_create_in_resource_group

    Create/Overwrite Azure Advisor configuration.
    """
    config_contract = {"properties":{"lowCpuThreshold":"5","digests":[{"actionGroupResourceId":"actionGroupResourceId","name":"name","language":"language","categories":["HighAvailability","HighAvailability"],"state":"Active","frequency":0},{"actionGroupResourceId":"actionGroupResourceId","name":"name","language":"language","categories":["HighAvailability","HighAvailability"],"state":"Active","frequency":0}],"exclude":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Advisor/configurations/{configuration_name}'.format(subscription_id='subscription_id_example', configuration_name='configuration_name_example', resource_group='resource_group_example'),
        headers=headers,
        json=config_contract,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configurations_create_in_subscription(client):
    """Test case for configurations_create_in_subscription

    Create/Overwrite Azure Advisor configuration.
    """
    config_contract = {"properties":{"lowCpuThreshold":"5","digests":[{"actionGroupResourceId":"actionGroupResourceId","name":"name","language":"language","categories":["HighAvailability","HighAvailability"],"state":"Active","frequency":0},{"actionGroupResourceId":"actionGroupResourceId","name":"name","language":"language","categories":["HighAvailability","HighAvailability"],"state":"Active","frequency":0}],"exclude":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Advisor/configurations/{configuration_name}'.format(subscription_id='subscription_id_example', configuration_name='configuration_name_example'),
        headers=headers,
        json=config_contract,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configurations_list_by_resource_group(client):
    """Test case for configurations_list_by_resource_group

    Retrieve Azure Advisor configurations.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Advisor/configurations'.format(subscription_id='subscription_id_example', resource_group='resource_group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configurations_list_by_subscription(client):
    """Test case for configurations_list_by_subscription

    Retrieve Azure Advisor configurations.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Advisor/configurations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

