# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.log import Log


pytestmark = pytest.mark.asyncio

async def test_logs_actions(client):
    """Test case for logs_actions

    Actions
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/actions/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_read(client):
    """Test case for logs_read

    Retrieve a log
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/logs/{log_id}'.format(log_id='log_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

