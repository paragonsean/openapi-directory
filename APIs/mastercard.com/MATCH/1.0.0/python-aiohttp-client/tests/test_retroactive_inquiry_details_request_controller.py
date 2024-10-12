# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.retro_inquiry_request_schema import RetroInquiryRequestSchema
from openapi_server.models.retro_inquiry_response_schema import RetroInquiryResponseSchema


pytestmark = pytest.mark.asyncio

async def test_fraud_merchant_v3_retro_retro_inquiry_details_post(client):
    """Test case for fraud_merchant_v3_retro_retro_inquiry_details_post

    Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer's ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination.
    """
    retro_inquiry_request = {"RetroInquiryRequest":{"InquiryReferenceNumber":"19962014090300001"}}
    params = [('AcquirerId', 'acquirer_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/fraud/merchant/v3/retro/retro-inquiry-details',
        headers=headers,
        json=retro_inquiry_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

