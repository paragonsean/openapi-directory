# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.message import Message
from openapi_server.models.submission_entry import SubmissionEntry


pytestmark = pytest.mark.asyncio

async def test_messages_get(client):
    """Test case for messages_get

    Retrieve Messages
    """
    params = [('limit', 3.4),
                    ('filter', 'filter_example'),
                    ('sortOrder', 'sort_order_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_id_get(client):
    """Test case for messages_id_get

    Show Message
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/messages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_id_related_received_messages_get(client):
    """Test case for messages_id_related_received_messages_get

    List Related Messages
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/messages/{id}/relatedReceivedMessages'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_post(client):
    """Test case for messages_post

    Send Messages
    """
    body = {"protocolId":"IMPLICIT","deliveryReports":"ALL","messageClass":"FLASH_SMS","longMessageMaxParts":99,"userSuppliedId":"submission-12765","from":{"address":"1111111","type":"INTERNATIONAL"},"routingGroup":"ECONOMY","to":[{"address":"1111111","fields":["Jack","$200.00"],"type":"INTERNATIONAL"},{"address":"1111111","fields":["Jack","$200.00"],"type":"INTERNATIONAL"}],"body":"Hi there!","encoding":"TEXT"}
    params = [('deduplication-id', 56),
                    ('auto-unicode', False),
                    ('schedule-date', '2013-10-20T19:20:30+01:00'),
                    ('schedule-description', 'schedule_description_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/messages',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_send_get(client):
    """Test case for messages_send_get

    Send message by simple GET or POST
    """
    params = [('to', 'to_example'),
                    ('body', 'body_example'),
                    ('deduplication-id', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/messages/send',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

