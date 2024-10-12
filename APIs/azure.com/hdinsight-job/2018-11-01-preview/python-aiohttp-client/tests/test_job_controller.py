# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_state import AppState
from openapi_server.models.job_detail_root_json_object import JobDetailRootJsonObject
from openapi_server.models.job_list_json_object import JobListJsonObject
from openapi_server.models.job_operations_error_response import JobOperationsErrorResponse
from openapi_server.models.job_submission_json_response import JobSubmissionJsonResponse


pytestmark = pytest.mark.asyncio

async def test_job_get(client):
    """Test case for job_get

    
    """
    params = [('user.name', 'user_name_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/templeton/v1/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get_app_state(client):
    """Test case for job_get_app_state

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/v1/cluster/apps/{app_id}/state'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_kill(client):
    """Test case for job_kill

    
    """
    params = [('user.name', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/templeton/v1/jobs/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list(client):
    """Test case for job_list

    
    """
    params = [('user.name', 'user_name_example'),
                    ('showall', 'showall_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/templeton/v1/jobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list_after_job_id(client):
    """Test case for job_list_after_job_id

    
    """
    params = [('user.name', 'user_name_example'),
                    ('jobid', 'jobid_example'),
                    ('numrecords', 56),
                    ('showall', 'showall_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/templeton/v1/jobs?op=LISTAFTERID',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/text not supported by Connexion")
async def test_job_submit_hive_job(client):
    """Test case for job_submit_hive_job

    
    """
    content = None
    params = [('user.name', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/text',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/templeton/v1/hive',
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_job_submit_map_reduce_job(client):
    """Test case for job_submit_map_reduce_job

    
    """
    content = None
    params = [('user.name', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/templeton/v1/mapreduce/jar',
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_job_submit_map_reduce_streaming_job(client):
    """Test case for job_submit_map_reduce_streaming_job

    
    """
    content = None
    params = [('user.name', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/templeton/v1/mapreduce/streaming',
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_job_submit_pig_job(client):
    """Test case for job_submit_pig_job

    
    """
    content = None
    params = [('user.name', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/templeton/v1/pig',
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_job_submit_sqoop_job(client):
    """Test case for job_submit_sqoop_job

    
    """
    content = None
    params = [('user.name', 'user_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/templeton/v1/sqoop',
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

