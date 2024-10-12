# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.expression_traces import ExpressionTraces
from openapi_server.models.request_history import RequestHistory
from openapi_server.models.request_history_list_result import RequestHistoryListResult
from openapi_server.models.workflow_run_action import WorkflowRunAction
from openapi_server.models.workflow_run_action_list_result import WorkflowRunActionListResult
from openapi_server.models.workflow_run_action_repetition_definition import WorkflowRunActionRepetitionDefinition
from openapi_server.models.workflow_run_action_repetition_definition_collection import WorkflowRunActionRepetitionDefinitionCollection


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_repetitions_get(client):
    """Test case for workflow_run_action_repetitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/repetitions/{repetition_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example', repetition_name='repetition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_repetitions_list(client):
    """Test case for workflow_run_action_repetitions_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/repetitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_repetitions_list_expression_traces(client):
    """Test case for workflow_run_action_repetitions_list_expression_traces

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/repetitions/{repetition_name}/listExpressionTraces'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example', repetition_name='repetition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_repetitions_request_histories_get(client):
    """Test case for workflow_run_action_repetitions_request_histories_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/repetitions/{repetition_name}/requestHistories/{request_history_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example', repetition_name='repetition_name_example', request_history_name='request_history_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_repetitions_request_histories_list(client):
    """Test case for workflow_run_action_repetitions_request_histories_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/repetitions/{repetition_name}/requestHistories'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example', repetition_name='repetition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_request_histories_get(client):
    """Test case for workflow_run_action_request_histories_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/requestHistories/{request_history_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example', request_history_name='request_history_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_request_histories_list(client):
    """Test case for workflow_run_action_request_histories_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/requestHistories'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_scoped_repetitions_get(client):
    """Test case for workflow_run_action_scoped_repetitions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/scopeRepetitions/{repetition_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example', repetition_name='repetition_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_action_scoped_repetitions_list(client):
    """Test case for workflow_run_action_scoped_repetitions_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/scopeRepetitions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_actions_get(client):
    """Test case for workflow_run_actions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_actions_list(client):
    """Test case for workflow_run_actions_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workflow_run_actions_list_expression_traces(client):
    """Test case for workflow_run_actions_list_expression_traces

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/workflows/{workflow_name}/runs/{run_name}/actions/{action_name}/listExpressionTraces'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workflow_name='workflow_name_example', run_name='run_name_example', action_name='action_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

