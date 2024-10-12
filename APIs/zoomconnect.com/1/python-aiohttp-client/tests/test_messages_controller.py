# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.web_service_analyse_message_request_message_and_recipient_number import WebServiceAnalyseMessageRequestMessageAndRecipientNumber
from openapi_server.models.web_service_analyse_message_request_message_only import WebServiceAnalyseMessageRequestMessageOnly
from openapi_server.models.web_service_analyse_message_response import WebServiceAnalyseMessageResponse
from openapi_server.models.web_service_message import WebServiceMessage
from openapi_server.models.web_service_messages import WebServiceMessages


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyse(client):
    """Test case for analyse

    analyse-
    """
    body = {"message":"message","recipientNumber":"recipientNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/messages/analyse/message-length-within-max-allowed',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyse_full(client):
    """Test case for analyse_full

    analyse-full
    """
    body = {"message":"message","recipientNumber":"recipientNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/messages/analyse/full',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyse_message_credit_cost(client):
    """Test case for analyse_message_credit_cost

    analyse-message-credit-cost
    """
    body = {"message":"message","recipientNumber":"recipientNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/messages/analyse/message-credit-cost',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyse_message_encoding(client):
    """Test case for analyse_message_encoding

    analyse-message-encoding
    """
    body = {"message":"message","recipientNumber":"recipientNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/messages/analyse/message-encoding',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyse_message_length(client):
    """Test case for analyse_message_length

    analyse-message-length
    """
    body = {"message":"message","recipientNumber":"recipientNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/messages/analyse/message-length',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_analyse_number_of_messages(client):
    """Test case for analyse_number_of_messages

    analyse-number-of-messages
    """
    body = {"message":"message","recipientNumber":"recipientNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/messages/analyse/number-of-messages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_messages_all_get(client):
    """Test case for api_rest_v1_messages_all_get

    all
    """
    params = [('pageSize', 100),
                    ('page', 1),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
                    ('fromDateTimeSent', '2013-10-20T19:20:30+01:00'),
                    ('toDateTimeSent', '2013-10-20T19:20:30+01:00'),
                    ('fromDateTimeReceived', '2013-10-20T19:20:30+01:00'),
                    ('toDateTimeReceived', '2013-10-20T19:20:30+01:00'),
                    ('fromNumber', 'from_number_example'),
                    ('toNumber', 'to_number_example'),
                    ('message', 'message_example'),
                    ('campaign', 'campaign_example'),
                    ('dataField', 'data_field_example'),
                    ('deleted', True),
                    ('read', True),
                    ('repliesToMessageId', 'replies_to_message_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/messages/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_messages_message_id_delete(client):
    """Test case for api_rest_v1_messages_message_id_delete

    delete
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/app/api/rest/v1/messages/{message_id}'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_messages_message_id_get(client):
    """Test case for api_rest_v1_messages_message_id_get

    get
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app/api/rest/v1/messages/{message_id}'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_messages_message_id_mark_read_post(client):
    """Test case for api_rest_v1_messages_message_id_mark_read_post

    markRead
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/messages/{message_id}/markRead'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_messages_message_id_mark_read_put(client):
    """Test case for api_rest_v1_messages_message_id_mark_read_put

    markRead
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/app/api/rest/v1/messages/{message_id}/markRead'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_messages_message_id_mark_unread_post(client):
    """Test case for api_rest_v1_messages_message_id_mark_unread_post

    markUnread
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app/api/rest/v1/messages/{message_id}/markUnread'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rest_v1_messages_message_id_mark_unread_put(client):
    """Test case for api_rest_v1_messages_message_id_mark_unread_put

    markUnread
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/app/api/rest/v1/messages/{message_id}/markUnread'.format(message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

