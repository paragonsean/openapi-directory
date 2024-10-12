# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clusters_execute_script_actions_default_response import ClustersExecuteScriptActionsDefaultResponse
from openapi_server.models.script_action_execution_history_list import ScriptActionExecutionHistoryList
from openapi_server.models.script_actions_get_execution_detail200_response import ScriptActionsGetExecutionDetail200Response


pytestmark = pytest.mark.asyncio

async def test_script_actions_get_execution_detail(client):
    """Test case for script_actions_get_execution_detail

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/scriptExecutionHistory/{script_execution_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', script_execution_id='script_execution_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_script_execution_history_list_by_cluster(client):
    """Test case for script_execution_history_list_by_cluster

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/scriptExecutionHistory'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

