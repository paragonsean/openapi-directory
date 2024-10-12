# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clusters_execute_script_actions_default_response import ClustersExecuteScriptActionsDefaultResponse
from openapi_server.models.clusters_execute_script_actions_request import ClustersExecuteScriptActionsRequest


pytestmark = pytest.mark.asyncio

async def test_clusters_execute_script_actions(client):
    """Test case for clusters_execute_script_actions

    
    """
    parameters = openapi_server.ClustersExecuteScriptActionsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/executeScriptActions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

