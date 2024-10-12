# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.logs import Logs
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners
from openapi_server.models.run import Run
from openapi_server.models.run_manually import RunManually
from openapi_server.models.runs import Runs
from openapi_server.models.task import Task
from openapi_server.models.task_create_request import TaskCreateRequest
from openapi_server.models.task_update_request import TaskUpdateRequest
from openapi_server.models.tasks import Tasks


pytestmark = pytest.mark.asyncio

async def test_delete_tasks_id(client):
    """Test case for delete_tasks_id

    Delete a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/tasks/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tasks_id_labels_id(client):
    """Test case for delete_tasks_id_labels_id

    Delete a label from a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/tasks/{task_id}/labels/{label_id}'.format(task_id='task_id_example', label_id='label_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tasks_id_members_id(client):
    """Test case for delete_tasks_id_members_id

    Remove a member from a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/tasks/{task_id}/members/{user_id}'.format(user_id='user_id_example', task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tasks_id_owners_id(client):
    """Test case for delete_tasks_id_owners_id

    Remove an owner from a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/tasks/{task_id}/owners/{user_id}'.format(user_id='user_id_example', task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tasks_id_runs_id(client):
    """Test case for delete_tasks_id_runs_id

    Cancel a running task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/tasks/{task_id}/runs/{run_id}'.format(task_id='task_id_example', run_id='run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks(client):
    """Test case for get_tasks

    List all tasks
    """
    params = [('name', 'name_example'),
                    ('after', 'after_example'),
                    ('user', 'user_example'),
                    ('org', 'org_example'),
                    ('orgID', 'org_id_example'),
                    ('status', 'status_example'),
                    ('limit', 100)]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_id(client):
    """Test case for get_tasks_id

    Retrieve a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_id_labels(client):
    """Test case for get_tasks_id_labels

    List all labels for a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks/{task_id}/labels'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_id_logs(client):
    """Test case for get_tasks_id_logs

    Retrieve all logs for a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks/{task_id}/logs'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_id_members(client):
    """Test case for get_tasks_id_members

    List all task members
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks/{task_id}/members'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_id_owners(client):
    """Test case for get_tasks_id_owners

    List all owners of a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks/{task_id}/owners'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_id_runs(client):
    """Test case for get_tasks_id_runs

    List runs for a task
    """
    params = [('after', 'after_example'),
                    ('limit', 100),
                    ('afterTime', '2013-10-20T19:20:30+01:00'),
                    ('beforeTime', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks/{task_id}/runs'.format(task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_id_runs_id(client):
    """Test case for get_tasks_id_runs_id

    Retrieve a single run for a task
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks/{task_id}/runs/{run_id}'.format(task_id='task_id_example', run_id='run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_id_runs_id_logs(client):
    """Test case for get_tasks_id_runs_id_logs

    Retrieve all logs for a run
    """
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/tasks/{task_id}/runs/{run_id}/logs'.format(task_id='task_id_example', run_id='run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_tasks_id(client):
    """Test case for patch_tasks_id

    Update a task
    """
    body = {"cron":"cron","offset":"offset","name":"name","description":"description","flux":"flux","every":"every","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/tasks/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_tasks(client):
    """Test case for post_tasks

    Create a new task
    """
    body = {"org":"org","description":"description","flux":"flux","orgID":"orgID","status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/tasks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_tasks_id_labels(client):
    """Test case for post_tasks_id_labels

    Add a label to a task
    """
    body = {"labelID":"labelID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/tasks/{task_id}/labels'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_tasks_id_members(client):
    """Test case for post_tasks_id_members

    Add a member to a task
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/tasks/{task_id}/members'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_tasks_id_owners(client):
    """Test case for post_tasks_id_owners

    Add an owner to a task
    """
    body = {"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/tasks/{task_id}/owners'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_tasks_id_runs(client):
    """Test case for post_tasks_id_runs

    Manually start a task run, overriding the current schedule
    """
    body = {"scheduledFor":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/tasks/{task_id}/runs'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_post_tasks_id_runs_id_retry(client):
    """Test case for post_tasks_id_runs_id_retry

    Retry a task run
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=utf-8',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/tasks/{task_id}/runs/{run_id}/retry'.format(task_id='task_id_example', run_id='run_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

