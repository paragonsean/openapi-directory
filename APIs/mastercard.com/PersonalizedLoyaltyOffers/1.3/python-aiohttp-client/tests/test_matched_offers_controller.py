# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.matched_offers_response import MatchedOffersResponse


pytestmark = pytest.mark.asyncio

async def test_matchedoffers_get(client):
    """Test case for matchedoffers_get

    Returns Matched Offers
    """
    params = [('FId', '999999'),
                    ('UserToken', 'user_token_example'),
                    ('Lang', 'en_US'),
                    ('MerchantName', 'Example.com'),
                    ('Category', 'DEPARTMENTSTORE'),
                    ('OfferType', 'POSTPAIDCREDIT'),
                    ('PageNumber', 1),
                    ('ItemsPerPage', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plo/v1/matchedoffers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

