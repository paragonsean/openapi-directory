# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.termination_inquiry_schema import TerminationInquirySchema


pytestmark = pytest.mark.asyncio

async def test_fraud_merchant_v3_termination_inquiry_irnget(client):
    """Test case for fraud_merchant_v3_termination_inquiry_irnget

    Returns information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank from a previous inquiry. The Inquiry History Results resource displays the inquiry with the option to view either; Possible Merchant Matches or Possible Inquiry Matches.
    """
    params = [('PageOffset', 0),
                    ('PageLength', 10),
                    ('AcquirerId', '1996')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/fraud/merchant/v3/termination-inquiry/{irn}'.format(irn='19962016070500348'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

