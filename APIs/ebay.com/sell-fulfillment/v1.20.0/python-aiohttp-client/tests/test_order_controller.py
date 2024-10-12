# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issue_refund_request import IssueRefundRequest
from openapi_server.models.order import Order
from openapi_server.models.order_search_paged_collection import OrderSearchPagedCollection
from openapi_server.models.refund import Refund


pytestmark = pytest.mark.asyncio

async def test_get_order(client):
    """Test case for get_order

    
    """
    params = [('fieldGroups', 'field_groups_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/fulfillment/v1/order/{order_id}'.format(order_id='order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_orders(client):
    """Test case for get_orders

    
    """
    params = [('fieldGroups', 'field_groups_example'),
                    ('filter', 'filter_example'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('orderIds', 'order_ids_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/fulfillment/v1/order',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_issue_refund(client):
    """Test case for issue_refund

    Issue Refund
    """
    body = {"reasonForRefund":"reasonForRefund","refundItems":[{"lineItemId":"lineItemId","legacyReference":{"legacyTransactionId":"legacyTransactionId","legacyItemId":"legacyItemId"},"refundAmount":{"currency":"currency","value":"value"}},{"lineItemId":"lineItemId","legacyReference":{"legacyTransactionId":"legacyTransactionId","legacyItemId":"legacyItemId"},"refundAmount":{"currency":"currency","value":"value"}}],"orderLevelRefundAmount":{"currency":"currency","value":"value"},"comment":"comment"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/fulfillment/v1/order/{order_id}/issue_refund'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

