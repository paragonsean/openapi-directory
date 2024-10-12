# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.card_details_request import CardDetailsRequest
from openapi_server.models.card_details_response import CardDetailsResponse
from openapi_server.models.create_checkout_session_request import CreateCheckoutSessionRequest
from openapi_server.models.create_checkout_session_response import CreateCheckoutSessionResponse
from openapi_server.models.payment_details_request import PaymentDetailsRequest
from openapi_server.models.payment_details_response import PaymentDetailsResponse
from openapi_server.models.payment_methods_request import PaymentMethodsRequest
from openapi_server.models.payment_methods_response import PaymentMethodsResponse
from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_response import PaymentResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.session_result_response import SessionResultResponse


pytestmark = pytest.mark.asyncio

async def test_get_sessions_session_id(client):
    """Test case for get_sessions_session_id

    Get the result of a payment session
    """
    params = [('sessionResult', 'session_result_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v70/sessions/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


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
        path='/v70/cardDetails',
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
        path='/v70/paymentMethods',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments(client):
    """Test case for post_payments

    Start a transaction
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":2,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"sessionValidity":"sessionValidity","splits":[{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"}],"deviceFingerprint":"deviceFingerprint","redirectToIssuerMethod":"redirectToIssuerMethod","channel":"iOS","platformChargebackLogic":{"costAllocationAccount":"costAllocationAccount","targetAccount":"targetAccount","behavior":"deductAccordingToSplitRatio"},"checkoutAttemptId":"checkoutAttemptId","mcc":"mcc","threeDSAuthenticationOnly":False,"merchantRiskIndicator":{"preOrderDate":"2000-01-23T04:56:07.000+00:00","shipIndicator":"shipIndicator","giftCardAmount":{"currency":"currency","value":0},"preOrderPurchaseInd":"preOrderPurchaseInd","deliveryEmail":"deliveryEmail","giftCardCount":1,"addressMatch":True,"deliveryTimeframe":"electronicDelivery","reorderItems":True,"deliveryEmailAddress":"deliveryEmailAddress","preOrderPurchase":True,"giftCardCurr":"giftCardCurr","reorderItemsInd":"reorderItemsInd","deliveryAddressIndicator":"shipToBillingAddress"},"lineItems":[{"quantity":1,"color":"color","itemCategory":"itemCategory","amountExcludingTax":1,"taxPercentage":7,"description":"description","upc":"upc","manufacturer":"manufacturer","size":"size","imageUrl":"imageUrl","id":"id","amountIncludingTax":1,"productUrl":"productUrl","sku":"sku","taxAmount":6,"brand":"brand","receiverEmail":"receiverEmail"},{"quantity":1,"color":"color","itemCategory":"itemCategory","amountExcludingTax":1,"taxPercentage":7,"description":"description","upc":"upc","manufacturer":"manufacturer","size":"size","imageUrl":"imageUrl","id":"id","amountIncludingTax":1,"productUrl":"productUrl","sku":"sku","taxAmount":6,"brand":"brand","receiverEmail":"receiverEmail"}],"reference":"reference","deliveryAddress":{"country":"country","firstName":"firstName","lastName":"lastName","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"plan":"regular","value":7},"recurringProcessingModel":"CardOnFile","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"order":{"orderData":"orderData","pspReference":"pspReference"},"trustedShopper":True,"enablePayOut":True,"fraudOffset":6,"additionalAmount":{"currency":"currency","value":0},"entityType":"NaturalPerson","shopperEmail":"shopperEmail","enableOneClick":True,"threeDS2RequestData":{"notificationURL":"notificationURL","paymentAuthenticationUseCase":"paymentAuthenticationUseCase","recurringFrequency":"recurringFrequency","mcc":"mcc","platform":"iOS","sdkEphemPubKey":{"kty":"kty","crv":"crv","x":"x","y":"y"},"merchantName":"merchantName","recurringExpiry":"recurringExpiry","threeDSRequestorAuthenticationInd":"threeDSRequestorAuthenticationInd","addrMatch":"Y","threeDSRequestorURL":"threeDSRequestorURL","sdkReferenceNumber":"sdkReferenceNumber","threeDSRequestorName":"threeDSRequestorName","acquirerMerchantID":"acquirerMerchantID","sdkAppID":"sdkAppID","messageVersion":"messageVersion","sdkTransID":"sdkTransID","whiteListStatus":"whiteListStatus","authenticationOnly":False,"sdkMaxTimeout":9,"homePhone":{"cc":"cc","subscriber":"subscriber"},"payTokenInd":True,"purchaseInstalData":"purchaseInstalData","acquirerBIN":"acquirerBIN","threeDSRequestorID":"threeDSRequestorID","deviceRenderOptions":{"sdkUiType":["multiSelect","multiSelect"],"sdkInterface":"both"},"transactionType":"goodsOrServicePurchase","acctInfo":{"shipAddressUsageInd":"01","paymentAccAge":"paymentAccAge","paymentAccInd":"01","txnActivityYear":"txnActivityYear","shipNameIndicator":"01","chAccPwChangeInd":"01","provisionAttemptsDay":"provisionAttemptsDay","chAccChange":"chAccChange","chAccChangeInd":"01","chAccString":"chAccString","nbPurchaseAccount":"nbPurchaseAccount","chAccAgeInd":"01","chAccPwChange":"chAccPwChange","shipAddressUsage":"shipAddressUsage","suspiciousAccActivity":"01","txnActivityDay":"txnActivityDay"},"threeDSRequestorChallengeInd":"01","mobilePhone":{"cc":"cc","subscriber":"subscriber"},"threeDSRequestorAuthenticationInfo":{"threeDSReqAuthMethod":"01","threeDSReqAuthData":"threeDSReqAuthData","threeDSReqAuthTimestamp":"threeDSReqAuthTimestamp"},"transType":"01","challengeIndicator":"noPreference","acctType":"01","workPhone":{"cc":"cc","subscriber":"subscriber"},"threeDSCompInd":"threeDSCompInd","threeDSRequestorPriorAuthenticationInfo":{"threeDSReqPriorRef":"threeDSReqPriorRef","threeDSReqPriorAuthData":"threeDSReqPriorAuthData","threeDSReqPriorAuthMethod":"01","threeDSReqPriorAuthTimestamp":"threeDSReqPriorAuthTimestamp"}},"deliverAt":"2000-01-23T04:56:07.000+00:00","orderReference":"orderReference","paymentMethod":{"bankAccountType":"balance","ownerName":"ownerName","storedPaymentMethodId":"storedPaymentMethodId","encryptedBankAccountNumber":"encryptedBankAccountNumber","recurringDetailReference":"recurringDetailReference","bankAccountNumber":"bankAccountNumber","checkoutAttemptId":"checkoutAttemptId","bankLocationId":"bankLocationId","type":"ach","encryptedBankLocationId":"encryptedBankLocationId"},"shopperLocale":"shopperLocale","captureDelayHours":0,"applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"browserInfo":{"acceptHeader":"acceptHeader","screenWidth":7,"javaEnabled":True,"screenHeight":2,"timeZoneOffset":9,"javaScriptEnabled":True,"language":"language","userAgent":"userAgent","colorDepth":5},"shopperReference":"shopperReference","shopperStatement":"shopperStatement","industryUsage":"delayedCharge","mandate":{"amount":"amount","amountRule":"max","billingDay":"billingDay","startsAt":"startsAt","billingAttemptsRule":True,"endsAt":"endsAt","remarks":"remarks","frequency":"adhoc"},"recurringFrequency":"recurringFrequency","telephoneNumber":"telephoneNumber","localizedShopperStatement":{"key":"localizedShopperStatement"},"socialSecurityNumber":"socialSecurityNumber","origin":"origin","shopperIP":"shopperIP","fundOrigin":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"telephoneNumber":"telephoneNumber","walletIdentifier":"walletIdentifier","shopperEmail":"shopperEmail","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"}},"recurringExpiry":"recurringExpiry","shopperName":{"firstName":"firstName","lastName":"lastName"},"countryCode":"countryCode","shopperInteraction":"Ecommerce","company":{"registrationNumber":"registrationNumber","registryLocation":"registryLocation","taxId":"taxId","name":"name","type":"type","homepage":"homepage"},"deliveryDate":"2000-01-23T04:56:07.000+00:00","returnUrl":"returnUrl","conversionId":"conversionId","accountInfo":{"passwordChangeDate":"2000-01-23T04:56:07.000+00:00","paymentAccountIndicator":"notApplicable","suspiciousActivity":True,"deliveryAddressUsageIndicator":"thisTransaction","pastTransactionsYear":1,"accountType":"notApplicable","homePhone":"homePhone","paymentAccountAge":"2000-01-23T04:56:07.000+00:00","accountAgeIndicator":"notApplicable","deliveryAddressUsageDate":"2000-01-23T04:56:07.000+00:00","accountChangeDate":"2000-01-23T04:56:07.000+00:00","accountCreationDate":"2000-01-23T04:56:07.000+00:00","mobilePhone":"mobilePhone","pastTransactionsDay":6,"accountChangeIndicator":"thisTransaction","passwordChangeIndicator":"notApplicable","addCardAttemptsDay":0,"workPhone":"workPhone","purchasesLast6Months":5},"authenticationData":{"authenticationOnly":False,"threeDSRequestData":{"challengeWindowSize":"01","dataOnly":"false","threeDSVersion":"2.1.0","nativeThreeDS":"preferred"},"attemptAuthentication":"always"},"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"redirectFromIssuerMethod":"redirectFromIssuerMethod","dateOfBirth":"2000-01-23T04:56:07.000+00:00","store":"store","riskData":{"fraudOffset":4,"customFields":{"key":"customFields"},"profileReference":"profileReference","clientData":"clientData"},"storePaymentMethod":True,"merchantAccount":"merchantAccount","fundRecipient":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"subMerchant":{"country":"country","city":"city","taxId":"taxId","name":"name","mcc":"mcc"},"telephoneNumber":"telephoneNumber","storedPaymentMethodId":"storedPaymentMethodId","walletIdentifier":"walletIdentifier","paymentMethod":{"holderName":"holderName","cupsecureplus.smscode":"cupsecureplus.smscode","expiryMonth":"expiryMonth","threeDS2SdkVersion":"threeDS2SdkVersion","networkPaymentReference":"networkPaymentReference","checkoutAttemptId":"checkoutAttemptId","expiryYear":"expiryYear","type":"scheme","shopperNotificationReference":"shopperNotificationReference","cvc":"cvc","number":"number","encryptedCardNumber":"encryptedCardNumber","encryptedSecurityCode":"encryptedSecurityCode","encryptedExpiryYear":"encryptedExpiryYear","storedPaymentMethodId":"storedPaymentMethodId","recurringDetailReference":"recurringDetailReference","encryptedExpiryMonth":"encryptedExpiryMonth","fundingSource":"credit","brand":"brand"},"shopperEmail":"shopperEmail","walletOwnerTaxId":"walletOwnerTaxId","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperReference":"shopperReference"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"enableRecurring":True,"mpiData":{"cavv":"cavv","authenticationResponse":"Y","xid":"xid","cavvAlgorithm":"cavvAlgorithm","dsTransID":"dsTransID","tokenAuthenticationVerificationValue":"tokenAuthenticationVerificationValue","transStatusReason":"transStatusReason","challengeCancel":"01","directoryResponse":"A","eci":"eci","riskScore":"riskScore","threeDSVersion":"threeDSVersion"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v70/payments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments_details(client):
    """Test case for post_payments_details

    Submit details for a payment
    """
    body = {"authenticationData":{"authenticationOnly":False},"paymentData":"paymentData","details":{"cupsecureplus.smscode":"cupsecureplus.smscode","orderID":"orderID","payerID":"payerID","resultCode":"resultCode","threeDSResult":"threeDSResult","oneTimePasscode":"oneTimePasscode","threeds2.challengeResult":"threeds2.challengeResult","redirectResult":"redirectResult","threeds2.fingerprint":"threeds2.fingerprint","authorization_token":"authorization_token","payload":"payload","billingToken":"billingToken","paymentID":"paymentID","MD":"MD","PaReq":"PaReq","PaRes":"PaRes","paymentStatus":"paymentStatus","facilitatorAccessToken":"facilitatorAccessToken"},"threeDSAuthenticationOnly":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v70/payments/details',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_sessions(client):
    """Test case for post_sessions

    Create a payment session
    """
    body = {"metadata":{"key":"metadata"},"splits":[{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"}],"redirectToIssuerMethod":"redirectToIssuerMethod","channel":"iOS","platformChargebackLogic":{"costAllocationAccount":"costAllocationAccount","targetAccount":"targetAccount","behavior":"deductAccordingToSplitRatio"},"mcc":"mcc","threeDSAuthenticationOnly":False,"lineItems":[{"quantity":1,"color":"color","itemCategory":"itemCategory","amountExcludingTax":1,"taxPercentage":7,"description":"description","upc":"upc","manufacturer":"manufacturer","size":"size","imageUrl":"imageUrl","id":"id","amountIncludingTax":1,"productUrl":"productUrl","sku":"sku","taxAmount":6,"brand":"brand","receiverEmail":"receiverEmail"},{"quantity":1,"color":"color","itemCategory":"itemCategory","amountExcludingTax":1,"taxPercentage":7,"description":"description","upc":"upc","manufacturer":"manufacturer","size":"size","imageUrl":"imageUrl","id":"id","amountIncludingTax":1,"productUrl":"productUrl","sku":"sku","taxAmount":6,"brand":"brand","receiverEmail":"receiverEmail"}],"mode":"embedded","reference":"reference","deliveryAddress":{"country":"country","firstName":"firstName","lastName":"lastName","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"recurringProcessingModel":"CardOnFile","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"blockedPaymentMethods":["blockedPaymentMethods","blockedPaymentMethods"],"trustedShopper":True,"enablePayOut":True,"additionalAmount":{"currency":"currency","value":0},"shopperEmail":"shopperEmail","enableOneClick":True,"storePaymentMethodMode":"askForConsent","deliverAt":"2000-01-23T04:56:07.000+00:00","showRemovePaymentMethodButton":True,"shopperLocale":"shopperLocale","captureDelayHours":0,"applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"shopperReference":"shopperReference","shopperStatement":"shopperStatement","mandate":{"amount":"amount","amountRule":"max","billingDay":"billingDay","startsAt":"startsAt","billingAttemptsRule":True,"endsAt":"endsAt","remarks":"remarks","frequency":"adhoc"},"recurringFrequency":"recurringFrequency","telephoneNumber":"telephoneNumber","socialSecurityNumber":"socialSecurityNumber","splitCardFundingSources":False,"themeId":"themeId","shopperIP":"shopperIP","fundOrigin":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"telephoneNumber":"telephoneNumber","walletIdentifier":"walletIdentifier","shopperEmail":"shopperEmail","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"}},"recurringExpiry":"recurringExpiry","shopperName":{"firstName":"firstName","lastName":"lastName"},"countryCode":"countryCode","shopperInteraction":"Ecommerce","company":{"registrationNumber":"registrationNumber","registryLocation":"registryLocation","taxId":"taxId","name":"name","type":"type","homepage":"homepage"},"returnUrl":"returnUrl","accountInfo":{"passwordChangeDate":"2000-01-23T04:56:07.000+00:00","paymentAccountIndicator":"notApplicable","suspiciousActivity":True,"deliveryAddressUsageIndicator":"thisTransaction","pastTransactionsYear":1,"accountType":"notApplicable","homePhone":"homePhone","paymentAccountAge":"2000-01-23T04:56:07.000+00:00","accountAgeIndicator":"notApplicable","deliveryAddressUsageDate":"2000-01-23T04:56:07.000+00:00","accountChangeDate":"2000-01-23T04:56:07.000+00:00","accountCreationDate":"2000-01-23T04:56:07.000+00:00","mobilePhone":"mobilePhone","pastTransactionsDay":6,"accountChangeIndicator":"thisTransaction","passwordChangeIndicator":"notApplicable","addCardAttemptsDay":0,"workPhone":"workPhone","purchasesLast6Months":5},"authenticationData":{"authenticationOnly":False,"threeDSRequestData":{"challengeWindowSize":"01","dataOnly":"false","threeDSVersion":"2.1.0","nativeThreeDS":"preferred"},"attemptAuthentication":"always"},"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"redirectFromIssuerMethod":"redirectFromIssuerMethod","dateOfBirth":"2000-01-23","showInstallmentAmount":True,"store":"store","allowedPaymentMethods":["allowedPaymentMethods","allowedPaymentMethods"],"riskData":{"fraudOffset":4,"customFields":{"key":"customFields"},"profileReference":"profileReference","clientData":"clientData"},"expiresAt":"2000-01-23T04:56:07.000+00:00","storePaymentMethod":True,"merchantAccount":"merchantAccount","installmentOptions":{"key":{"preselectedValue":6,"plans":["regular","regular"],"values":[1,1]}},"fundRecipient":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"subMerchant":{"country":"country","city":"city","taxId":"taxId","name":"name","mcc":"mcc"},"telephoneNumber":"telephoneNumber","storedPaymentMethodId":"storedPaymentMethodId","walletIdentifier":"walletIdentifier","paymentMethod":{"holderName":"holderName","cupsecureplus.smscode":"cupsecureplus.smscode","expiryMonth":"expiryMonth","threeDS2SdkVersion":"threeDS2SdkVersion","networkPaymentReference":"networkPaymentReference","checkoutAttemptId":"checkoutAttemptId","expiryYear":"expiryYear","type":"scheme","shopperNotificationReference":"shopperNotificationReference","cvc":"cvc","number":"number","encryptedCardNumber":"encryptedCardNumber","encryptedSecurityCode":"encryptedSecurityCode","encryptedExpiryYear":"encryptedExpiryYear","storedPaymentMethodId":"storedPaymentMethodId","recurringDetailReference":"recurringDetailReference","encryptedExpiryMonth":"encryptedExpiryMonth","fundingSource":"credit","brand":"brand"},"shopperEmail":"shopperEmail","walletOwnerTaxId":"walletOwnerTaxId","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperReference":"shopperReference"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"enableRecurring":True,"mpiData":{"cavv":"cavv","authenticationResponse":"Y","xid":"xid","cavvAlgorithm":"cavvAlgorithm","dsTransID":"dsTransID","tokenAuthenticationVerificationValue":"tokenAuthenticationVerificationValue","transStatusReason":"transStatusReason","challengeCancel":"01","directoryResponse":"A","eci":"eci","riskScore":"riskScore","threeDSVersion":"threeDSVersion"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v70/sessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

