# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.crm_response import CRMResponse
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_crm_check(client):
    """Test case for crm_check

    CRM check of a particular vin
    """
    params = [('api_key', 'api_key_example'),
                    ('sale_date', 'sale_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/crm_check/car/{vin}'.format(vin='vin_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

