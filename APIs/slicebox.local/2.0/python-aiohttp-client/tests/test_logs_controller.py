# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.log_entry import LogEntry


pytestmark = pytest.mark.asyncio

async def test_log_delete(client):
    """Test case for log_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/log',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_get(client):
    """Test case for log_get

    
    """
    params = [('startindex', 0),
                    ('count', 20),
                    ('subject', 'subject_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/log',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_id_delete(client):
    """Test case for log_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/log/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

