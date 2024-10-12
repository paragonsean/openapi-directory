# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annunciator_message_type import AnnunciatorMessageType
from openapi_server.models.message_view_model import MessageViewModel


pytestmark = pytest.mark.asyncio

async def test_api_message_message_annunciator_current_get(client):
    """Test case for api_message_message_annunciator_current_get

    Return the current message by annunciator type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Message/message/{annunciator}/current'.format(annunciator=openapi_server.AnnunciatorMessageType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_message_message_annunciator_date_get(client):
    """Test case for api_message_message_annunciator_date_get

    Return the most recent message by annunciator after date time specified
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Message/message/{annunciator}/{_date}'.format(annunciator=openapi_server.AnnunciatorMessageType(), _date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

