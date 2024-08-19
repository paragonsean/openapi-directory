# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.redeemed_offers_response import RedeemedOffersResponse


pytestmark = pytest.mark.asyncio

async def test_redeemedoffers_get(client):
    """Test case for redeemedoffers_get

    Returns Redeemed Offers
    """
    params = [('FId', '999999'),
                    ('UserToken', 'user_token_example'),
                    ('Lang', 'en_US'),
                    ('PageNumber', 1),
                    ('ItemsPerPage', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plo/v1/redeemedoffers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

