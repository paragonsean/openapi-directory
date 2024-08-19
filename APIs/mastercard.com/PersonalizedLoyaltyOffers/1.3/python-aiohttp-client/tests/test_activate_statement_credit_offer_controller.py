# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activate_offer_response import ActivateOfferResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_activatestatementcreditoffer_post(client):
    """Test case for activatestatementcreditoffer_post

    Make Statement Credit Offer Available Redeemable
    """
    params = [('FId', '999999'),
                    ('UserToken', 'user_token_example'),
                    ('OfferId', 'c7dcfca7-cf35-36b0-9e67-d4f363d643e0')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/plo/v1/activatestatementcreditoffer',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

