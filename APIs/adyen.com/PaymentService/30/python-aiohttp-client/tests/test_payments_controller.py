# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_request import PaymentRequest
from openapi_server.models.payment_request3d import PaymentRequest3d
from openapi_server.models.payment_result import PaymentResult
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_authorise(client):
    """Test case for post_authorise

    Create an authorisation
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":6,"account":"account","baseAmount":{"currency":"currency","value":0}},"mandate":{"amount":"amount","amountRule":"max","billingDay":"billingDay","startsAt":"startsAt","billingAttemptsRule":True,"endsAt":"endsAt","remarks":"remarks","frequency":"adhoc"},"metadata":{"key":"metadata"},"telephoneNumber":"telephoneNumber","deviceFingerprint":"deviceFingerprint","socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","mcc":"mcc","reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"value":5},"recurringProcessingModel":"CardOnFile","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","totalsGroup":"totalsGroup","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"selectedBrand":"selectedBrand","deliveryDate":"2000-01-23T04:56:07.000+00:00","bankAccount":{"ownerName":"ownerName","countryCode":"countryCode","taxId":"taxId","iban":"iban","bankAccountNumber":"bankAccountNumber","bankName":"bankName","bankLocationId":"bankLocationId","bic":"bic","bankCity":"bankCity"},"fraudOffset":1,"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"additionalAmount":{"currency":"currency","value":0},"entityType":"NaturalPerson","recurring":{"tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","sessionId":"sessionId","store":"store","merchantAccount":"merchantAccount","nationality":"nationality","orderReference":"orderReference","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperLocale":"shopperLocale","captureDelayHours":0,"browserInfo":{"acceptHeader":"acceptHeader","userAgent":"userAgent"},"card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"},"mpiData":{"cavv":"cavv","authenticationResponse":"Y","xid":"xid","cavvAlgorithm":"cavvAlgorithm","directoryResponse":"A","eci":"eci"},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v30/authorise',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_authorise3d(client):
    """Test case for post_authorise3d

    Complete a 3DS authorisation
    """
    body = {"dccQuote":{"reference":"reference","validTill":"2000-01-23T04:56:07.000+00:00","signature":"signature","accountType":"accountType","buy":{"currency":"currency","value":0},"sell":{"currency":"currency","value":0},"interbank":{"currency":"currency","value":0},"source":"source","type":"type","basePoints":6,"account":"account","baseAmount":{"currency":"currency","value":0}},"metadata":{"key":"metadata"},"telephoneNumber":"telephoneNumber","deviceFingerprint":"deviceFingerprint","socialSecurityNumber":"socialSecurityNumber","shopperIP":"shopperIP","mcc":"mcc","reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"installments":{"value":5},"md":"md","recurringProcessingModel":"CardOnFile","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","totalsGroup":"totalsGroup","additionalData":{"challengeWindowSize":"01","mpiImplementationType":"mpiImplementationType","allow3DS2":"allow3DS2","executeThreeD":"executeThreeD","threeDSVersion":"threeDSVersion","scaExemption":"scaExemption"},"selectedBrand":"selectedBrand","deliveryDate":"2000-01-23T04:56:07.000+00:00","fraudOffset":6,"merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"additionalAmount":{"currency":"currency","value":0},"recurring":{"tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"dateOfBirth":"2000-01-23","shopperEmail":"shopperEmail","sessionId":"sessionId","store":"store","paResponse":"paResponse","merchantAccount":"merchantAccount","orderReference":"orderReference","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperLocale":"shopperLocale","captureDelayHours":0,"browserInfo":{"acceptHeader":"acceptHeader","userAgent":"userAgent"},"shopperReference":"shopperReference","shopperStatement":"shopperStatement"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payment/v30/authorise3d',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

