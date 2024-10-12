# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contact_request_schema import ContactRequestSchema
from openapi_server.models.contact_response_schema import ContactResponseSchema
from openapi_server.models.errors_response import ErrorsResponse


pytestmark = pytest.mark.asyncio

async def test_fraud_merchant_v3_common_contact_details_post(client):
    """Test case for fraud_merchant_v3_common_contact_details_post

    Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH.
    """
    contact_request = {"ContactRequest":{"AcquirerId":"12086"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/fraud/merchant/v3/common/contact-details',
        headers=headers,
        json=contact_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

