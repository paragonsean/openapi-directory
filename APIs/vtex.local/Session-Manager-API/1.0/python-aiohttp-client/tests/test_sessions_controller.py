# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.createnewsession_request import CreatenewsessionRequest
from openapi_server.models.editsession_request import EditsessionRequest


pytestmark = pytest.mark.asyncio

async def test_createnewsession(client):
    """Test case for createnewsession

    Create new session
    """
    body = {"public":{"country":{"value":"BR"},"postalCode":{"value":"12345"}}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/sessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_editsession(client):
    """Test case for editsession

    Edit session
    """
    body = {"public":{"newValue":{"value":"patched"}}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/sessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session(client):
    """Test case for get_session

    Get Session
    """
    params = [('items', 'namespace1.key1,namespace2.key2')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/sessions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

