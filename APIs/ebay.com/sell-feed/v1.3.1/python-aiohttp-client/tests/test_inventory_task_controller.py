# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_inventory_task_request import CreateInventoryTaskRequest
from openapi_server.models.inventory_task import InventoryTask
from openapi_server.models.inventory_task_collection import InventoryTaskCollection


pytestmark = pytest.mark.asyncio

async def test_create_inventory_task(client):
    """Test case for create_inventory_task

    
    """
    body = {"filterCriteria":{"listingFormat":"listingFormat"},"schemaVersion":"schemaVersion","feedType":"feedType"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/feed/v1/inventory_task',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_inventory_task(client):
    """Test case for get_inventory_task

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/inventory_task/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_inventory_tasks(client):
    """Test case for get_inventory_tasks

    
    """
    params = [('feed_type', 'feed_type_example'),
                    ('schedule_id', 'schedule_id_example'),
                    ('look_back_days', 'look_back_days_example'),
                    ('date_range', 'date_range_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/feed/v1/inventory_task',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

