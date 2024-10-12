# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.order import Order
from openapi_server.models.order_history import OrderHistory
from openapi_server.models.set_merchant_order_info_request import SetMerchantOrderInfoRequest


pytestmark = pytest.mark.asyncio

async def test_change_order(client):
    """Test case for change_order

    [DEPRECATED] Change your marketplace Order Information (accept, ship, etc.)
    """
    body = {'key': 'body_example'}
    params = [('userName', 'user_name_example'),
                    ('testMode', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/{marketplace_technical_code}/{account_id}/{beez_up_order_id}/{change_order_type}'.format(marketplace_technical_code='Amazon', account_id=1001, beez_up_order_id='00000000000000000000000000000000000000000000000', change_order_type='change_order_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clear_merchant_order_info(client):
    """Test case for clear_merchant_order_info

    [DEPRECATED] Clear an Order's merchant information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/{marketplace_technical_code}/{account_id}/{beez_up_order_id}/clearMerchantOrderInfo'.format(marketplace_technical_code='Amazon', account_id=1001, beez_up_order_id='00000000000000000000000000000000000000000000000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order(client):
    """Test case for get_order

    [DEPRECATED] DEPRECATED - Get full Order and Order Item(s) properties
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/{marketplace_technical_code}/{account_id}/{beez_up_order_id}'.format(marketplace_technical_code='Amazon', account_id=1001, beez_up_order_id='00000000000000000000000000000000000000000000000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_history(client):
    """Test case for get_order_history

    [DEPRECATED] Get an Order's harvest and change history
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/{marketplace_technical_code}/{account_id}/{beez_up_order_id}/history'.format(marketplace_technical_code='Amazon', account_id=1001, beez_up_order_id='00000000000000000000000000000000000000000000000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_harvest_order(client):
    """Test case for harvest_order

    [DEPRECATED] Send harvest request for a single Order
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/{marketplace_technical_code}/{account_id}/{beez_up_order_id}/harvest'.format(marketplace_technical_code='Amazon', account_id=1001, beez_up_order_id='00000000000000000000000000000000000000000000000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_head_order(client):
    """Test case for head_order

    [DEPRECATED] DEPRECATED - Get the meta information about the order (ETag, Last-Modified)
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='HEAD',
        path='/v2/user/marketplaces/orders/{marketplace_technical_code}/{account_id}/{beez_up_order_id}'.format(marketplace_technical_code='Amazon', account_id=1001, beez_up_order_id='00000000000000000000000000000000000000000000000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_merchant_order_info(client):
    """Test case for set_merchant_order_info

    [DEPRECATED] Set an Order's merchant information
    """
    body = openapi_server.SetMerchantOrderInfoRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/{marketplace_technical_code}/{account_id}/{beez_up_order_id}/setMerchantOrderInfo'.format(marketplace_technical_code='Amazon', account_id=1001, beez_up_order_id='00000000000000000000000000000000000000000000000'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

