# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clearorder_form_messages200_response import ClearorderFormMessages200Response
from openapi_server.models.updateorder_formconfiguration_request import UpdateorderFormconfigurationRequest
from openapi_server.models.waiting_time import WaitingTime


pytestmark = pytest.mark.asyncio

async def test_clearorder_form_messages(client):
    """Test case for clearorder_form_messages

    Clear orderForm messages
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/messages/clear'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_window_to_change_seller(client):
    """Test case for get_window_to_change_seller

    Get window to change seller
    """
    headers = { 
        'Accept': 'text/plain',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pvt/configuration/window-to-change-seller',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getorder_formconfiguration(client):
    """Test case for getorder_formconfiguration

    Get orderForm configuration
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pvt/configuration/orderForm',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_window_to_change_seller(client):
    """Test case for update_window_to_change_seller

    Update window to change seller
    """
    body = {"waitingTime":0}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pvt/configuration/window-to-change-seller',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updateorder_formconfiguration(client):
    """Test case for updateorder_formconfiguration

    Update orderForm configuration
    """
    body = {"allowManualPrice":null,"allowMultipleDeliveries":null,"apps":null,"decimalDigitsPrecision":2,"minimumQuantityAccumulatedForItems":1,"minimumValueAccumulated":null,"paymentConfiguration":{"requiresAuthenticationForPreAuthorizedPaymentOption":False},"taxConfiguration":null}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pvt/configuration/orderForm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

