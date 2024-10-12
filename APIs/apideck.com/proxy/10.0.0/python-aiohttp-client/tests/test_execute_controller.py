# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_proxy401_response import GetProxy401Response
from openapi_server.models.post_proxy_request import PostProxyRequest
from openapi_server.models.put_proxy_request import PutProxyRequest


pytestmark = pytest.mark.asyncio

async def test_delete_proxy(client):
    """Test case for delete_proxy

    DELETE
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'close',
        'x_apideck_downstream_url': 'https://api.close.com/api/v1/lead',
        'x_apideck_downstream_authorization': 'Bearer XXXXXXXXXXXXXXXXX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/proxy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_proxy(client):
    """Test case for get_proxy

    GET
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'close',
        'x_apideck_downstream_url': 'https://api.close.com/api/v1/lead',
        'x_apideck_downstream_authorization': 'Bearer XXXXXXXXXXXXXXXXX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/proxy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_options_proxy(client):
    """Test case for options_proxy

    OPTIONS
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'close',
        'x_apideck_downstream_url': 'https://api.close.com/api/v1/lead',
        'x_apideck_downstream_authorization': 'Bearer XXXXXXXXXXXXXXXXX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='OPTIONS',
        path='/proxy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_proxy(client):
    """Test case for patch_proxy

    PATCH
    """
    body = openapi_server.PostProxyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'close',
        'x_apideck_downstream_url': 'https://api.close.com/api/v1/lead',
        'x_apideck_downstream_authorization': 'Bearer XXXXXXXXXXXXXXXXX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/proxy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_proxy(client):
    """Test case for post_proxy

    POST
    """
    body = openapi_server.PostProxyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'close',
        'x_apideck_downstream_url': 'https://api.close.com/api/v1/lead',
        'x_apideck_downstream_authorization': 'Bearer XXXXXXXXXXXXXXXXX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/proxy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_put_proxy(client):
    """Test case for put_proxy

    PUT
    """
    body = openapi_server.PutProxyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'close',
        'x_apideck_downstream_url': 'https://api.close.com/api/v1/lead',
        'x_apideck_downstream_authorization': 'Bearer XXXXXXXXXXXXXXXXX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/proxy',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

