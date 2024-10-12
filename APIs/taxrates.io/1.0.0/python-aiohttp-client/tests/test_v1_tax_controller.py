# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tax_rates_by_country_code200_response import TaxRatesByCountryCode200Response
from openapi_server.models.tax_rates_by_country_code500_response import TaxRatesByCountryCode500Response


pytestmark = pytest.mark.asyncio

async def test_tax_rates_by_country_code(client):
    """Test case for tax_rates_by_country_code

    Tax rates by Country Code
    """
    params = [('domain', 'api.taxrates.io'),
                    ('country_code', 'US'),
                    ('filter', ''),
                    ('zip', '71642'),
                    ('product_codes[]', 'C010'),
                    ('province ', ''),
                    ('date', '2020-09-02')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tax/countrycode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tax_rates_by_ip_address(client):
    """Test case for tax_rates_by_ip_address

    Tax rates by IP address
    """
    params = [('domain', 'api.taxrates.io'),
                    ('ip', '86.139.70.49'),
                    ('filter', ''),
                    ('zip', ''),
                    ('product_code', 'C010')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tax/ip',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

