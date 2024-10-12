# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.invoice_lines_get200_response import InvoiceLinesGet200Response
from openapi_server.models.invoice_lines_invoice_line_id_get200_response import InvoiceLinesInvoiceLineIdGet200Response
from openapi_server.models.invoice_lines_invoice_line_id_put_request import InvoiceLinesInvoiceLineIdPutRequest
from openapi_server.models.invoice_lines_post_request import InvoiceLinesPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_invoice_line_texts_invoice_line_text_id_post(client):
    """Test case for invoice_line_texts_invoice_line_text_id_post

    Edit invoice line text
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    data = FormData()
    data.add_field('html', 'html_example')
    data.add_field('image', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/invoice_line_texts/{invoice_line_text_id}'.format(invoice_line_text_id='invoice_line_text_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_invoice_line_texts_post(client):
    """Test case for invoice_line_texts_post

    Add invoice line text
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    data = FormData()
    data.add_field('html', 'html_example')
    data.add_field('image', '/path/to/file')
    data.add_field('invoice_id', 'invoice_id_example')
    data.add_field('placement', 56)
    response = await client.request(
        method='POST',
        path='/api/v1/invoice_line_texts/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_lines_get(client):
    """Test case for invoice_lines_get

    View list of invoice lines
    """
    params = [('invoice_id', 'invoice_id_example'),
                    ('product_id', 'product_id_example'),
                    ('user_id', 'user_id_example'),
                    ('name', 'name_example'),
                    ('discount_text', 'discount_text_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoice_lines',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_lines_invoice_line_id_delete(client):
    """Test case for invoice_lines_invoice_line_id_delete

    Delete invoice line
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/invoice_lines/{invoice_line_id}'.format(invoice_line_id='invoice_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_lines_invoice_line_id_get(client):
    """Test case for invoice_lines_invoice_line_id_get

    View invoice line
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoice_lines/{invoice_line_id}'.format(invoice_line_id='invoice_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_lines_invoice_line_id_put(client):
    """Test case for invoice_lines_invoice_line_id_put

    Edit invoice line
    """
    body = openapi_server.InvoiceLinesInvoiceLineIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/invoice_lines/{invoice_line_id}'.format(invoice_line_id='invoice_line_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_lines_post(client):
    """Test case for invoice_lines_post

    Add invoice line
    """
    body = openapi_server.InvoiceLinesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/invoice_lines',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

