# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cost_estimate_request import CostEstimateRequest
from openapi_server.models.cost_estimate_response import CostEstimateResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.three_ds_availability_request import ThreeDSAvailabilityRequest
from openapi_server.models.three_ds_availability_response import ThreeDSAvailabilityResponse


pytestmark = pytest.mark.asyncio

async def test_post_get3ds_availability(client):
    """Test case for post_get3ds_availability

    Check if 3D Secure is available
    """
    body = {"brands":["brands","brands"],"merchantAccount":"merchantAccount","recurringDetailReference":"recurringDetailReference","additionalData":{"key":"additionalData"},"cardNumber":"cardNumber","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/BinLookup/v50/get3dsAvailability',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_get_cost_estimate(client):
    """Test case for post_get_cost_estimate

    Get a fees cost estimate
    """
    body = {"amount":{"currency":"currency","value":0},"encryptedCardNumber":"encryptedCardNumber","merchantAccount":"merchantAccount","recurring":{"recurringExpiry":"2000-01-23T04:56:07.000+00:00","recurringFrequency":"recurringFrequency","tokenService":"VISATOKENSERVICE","contract":"ONECLICK","recurringDetailName":"recurringDetailName"},"selectedRecurringDetailReference":"selectedRecurringDetailReference","shopperInteraction":"Ecommerce","merchantDetails":{"countryCode":"countryCode","enrolledIn3DSecure":True,"mcc":"mcc"},"assumptions":{"installments":0,"assume3DSecureAuthenticated":True,"assumeLevel3Data":True},"cardNumber":"cardNumber","shopperReference":"shopperReference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/BinLookup/v50/getCostEstimate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

