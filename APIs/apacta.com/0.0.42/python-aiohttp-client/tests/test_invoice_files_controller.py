# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_invoice_files200_response import GetInvoiceFiles200Response
from openapi_server.models.get_one_invoice_files200_response import GetOneInvoiceFiles200Response
from openapi_server.models.unauthorized_error import UnauthorizedError


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_invoice_file(client):
    """Test case for create_invoice_file

    Create a new invoice file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'file_id': 'file_id_example',
        'invoice_id2': 'invoice_id_example',
        'type': 'type_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v1/invoices/{invoice_id}/files'.format(invoice_id='invoice_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_files(client):
    """Test case for get_invoice_files

    Get list of invoice files
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoices/{invoice_id}/files'.format(invoice_id='invoice_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_one_invoice_files(client):
    """Test case for get_one_invoice_files

    Get an invoice files
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoices/{invoice_id}/files/{file_id}'.format(invoice_id='invoice_id_example', file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_invoice_id_files_file_id_delete(client):
    """Test case for invoices_invoice_id_files_file_id_delete

    Delete invoice file
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/invoices/{invoice_id}/files/{file_id}'.format(invoice_id='invoice_id_example', file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

