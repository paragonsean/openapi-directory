# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_message_response import CreateMessageResponse
from openapi_server.models.delete_message_response import DeleteMessageResponse
from openapi_server.models.get_message_response import GetMessageResponse
from openapi_server.models.get_messages_response import GetMessagesResponse
from openapi_server.models.message import Message
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_message_response import UpdateMessageResponse


pytestmark = pytest.mark.asyncio

async def test_messages_add(client):
    """Test case for messages_add

    Create Message
    """
    body = {"webhook_url":"https://unify.apideck.com/webhook/webhooks/eyz329dkffdl4949/x/sms","subject":"Picture","created_at":"2020-09-30T07:43:32Z","scheduled_at":"2020-09-30T07:43:32Z","body":"Hi! How are you doing?","error":{"code":"X1","message":"Something went wrong"},"type":"sms","created_by":"12345","custom_mappings":"{}","reference":"CUST001","sent_at":"2020-09-30T07:43:32Z","messaging_service_id":"123456","updated_at":"2020-09-30T07:43:32Z","price":{"currency":"USD","per_unit":"0.01","total_amount":"0.01"},"number_of_media_files":1,"updated_by":"12345","from":"+15017122661","id":"12345","to":"+15017122662","direction":"outbound-api","number_of_units":1,"status":"sent"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/sms/messages',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_all(client):
    """Test case for messages_all

    List Messages
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sms/messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_delete(client):
    """Test case for messages_delete

    Delete Message
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sms/messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_one(client):
    """Test case for messages_one

    Get Message
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sms/messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_update(client):
    """Test case for messages_update

    Update Message
    """
    body = {"webhook_url":"https://unify.apideck.com/webhook/webhooks/eyz329dkffdl4949/x/sms","subject":"Picture","created_at":"2020-09-30T07:43:32Z","scheduled_at":"2020-09-30T07:43:32Z","body":"Hi! How are you doing?","error":{"code":"X1","message":"Something went wrong"},"type":"sms","created_by":"12345","custom_mappings":"{}","reference":"CUST001","sent_at":"2020-09-30T07:43:32Z","messaging_service_id":"123456","updated_at":"2020-09-30T07:43:32Z","price":{"currency":"USD","per_unit":"0.01","total_amount":"0.01"},"number_of_media_files":1,"updated_by":"12345","from":"+15017122661","id":"12345","to":"+15017122662","direction":"outbound-api","number_of_units":1,"status":"sent"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/sms/messages/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

