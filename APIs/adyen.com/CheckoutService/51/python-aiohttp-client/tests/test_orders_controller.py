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
        path='/v51/orders',
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
        path='/v51/orders/cancel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_methods_balance(client):
    """Test case for post_payment_methods_balance

    Get the balance of a gift card
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":2,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"splits":[{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"}],"telephoneNumber":"telephoneNumber","deviceFingerprint":"deviceFingerprint","socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","mcc":"mcc","threeDSAuthenticationOnly":False,"merchantRiskIndicator":{"deliveryTimeframe":"electronicDelivery","reorderItems":True,"preOrderPurchase":True,"preOrderDate":"2000-01-23T04:56:07.000+00:00","giftCardAmount":{"currency":"currency","value":0},"deliveryEmail":"deliveryEmail","giftCardCount":1,"addressMatch":True,"deliveryAddressIndicator":"shipToBillingAddress"},"reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"enableRealTimeUpdate":True,"deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"value":7},"recurringProcessingModel":"CardOnFile","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","totalsGroup":"totalsGroup","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"selectedBrand":"selectedBrand","deliveryDate":"2000-01-23T04:56:07.000+00:00","trustedShopper":True,"accountInfo":{"passwordChangeDate":"2000-01-23T04:56:07.000+00:00","paymentAccountIndicator":"notApplicable","suspiciousActivity":True,"deliveryAddressUsageIndicator":"thisTransaction","pastTransactionsYear":1,"accountType":"notApplicable","homePhone":"homePhone","paymentAccountAge":"2000-01-23T04:56:07.000+00:00","accountAgeIndicator":"notApplicable","deliveryAddressUsageDate":"2000-01-23T04:56:07.000+00:00","accountChangeDate":"2000-01-23T04:56:07.000+00:00","accountCreationDate":"2000-01-23T04:56:07.000+00:00","mobilePhone":"mobilePhone","pastTransactionsDay":6,"accountChangeIndicator":"thisTransaction","passwordChangeIndicator":"notApplicable","addCardAttemptsDay":0,"workPhone":"workPhone","purchasesLast6Months":5},"fraudOffset":6,"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"additionalAmount":{"currency":"currency","value":0},"recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","sessionId":"sessionId","store":"store","merchantAccount":"merchantAccount","threeDS2RequestData":{"notificationURL":"notificationURL","whiteListStatus":"whiteListStatus","authenticationOnly":False,"sdkMaxTimeout":1,"sdkEncData":"sdkEncData","acquirerBIN":"acquirerBIN","mcc":"mcc","threeDSRequestorID":"threeDSRequestorID","deviceChannel":"deviceChannel","deviceRenderOptions":{"sdkUiType":["multiSelect","multiSelect"],"sdkInterface":"both"},"platform":"iOS","sdkEphemPubKey":{"kty":"kty","crv":"crv","x":"x","y":"y"},"merchantName":"merchantName","transactionType":"goodsOrServicePurchase","threeDSRequestorURL":"threeDSRequestorURL","sdkReferenceNumber":"sdkReferenceNumber","challengeIndicator":"noPreference","threeDSRequestorName":"threeDSRequestorName","acquirerMerchantID":"acquirerMerchantID","sdkAppID":"sdkAppID","sdkVersion":"sdkVersion","messageVersion":"messageVersion","threeDSCompInd":"threeDSCompInd","sdkTransID":"sdkTransID"},"orderReference":"orderReference","paymentMethod":{"key":"paymentMethod"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperLocale":"shopperLocale","captureDelayHours":0,"applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"browserInfo":{"acceptHeader":"acceptHeader","screenWidth":7,"javaEnabled":True,"screenHeight":2,"timeZoneOffset":9,"javaScriptEnabled":True,"language":"language","userAgent":"userAgent","colorDepth":5},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v51/paymentMethods/balance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

