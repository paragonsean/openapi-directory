# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.export_order_list_request import ExportOrderListRequest
from openapi_server.models.order_exportations import OrderExportations


pytestmark = pytest.mark.asyncio

async def test_export_orders(client):
    """Test case for export_orders

    Request a new Order report exportation to be generated
    """
    body = openapi_server.ExportOrderListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/exportations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_exportations(client):
    """Test case for get_order_exportations

    Get a paginated list of Order report exportations
    """
    params = [('pageNumber', 1),
                    ('pageSize', 25),
                    ('storeId', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/exportations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

