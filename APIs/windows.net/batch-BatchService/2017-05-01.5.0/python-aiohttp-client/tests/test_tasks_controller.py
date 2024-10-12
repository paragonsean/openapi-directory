# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.cloud_task import CloudTask
from openapi_server.models.cloud_task_list_result import CloudTaskListResult
from openapi_server.models.cloud_task_list_subtasks_result import CloudTaskListSubtasksResult
from openapi_server.models.task_add_collection_parameter import TaskAddCollectionParameter
from openapi_server.models.task_add_collection_result import TaskAddCollectionResult
from openapi_server.models.task_add_parameter import TaskAddParameter
from openapi_server.models.task_update_parameter import TaskUpdateParameter


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_task_add(client):
    """Test case for task_add

    Adds a task to the specified job.
    """
    task = openapi_server.TaskAddParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/jobs/{job_id}/tasks'.format(job_id='job_id_example'),
        headers=headers,
        json=task,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_task_add_collection(client):
    """Test case for task_add_collection

    Adds a collection of tasks to the specified job.
    """
    task_collection = openapi_server.TaskAddCollectionParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='POST',
        path='/jobs/{job_id}/addtaskcollection'.format(job_id='job_id_example'),
        headers=headers,
        json=task_collection,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_delete(client):
    """Test case for task_delete

    Deletes a task from the specified job.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='DELETE',
        path='/jobs/{job_id}/tasks/{task_id}'.format(job_id='job_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_get(client):
    """Test case for task_get

    Gets information about the specified task.
    """
    params = [('$select', 'select_example'),
                    ('$expand', 'expand_example'),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{job_id}/tasks/{task_id}'.format(job_id='job_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_list(client):
    """Test case for task_list

    Lists all of the tasks that are associated with the specified job.
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example'),
                    ('maxresults', 1000),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{job_id}/tasks'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_list_subtasks(client):
    """Test case for task_list_subtasks

    Lists all of the subtasks that are associated with the specified multi-instance task.
    """
    params = [('$select', 'select_example'),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{job_id}/tasks/{task_id}/subtasksinfo'.format(job_id='job_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_reactivate(client):
    """Test case for task_reactivate

    Reactivates the specified task.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='POST',
        path='/jobs/{job_id}/tasks/{task_id}/reactivate'.format(job_id='job_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_terminate(client):
    """Test case for task_terminate

    Terminates the specified task.
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='POST',
        path='/jobs/{job_id}/tasks/{task_id}/terminate'.format(job_id='job_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; odata&#x3D;minimalmetadata not supported by Connexion")
async def test_task_update(client):
    """Test case for task_update

    
    """
    task_update_parameter = openapi_server.TaskUpdateParameter()
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json; odata=minimalmetadata',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='PUT',
        path='/jobs/{job_id}/tasks/{task_id}'.format(job_id='job_id_example', task_id='task_id_example'),
        headers=headers,
        json=task_update_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

