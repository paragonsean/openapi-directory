# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_dto import PaymentDTO
from openapi_server.models.provider_invoice_create_dto import ProviderInvoiceCreateDTO
from openapi_server.models.provider_invoice_create_result_dto import ProviderInvoiceCreateResultDTO
from openapi_server.models.provider_invoice_dto import ProviderInvoiceDTO
from openapi_server.models.status_request_dto import StatusRequestDTO
from openapi_server.models.url_result_dto import UrlResultDTO


pytestmark = pytest.mark.asyncio

async def test_create4(client):
    """Test case for create4

    Creates a new invoice.
    """
    body = {"jobsIds":[0,0]}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/providers/invoices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_create_payment1(client):
    """Test case for create_payment1

    Creates a new payment on the vendor account and assigns the payment to the invoice.
    """
    body = /home-api/assets/examples/accounting/providers/invoices/createPayment.json#requestBody
    headers = { 
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/providers/invoices/{invoice_id}/payments'.format(invoice_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete6(client):
    """Test case for delete6

    Removes a provider invoice.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/accounting/providers/invoices/{invoice_id}'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete7(client):
    """Test case for delete7

    Removes a provider payment.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/accounting/providers/payments/{payment_id}'.format(payment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all2(client):
    """Test case for get_all2

    Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date.
    """
    params = [('updatedSince', 56)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/providers/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_ids3(client):
    """Test case for get_all_ids3

    Returns vendor invoices' internal identifiers.
    """
    params = [('updatedSince', 56)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/providers/invoices/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id3(client):
    """Test case for get_by_id3

    Returns provider invoice details.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/providers/invoices/{invoice_id}'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document1(client):
    """Test case for get_document1

    Generates provider invoice document (PDF).
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/providers/invoices/{invoice_id}/document'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments1(client):
    """Test case for get_payments1

    Returns all payments for the vendor invoice.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/providers/invoices/{invoice_id}/payments'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send(client):
    """Test case for send

    Sends a provider invoice.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/providers/invoices/{invoice_id}/send'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_status(client):
    """Test case for set_status

    Changes invoice status to given status.
    """
    body = {"status":"POSTPONED"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/providers/invoices/{invoice_id}/status'.format(invoice_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

