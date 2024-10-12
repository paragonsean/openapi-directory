# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_configuration import BatchConfiguration
from openapi_server.models.batch_configuration_collection import BatchConfigurationCollection


pytestmark = pytest.mark.asyncio

async def test_integration_account_batch_configurations_create_or_update(client):
    """Test case for integration_account_batch_configurations_create_or_update

    
    """
    batch_configuration = {"properties":{"createdTime":"2000-01-23T04:56:07.000+00:00","releaseCriteria":{"recurrence":{"schedule":{"hours":[5,5],"monthlyOccurrences":[{"occurrence":7,"day":"Sunday"},{"occurrence":7,"day":"Sunday"}],"weekDays":["Sunday","Sunday"],"minutes":[5,5],"monthDays":[2,2]},"timeZone":"timeZone","interval":1,"startTime":"startTime","endTime":"endTime","frequency":"NotSpecified"},"messageCount":6,"batchSize":0},"changedTime":"2000-01-23T04:56:07.000+00:00","batchGroupName":"batchGroupName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/batchConfigurations/{batch_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', batch_configuration_name='batch_configuration_name_example'),
        headers=headers,
        json=batch_configuration,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_batch_configurations_delete(client):
    """Test case for integration_account_batch_configurations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/batchConfigurations/{batch_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', batch_configuration_name='batch_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_batch_configurations_get(client):
    """Test case for integration_account_batch_configurations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/batchConfigurations/{batch_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', batch_configuration_name='batch_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_integration_account_batch_configurations_list(client):
    """Test case for integration_account_batch_configurations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/batchConfigurations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

