# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.task_run import TaskRun
from openapi_server.models.task_run_list_result import TaskRunListResult
from openapi_server.models.task_run_update_parameters import TaskRunUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_task_runs_create(client):
    """Test case for task_runs_create

    
    """
    task_run = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"properties":{"runRequest":{"isArchiveEnabled":False,"type":"type"},"provisioningState":"Creating","runResult":{"properties":{"finishTime":"2000-01-23T04:56:07.000+00:00","runType":"QuickBuild","runErrorMessage":"runErrorMessage","imageUpdateTrigger":{"images":[{"registry":"registry","digest":"digest","tag":"tag","repository":"repository"},{"registry":"registry","digest":"digest","tag":"tag","repository":"repository"}],"id":"id","timestamp":"2000-01-23T04:56:07.000+00:00"},"updateTriggerToken":"updateTriggerToken","provisioningState":"Creating","sourceTrigger":{"branchName":"branchName","commitId":"commitId","eventType":"eventType","id":"id","pullRequestId":"pullRequestId","providerType":"providerType","repositoryUrl":"repositoryUrl"},"platform":{"os":"Windows","variant":"v6","architecture":"amd64"},"sourceRegistryAuth":"sourceRegistryAuth","timerTrigger":{"scheduleOccurrence":"scheduleOccurrence","timerTriggerName":"timerTriggerName"},"task":"task","agentConfiguration":{"cpu":0},"createTime":"2000-01-23T04:56:07.000+00:00","customRegistries":["customRegistries","customRegistries"],"outputImages":[{"registry":"registry","digest":"digest","tag":"tag","repository":"repository"},{"registry":"registry","digest":"digest","tag":"tag","repository":"repository"}],"lastUpdatedTime":"2000-01-23T04:56:07.000+00:00","startTime":"2000-01-23T04:56:07.000+00:00","isArchiveEnabled":False,"runId":"runId","status":"Queued"}},"forceUpdateTag":"forceUpdateTag"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/taskRuns/{task_run_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_run_name='task_run_name_example'),
        headers=headers,
        json=task_run,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_runs_delete(client):
    """Test case for task_runs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/taskRuns/{task_run_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_run_name='task_run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_runs_get(client):
    """Test case for task_runs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/taskRuns/{task_run_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_run_name='task_run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_runs_list(client):
    """Test case for task_runs_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/taskRuns'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_runs_update(client):
    """Test case for task_runs_update

    
    """
    update_parameters = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"properties":{"runRequest":{"isArchiveEnabled":False,"type":"type"},"forceUpdateTag":"forceUpdateTag"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/taskRuns/{task_run_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_run_name='task_run_name_example'),
        headers=headers,
        json=update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

