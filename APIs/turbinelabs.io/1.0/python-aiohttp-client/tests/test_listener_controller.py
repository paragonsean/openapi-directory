# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.listener import Listener
from openapi_server.models.listener_create import ListenerCreate
from openapi_server.models.listener_result import ListenerResult
from openapi_server.models.multi_listener_result import MultiListenerResult


pytestmark = pytest.mark.asyncio

async def test_listener_get(client):
    """Test case for listener_get

    list listeners
    """
    params = [('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/listener',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listener_listener_key_delete(client):
    """Test case for listener_listener_key_delete

    delete listener
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/listener/{listener_key}'.format(listener_key='72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listener_listener_key_get(client):
    """Test case for listener_listener_key_get

    get listener
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/listener/{listener_key}'.format(listener_key='72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listener_listener_key_put(client):
    """Test case for listener_listener_key_put

    modify listener
    """
    listener = {"protocol":"http","listener_key":"listener_key","port":0,"ip":"ip","tracing_config":{"ingress":True,"request_headers_for_tags":["request_headers_for_tags","request_headers_for_tags"]},"name":"name","zone_key":"zone_key","checksum":"checksum","domain_keys":["domain_keys","domain_keys"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.0/listener/{listener_key}'.format(listener_key='5074fe62-821e-4034-55bd-b9caa09af2a1'),
        headers=headers,
        json=listener,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listener_post(client):
    """Test case for listener_post

    create listener
    """
    listener = {"protocol":"http","port":0,"ip":"ip","tracing_config":{"ingress":True,"request_headers_for_tags":["request_headers_for_tags","request_headers_for_tags"]},"name":"name","zone_key":"zone_key","domain_keys":["domain_keys","domain_keys"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/listener',
        headers=headers,
        json=listener,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

