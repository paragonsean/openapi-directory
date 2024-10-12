# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_invoice_item_response import CreateInvoiceItemResponse
from openapi_server.models.delete_tax_rate_response import DeleteTaxRateResponse
from openapi_server.models.get_invoice_item_response import GetInvoiceItemResponse
from openapi_server.models.get_invoice_items_response import GetInvoiceItemsResponse
from openapi_server.models.invoice_item import InvoiceItem
from openapi_server.models.invoice_items_filter import InvoiceItemsFilter
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_invoice_items_response import UpdateInvoiceItemsResponse


pytestmark = pytest.mark.asyncio

async def test_invoice_items_add(client):
    """Test case for invoice_items_add

    Create Invoice Item
    """
    body = {"code":"120-C","purchase_details":{"tax_inclusive":True,"unit_of_measure":"pc.","unit_price":27500.5,"tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"}},"sales_details":{"tax_inclusive":True,"unit_of_measure":"pc.","unit_price":27500.5,"tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"}},"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","tracked":True,"type":"inventory","inventory_date":"2020-10-30","custom_mappings":"{}","asset_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"expense_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"updated_at":"2020-09-30T07:43:32Z","id":"123456","income_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"sold":True,"quantity":1,"taxable":True,"active":True,"tracking_category":{"name":"New York","id":"123456"},"unit_price":27500.5,"created_by":"12345","purchased":True,"row_version":"1-12345","name":"Model Y","updated_by":"12345"}
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
        path='/accounting/invoice-items',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_items_all(client):
    """Test case for invoice_items_all

    List Invoice Items
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.InvoiceItemsFilter()),
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
        path='/accounting/invoice-items',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_items_delete(client):
    """Test case for invoice_items_delete

    Delete Invoice Item
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
        path='/accounting/invoice-items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_items_one(client):
    """Test case for invoice_items_one

    Get Invoice Item
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
        path='/accounting/invoice-items/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_items_update(client):
    """Test case for invoice_items_update

    Update Invoice Item
    """
    body = {"code":"120-C","purchase_details":{"tax_inclusive":True,"unit_of_measure":"pc.","unit_price":27500.5,"tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"}},"sales_details":{"tax_inclusive":True,"unit_of_measure":"pc.","unit_price":27500.5,"tax_rate":{"code":"N-T","rate":10,"name":"GST on Purchases","id":"123456"}},"created_at":"2020-09-30T07:43:32Z","description":"Model Y is a fully electric, mid-size SUV, with seating for up to seven, dual motor AWD and unparalleled protection.","tracked":True,"type":"inventory","inventory_date":"2020-10-30","custom_mappings":"{}","asset_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"expense_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"updated_at":"2020-09-30T07:43:32Z","id":"123456","income_account":{"code":"453","nominal_code":"N091","name":"Bank account","id":"123456"},"sold":True,"quantity":1,"taxable":True,"active":True,"tracking_category":{"name":"New York","id":"123456"},"unit_price":27500.5,"created_by":"12345","purchased":True,"row_version":"1-12345","name":"Model Y","updated_by":"12345"}
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
        path='/accounting/invoice-items/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

