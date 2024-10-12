# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.all_tax_rates200_response_inner import AllTaxRates200ResponseInner
from openapi_server.models.tax_rates_by_country_code500_response import TaxRatesByCountryCode500Response


pytestmark = pytest.mark.asyncio

async def test_all_tax_rates(client):
    """Test case for all_tax_rates

    All tax rates
    """
    params = [('domain', '<string>'),
                    ('filter', ''),
                    ('cursor', ''),
                    ('Product_code', 'C012')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/tax/rates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

