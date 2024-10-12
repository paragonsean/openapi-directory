# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.workflow_trigger_history import WorkflowTriggerHistory
from openapi_server.models.workflow_trigger_history_list_result import WorkflowTriggerHistoryListResult


pytestmark = pytest.mark.asyncio

async def test_workflow_trigger_histories_get(client):
    """Test case for workflow_trigger_histories_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}/histories/{history_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example', history_name='history_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_trigger_histories_list(client):
    """Test case for workflow_trigger_histories_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}/histories'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_trigger_histories_resubmit(client):
    """Test case for workflow_trigger_histories_resubmit

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/triggers/{trigger_name}/histories/{history_name}/resubmit'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', trigger_name='trigger_name_example', history_name='history_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

