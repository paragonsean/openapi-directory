# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.donation_payment_request import DonationPaymentRequest
from openapi_server.models.donation_payment_response import DonationPaymentResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_donations(client):
    """Test case for post_donations

    Start a transaction for donations
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":6,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"sessionValidity":"sessionValidity","splits":[{"reference":"reference","amount":{"currency":"currency","value":2},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":2},"description":"description","type":"AcquiringFees","account":"account"}],"deviceFingerprint":"deviceFingerprint","redirectToIssuerMethod":"redirectToIssuerMethod","channel":"iOS","mcc":"mcc","donationAccount":"donationAccount","donationToken":"donationToken","lineItems":[{"quantity":7,"itemCategory":"itemCategory","amountExcludingTax":5,"imageUrl":"imageUrl","taxPercentage":3,"description":"description","id":"id","amountIncludingTax":2,"productUrl":"productUrl","taxAmount":9},{"quantity":7,"itemCategory":"itemCategory","amountExcludingTax":5,"imageUrl":"imageUrl","taxPercentage":3,"description":"description","id":"id","amountIncludingTax":2,"productUrl":"productUrl","taxAmount":9}],"reference":"reference","deliveryAddress":{"country":"country","firstName":"firstName","lastName":"lastName","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"value":5},"recurringProcessingModel":"CardOnFile","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"blockedPaymentMethods":["blockedPaymentMethods","blockedPaymentMethods"],"order":{"orderData":"orderData","pspReference":"pspReference"},"trustedShopper":True,"enablePayOut":True,"fraudOffset":1,"additionalAmount":{"currency":"currency","value":0},"entityType":"NaturalPerson","shopperEmail":"shopperEmail","enableOneClick":True,"orderReference":"orderReference","paymentMethod":{"recurringDetailReference":"recurringDetailReference","applePayToken":"applePayToken","fundingSource":"credit","type":"applepay"},"shopperLocale":"shopperLocale","captureDelayHours":0,"browserInfo":{"acceptHeader":"acceptHeader","userAgent":"userAgent"},"shopperReference":"shopperReference","shopperStatement":"shopperStatement","mandate":{"amount":"amount","amountRule":"max","billingDay":"billingDay","startsAt":"startsAt","billingAttemptsRule":True,"endsAt":"endsAt","remarks":"remarks","frequency":"adhoc"},"recurringFrequency":"recurringFrequency","telephoneNumber":"telephoneNumber","socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","fundOrigin":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"telephoneNumber":"telephoneNumber","walletIdentifier":"walletIdentifier","shopperEmail":"shopperEmail","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"}},"recurringExpiry":"recurringExpiry","shopperName":{"firstName":"firstName","lastName":"lastName"},"countryCode":"countryCode","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","company":{"registrationNumber":"registrationNumber","registryLocation":"registryLocation","taxId":"taxId","name":"name","type":"type","homepage":"homepage"},"deliveryDate":"2000-01-23T04:56:07.000+00:00","returnUrl":"returnUrl","merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"redirectFromIssuerMethod":"redirectFromIssuerMethod","dateOfBirth":"2000-01-23T04:56:07.000+00:00","store":"store","allowedPaymentMethods":["allowedPaymentMethods","allowedPaymentMethods"],"riskData":{"clientData":"clientData"},"merchantAccount":"merchantAccount","donationOriginalPspReference":"donationOriginalPspReference","fundRecipient":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"subMerchant":{"country":"country","city":"city","taxId":"taxId","name":"name","mcc":"mcc"},"telephoneNumber":"telephoneNumber","storedPaymentMethodId":"storedPaymentMethodId","walletIdentifier":"walletIdentifier","paymentMethod":{"holderName":"holderName","cupsecureplus.smscode":"cupsecureplus.smscode","expiryMonth":"expiryMonth","threeDS2SdkVersion":"threeDS2SdkVersion","networkPaymentReference":"networkPaymentReference","expiryYear":"expiryYear","type":"scheme","shopperNotificationReference":"shopperNotificationReference","cvc":"cvc","number":"number","encryptedCardNumber":"encryptedCardNumber","encryptedSecurityCode":"encryptedSecurityCode","encryptedExpiryYear":"encryptedExpiryYear","recurringDetailReference":"recurringDetailReference","encryptedExpiryMonth":"encryptedExpiryMonth","fundingSource":"credit","brand":"brand"},"shopperEmail":"shopperEmail","walletOwnerTaxId":"walletOwnerTaxId","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperReference":"shopperReference"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"enableRecurring":True,"mpiData":{"cavv":"cavv","authenticationResponse":"Y","xid":"xid","cavvAlgorithm":"cavvAlgorithm","directoryResponse":"A","eci":"eci"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v37/donations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

