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
        path='/v70/orders',
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
        path='/v70/orders/cancel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_methods_balance(client):
    """Test case for post_payment_methods_balance

    Get the balance of a gift card
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":2,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"splits":[{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"}],"telephoneNumber":"telephoneNumber","deviceFingerprint":"deviceFingerprint","localizedShopperStatement":{"key":"localizedShopperStatement"},"socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","mcc":"mcc","threeDSAuthenticationOnly":False,"merchantRiskIndicator":{"preOrderDate":"2000-01-23T04:56:07.000+00:00","shipIndicator":"shipIndicator","giftCardAmount":{"currency":"currency","value":0},"preOrderPurchaseInd":"preOrderPurchaseInd","deliveryEmail":"deliveryEmail","giftCardCount":1,"addressMatch":True,"deliveryTimeframe":"electronicDelivery","reorderItems":True,"deliveryEmailAddress":"deliveryEmailAddress","preOrderPurchase":True,"giftCardCurr":"giftCardCurr","reorderItemsInd":"reorderItemsInd","deliveryAddressIndicator":"shipToBillingAddress"},"reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"plan":"regular","value":7},"recurringProcessingModel":"CardOnFile","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","totalsGroup":"totalsGroup","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"selectedBrand":"selectedBrand","deliveryDate":"2000-01-23T04:56:07.000+00:00","trustedShopper":True,"accountInfo":{"passwordChangeDate":"2000-01-23T04:56:07.000+00:00","paymentAccountIndicator":"notApplicable","suspiciousActivity":True,"deliveryAddressUsageIndicator":"thisTransaction","pastTransactionsYear":1,"accountType":"notApplicable","homePhone":"homePhone","paymentAccountAge":"2000-01-23T04:56:07.000+00:00","accountAgeIndicator":"notApplicable","deliveryAddressUsageDate":"2000-01-23T04:56:07.000+00:00","accountChangeDate":"2000-01-23T04:56:07.000+00:00","accountCreationDate":"2000-01-23T04:56:07.000+00:00","mobilePhone":"mobilePhone","pastTransactionsDay":6,"accountChangeIndicator":"thisTransaction","passwordChangeIndicator":"notApplicable","addCardAttemptsDay":0,"workPhone":"workPhone","purchasesLast6Months":5},"fraudOffset":6,"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"additionalAmount":{"currency":"currency","value":0},"recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","sessionId":"sessionId","store":"store","merchantAccount":"merchantAccount","threeDS2RequestData":{"notificationURL":"notificationURL","paymentAuthenticationUseCase":"paymentAuthenticationUseCase","recurringFrequency":"recurringFrequency","mcc":"mcc","platform":"iOS","sdkEphemPubKey":{"kty":"kty","crv":"crv","x":"x","y":"y"},"merchantName":"merchantName","recurringExpiry":"recurringExpiry","threeDSRequestorAuthenticationInd":"threeDSRequestorAuthenticationInd","addrMatch":"Y","threeDSRequestorURL":"threeDSRequestorURL","sdkReferenceNumber":"sdkReferenceNumber","threeDSRequestorName":"threeDSRequestorName","acquirerMerchantID":"acquirerMerchantID","sdkAppID":"sdkAppID","messageVersion":"messageVersion","sdkTransID":"sdkTransID","whiteListStatus":"whiteListStatus","authenticationOnly":False,"sdkMaxTimeout":1,"homePhone":{"cc":"cc","subscriber":"subscriber"},"payTokenInd":True,"sdkEncData":"sdkEncData","purchaseInstalData":"purchaseInstalData","acquirerBIN":"acquirerBIN","threeDSRequestorID":"threeDSRequestorID","deviceChannel":"deviceChannel","deviceRenderOptions":{"sdkUiType":["multiSelect","multiSelect"],"sdkInterface":"both"},"transactionType":"goodsOrServicePurchase","acctInfo":{"shipAddressUsageInd":"01","paymentAccAge":"paymentAccAge","paymentAccInd":"01","txnActivityYear":"txnActivityYear","shipNameIndicator":"01","chAccPwChangeInd":"01","provisionAttemptsDay":"provisionAttemptsDay","chAccChange":"chAccChange","chAccChangeInd":"01","chAccString":"chAccString","nbPurchaseAccount":"nbPurchaseAccount","chAccAgeInd":"01","chAccPwChange":"chAccPwChange","shipAddressUsage":"shipAddressUsage","suspiciousAccActivity":"01","txnActivityDay":"txnActivityDay"},"threeDSRequestorChallengeInd":"01","mobilePhone":{"cc":"cc","subscriber":"subscriber"},"threeDSRequestorAuthenticationInfo":{"threeDSReqAuthMethod":"01","threeDSReqAuthData":"threeDSReqAuthData","threeDSReqAuthTimestamp":"threeDSReqAuthTimestamp"},"transType":"01","challengeIndicator":"noPreference","acctType":"01","sdkVersion":"sdkVersion","workPhone":{"cc":"cc","subscriber":"subscriber"},"threeDSCompInd":"threeDSCompInd","threeDSRequestorPriorAuthenticationInfo":{"threeDSReqPriorRef":"threeDSReqPriorRef","threeDSReqPriorAuthData":"threeDSReqPriorAuthData","threeDSReqPriorAuthMethod":"01","threeDSReqPriorAuthTimestamp":"threeDSReqPriorAuthTimestamp"}},"orderReference":"orderReference","paymentMethod":{"key":"paymentMethod"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperLocale":"shopperLocale","captureDelayHours":0,"applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"browserInfo":{"acceptHeader":"acceptHeader","screenWidth":7,"javaEnabled":True,"screenHeight":2,"timeZoneOffset":9,"javaScriptEnabled":True,"language":"language","userAgent":"userAgent","colorDepth":5},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v70/paymentMethods/balance',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

