# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.invoice_line_text_template_get200_response import InvoiceLineTextTemplateGet200Response
from openapi_server.models.invoice_line_text_template_invoice_line_text_template_id_get200_response import InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response


pytestmark = pytest.mark.asyncio

async def test_invoice_line_text_template_get(client):
    """Test case for invoice_line_text_template_get

    Get a list of invoice line text templates
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoice_line_text_template',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_line_text_template_invoice_line_text_template_id_delete(client):
    """Test case for invoice_line_text_template_invoice_line_text_template_id_delete

    Delete an invoice line text template
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/invoice_line_text_template/{invoice_line_text_template_id}'.format(invoice_line_text_template_id='invoice_line_text_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_line_text_template_invoice_line_text_template_id_get(client):
    """Test case for invoice_line_text_template_invoice_line_text_template_id_get

    Get a single invoice line text template
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoice_line_text_template/{invoice_line_text_template_id}'.format(invoice_line_text_template_id='invoice_line_text_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_invoice_line_text_template_invoice_line_text_template_id_post(client):
    """Test case for invoice_line_text_template_invoice_line_text_template_id_post

    Edit an invoice line text template
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
        path='/api/v1/invoice_line_text_template/{invoice_line_text_template_id}'.format(invoice_line_text_template_id='invoice_line_text_template_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_invoice_line_text_template_post(client):
    """Test case for invoice_line_text_template_post

    Add a new invoice line text template
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('html', 'html_example')
    data.add_field('image', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/invoice_line_text_template',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

