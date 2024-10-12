# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.workflow_run import WorkflowRun
from openapi_server.models.workflow_run_list_result import WorkflowRunListResult


pytestmark = pytest.mark.asyncio

async def test_workflow_runs_cancel(client):
    """Test case for workflow_runs_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/cancel'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_runs_delete(client):
    """Test case for workflow_runs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_runs_get(client):
    """Test case for workflow_runs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_runs_list(client):
    """Test case for workflow_runs_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

