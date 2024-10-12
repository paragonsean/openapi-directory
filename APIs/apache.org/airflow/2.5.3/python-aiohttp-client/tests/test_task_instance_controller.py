# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.extra_link_collection import ExtraLinkCollection
from openapi_server.models.get_log200_response import GetLog200Response
from openapi_server.models.list_task_instance_form import ListTaskInstanceForm
from openapi_server.models.set_task_instance_note import SetTaskInstanceNote
from openapi_server.models.task_instance import TaskInstance
from openapi_server.models.task_instance_collection import TaskInstanceCollection
from openapi_server.models.task_instance_reference import TaskInstanceReference
from openapi_server.models.update_task_instance import UpdateTaskInstance


pytestmark = pytest.mark.asyncio

async def test_get_extra_links(client):
    """Test case for get_extra_links

    List extra links
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_log(client):
    """Test case for get_log

    Get logs
    """
    params = [('full_content', True),
                    ('map_index', 56),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example', task_try_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mapped_task_instance(client):
    """Test case for get_mapped_task_instance

    Get a mapped task instance
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example', map_index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mapped_task_instances(client):
    """Test case for get_mapped_task_instances

    List mapped task instances
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('execution_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('execution_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('start_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('start_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('end_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('end_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('duration_gte', 3.4),
                    ('duration_lte', 3.4),
                    ('state', ['state_example']),
                    ('pool', ['pool_example']),
                    ('queue', ['queue_example']),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/listMapped'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_instance(client):
    """Test case for get_task_instance

    Get a task instance
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_instances(client):
    """Test case for get_task_instances

    List task instances
    """
    params = [('execution_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('execution_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('start_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('start_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('end_date_gte', '2013-10-20T19:20:30+01:00'),
                    ('end_date_lte', '2013-10-20T19:20:30+01:00'),
                    ('duration_gte', 3.4),
                    ('duration_lte', 3.4),
                    ('state', ['state_example']),
                    ('pool', ['pool_example']),
                    ('queue', ['queue_example']),
                    ('limit', 100),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_instances_batch(client):
    """Test case for get_task_instances_batch

    List task instances (batch)
    """
    body = {"end_date_lte":"2000-01-23T04:56:07.000+00:00","start_date_gte":"2000-01-23T04:56:07.000+00:00","duration_gte":0.8008281904610115,"execution_date_gte":"2000-01-23T04:56:07.000+00:00","execution_date_lte":"2000-01-23T04:56:07.000+00:00","pool":["pool","pool"],"duration_lte":6.027456183070403,"end_date_gte":"2000-01-23T04:56:07.000+00:00","state":["success","success"],"start_date_lte":"2000-01-23T04:56:07.000+00:00","dag_ids":["dag_ids","dag_ids"],"queue":["queue","queue"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/dags/~/dagRuns/~/taskInstances/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_mapped_task_instance(client):
    """Test case for patch_mapped_task_instance

    Updates the state of a mapped task instance
    """
    body = {"new_state":"success","dry_run":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example', map_index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_task_instance(client):
    """Test case for patch_task_instance

    Updates the state of a task instance
    """
    body = {"new_state":"success","dry_run":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_mapped_task_instance_note(client):
    """Test case for set_mapped_task_instance_note

    Update the TaskInstance note.
    """
    body = {"note":"note"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/{map_index}/setNote'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example', map_index=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_task_instance_note(client):
    """Test case for set_task_instance_note

    Update the TaskInstance note.
    """
    body = {"note":"note"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/setNote'.format(dag_id='dag_id_example', dag_run_id='dag_run_id_example', task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

