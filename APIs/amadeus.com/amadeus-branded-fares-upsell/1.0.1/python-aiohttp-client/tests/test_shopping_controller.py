# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_upsell_query import GetUpsellQuery
from openapi_server.models.success_upsell import SuccessUpsell


pytestmark = pytest.mark.asyncio

async def test_upsell_air_offers(client):
    """Test case for upsell_air_offers

    Return a list of upsell Flight Offers based on given Flight Offers
    """
    upsell_flight_offers_body = openapi_server.GetUpsellQuery()
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
        'Content-Type': 'application/vnd.amadeus+json',
        'x_http_method_override': 'GET',
    }
    response = await client.request(
        method='POST',
        path='/v1/shopping/flight-offers/upselling',
        headers=headers,
        json=upsell_flight_offers_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

