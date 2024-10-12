# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hybrid_runbook_worker_group import HybridRunbookWorkerGroup
from openapi_server.models.hybrid_runbook_worker_group_list_by_automation_account_default_response import HybridRunbookWorkerGroupListByAutomationAccountDefaultResponse
from openapi_server.models.hybrid_runbook_worker_group_update_parameters import HybridRunbookWorkerGroupUpdateParameters
from openapi_server.models.hybrid_runbook_worker_groups_list_result import HybridRunbookWorkerGroupsListResult


pytestmark = pytest.mark.asyncio

async def test_hybrid_runbook_worker_group_delete(client):
    """Test case for hybrid_runbook_worker_group_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/hybridRunbookWorkerGroups/{hybrid_runbook_worker_group_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', hybrid_runbook_worker_group_name='hybrid_runbook_worker_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hybrid_runbook_worker_group_get(client):
    """Test case for hybrid_runbook_worker_group_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/hybridRunbookWorkerGroups/{hybrid_runbook_worker_group_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', hybrid_runbook_worker_group_name='hybrid_runbook_worker_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hybrid_runbook_worker_group_list_by_automation_account(client):
    """Test case for hybrid_runbook_worker_group_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/hybridRunbookWorkerGroups'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hybrid_runbook_worker_group_update(client):
    """Test case for hybrid_runbook_worker_group_update

    
    """
    parameters = {"credential":{"name":"name"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/hybridRunbookWorkerGroups/{hybrid_runbook_worker_group_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', hybrid_runbook_worker_group_name='hybrid_runbook_worker_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

