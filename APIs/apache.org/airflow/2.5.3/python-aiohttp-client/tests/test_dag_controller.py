# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clear_task_instances import ClearTaskInstances
from openapi_server.models.dag import DAG
from openapi_server.models.dag_collection import DAGCollection
from openapi_server.models.dag_detail import DAGDetail
from openapi_server.models.error import Error
from openapi_server.models.get_dag_source200_response import GetDagSource200Response
from openapi_server.models.task import Task
from openapi_server.models.task_collection import TaskCollection
from openapi_server.models.task_instance_reference_collection import TaskInstanceReferenceCollection
from openapi_server.models.update_task_instances_state import UpdateTaskInstancesState


pytestmark = pytest.mark.asyncio

async def test_delete_dag(client):
    """Test case for delete_dag

    Delete a DAG
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/dags/{dag_id}'.format(dag_id='dag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dag(client):
    """Test case for get_dag

    Get basic information about a DAG
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}'.format(dag_id='dag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dag_details(client):
    """Test case for get_dag_details

    Get a simplified representation of DAG
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/details'.format(dag_id='dag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dag_source(client):
    """Test case for get_dag_source

    Get a source code
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dagSources/{file_token}'.format(file_token='file_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dags(client):
    """Test case for get_dags

    List DAGs
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example'),
                    ('tags', ['tags_example']),
                    ('only_active', True),
                    ('dag_id_pattern', 'dag_id_pattern_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task(client):
    """Test case for get_task

    Get simplified representation of a task
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/tasks/{task_id}'.format(dag_id='dag_id_example', task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks(client):
    """Test case for get_tasks

    Get tasks for DAG
    """
    params = [('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dags/{dag_id}/tasks'.format(dag_id='dag_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_dag(client):
    """Test case for patch_dag

    Update a DAG
    """
    body = {"description":"description","owners":["owners","owners"],"fileloc":"fileloc","has_task_concurrency_limits":True,"root_dag_id":"root_dag_id","has_import_errors":True,"last_pickled":"2000-01-23T04:56:07.000+00:00","last_parsed_time":"2000-01-23T04:56:07.000+00:00","next_dagrun_create_after":"2000-01-23T04:56:07.000+00:00","dag_id":"dag_id","scheduler_lock":True,"default_view":"default_view","next_dagrun_data_interval_end":"2000-01-23T04:56:07.000+00:00","next_dagrun_data_interval_start":"2000-01-23T04:56:07.000+00:00","is_active":True,"last_expired":"2000-01-23T04:56:07.000+00:00","max_active_runs":0,"file_token":"file_token","max_active_tasks":6,"pickle_id":"pickle_id","tags":[{"name":"name"},{"name":"name"}],"timetable_description":"timetable_description","is_paused":True,"schedule_interval":{"seconds":5,"__type":"__type","days":1,"microseconds":5},"is_subdag":True,"next_dagrun":"2000-01-23T04:56:07.000+00:00"}
    params = [('update_mask', ['update_mask_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/dags/{dag_id}'.format(dag_id='dag_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_dags(client):
    """Test case for patch_dags

    Update DAGs
    """
    body = {"description":"description","owners":["owners","owners"],"fileloc":"fileloc","has_task_concurrency_limits":True,"root_dag_id":"root_dag_id","has_import_errors":True,"last_pickled":"2000-01-23T04:56:07.000+00:00","last_parsed_time":"2000-01-23T04:56:07.000+00:00","next_dagrun_create_after":"2000-01-23T04:56:07.000+00:00","dag_id":"dag_id","scheduler_lock":True,"default_view":"default_view","next_dagrun_data_interval_end":"2000-01-23T04:56:07.000+00:00","next_dagrun_data_interval_start":"2000-01-23T04:56:07.000+00:00","is_active":True,"last_expired":"2000-01-23T04:56:07.000+00:00","max_active_runs":0,"file_token":"file_token","max_active_tasks":6,"pickle_id":"pickle_id","tags":[{"name":"name"},{"name":"name"}],"timetable_description":"timetable_description","is_paused":True,"schedule_interval":{"seconds":5,"__type":"__type","days":1,"microseconds":5},"is_subdag":True,"next_dagrun":"2000-01-23T04:56:07.000+00:00"}
    params = [('limit', 100),
                    ('offset', 56),
                    ('tags', ['tags_example']),
                    ('update_mask', ['update_mask_example']),
                    ('only_active', True),
                    ('dag_id_pattern', 'dag_id_pattern_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/dags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_clear_task_instances(client):
    """Test case for post_clear_task_instances

    Clear a set of task instances
    """
    body = {"end_date":"end_date","include_future":False,"include_past":False,"reset_dag_runs":True,"include_parentdag":True,"include_subdags":True,"task_ids":["task_ids","task_ids"],"include_downstream":False,"only_running":False,"dag_run_id":"dag_run_id","include_upstream":False,"dry_run":True,"only_failed":True,"start_date":"start_date"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/dags/{dag_id}/clearTaskInstances'.format(dag_id='dag_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_set_task_instances_state(client):
    """Test case for post_set_task_instances_state

    Set a state of task instances
    """
    body = {"include_future":True,"include_past":True,"execution_date":"execution_date","dag_run_id":"dag_run_id","include_upstream":True,"new_state":"success","dry_run":True,"task_id":"task_id","include_downstream":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/dags/{dag_id}/updateTaskInstancesState'.format(dag_id='dag_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

