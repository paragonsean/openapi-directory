# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_setup_request import PaymentSetupRequest
from openapi_server.models.payment_setup_response import PaymentSetupResponse
from openapi_server.models.payment_verification_request import PaymentVerificationRequest
from openapi_server.models.payment_verification_response import PaymentVerificationResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_payment_session(client):
    """Test case for post_payment_session

    Create a payment session
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":2,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"sessionValidity":"sessionValidity","splits":[{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":4},"description":"description","type":"AcquiringFees","account":"account"}],"channel":"iOS","mcc":"mcc","threeDSAuthenticationOnly":False,"lineItems":[{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6},{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6}],"reference":"reference","deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"value":7},"additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"blockedPaymentMethods":["blockedPaymentMethods","blockedPaymentMethods"],"trustedShopper":True,"enablePayOut":True,"fraudOffset":1,"additionalAmount":{"currency":"currency","value":0},"entityType":"NaturalPerson","shopperEmail":"shopperEmail","enableOneClick":True,"orderReference":"orderReference","sdkVersion":"sdkVersion","shopperLocale":"shopperLocale","captureDelayHours":0,"applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"shopperReference":"shopperReference","shopperStatement":"shopperStatement","mandate":{"amount":"amount","amountRule":"max","billingDay":"billingDay","startsAt":"startsAt","billingAttemptsRule":True,"endsAt":"endsAt","remarks":"remarks","frequency":"adhoc"},"recurringFrequency":"recurringFrequency","telephoneNumber":"telephoneNumber","configuration":{"cardHolderName":"NONE","installments":{"maxNumberOfInstallments":6},"shopperInput":{"deliveryAddress":"editable","personalDetails":"editable","billingAddress":"editable"},"avs":{"addressEditable":True,"enabled":True}},"socialSecurityNumber":"socialSecurityNumber","origin":"origin","shopperIP":"shopperIP","recurringExpiry":"recurringExpiry","shopperName":{"firstName":"firstName","lastName":"lastName"},"enableRealTimeUpdate":True,"countryCode":"countryCode","shopperInteraction":"Ecommerce","company":{"registrationNumber":"registrationNumber","registryLocation":"registryLocation","taxId":"taxId","name":"name","type":"type","homepage":"homepage"},"deliveryDate":"2000-01-23T04:56:07.000+00:00","returnUrl":"returnUrl","conversionId":"conversionId","merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"dateOfBirth":"2000-01-23","store":"store","allowedPaymentMethods":["allowedPaymentMethods","allowedPaymentMethods"],"riskData":{"clientData":"clientData"},"token":"token","storePaymentMethod":True,"merchantAccount":"merchantAccount","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"enableRecurring":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v51/paymentSession',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payments_result(client):
    """Test case for post_payments_result

    Verify a payment result
    """
    body = {"payload":"payload"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v51/payments/result',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

