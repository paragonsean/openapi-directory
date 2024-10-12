# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sales_tax_jurisdictions import SalesTaxJurisdictions


pytestmark = pytest.mark.asyncio

async def test_get_sales_tax_jurisdictions(client):
    """Test case for get_sales_tax_jurisdictions

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/metadata/v1/country/{country_code}/sales_tax_jurisdiction'.format(country_code='country_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

