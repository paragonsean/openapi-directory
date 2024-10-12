# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_usage import ApiUsage
from openapi_server.models.convert_price import ConvertPrice
from openapi_server.models.country_code_check import CountryCodeCheck
from openapi_server.models.create_invoice import CreateInvoice
from openapi_server.models.currency_conversion import CurrencyConversion
from openapi_server.models.ip_check import IPCheck
from openapi_server.models.invoice_data import InvoiceData
from openapi_server.models.retrieve_invoice import RetrieveInvoice
from openapi_server.models.update_invoice import UpdateInvoice
from openapi_server.models.update_invoice_array import UpdateInvoiceArray
from openapi_server.models.vat_rates import VatRates


pytestmark = pytest.mark.asyncio

async def test_api_usage(client):
    """Test case for api_usage

    Check api requests remaining on current subscription plan
    """
    headers = { 
        'Accept': '*/*',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/usage-check',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_price(client):
    """Test case for convert_price

    Convert a price to or from VAT price.
    """
    params = [('code', 'code_example'),
                    ('country_rate', 'country_rate_example'),
                    ('price', 56),
                    ('type', 'type_example')]
    headers = { 
        'Accept': '*/*',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vat-price',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_country_code_check(client):
    """Test case for country_code_check

    Retrieve a countries VAT rates by its 2 digit country code
    """
    params = [('code', 'code_example')]
    headers = { 
        'Accept': '*/*',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/country-code-check',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_invoice(client):
    """Test case for create_invoice

    Create a VAT invoice
    """
    body = openapi_server.InvoiceData()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/invoice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currency_conversion(client):
    """Test case for currency_conversion

    Convert a currency
    """
    params = [('currency_from', 'currency_from_example'),
                    ('currency_to', 'currency_to_example'),
                    ('amount', 56)]
    headers = { 
        'Accept': '*/*',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/currency-conversion',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice(client):
    """Test case for get_invoice

    Retrieve an invoice
    """
    headers = { 
        'Accept': '*/*',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/invoice/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_delete(client):
    """Test case for invoice_delete

    Delete an invoice
    """
    headers = { 
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/invoice/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_invoice_update(client):
    """Test case for invoice_update

    Update an existing invoice
    """
    body = openapi_server.UpdateInvoiceArray()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/invoice/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ip_check(client):
    """Test case for ip_check

    Retrieve a countries VAT rates from an IP address
    """
    params = [('address', 'address_example')]
    headers = { 
        'Accept': '*/*',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/ip-check',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vat_number_validate(client):
    """Test case for vat_number_validate

    Validate a VAT number
    """
    params = [('vatid', 'vatid_example')]
    headers = { 
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vat-number-check',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vat_rates(client):
    """Test case for vat_rates

    Retrieve all current EU VAT rates
    """
    headers = { 
        'Accept': '*/*',
        'response_type': 'response_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/vat-rates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

