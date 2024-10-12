# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agent_registration_information_get_default_response import AgentRegistrationInformationGetDefaultResponse
from openapi_server.models.dsc_node import DscNode
from openapi_server.models.dsc_node_list_result import DscNodeListResult
from openapi_server.models.dsc_node_update_parameters import DscNodeUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_dsc_node_delete(client):
    """Test case for dsc_node_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodes/{node_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_id='node_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_node_get(client):
    """Test case for dsc_node_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodes/{node_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_id='node_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_node_list_by_automation_account(client):
    """Test case for dsc_node_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodes'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_node_update(client):
    """Test case for dsc_node_update

    
    """
    parameters = {"nodeConfiguration":{"name":"name"},"nodeId":"nodeId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodes/{node_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', node_id='node_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

