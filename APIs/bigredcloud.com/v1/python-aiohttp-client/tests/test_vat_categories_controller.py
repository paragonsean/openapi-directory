# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_vat_category_dto import PageResultVatCategoryDto
from openapi_server.models.vat_rates_by_vat_category_dto import VatRatesByVatCategoryDto


pytestmark = pytest.mark.asyncio

async def test_vat_categories_get(client):
    """Test case for vat_categories_get

    Returns a list of global Vat Categories. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/vatCategories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vat_categories_process_vat_rates(client):
    """Test case for vat_categories_process_vat_rates

    Process Vat Rates
    """
    body = {"vatCategoryId":1,"vatRates":[{"id":0,"isActive":True,"isDefault":False,"orderIndex":0,"percentage":30,"vatCategoryId":1}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/vatCategories/vatRates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

