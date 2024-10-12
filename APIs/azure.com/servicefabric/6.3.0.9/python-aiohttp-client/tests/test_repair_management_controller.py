# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.repair_task import RepairTask
from openapi_server.models.repair_task_approve_description import RepairTaskApproveDescription
from openapi_server.models.repair_task_cancel_description import RepairTaskCancelDescription
from openapi_server.models.repair_task_delete_description import RepairTaskDeleteDescription
from openapi_server.models.repair_task_update_health_policy_description import RepairTaskUpdateHealthPolicyDescription
from openapi_server.models.repair_task_update_info import RepairTaskUpdateInfo


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_cancel_repair_task(client):
    """Test case for cancel_repair_task

    Requests the cancellation of the given repair task.
    """
    repair_task_cancel_description = openapi_server.RepairTaskCancelDescription()
    params = [('api-version', 6.0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/CancelRepairTask',
        headers=headers,
        json=repair_task_cancel_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_repair_task(client):
    """Test case for create_repair_task

    Creates a new repair task.
    """
    repair_task = openapi_server.RepairTask()
    params = [('api-version', 6.0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/CreateRepairTask',
        headers=headers,
        json=repair_task,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_delete_repair_task(client):
    """Test case for delete_repair_task

    Deletes a completed repair task.
    """
    repair_task_delete_description = openapi_server.RepairTaskDeleteDescription()
    params = [('api-version', 6.0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/DeleteRepairTask',
        headers=headers,
        json=repair_task_delete_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_force_approve_repair_task(client):
    """Test case for force_approve_repair_task

    Forces the approval of the given repair task.
    """
    repair_task_approve_description = openapi_server.RepairTaskApproveDescription()
    params = [('api-version', 6.0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/ForceApproveRepairTask',
        headers=headers,
        json=repair_task_approve_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_repair_task_list(client):
    """Test case for get_repair_task_list

    Gets a list of repair tasks matching the given filters.
    """
    params = [('api-version', 6.0),
                    ('TaskIdFilter', 'task_id_filter_example'),
                    ('StateFilter', 56),
                    ('ExecutorFilter', 'executor_filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/$/GetRepairTaskList',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_repair_execution_state(client):
    """Test case for update_repair_execution_state

    Updates the execution state of a repair task.
    """
    repair_task = openapi_server.RepairTask()
    params = [('api-version', 6.0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/UpdateRepairExecutionState',
        headers=headers,
        json=repair_task,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_repair_task_health_policy(client):
    """Test case for update_repair_task_health_policy

    Updates the health policy of the given repair task.
    """
    repair_task_update_health_policy_description = openapi_server.RepairTaskUpdateHealthPolicyDescription()
    params = [('api-version', 6.0)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/$/UpdateRepairTaskHealthPolicy',
        headers=headers,
        json=repair_task_update_health_policy_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

