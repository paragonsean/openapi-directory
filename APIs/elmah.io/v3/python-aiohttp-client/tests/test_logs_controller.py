# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_log import CreateLog
from openapi_server.models.create_log_result import CreateLogResult
from openapi_server.models.log import Log


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_logs_create(client):
    """Test case for logs_create

    Create a new log.
    """
    body = {"color":"color","environmentName":"environmentName","name":"name","disabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/logs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_diagnose(client):
    """Test case for logs_diagnose

    Help diagnose logging problems.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/logs/{id}/_diagnose'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_disable(client):
    """Test case for logs_disable

    Disable a log by its ID.
    """
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/logs/{id}/_disable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_enable(client):
    """Test case for logs_enable

    Enable a log by its ID.
    """
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/logs/{id}/_enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_get(client):
    """Test case for logs_get

    Fetch a log by its ID.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/logs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logs_get_all(client):
    """Test case for logs_get_all

    Fetch a list of logs.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/logs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

