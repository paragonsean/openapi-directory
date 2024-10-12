# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calculate_simple_tax_out import CalculateSimpleTaxOut
from openapi_server.models.calculate_tax_in import CalculateTaxIn
from openapi_server.models.calculate_tax_location_out import CalculateTaxLocationOut
from openapi_server.models.calculate_tax_out import CalculateTaxOut
from openapi_server.models.validate_tax_number_out import ValidateTaxNumberOut


pytestmark = pytest.mark.asyncio

async def test_calculate_simple_tax(client):
    """Test case for calculate_simple_tax

    Simple tax
    """
    params = [('product_type', 'product_type_example'),
                    ('invoice_address_city', 'invoice_address_city_example'),
                    ('buyer_credit_card_prefix', 'buyer_credit_card_prefix_example'),
                    ('currency_code', 'currency_code_example'),
                    ('invoice_address_region', 'invoice_address_region_example'),
                    ('unit_price', 3.4),
                    ('quantity', 3.4),
                    ('buyer_tax_number', 'buyer_tax_number_example'),
                    ('force_country_code', 'force_country_code_example'),
                    ('order_date', 'order_date_example'),
                    ('amount', 3.4),
                    ('billing_country_code', 'billing_country_code_example'),
                    ('invoice_address_postal_code', 'invoice_address_postal_code_example'),
                    ('total_amount', 3.4),
                    ('tax_deducted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tax/calculate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_tax(client):
    """Test case for calculate_tax

    Calculate tax
    """
    input = openapi_server.CalculateTaxIn()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/tax/calculate',
        headers=headers,
        json=input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_tax_location(client):
    """Test case for calculate_tax_location

    Calculate location
    """
    params = [('billing_country_code', 'billing_country_code_example'),
                    ('buyer_credit_card_prefix', 'buyer_credit_card_prefix_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tax/location/calculate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_tax_number(client):
    """Test case for validate_tax_number

    Validate VAT number
    """
    params = [('country_code', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/tax/vat_numbers/{tax_number}/validate'.format(tax_number='tax_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

