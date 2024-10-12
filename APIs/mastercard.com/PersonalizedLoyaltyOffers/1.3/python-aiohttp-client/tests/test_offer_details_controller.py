# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.offer_details_response import OfferDetailsResponse


pytestmark = pytest.mark.asyncio

async def test_offerdetails_get(client):
    """Test case for offerdetails_get

    Returns Information on an Offer
    """
    params = [('FId', '999999'),
                    ('UserToken', 'mh3WonUm5xmE'),
                    ('OfferId', 'c7dcfca7-cf35-36b0-9e67-d4f363d643e0')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plo/v1/offerdetails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

