# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payout_request import PayoutRequest
from openapi_server.models.payout_response import PayoutResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_payout(client):
    """Test case for post_payout

    Make an instant card payout
    """
    body = {"fraudOffset":0,"amount":{"currency":"currency","value":0},"telephoneNumber":"telephoneNumber","recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"shopperEmail":"shopperEmail","fundSource":{"shopperName":{"firstName":"firstName","lastName":"lastName"},"telephoneNumber":"telephoneNumber","shopperEmail":"shopperEmail","additionalData":{"key":"additionalData"},"billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"}},"reference":"reference","shopperName":{"firstName":"firstName","lastName":"lastName"},"merchantAccount":"merchantAccount","selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","billingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"card":{"cvc":"cvc","number":"number","holderName":"holderName","startMonth":"startMonth","issueNumber":"issueNumber","expiryMonth":"expiryMonth","startYear":"startYear","expiryYear":"expiryYear"},"shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/Payout/v51/payout',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

