# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_download_log_json(client):
    """Test case for download_log_json

    
    """
    params = [('minimum-log-level', INFO),
                    ('last-timestamp', 0.0),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/logging/groovLogs.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_log_text(client):
    """Test case for download_log_text

    
    """
    params = [('minimum-log-level', INFO),
                    ('last-timestamp', 0.0),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/logging/groovLogs.txt',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

