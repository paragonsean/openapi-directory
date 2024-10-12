# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_order_status_api_model import ChangeOrderStatusApiModel
from openapi_server.models.list_result_order_details_api_model import ListResultOrderDetailsApiModel
from openapi_server.models.order_create_api_model import OrderCreateApiModel
from openapi_server.models.order_delete_api_model import OrderDeleteApiModel
from openapi_server.models.order_full_details_api_model import OrderFullDetailsApiModel
from openapi_server.models.order_shipping_details_api_model import OrderShippingDetailsApiModel


pytestmark = pytest.mark.asyncio

async def test_order_api_all(client):
    """Test case for order_api_all

    Return all orders for the account
    """
    params = [('queryOptions.page', 56),
                    ('queryOptions.pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/order/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_change_shipping_details(client):
    """Test case for order_api_change_shipping_details

    Change order shipping details
    """
    body = {"CountryId":2,"Email":"Email","Address":"Address","PhoneNumber":"PhoneNumber","Name":"Name"}
    params = [('orderId', 56)]
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/order/changeshippingdetails',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_change_status(client):
    """Test case for order_api_change_status

    Change order status
    """
    body = {"Status":"PendingPayment","Id":0,"Reason":"Reason"}
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/order/changestatus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_delete(client):
    """Test case for order_api_delete

    Delete an existing order
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/order/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_details(client):
    """Test case for order_api_details

    Return order details
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/order/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_order_api_new(client):
    """Test case for order_api_new

    Create an order
    """
    body = {"Status":"PendingPayment","Description":"Description","OrderBillingDetails":{"CountryId":5,"Email":"Email","Address":"Address","PhoneNumber":"PhoneNumber","Name":"Name"},"ShippingAmount":5.962133916683182,"ProductId":1,"TotalAmount":7.061401241503109,"Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":0,"DiscountAmount":6.027456183070403,"Name":"Name","TaxAmount":2.3021358869347655,"CouponCode":"CouponCode","ShippingDescription":"ShippingDescription","Referral":"Referral","AfterPaymentDescription":"AfterPaymentDescription","Note":"Note","WhatHappensNextDescription":"WhatHappensNextDescription","Items":[{"WorkTypeId":1,"TaxAmount":3.616076749251911,"Description":"Description","ProductItemId":2,"ReferenceId":"ReferenceId","TaxPercentage":4.145608029883936,"Quantity":7.061401241503109,"TaxId":2,"TotalAmount":7.386281948385884,"Cost":5.637376656633329,"SubTotalAmount":9.301444243932576},{"WorkTypeId":1,"TaxAmount":3.616076749251911,"Description":"Description","ProductItemId":2,"ReferenceId":"ReferenceId","TaxPercentage":4.145608029883936,"Quantity":7.061401241503109,"TaxId":2,"TotalAmount":7.386281948385884,"Cost":5.637376656633329,"SubTotalAmount":9.301444243932576}],"SubTotalAmount":5.637376656633329,"OrderShippingDetails":{"CountryId":2,"Email":"Email","Address":"Address","PhoneNumber":"PhoneNumber","Name":"Name"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/order/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

