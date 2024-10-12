# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_order_task_request import CreateOrderTaskRequest
from openapi_server.models.order_task import OrderTask
from openapi_server.models.order_task_collection import OrderTaskCollection


pytestmark = pytest.mark.asyncio

async def test_create_order_task(client):
    """Test case for create_order_task

    
    """
    body = {"filterCriteria":{"creationDateRange":{"from":"from","to":"to"},"orderStatus":"orderStatus","modifiedDateRange":{"from":"from","to":"to"}},"schemaVersion":"schemaVersion","feedType":"feedType"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/feed/v1/order_task',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_task(client):
    """Test case for get_order_task

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/order_task/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_tasks(client):
    """Test case for get_order_tasks

    
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
        path='/sell/feed/v1/order_task',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

