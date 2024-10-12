# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.node_file_list_result import NodeFileListResult


pytestmark = pytest.mark.asyncio

async def test_file_delete_from_compute_node(client):
    """Test case for file_delete_from_compute_node

    Deletes the specified file from the compute node.
    """
    params = [('recursive', True),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/pools/{pool_id}/nodes/{node_id}/files/{file_path}'.format(pool_id='pool_id_example', node_id='node_id_example', file_path='file_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_delete_from_task(client):
    """Test case for file_delete_from_task

    Deletes the specified task file from the compute node where the task ran.
    """
    params = [('recursive', True),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/jobs/{job_id}/tasks/{task_id}/files/{file_path}'.format(job_id='job_id_example', task_id='task_id_example', file_path='file_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_get_from_compute_node(client):
    """Test case for file_get_from_compute_node

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'ocp_range': 'ocp_range_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pools/{pool_id}/nodes/{node_id}/files/{file_path}'.format(pool_id='pool_id_example', node_id='node_id_example', file_path='file_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_get_from_task(client):
    """Test case for file_get_from_task

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'ocp_range': 'ocp_range_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{job_id}/tasks/{task_id}/files/{file_path}'.format(job_id='job_id_example', task_id='task_id_example', file_path='file_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_get_properties_from_compute_node(client):
    """Test case for file_get_properties_from_compute_node

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/pools/{pool_id}/nodes/{node_id}/files/{file_path}'.format(pool_id='pool_id_example', node_id='node_id_example', file_path='file_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_get_properties_from_task(client):
    """Test case for file_get_properties_from_task

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/jobs/{job_id}/tasks/{task_id}/files/{file_path}'.format(job_id='job_id_example', task_id='task_id_example', file_path='file_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_list_from_compute_node(client):
    """Test case for file_list_from_compute_node

    Lists all of the files in task directories on the specified compute node.
    """
    params = [('$filter', 'filter_example'),
                    ('recursive', True),
                    ('maxresults', 1000),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pools/{pool_id}/nodes/{node_id}/files'.format(pool_id='pool_id_example', node_id='node_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_list_from_task(client):
    """Test case for file_list_from_task

    Lists the files in a task's directory on its compute node.
    """
    params = [('$filter', 'filter_example'),
                    ('recursive', True),
                    ('maxresults', 1000),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': False,
        'ocp_date': 'ocp_date_example',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{job_id}/tasks/{task_id}/files'.format(job_id='job_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

