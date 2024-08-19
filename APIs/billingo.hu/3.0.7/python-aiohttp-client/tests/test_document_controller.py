# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_error import ClientError
from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.document import Document
from openapi_server.models.document_insert import DocumentInsert
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_public_url import DocumentPublicUrl
from openapi_server.models.online_szamla_status import OnlineSzamlaStatus
from openapi_server.models.payment_history import PaymentHistory
from openapi_server.models.payment_method import PaymentMethod
from openapi_server.models.payment_status import PaymentStatus
from openapi_server.models.send_document import SendDocument
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_document(client):
    """Test case for cancel_document

    Cancel a document
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/documents/{id}/cancel'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_document(client):
    """Test case for create_document

    Create a document
    """
    body = {"bank_account_id":0,"settings":{"mediated_service":False,"round":"five","online_payment":"","without_financial_fulfillment":False,"place_id":1},"due_date":"2000-01-23","language":"de","type":"advance","fulfillment_date":"2000-01-23","block_id":6,"partner_id":2,"vendor_id":"vendor_id","electronic":False,"paid":False,"comment":"comment","currency":"AUD","conversion_rate":1.4658129,"items":[{"quantity":5.637377,"product_id":5},{"quantity":5.637377,"product_id":5}],"payment_method":"aruhitel"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/documents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_document_from_proforma(client):
    """Test case for create_document_from_proforma

    Create a document from proforma.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/documents/{id}/create-from-proforma'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_payment(client):
    """Test case for delete_payment

    Delete all payment history on document
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/documents/{id}/payments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_document(client):
    """Test case for download_document

    Download a document in PDF format.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/documents/{id}/download'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document(client):
    """Test case for get_document

    Retrieve a document
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/documents/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_online_szamla_status(client):
    """Test case for get_online_szamla_status

    Retrieve a document Online Számla status
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/documents/{id}/online-szamla'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment(client):
    """Test case for get_payment

    Retrieve a payment histroy
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/documents/{id}/payments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_url(client):
    """Test case for get_public_url

    Retrieve a document download public url.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/documents/{id}/public-url'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_document(client):
    """Test case for list_document

    List all documents
    """
    params = [('page', 56),
                    ('per_page', 25),
                    ('block_id', 56),
                    ('partner_id', 56),
                    ('payment_method', openapi_server.PaymentMethod()),
                    ('payment_status', openapi_server.PaymentStatus()),
                    ('start_date', '2020-05-15'),
                    ('end_date', '2020-05-15'),
                    ('start_number', 1),
                    ('end_number', 10),
                    ('start_year', 2020),
                    ('end_year', 2020)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_document(client):
    """Test case for send_document

    Send invoice to given email adresses.
    """
    body = {"emails":["emails","emails"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/documents/{id}/send'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payment(client):
    """Test case for update_payment

    Update payment history
    """
    body = {"date":"2000-01-23","price":6.0274563,"voucher_number":"voucher_number","conversion_rate":0.8008282,"payment_method":"aruhitel"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/documents/{id}/payments'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

