# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.retro_request_schema import RetroRequestSchema
from openapi_server.models.retro_response_schema import RetroResponseSchema


pytestmark = pytest.mark.asyncio

async def test_fraud_merchant_v3_retro_retro_list_post(client):
    """Test case for fraud_merchant_v3_retro_retro_list_post

    Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service.
    """
    retro_request = {"RetroRequest":{"AcquirerId":"1996"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/fraud/merchant/v3/retro/retro-list',
        headers=headers,
        json=retro_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

