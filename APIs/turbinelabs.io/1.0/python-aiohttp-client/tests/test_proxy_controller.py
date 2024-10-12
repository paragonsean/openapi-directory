# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.multi_proxy_result import MultiProxyResult
from openapi_server.models.proxy import Proxy
from openapi_server.models.proxy_create import ProxyCreate
from openapi_server.models.proxy_result import ProxyResult


pytestmark = pytest.mark.asyncio

async def test_proxy_get(client):
    """Test case for proxy_get

    list proxies
    """
    params = [('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/proxy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proxy_post(client):
    """Test case for proxy_post

    create proxy
    """
    proxy = {"name":"name","zone_key":"zone_key","domain_keys":["domain_keys","domain_keys"],"listener_keys":["listener_keys","listener_keys"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/proxy',
        headers=headers,
        json=proxy,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proxy_proxy_key_delete(client):
    """Test case for proxy_proxy_key_delete

    delete proxy
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/proxy/{proxy_key}'.format(proxy_key='72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proxy_proxy_key_get(client):
    """Test case for proxy_proxy_key_get

    get proxy
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/proxy/{proxy_key}'.format(proxy_key='72c86057-ee8d-4a2b-a3a7-760fbd1d3b9f'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

