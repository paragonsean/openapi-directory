# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.log import Log


pytestmark = pytest.mark.asyncio

async def test_delete_log_by_id(client):
    """Test case for delete_log_by_id

    Delete a specific log
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/logs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_export_logs(client):
    """Test case for get_export_logs

    Get a CSV or PDF file contain the list of logs
    """
    params = [('format', 'format_example'),
                    ('site', 56),
                    ('filter_type', 'filter_type_example'),
                    ('search', 'search_example'),
                    ('startdate', 'startdate_example'),
                    ('enddate', 'enddate_example'),
                    ('limit', 56),
                    ('startid', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/logs/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fields_logs(client):
    """Test case for get_fields_logs

    Get the list of fields
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/logs/metadata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_types_logs(client):
    """Test case for get_types_logs

    Get the list of log types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/logs/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_get(client):
    """Test case for logs_get

    Get a list of logs
    """
    params = [('log_type', 'log_type_example'),
                    ('log_entry', 'log_entry_example'),
                    ('from', '_from_example'),
                    ('to', 'to_example'),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/logs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

