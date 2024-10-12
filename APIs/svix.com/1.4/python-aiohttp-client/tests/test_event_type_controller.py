# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_type_in import EventTypeIn
from openapi_server.models.event_type_out import EventTypeOut
from openapi_server.models.event_type_update import EventTypeUpdate
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_event_type_out import ListResponseEventTypeOut


pytestmark = pytest.mark.asyncio

async def test_create_event_type_api_v1_event_type_post(client):
    """Test case for create_event_type_api_v1_event_type_post

    Create Event Type
    """
    body = {"archived":False,"featureFlag":"cool-new-feature","schemas":{"1":{"description":"An invoice was paid by a user","properties":{"invoiceId":{"description":"The invoice id","type":"string"},"userId":{"description":"The user id","type":"string"}},"required":["invoiceId","userId"],"title":"Invoice Paid Event","type":"object"}},"name":"user.signup","description":"A user has signed up"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/event-type/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_event_type_api_v1_event_type_event_type_name_delete(client):
    """Test case for delete_event_type_api_v1_event_type_event_type_name_delete

    Archive Event Type
    """
    params = [('expunge', False)]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/event-type/{event_type_name}'.format(event_type_name='user.signup'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_event_type_api_v1_event_type_event_type_name_get(client):
    """Test case for get_event_type_api_v1_event_type_event_type_name_get

    Get Event Type
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/event-type/{event_type_name}'.format(event_type_name='user.signup'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_event_types_api_v1_event_type_get(client):
    """Test case for list_event_types_api_v1_event_type_get

    List Event Types
    """
    params = [('iterator', 'user.signup'),
                    ('limit', 50),
                    ('with_content', False),
                    ('include_archived', False)]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/event-type/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_event_type_api_v1_event_type_event_type_name_put(client):
    """Test case for update_event_type_api_v1_event_type_event_type_name_put

    Update Event Type
    """
    body = {"archived":False,"featureFlag":"cool-new-feature","schemas":{"1":{"description":"An invoice was paid by a user","properties":{"invoiceId":{"description":"The invoice id","type":"string"},"userId":{"description":"The user id","type":"string"}},"required":["invoiceId","userId"],"title":"Invoice Paid Event","type":"object"}},"description":"A user has signed up"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/event-type/{event_type_name}'.format(event_type_name='user.signup'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

