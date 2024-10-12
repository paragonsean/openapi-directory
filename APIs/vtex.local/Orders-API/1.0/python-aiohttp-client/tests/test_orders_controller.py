# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_log_request import AddLogRequest
from openapi_server.models.cancel_order200_response import CancelOrder200Response
from openapi_server.models.cancel_order_request import CancelOrderRequest
from openapi_server.models.get_order200_response import GetOrder200Response
from openapi_server.models.list_orders import ListOrders
from openapi_server.models.register_change import RegisterChange
from openapi_server.models.register_change_request import RegisterChangeRequest
from openapi_server.models.start_handling401_response import StartHandling401Response
from openapi_server.models.start_handling409_response import StartHandling409Response


pytestmark = pytest.mark.asyncio

async def test_add_log(client):
    """Test case for add_log

    Add log in orders
    """
    body = {"message":"Teste add interactions","source":"Postman"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/oms/pvt/orders/{order_id}/interactions'.format(order_id='1172452900788-01'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_order(client):
    """Test case for cancel_order

    Cancel order
    """
    body = openapi_server.CancelOrderRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/oms/pvt/orders/{order_id}/cancel'.format(order_id='1172452900788-01'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order(client):
    """Test case for get_order

    Get order
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/pvt/orders/{order_id}'.format(order_id='1172452900788-01 or seq501456'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_orders(client):
    """Test case for list_orders

    List orders
    """
    params = [('orderBy', 'v502556llux-01,asc'),
                    ('page', 10),
                    ('per_page', 15),
                    ('f_creationDate', 'creationDate:[2016-01-01T02:00:00.000Z TO 2021-01-01T01:59:59.999Z]'),
                    ('f_hasInputInvoice', False),
                    ('q', '''- OrderID: v212333lux-02 
- Client email: taylor@email.com 
- Client document: 21133355524 
- Client name: Taylor'''),
                    ('utc', -2000),
                    ('f_shippingEstimate', '0.days'),
                    ('f_invoicedDate', 'invoicedDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]'),
                    ('f_authorizedDate', 'creationDate:[2022-01-01T02:00:00.000Z TO 2022-01-02T01:59:59.999Z]'),
                    ('f_UtmSource', 'christmas_campaign'),
                    ('f_sellerNames', 'SellerName'),
                    ('f_callCenterOperatorName', 'Operator%20Name'),
                    ('f_salesChannel', 'Main'),
                    ('salesChannelId', '1'),
                    ('f_affiliateId', 'WLM'),
                    ('f_status', 'ready-for-handling'),
                    ('incompleteOrders', True),
                    ('f_paymentNames', 'Visa'),
                    ('f_RnB', 'Free+Shipping'),
                    ('searchField', '''
- SKU ID: `25` 
- Gift List ID: `11223` 
- Transaction ID (TID): `54546300238810034995829230012` 
- PCI Connector's Transaction ID (TID): `7032909234899834298423209` 
- Payment ID (PID): `2` 
- Connector's NSU: `2437281`'''),
                    ('f_isInstore', True)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/pvt/orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_change(client):
    """Test case for register_change

    Register change on order
    """
    body = {"discountValue":1000,"incrementValue":0,"itemsAdded":[{"id":"234788","price":200,"quantity":1}],"itemsRemoved":[{"id":"234794","price":600,"quantity":2}],"reason":"Promoção dada por telefone","requestId":"change-request-0123"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/oms/pvt/orders/{order_id}/changes'.format(order_id='1172452900788-01'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_handling(client):
    """Test case for start_handling

    Start handling order
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/oms/pvt/orders/{order_id}/start-handling'.format(order_id='1172452900788-01'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

