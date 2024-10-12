# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_insurance_prices200_ok import GetInsurancePrices200Ok
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable


pytestmark = pytest.mark.asyncio

async def test_get_insurance_prices(client):
    """Test case for get_insurance_prices

    List insurance levels
    """
    params = [('datasource', tranquility),
                    ('language', en-us)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': en-us,
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/latest/insurance/prices/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

