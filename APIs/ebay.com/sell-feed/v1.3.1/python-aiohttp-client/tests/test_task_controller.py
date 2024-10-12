# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.create_task_request import CreateTaskRequest
from openapi_server.models.task import Task
from openapi_server.models.task_collection import TaskCollection


pytestmark = pytest.mark.asyncio

async def test_create_task(client):
    """Test case for create_task

    
    """
    body = {"schemaVersion":"schemaVersion","feedType":"feedType"}
    headers = { 
        'Content-Type': 'application/json',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/feed/v1/task',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_input_file(client):
    """Test case for get_input_file

    
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/task/{task_id}/download_input_file'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_result_file(client):
    """Test case for get_result_file

    
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/task/{task_id}/download_result_file'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task(client):
    """Test case for get_task

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/task/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks(client):
    """Test case for get_tasks

    
    """
    params = [('date_range', 'date_range_example'),
                    ('feed_type', 'feed_type_example'),
                    ('limit', 'limit_example'),
                    ('look_back_days', 'look_back_days_example'),
                    ('offset', 'offset_example'),
                    ('schedule_id', 'schedule_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/task',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file(client):
    """Test case for upload_file

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('creation_date', 'creation_date_example')
    data.add_field('file_name', 'file_name_example')
    data.add_field('modification_date', 'modification_date_example')
    data.add_field('name', 'name_example')
    data.add_field('parameters', None)
    data.add_field('read_date', 'read_date_example')
    data.add_field('size', 56)
    data.add_field('type', 'type_example')
    response = await client.request(
        method='POST',
        path='/sell/feed/v1/task/{task_id}/upload_file'.format(task_id='task_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

