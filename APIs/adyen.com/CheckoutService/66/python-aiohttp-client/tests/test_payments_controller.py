# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.card_details_request import CardDetailsRequest
from openapi_server.models.card_details_response import CardDetailsResponse
from openapi_server.models.payment_details_request import PaymentDetailsRequest
from openapi_server.models.payment_details_response import PaymentDetailsResponse
from openapi_server.models.payment_methods_request import PaymentMethodsRequest
from openapi_server.models.payment_methods_response import PaymentMethodsResponse
from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_response import PaymentResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_card_details(client):
    """Test case for post_card_details

    Get the list of brands on the card
    """
    body = {"encryptedCardNumber":"encryptedCardNumber","merchantAccount":"merchantAccount","countryCode":"countryCode","supportedBrands":["supportedBrands","supportedBrands"],"cardNumber":"cardNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v66/cardDetails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_methods(client):
    """Test case for post_payment_methods

    Get a list of available payment methods
    """
    body = {"amount":{"currency":"currency","value":0},"merchantAccount":"merchantAccount","countryCode":"countryCode","splitCardFundingSources":False,"channel":"iOS","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"blockedPaymentMethods":["blockedPaymentMethods","blockedPaymentMethods"],"shopperLocale":"shopperLocale","store":"store","allowedPaymentMethods":["allowedPaymentMethods","allowedPaymentMethods"],"order":{"orderData":"orderData","pspReference":"pspReference"},"shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v66/paymentMethods',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments(client):
    """Test case for post_payments

    Start a transaction
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":2,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"sessionValidity":"sessionValidity","splits":[{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"}],"deviceFingerprint":"deviceFingerprint","redirectToIssuerMethod":"redirectToIssuerMethod","channel":"iOS","mcc":"mcc","threeDSAuthenticationOnly":False,"merchantRiskIndicator":{"deliveryTimeframe":"electronicDelivery","reorderItems":True,"preOrderPurchase":True,"preOrderDate":"2000-01-23T04:56:07.000+00:00","giftCardAmount":{"currency":"currency","value":0},"deliveryEmail":"deliveryEmail","giftCardCount":1,"addressMatch":True,"deliveryAddressIndicator":"shipToBillingAddress"},"lineItems":[{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6},{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6}],"reference":"reference","deliveryAddress":{"country":"country","firstName":"firstName","lastName":"lastName","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"plan":"regular","value":7},"recurringProcessingModel":"CardOnFile","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"order":{"orderData":"orderData","pspReference":"pspReference"},"trustedShopper":True,"enablePayOut":True,"fraudOffset":6,"additionalAmount":{"currency":"currency","value":0},"entityType":"NaturalPerson","shopperEmail":"shopperEmail","enableOneClick":True,"threeDS2RequestData":{"notificationURL":"notificationURL","whiteListStatus":"whiteListStatus","authenticationOnly":False,"sdkMaxTimeout":9,"acquirerBIN":"acquirerBIN","mcc":"mcc","threeDSRequestorID":"threeDSRequestorID","deviceRenderOptions":{"sdkUiType":["multiSelect","multiSelect"],"sdkInterface":"both"},"platform":"iOS","sdkEphemPubKey":{"kty":"kty","crv":"crv","x":"x","y":"y"},"merchantName":"merchantName","transactionType":"goodsOrServicePurchase","threeDSRequestorURL":"threeDSRequestorURL","sdkReferenceNumber":"sdkReferenceNumber","challengeIndicator":"noPreference","threeDSRequestorName":"threeDSRequestorName","acquirerMerchantID":"acquirerMerchantID","sdkAppID":"sdkAppID","messageVersion":"messageVersion","threeDSCompInd":"threeDSCompInd","sdkTransID":"sdkTransID"},"orderReference":"orderReference","paymentMethod":{"bankAccountType":"balance","ownerName":"ownerName","storedPaymentMethodId":"storedPaymentMethodId","encryptedBankAccountNumber":"encryptedBankAccountNumber","recurringDetailReference":"recurringDetailReference","bankAccountNumber":"bankAccountNumber","bankLocationId":"bankLocationId","type":"ach","encryptedBankLocationId":"encryptedBankLocationId"},"shopperLocale":"shopperLocale","captureDelayHours":0,"applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"browserInfo":{"acceptHeader":"acceptHeader","screenWidth":7,"javaEnabled":True,"screenHeight":2,"timeZoneOffset":9,"javaScriptEnabled":True,"language":"language","userAgent":"userAgent","colorDepth":5},"shopperReference":"shopperReference","shopperStatement":"shopperStatement","mandate":{"amount":"amount","amountRule":"max","billingDay":"billingDay","startsAt":"startsAt","billingAttemptsRule":True,"endsAt":"endsAt","remarks":"remarks","frequency":"adhoc"},"recurringFrequency":"recurringFrequency","telephoneNumber":"telephoneNumber","socialSecurityNumber":"socialSecurityNumber","origin":"origin","shopperIP":"shopperIP","fundOrigin":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"telephoneNumber":"telephoneNumber","walletIdentifier":"walletIdentifier","shopperEmail":"shopperEmail","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"}},"recurringExpiry":"recurringExpiry","shopperName":{"firstName":"firstName","lastName":"lastName"},"countryCode":"countryCode","shopperInteraction":"Ecommerce","company":{"registrationNumber":"registrationNumber","registryLocation":"registryLocation","taxId":"taxId","name":"name","type":"type","homepage":"homepage"},"deliveryDate":"2000-01-23T04:56:07.000+00:00","returnUrl":"returnUrl","conversionId":"conversionId","accountInfo":{"passwordChangeDate":"2000-01-23T04:56:07.000+00:00","paymentAccountIndicator":"notApplicable","suspiciousActivity":True,"deliveryAddressUsageIndicator":"thisTransaction","pastTransactionsYear":1,"accountType":"notApplicable","homePhone":"homePhone","paymentAccountAge":"2000-01-23T04:56:07.000+00:00","accountAgeIndicator":"notApplicable","deliveryAddressUsageDate":"2000-01-23T04:56:07.000+00:00","accountChangeDate":"2000-01-23T04:56:07.000+00:00","accountCreationDate":"2000-01-23T04:56:07.000+00:00","mobilePhone":"mobilePhone","pastTransactionsDay":6,"accountChangeIndicator":"thisTransaction","passwordChangeIndicator":"notApplicable","addCardAttemptsDay":0,"workPhone":"workPhone","purchasesLast6Months":5},"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"redirectFromIssuerMethod":"redirectFromIssuerMethod","dateOfBirth":"2000-01-23T04:56:07.000+00:00","store":"store","riskData":{"fraudOffset":4,"customFields":{"key":"customFields"},"profileReference":"profileReference","clientData":"clientData"},"storePaymentMethod":True,"merchantAccount":"merchantAccount","fundRecipient":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"subMerchant":{"country":"country","city":"city","taxId":"taxId","name":"name","mcc":"mcc"},"telephoneNumber":"telephoneNumber","storedPaymentMethodId":"storedPaymentMethodId","walletIdentifier":"walletIdentifier","paymentMethod":{"holderName":"holderName","cupsecureplus.smscode":"cupsecureplus.smscode","expiryMonth":"expiryMonth","threeDS2SdkVersion":"threeDS2SdkVersion","networkPaymentReference":"networkPaymentReference","expiryYear":"expiryYear","type":"scheme","shopperNotificationReference":"shopperNotificationReference","cvc":"cvc","number":"number","encryptedCardNumber":"encryptedCardNumber","encryptedSecurityCode":"encryptedSecurityCode","encryptedExpiryYear":"encryptedExpiryYear","storedPaymentMethodId":"storedPaymentMethodId","recurringDetailReference":"recurringDetailReference","encryptedExpiryMonth":"encryptedExpiryMonth","fundingSource":"credit","brand":"brand"},"shopperEmail":"shopperEmail","walletOwnerTaxId":"walletOwnerTaxId","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperReference":"shopperReference"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"enableRecurring":True,"mpiData":{"cavv":"cavv","authenticationResponse":"Y","xid":"xid","cavvAlgorithm":"cavvAlgorithm","dsTransID":"dsTransID","directoryResponse":"A","eci":"eci","threeDSVersion":"threeDSVersion"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v66/payments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments_details(client):
    """Test case for post_payments_details

    Submit details for a payment
    """
    body = {"paymentData":"paymentData","details":{"cupsecureplus.smscode":"cupsecureplus.smscode","orderID":"orderID","payerID":"payerID","resultCode":"resultCode","threeDSResult":"threeDSResult","oneTimePasscode":"oneTimePasscode","threeds2.challengeResult":"threeds2.challengeResult","redirectResult":"redirectResult","threeds2.fingerprint":"threeds2.fingerprint","authorization_token":"authorization_token","payload":"payload","billingToken":"billingToken","paymentID":"paymentID","MD":"MD","PaReq":"PaReq","PaRes":"PaRes","paymentStatus":"paymentStatus","facilitatorAccessToken":"facilitatorAccessToken"},"threeDSAuthenticationOnly":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v66/payments/details',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

