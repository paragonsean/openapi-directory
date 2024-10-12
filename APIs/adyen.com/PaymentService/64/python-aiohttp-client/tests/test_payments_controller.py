# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authentication_result_request import AuthenticationResultRequest
from openapi_server.models.authentication_result_response import AuthenticationResultResponse
from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_request3d import PaymentRequest3d
from openapi_server.models.payment_request3ds2 import PaymentRequest3ds2
from openapi_server.models.payment_result import PaymentResult
from openapi_server.models.service_error import ServiceError
from openapi_server.models.three_ds2_result_request import ThreeDS2ResultRequest
from openapi_server.models.three_ds2_result_response import ThreeDS2ResultResponse


pytestmark = pytest.mark.asyncio

async def test_post_authorise(client):
    """Test case for post_authorise

    Create an authorisation
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":2,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"splits":[{"reference":"reference","amount":{"currency":"currency","value":6},"description":"description","type":"BalanceAccount","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":6},"description":"description","type":"BalanceAccount","account":"account"}],"deviceFingerprint":"deviceFingerprint","mcc":"mcc","threeDSAuthenticationOnly":False,"merchantRiskIndicator":{"deliveryTimeframe":"electronicDelivery","reorderItems":True,"preOrderPurchase":True,"preOrderDate":"2000-01-23T04:56:07.000+00:00","giftCardAmount":{"currency":"currency","value":0},"deliveryEmail":"deliveryEmail","giftCardCount":1,"addressMatch":True,"deliveryAddressIndicator":"shipToBillingAddress"},"reference":"reference","deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"plan":"regular","value":7},"recurringProcessingModel":"CardOnFile","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"selectedBrand":"selectedBrand","trustedShopper":True,"bankAccount":{"ownerName":"ownerName","countryCode":"countryCode","taxId":"taxId","iban":"iban","bankAccountNumber":"bankAccountNumber","bankName":"bankName","bankLocationId":"bankLocationId","bic":"bic","bankCity":"bankCity"},"fraudOffset":4,"fundDestination":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"subMerchant":{"country":"country","city":"city","taxId":"taxId","name":"name","mcc":"mcc"},"telephoneNumber":"telephoneNumber","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperEmail":"shopperEmail","additionalData":{"key":"additionalData"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"},"shopperReference":"shopperReference"},"additionalAmount":{"currency":"currency","value":0},"entityType":"NaturalPerson","recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"shopperEmail":"shopperEmail","nationality":"nationality","threeDS2RequestData":{"notificationURL":"notificationURL","whiteListStatus":"whiteListStatus","authenticationOnly":False,"sdkMaxTimeout":1,"sdkEncData":"sdkEncData","acquirerBIN":"acquirerBIN","mcc":"mcc","threeDSRequestorID":"threeDSRequestorID","deviceChannel":"deviceChannel","deviceRenderOptions":{"sdkUiType":["multiSelect","multiSelect"],"sdkInterface":"both"},"sdkEphemPubKey":{"kty":"kty","crv":"crv","x":"x","y":"y"},"merchantName":"merchantName","transactionType":"goodsOrServicePurchase","threeDSRequestorURL":"threeDSRequestorURL","sdkReferenceNumber":"sdkReferenceNumber","challengeIndicator":"noPreference","threeDSRequestorName":"threeDSRequestorName","acquirerMerchantID":"acquirerMerchantID","sdkAppID":"sdkAppID","sdkVersion":"sdkVersion","messageVersion":"messageVersion","threeDSCompInd":"threeDSCompInd","sdkTransID":"sdkTransID"},"orderReference":"orderReference","shopperLocale":"shopperLocale","captureDelayHours":3,"fundingSource":"credit","applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"browserInfo":{"acceptHeader":"acceptHeader","screenWidth":7,"javaEnabled":True,"screenHeight":2,"timeZoneOffset":9,"javaScriptEnabled":True,"language":"language","userAgent":"userAgent","colorDepth":5},"card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"},"shopperReference":"shopperReference","shopperStatement":"shopperStatement","mandate":{"amount":"amount","amountRule":"max","billingDay":"billingDay","startsAt":"startsAt","billingAttemptsRule":True,"endsAt":"endsAt","remarks":"remarks","frequency":"adhoc"},"telephoneNumber":"telephoneNumber","socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","shopperName":{"firstName":"firstName","lastName":"lastName"},"enableRealTimeUpdate":True,"selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","totalsGroup":"totalsGroup","deliveryDate":"2000-01-23T04:56:07.000+00:00","accountInfo":{"passwordChangeDate":"2000-01-23T04:56:07.000+00:00","paymentAccountIndicator":"notApplicable","suspiciousActivity":True,"deliveryAddressUsageIndicator":"thisTransaction","pastTransactionsYear":1,"accountType":"notApplicable","homePhone":"homePhone","paymentAccountAge":"2000-01-23T04:56:07.000+00:00","accountAgeIndicator":"notApplicable","deliveryAddressUsageDate":"2000-01-23T04:56:07.000+00:00","accountChangeDate":"2000-01-23T04:56:07.000+00:00","accountCreationDate":"2000-01-23T04:56:07.000+00:00","mobilePhone":"mobilePhone","pastTransactionsDay":6,"accountChangeIndicator":"thisTransaction","passwordChangeIndicator":"notApplicable","addCardAttemptsDay":0,"workPhone":"workPhone","purchasesLast6Months":5},"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"dateOfBirth":"2000-01-23","sessionId":"sessionId","store":"store","fundSource":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"telephoneNumber":"telephoneNumber","shopperEmail":"shopperEmail","additionalData":{"key":"additionalData"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"}},"merchantAccount":"merchantAccount","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"mpiData":{"cavv":"cavv","authenticationResponse":"Y","xid":"xid","cavvAlgorithm":"cavvAlgorithm","dsTransID":"dsTransID","directoryResponse":"A","eci":"eci","threeDSVersion":"threeDSVersion"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v64/authorise',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_authorise3d(client):
    """Test case for post_authorise3d

    Complete a 3DS authorisation
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":2,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"splits":[{"reference":"reference","amount":{"currency":"currency","value":6},"description":"description","type":"BalanceAccount","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":6},"description":"description","type":"BalanceAccount","account":"account"}],"telephoneNumber":"telephoneNumber","deviceFingerprint":"deviceFingerprint","socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","mcc":"mcc","threeDSAuthenticationOnly":False,"merchantRiskIndicator":{"deliveryTimeframe":"electronicDelivery","reorderItems":True,"preOrderPurchase":True,"preOrderDate":"2000-01-23T04:56:07.000+00:00","giftCardAmount":{"currency":"currency","value":0},"deliveryEmail":"deliveryEmail","giftCardCount":1,"addressMatch":True,"deliveryAddressIndicator":"shipToBillingAddress"},"reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"enableRealTimeUpdate":True,"deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"plan":"regular","value":7},"md":"md","recurringProcessingModel":"CardOnFile","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","totalsGroup":"totalsGroup","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"selectedBrand":"selectedBrand","deliveryDate":"2000-01-23T04:56:07.000+00:00","trustedShopper":True,"accountInfo":{"passwordChangeDate":"2000-01-23T04:56:07.000+00:00","paymentAccountIndicator":"notApplicable","suspiciousActivity":True,"deliveryAddressUsageIndicator":"thisTransaction","pastTransactionsYear":1,"accountType":"notApplicable","homePhone":"homePhone","paymentAccountAge":"2000-01-23T04:56:07.000+00:00","accountAgeIndicator":"notApplicable","deliveryAddressUsageDate":"2000-01-23T04:56:07.000+00:00","accountChangeDate":"2000-01-23T04:56:07.000+00:00","accountCreationDate":"2000-01-23T04:56:07.000+00:00","mobilePhone":"mobilePhone","pastTransactionsDay":6,"accountChangeIndicator":"thisTransaction","passwordChangeIndicator":"notApplicable","addCardAttemptsDay":0,"workPhone":"workPhone","purchasesLast6Months":5},"fraudOffset":6,"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"additionalAmount":{"currency":"currency","value":0},"recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","sessionId":"sessionId","store":"store","paResponse":"paResponse","merchantAccount":"merchantAccount","threeDS2RequestData":{"notificationURL":"notificationURL","whiteListStatus":"whiteListStatus","authenticationOnly":False,"sdkMaxTimeout":1,"sdkEncData":"sdkEncData","acquirerBIN":"acquirerBIN","mcc":"mcc","threeDSRequestorID":"threeDSRequestorID","deviceChannel":"deviceChannel","deviceRenderOptions":{"sdkUiType":["multiSelect","multiSelect"],"sdkInterface":"both"},"sdkEphemPubKey":{"kty":"kty","crv":"crv","x":"x","y":"y"},"merchantName":"merchantName","transactionType":"goodsOrServicePurchase","threeDSRequestorURL":"threeDSRequestorURL","sdkReferenceNumber":"sdkReferenceNumber","challengeIndicator":"noPreference","threeDSRequestorName":"threeDSRequestorName","acquirerMerchantID":"acquirerMerchantID","sdkAppID":"sdkAppID","sdkVersion":"sdkVersion","messageVersion":"messageVersion","threeDSCompInd":"threeDSCompInd","sdkTransID":"sdkTransID"},"orderReference":"orderReference","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperLocale":"shopperLocale","captureDelayHours":0,"applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"browserInfo":{"acceptHeader":"acceptHeader","screenWidth":7,"javaEnabled":True,"screenHeight":2,"timeZoneOffset":9,"javaScriptEnabled":True,"language":"language","userAgent":"userAgent","colorDepth":5},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v64/authorise3d',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_authorise3ds2(client):
    """Test case for post_authorise3ds2

    Complete a 3DS2 authorisation
    """
    body = {"threeDS2Result":{"whiteListStatus":"whiteListStatus","cavvAlgorithm":"cavvAlgorithm","dsTransID":"dsTransID","transStatusReason":"transStatusReason","eci":"eci","messageVersion":"messageVersion","authenticationValue":"authenticationValue","transStatus":"transStatus","threeDSServerTransID":"threeDSServerTransID","timestamp":"timestamp"},"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":2,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"splits":[{"reference":"reference","amount":{"currency":"currency","value":6},"description":"description","type":"BalanceAccount","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":6},"description":"description","type":"BalanceAccount","account":"account"}],"telephoneNumber":"telephoneNumber","deviceFingerprint":"deviceFingerprint","socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","mcc":"mcc","threeDSAuthenticationOnly":False,"merchantRiskIndicator":{"deliveryTimeframe":"electronicDelivery","reorderItems":True,"preOrderPurchase":True,"preOrderDate":"2000-01-23T04:56:07.000+00:00","giftCardAmount":{"currency":"currency","value":0},"deliveryEmail":"deliveryEmail","giftCardCount":1,"addressMatch":True,"deliveryAddressIndicator":"shipToBillingAddress"},"reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"enableRealTimeUpdate":True,"deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"plan":"regular","value":7},"recurringProcessingModel":"CardOnFile","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","totalsGroup":"totalsGroup","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"selectedBrand":"selectedBrand","deliveryDate":"2000-01-23T04:56:07.000+00:00","trustedShopper":True,"accountInfo":{"passwordChangeDate":"2000-01-23T04:56:07.000+00:00","paymentAccountIndicator":"notApplicable","suspiciousActivity":True,"deliveryAddressUsageIndicator":"thisTransaction","pastTransactionsYear":1,"accountType":"notApplicable","homePhone":"homePhone","paymentAccountAge":"2000-01-23T04:56:07.000+00:00","accountAgeIndicator":"notApplicable","deliveryAddressUsageDate":"2000-01-23T04:56:07.000+00:00","accountChangeDate":"2000-01-23T04:56:07.000+00:00","accountCreationDate":"2000-01-23T04:56:07.000+00:00","mobilePhone":"mobilePhone","pastTransactionsDay":6,"accountChangeIndicator":"thisTransaction","passwordChangeIndicator":"notApplicable","addCardAttemptsDay":0,"workPhone":"workPhone","purchasesLast6Months":5},"fraudOffset":6,"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"threeDS2Token":"threeDS2Token","additionalAmount":{"currency":"currency","value":0},"recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","sessionId":"sessionId","store":"store","merchantAccount":"merchantAccount","threeDS2RequestData":{"notificationURL":"notificationURL","whiteListStatus":"whiteListStatus","authenticationOnly":False,"sdkMaxTimeout":1,"sdkEncData":"sdkEncData","acquirerBIN":"acquirerBIN","mcc":"mcc","threeDSRequestorID":"threeDSRequestorID","deviceChannel":"deviceChannel","deviceRenderOptions":{"sdkUiType":["multiSelect","multiSelect"],"sdkInterface":"both"},"sdkEphemPubKey":{"kty":"kty","crv":"crv","x":"x","y":"y"},"merchantName":"merchantName","transactionType":"goodsOrServicePurchase","threeDSRequestorURL":"threeDSRequestorURL","sdkReferenceNumber":"sdkReferenceNumber","challengeIndicator":"noPreference","threeDSRequestorName":"threeDSRequestorName","acquirerMerchantID":"acquirerMerchantID","sdkAppID":"sdkAppID","sdkVersion":"sdkVersion","messageVersion":"messageVersion","threeDSCompInd":"threeDSCompInd","sdkTransID":"sdkTransID"},"orderReference":"orderReference","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperLocale":"shopperLocale","captureDelayHours":0,"applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"browserInfo":{"acceptHeader":"acceptHeader","screenWidth":7,"javaEnabled":True,"screenHeight":2,"timeZoneOffset":9,"javaScriptEnabled":True,"language":"language","userAgent":"userAgent","colorDepth":5},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v64/authorise3ds2',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_authentication_result(client):
    """Test case for post_get_authentication_result

    Get the 3DS authentication result
    """
    body = {"merchantAccount":"merchantAccount","pspReference":"pspReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v64/getAuthenticationResult',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_retrieve3ds2_result(client):
    """Test case for post_retrieve3ds2_result

    Get the 3DS2 authentication result
    """
    body = {"merchantAccount":"merchantAccount","pspReference":"pspReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v64/retrieve3ds2Result',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

