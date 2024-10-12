# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_tax_rate_response import CreateTaxRateResponse
from openapi_server.models.delete_tax_rate_response import DeleteTaxRateResponse
from openapi_server.models.get_tax_rate_response import GetTaxRateResponse
from openapi_server.models.get_tax_rates_response import GetTaxRatesResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.tax_rate import TaxRate
from openapi_server.models.tax_rates_filter import TaxRatesFilter
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_tax_rate_response import UpdateTaxRateResponse


pytestmark = pytest.mark.asyncio

async def test_tax_rates_add(client):
    """Test case for tax_rates_add

    Create Tax Rate
    """
    body = {"components":[{"rate":10,"name":"GST","id":"10","compound":True},{"rate":10,"name":"GST","id":"10","compound":True}],"code":"ABN","created_at":"2020-09-30T07:43:32Z","description":"Reduced rate GST Purchases","type":"NONE","created_by":"12345","custom_mappings":"{}","original_tax_rate_id":"12345","tax_remitted_account_id":"123456","tax_payable_account_id":"123456","updated_at":"2020-09-30T07:43:32Z","report_tax_type":"NONE","row_version":"1-12345","name":"GST on Purchases","updated_by":"12345","id":"1234","effective_tax_rate":10,"total_tax_rate":10,"status":"active"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/accounting/tax-rates',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tax_rates_all(client):
    """Test case for tax_rates_all

    List Tax Rates
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.TaxRatesFilter()),
                    ('pass_through', None),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounting/tax-rates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tax_rates_delete(client):
    """Test case for tax_rates_delete

    Delete Tax Rate
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/accounting/tax-rates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tax_rates_one(client):
    """Test case for tax_rates_one

    Get Tax Rate
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounting/tax-rates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tax_rates_update(client):
    """Test case for tax_rates_update

    Update Tax Rate
    """
    body = {"components":[{"rate":10,"name":"GST","id":"10","compound":True},{"rate":10,"name":"GST","id":"10","compound":True}],"code":"ABN","created_at":"2020-09-30T07:43:32Z","description":"Reduced rate GST Purchases","type":"NONE","created_by":"12345","custom_mappings":"{}","original_tax_rate_id":"12345","tax_remitted_account_id":"123456","tax_payable_account_id":"123456","updated_at":"2020-09-30T07:43:32Z","report_tax_type":"NONE","row_version":"1-12345","name":"GST on Purchases","updated_by":"12345","id":"1234","effective_tax_rate":10,"total_tax_rate":10,"status":"active"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/accounting/tax-rates/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

