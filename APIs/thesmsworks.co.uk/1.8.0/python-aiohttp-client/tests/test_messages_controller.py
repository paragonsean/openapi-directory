# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancelled_message_response import CancelledMessageResponse
from openapi_server.models.deleted_message_response import DeletedMessageResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.extended_error_model import ExtendedErrorModel
from openapi_server.models.message import Message
from openapi_server.models.message_response import MessageResponse
from openapi_server.models.query import Query
from openapi_server.models.scheduled_message_response import ScheduledMessageResponse
from openapi_server.models.scheduled_messages_response import ScheduledMessagesResponse
from openapi_server.models.send_message_response import SendMessageResponse


pytestmark = pytest.mark.asyncio

async def test_message_schedule_post(client):
    """Test case for message_schedule_post

    
    """
    sms_message = {"schedule":"Sun Sep 03 2020 15:34:23 GMT+0100 (BST)","metadata":[{"key":"myKey1","value":"myValue1"},{"key":"myKey2","value":"myValue2"}],"sender":"YourCompany","destination":"447777777777","responseemail":["my.email@mycompany.co.uk","my.other.email@mycompany.co.uk"],"tag":"SummerSpecial","validity":1440.0,"deliveryreporturl":"http://your.domain.com/delivery/report/path","ttl":10.0,"content":"Your super awesome message"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/message/schedule',
        headers=headers,
        json=sms_message,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_message_send_post(client):
    """Test case for message_send_post

    
    """
    sms_message = {"schedule":"Sun Sep 03 2020 15:34:23 GMT+0100 (BST)","metadata":[{"key":"myKey1","value":"myValue1"},{"key":"myKey2","value":"myValue2"}],"sender":"YourCompany","destination":"447777777777","responseemail":["my.email@mycompany.co.uk","my.other.email@mycompany.co.uk"],"tag":"SummerSpecial","validity":1440.0,"deliveryreporturl":"http://your.domain.com/delivery/report/path","ttl":10.0,"content":"Your super awesome message"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/message/send',
        headers=headers,
        json=sms_message,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_failed_post(client):
    """Test case for messages_failed_post

    
    """
    query = {"metadata":[{"key":"myKey1","value":"myValue1"},{"key":"myKey2","value":"myValue2"}],"credits":2.0,"sender":"YourCompany","unread":True,"destination":"447777777777","limit":1000.0,"from":"Wed Jul 12 2017 20:26:28 GMT+0100 (BST)","skip":2000.0,"to":"Wed Jul 19 2017 20:26:28 GMT+0100 (BST)","keyword":"SKYWALKER","status":"SENT"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/messages/failed',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_inbox_post(client):
    """Test case for messages_inbox_post

    
    """
    query = {"metadata":[{"key":"myKey1","value":"myValue1"},{"key":"myKey2","value":"myValue2"}],"credits":2.0,"sender":"YourCompany","unread":True,"destination":"447777777777","limit":1000.0,"from":"Wed Jul 12 2017 20:26:28 GMT+0100 (BST)","skip":2000.0,"to":"Wed Jul 19 2017 20:26:28 GMT+0100 (BST)","keyword":"SKYWALKER","status":"SENT"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/messages/inbox',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_messageid_delete(client):
    """Test case for messages_messageid_delete

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/messages/{messageid}'.format(messageid='messageid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_messageid_get(client):
    """Test case for messages_messageid_get

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/messages/{messageid}'.format(messageid='messageid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_post(client):
    """Test case for messages_post

    
    """
    query = {"metadata":[{"key":"myKey1","value":"myValue1"},{"key":"myKey2","value":"myValue2"}],"credits":2.0,"sender":"YourCompany","unread":True,"destination":"447777777777","limit":1000.0,"from":"Wed Jul 12 2017 20:26:28 GMT+0100 (BST)","skip":2000.0,"to":"Wed Jul 19 2017 20:26:28 GMT+0100 (BST)","keyword":"SKYWALKER","status":"SENT"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/messages',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_schedule_get(client):
    """Test case for messages_schedule_get

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/messages/schedule',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_schedule_messageid_delete(client):
    """Test case for messages_schedule_messageid_delete

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/messages/schedule/{messageid}'.format(messageid='messageid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_flash_message(client):
    """Test case for send_flash_message

    
    """
    sms_message = {"schedule":"Sun Sep 03 2020 15:34:23 GMT+0100 (BST)","metadata":[{"key":"myKey1","value":"myValue1"},{"key":"myKey2","value":"myValue2"}],"sender":"YourCompany","destination":"447777777777","responseemail":["my.email@mycompany.co.uk","my.other.email@mycompany.co.uk"],"tag":"SummerSpecial","validity":1440.0,"deliveryreporturl":"http://your.domain.com/delivery/report/path","ttl":10.0,"content":"Your super awesome message"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/message/flash',
        headers=headers,
        json=sms_message,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

