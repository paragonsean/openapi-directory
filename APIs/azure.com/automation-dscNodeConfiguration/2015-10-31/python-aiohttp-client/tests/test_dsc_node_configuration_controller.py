# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dsc_node_configuration import DscNodeConfiguration
from openapi_server.models.dsc_node_configuration_create_or_update_parameters import DscNodeConfigurationCreateOrUpdateParameters
from openapi_server.models.dsc_node_configuration_list_by_automation_account_default_response import DscNodeConfigurationListByAutomationAccountDefaultResponse
from openapi_server.models.dsc_node_configuration_list_result import DscNodeConfigurationListResult


pytestmark = pytest.mark.asyncio

async def test_dsc_node_configuration_create_or_update(client):
    """Test case for dsc_node_configuration_create_or_update

    
    """
    parameters = {"incrementNodeConfigurationBuild":True,"configuration":{"name":"name"},"name":"name","source":{"type":"embeddedContent","value":"value","version":"version","hash":{"value":"value","algorithm":"algorithm"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodeConfigurations/{node_configuration_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_configuration_name='node_configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_node_configuration_delete(client):
    """Test case for dsc_node_configuration_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodeConfigurations/{node_configuration_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_configuration_name='node_configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_node_configuration_get(client):
    """Test case for dsc_node_configuration_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodeConfigurations/{node_configuration_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_configuration_name='node_configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_node_configuration_list_by_automation_account(client):
    """Test case for dsc_node_configuration_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodeConfigurations'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

