# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_order_operation_response import BatchOrderOperationResponse
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.change_order_list_request import ChangeOrderListRequest
from openapi_server.models.clear_merchant_order_info_list_request import ClearMerchantOrderInfoListRequest
from openapi_server.models.set_merchant_order_info_list_request import SetMerchantOrderInfoListRequest


pytestmark = pytest.mark.asyncio

async def test_change_order_list(client):
    """Test case for change_order_list

    [DEPRECATED] Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)
    """
    body = openapi_server.ChangeOrderListRequest()
    params = [('userName', 'user_name_example'),
                    ('testMode', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/batches/changeOrders/{change_order_type}'.format(change_order_type='change_order_type_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clear_merchant_order_info_list(client):
    """Test case for clear_merchant_order_info_list

    [DEPRECATED] Send a batch of operations to clear an Order's merchant information (max 100 items per call)
    """
    body = openapi_server.ClearMerchantOrderInfoListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/batches/clearMerchantOrderInfos',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_merchant_order_info_list(client):
    """Test case for set_merchant_order_info_list

    [DEPRECATED] Send a batch of operations to set an Order's merchant information  (max 100 items per call)
    """
    body = openapi_server.SetMerchantOrderInfoListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/batches/setMerchantOrderInfos',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

