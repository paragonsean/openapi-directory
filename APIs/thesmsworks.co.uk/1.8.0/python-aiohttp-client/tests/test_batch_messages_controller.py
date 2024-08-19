# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_message import BatchMessage
from openapi_server.models.batch_message_response import BatchMessageResponse
from openapi_server.models.cancelled_message_response import CancelledMessageResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.extended_error_model import ExtendedErrorModel
from openapi_server.models.message import Message
from openapi_server.models.message_response import MessageResponse
from openapi_server.models.scheduled_batch_response import ScheduledBatchResponse


pytestmark = pytest.mark.asyncio

async def test_batch_any_post(client):
    """Test case for batch_any_post

    
    """
    messages = {"schedule":"Sun Sep 03 2020 15:34:23 GMT+0100 (BST)","metadata":[{"key":"myKey1","value":"myValue1"},{"key":"myKey2","value":"myValue2"}],"sender":"YourCompany","destination":"447777777777","responseemail":["my.email@mycompany.co.uk","my.other.email@mycompany.co.uk"],"tag":"SummerSpecial","validity":1440.0,"deliveryreporturl":"http://your.domain.com/delivery/report/path","ttl":10.0,"content":"Your super awesome message"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/batch/any',
        headers=headers,
        json=messages,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_batchid_get(client):
    """Test case for batch_batchid_get

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/batch/{batchid}'.format(batchid='batchid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_schedule_post(client):
    """Test case for batch_schedule_post

    
    """
    sms_message = {"schedule":"Wed Jul 19 2017 20:26:28 GMT+0100 (BST)","sender":"YourCompany","destinations":["447777777777","447777777778","447777777779"],"tag":"SummerSpecial","validity":1440.0,"deliveryreporturl":"http://your.domain.com/delivery/report/path","ttl":10.0,"content":"My super awesome batch message"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/batch/schedule',
        headers=headers,
        json=sms_message,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_send_post(client):
    """Test case for batch_send_post

    
    """
    sms_message = {"schedule":"Wed Jul 19 2017 20:26:28 GMT+0100 (BST)","sender":"YourCompany","destinations":["447777777777","447777777778","447777777779"],"tag":"SummerSpecial","validity":1440.0,"deliveryreporturl":"http://your.domain.com/delivery/report/path","ttl":10.0,"content":"My super awesome batch message"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/batch/send',
        headers=headers,
        json=sms_message,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batches_schedule_batchid_delete(client):
    """Test case for batches_schedule_batchid_delete

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/batches/schedule/{batchid}'.format(batchid='batchid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

