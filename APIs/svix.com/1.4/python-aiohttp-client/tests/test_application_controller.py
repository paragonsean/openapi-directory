# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_in import ApplicationIn
from openapi_server.models.application_out import ApplicationOut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_application_out import ListResponseApplicationOut
from openapi_server.models.ordering import Ordering


pytestmark = pytest.mark.asyncio

async def test_create_application_api_v1_app_post(client):
    """Test case for create_application_api_v1_app_post

    Create Application
    """
    body = {"uid":"unique-app-identifier","metadata":{"key":"metadata"},"rateLimit":1000,"name":"My first application"}
    params = [('get_if_exists', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_application_api_v1_app_app_id_delete(client):
    """Test case for delete_application_api_v1_app_app_id_delete

    Delete Application
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/app/{app_id}'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_api_v1_app_app_id_get(client):
    """Test case for get_application_api_v1_app_app_id_get

    Get Application
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_applications_api_v1_app_get(client):
    """Test case for list_applications_api_v1_app_get

    List Applications
    """
    params = [('iterator', 'app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('order', openapi_server.Ordering())]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_application_api_v1_app_app_id_put(client):
    """Test case for update_application_api_v1_app_app_id_put

    Update Application
    """
    body = {"uid":"unique-app-identifier","metadata":{"key":"metadata"},"rateLimit":1000,"name":"My first application"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/app/{app_id}'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

