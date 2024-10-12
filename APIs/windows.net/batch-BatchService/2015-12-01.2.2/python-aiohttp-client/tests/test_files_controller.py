# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.node_file_list_result import NodeFileListResult


pytestmark = pytest.mark.asyncio

async def test_file_delete_from_compute_node(client):
    """Test case for file_delete_from_compute_node

    
    """
    params = [('recursive', True),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='DELETE',
        path='/pools/{pool_id}/nodes/{node_id}/files/{file_name}'.format(pool_id='pool_id_example', node_id='node_id_example', file_name='file_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_delete_from_task(client):
    """Test case for file_delete_from_task

    
    """
    params = [('recursive', True),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='DELETE',
        path='/jobs/{job_id}/tasks/{task_id}/files/{file_name}'.format(job_id='job_id_example', task_id='task_id_example', file_name='file_name_example'),
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
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'ocp_range': 'ocp_range_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='GET',
        path='/pools/{pool_id}/nodes/{node_id}/files/{file_name}'.format(pool_id='pool_id_example', node_id='node_id_example', file_name='file_name_example'),
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
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'ocp_range': 'ocp_range_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{job_id}/tasks/{task_id}/files/{file_name}'.format(job_id='job_id_example', task_id='task_id_example', file_name='file_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_get_node_file_properties_from_compute_node(client):
    """Test case for file_get_node_file_properties_from_compute_node

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='HEAD',
        path='/pools/{pool_id}/nodes/{node_id}/files/{file_name}'.format(pool_id='pool_id_example', node_id='node_id_example', file_name='file_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_get_node_file_properties_from_task(client):
    """Test case for file_get_node_file_properties_from_task

    
    """
    params = [('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
        'if_modified_since': 'if_modified_since_example',
        'if_unmodified_since': 'if_unmodified_since_example',
    }
    response = await client.request(
        method='HEAD',
        path='/jobs/{job_id}/tasks/{task_id}/files/{file_name}'.format(job_id='job_id_example', task_id='task_id_example', file_name='file_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_list_from_compute_node(client):
    """Test case for file_list_from_compute_node

    
    """
    params = [('$filter', 'filter_example'),
                    ('recursive', True),
                    ('maxresults', 56),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
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

    
    """
    params = [('$filter', 'filter_example'),
                    ('recursive', True),
                    ('maxresults', 56),
                    ('timeout', 30),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'return_client_request_id': True,
        'ocp_date': 'ocp_date_example',
    }
    response = await client.request(
        method='GET',
        path='/jobs/{job_id}/tasks/{task_id}/files'.format(job_id='job_id_example', task_id='task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

