# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_vat_rate_dto import PageResultVatRateDto


pytestmark = pytest.mark.asyncio

async def test_vat_rates_get(client):
    """Test case for vat_rates_get

    Returns a list of company's Vat Rates. Supports OData querying protocol.  Filtering is allowed by \"vatCategoryId\" field.  Ordering is allowed by \"id\" and \"orderIndex\" fields.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vatRates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

