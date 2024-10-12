# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_check_request import BalanceCheckRequest
from openapi_server.models.balance_check_response import BalanceCheckResponse
from openapi_server.models.cancel_order_request import CancelOrderRequest
from openapi_server.models.cancel_order_response import CancelOrderResponse
from openapi_server.models.create_order_request import CreateOrderRequest
from openapi_server.models.create_order_response import CreateOrderResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_orders(client):
    """Test case for post_orders

    Create an order
    """
    body = {"reference":"reference","amount":{"currency":"currency","value":0},"merchantAccount":"merchantAccount","expiresAt":"expiresAt"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v37/orders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_orders_cancel(client):
    """Test case for post_orders_cancel

    Cancel an order
    """
    body = {"merchantAccount":"merchantAccount","order":{"orderData":"orderData","pspReference":"pspReference"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v37/orders/cancel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_methods_balance(client):
    """Test case for post_payment_methods_balance

    Get the balance of a gift card
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":6,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"splits":[{"reference":"reference","amount":{"currency":"currency","value":2},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":2},"description":"description","type":"AcquiringFees","account":"account"}],"telephoneNumber":"telephoneNumber","deviceFingerprint":"deviceFingerprint","socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","mcc":"mcc","reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"value":5},"recurringProcessingModel":"CardOnFile","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","totalsGroup":"totalsGroup","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"selectedBrand":"selectedBrand","deliveryDate":"2000-01-23T04:56:07.000+00:00","trustedShopper":True,"fraudOffset":6,"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"additionalAmount":{"currency":"currency","value":0},"recurring":{"tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","sessionId":"sessionId","store":"store","merchantAccount":"merchantAccount","orderReference":"orderReference","paymentMethod":{"key":"paymentMethod"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperLocale":"shopperLocale","captureDelayHours":0,"browserInfo":{"acceptHeader":"acceptHeader","userAgent":"userAgent"},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v37/paymentMethods/balance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

