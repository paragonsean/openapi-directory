# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sales_tax import SalesTax
from openapi_server.models.sales_tax_base import SalesTaxBase
from openapi_server.models.sales_taxes import SalesTaxes


pytestmark = pytest.mark.asyncio

async def test_create_or_replace_sales_tax(client):
    """Test case for create_or_replace_sales_tax

    
    """
    body = {"salesTaxPercentage":"salesTaxPercentage","shippingAndHandlingTaxed":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}'.format(country_code='country_code_example', jurisdiction_id='jurisdiction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sales_tax(client):
    """Test case for delete_sales_tax

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}'.format(country_code='country_code_example', jurisdiction_id='jurisdiction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sales_tax(client):
    """Test case for get_sales_tax

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}'.format(country_code='country_code_example', jurisdiction_id='jurisdiction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sales_taxes(client):
    """Test case for get_sales_taxes

    
    """
    params = [('country_code', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/sales_tax',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

