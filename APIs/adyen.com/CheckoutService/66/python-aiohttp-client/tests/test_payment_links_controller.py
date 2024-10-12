# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_link_request import PaymentLinkRequest
from openapi_server.models.payment_link_response import PaymentLinkResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.update_payment_link_request import UpdatePaymentLinkRequest


pytestmark = pytest.mark.asyncio

async def test_get_payment_links_link_id(client):
    """Test case for get_payment_links_link_id

    Get a payment link
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v66/paymentLinks/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_payment_links_link_id(client):
    """Test case for patch_payment_links_link_id

    Update the status of a payment link
    """
    body = {"status":"expired"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v66/paymentLinks/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_payment_links(client):
    """Test case for post_payment_links

    Create a payment link
    """
    body = {"metadata":{"key":"metadata"},"splits":[{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"},{"reference":"reference","amount":{"currency":"currency","value":5},"description":"description","type":"AcquiringFees","account":"account"}],"description":"description","lineItems":[{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6},{"quantity":1,"itemCategory":"itemCategory","amountExcludingTax":1,"imageUrl":"imageUrl","taxPercentage":7,"description":"description","id":"id","amountIncludingTax":1,"productUrl":"productUrl","taxAmount":6}],"reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"deliveryAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"countryCode":"countryCode","recurringProcessingModel":"CardOnFile","blockedPaymentMethods":["blockedPaymentMethods","blockedPaymentMethods"],"returnUrl":"returnUrl","merchantOrderReference":"merchantOrderReference","amount":{"currency":"currency","value":0},"manualCapture":True,"shopperEmail":"shopperEmail","store":"store","allowedPaymentMethods":["allowedPaymentMethods","allowedPaymentMethods"],"riskData":{"fraudOffset":4,"customFields":{"key":"customFields"},"profileReference":"profileReference","clientData":"clientData"},"expiresAt":"expiresAt","reusable":True,"storePaymentMethod":True,"merchantAccount":"merchantAccount","installmentOptions":{"key":{"preselectedValue":6,"maxValue":0,"plans":["regular","regular"],"values":[1,1]}},"deliverAt":"2000-01-23T04:56:07.000+00:00","showRemovePaymentMethodButton":True,"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"shopperLocale":"shopperLocale","applicationInfo":{"adyenLibrary":{"name":"name","version":"version"},"merchantApplication":{"name":"name","version":"version"},"adyenPaymentSource":{"name":"name","version":"version"},"merchantDevice":{"reference":"reference","os":"os","osVersion":"osVersion"},"shopperInteractionDevice":{"os":"os","osVersion":"osVersion","locale":"locale"},"externalPlatform":{"name":"name","integrator":"integrator","version":"version"}},"shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': '37ca9c97-d1d1-4c62-89e8-706891a563ed',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v66/paymentLinks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

