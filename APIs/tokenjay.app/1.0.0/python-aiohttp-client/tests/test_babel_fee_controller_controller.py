# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.mosaik_app import MosaikApp
from openapi_server.models.notification_check_response import NotificationCheckResponse


pytestmark = pytest.mark.asyncio

async def test_check_for_notifications(client):
    """Test case for check_for_notifications

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/mosaik/babelfee/notificationcheck',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ergo_pay_create_babel_box1(client):
    """Test case for ergo_pay_create_babel_box1

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/cancelbabel/{box_id}'.format(box_id='box_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_babel_fee_overview(client):
    """Test case for get_babel_fee_overview

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/mosaik/babelfee/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

