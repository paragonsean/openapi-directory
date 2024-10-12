# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_invoice_create_dto import CustomerInvoiceCreateDTO
from openapi_server.models.customer_invoice_create_result_dto import CustomerInvoiceCreateResultDTO
from openapi_server.models.customer_invoice_dto import CustomerInvoiceDTO
from openapi_server.models.customer_invoice_dates_dto import CustomerInvoiceDatesDTO
from openapi_server.models.download_documents_request_dto import DownloadDocumentsRequestDTO
from openapi_server.models.payment_dto import PaymentDTO
from openapi_server.models.payment_terms_dto import PaymentTermsDTO
from openapi_server.models.send_reminders_request_dto import SendRemindersRequestDTO
from openapi_server.models.send_reminders_response_dto import SendRemindersResponseDTO
from openapi_server.models.url_result_dto import UrlResultDTO


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_create1(client):
    """Test case for create1

    Creates a new invoice.
    """
    body = /home-api/assets/examples/accounting/customers/invoices/createMultipleFromTasks.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/customers/invoices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_create_payment(client):
    """Test case for create_payment

    Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated.
    """
    body = /home-api/assets/examples/accounting/customers/invoices/createPayment.json#requestBody
    headers = { 
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/customers/invoices/{invoice_id}/payments'.format(invoice_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete1(client):
    """Test case for delete1

    Removes a client invoice.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/accounting/customers/invoices/{invoice_id}'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete2(client):
    """Test case for delete2

    Removes a customer payment.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/accounting/customers/payments/{payment_id}'.format(payment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_download_documents(client):
    """Test case for download_documents

    Generates client invoices' documents.
    """
    body = /home-api/assets/examples/accounting/customers/invoices/downloadDocuments.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/customers/invoices/documents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_duplicate(client):
    """Test case for duplicate

    Duplicate client invoice.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/customers/invoices/{invoice_id}/duplicate'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_duplicate_as_pro_forma(client):
    """Test case for duplicate_as_pro_forma

    Duplicate client invoice as pro forma.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/customers/invoices/{invoice_id}/duplicate/proForma'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all(client):
    """Test case for get_all

    Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date.
    """
    params = [('updatedSince', 56)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/customers/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_ids(client):
    """Test case for get_all_ids

    Returns client invoices' internal identifiers.
    """
    params = [('updatedSince', 56)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/customers/invoices/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id(client):
    """Test case for get_by_id

    Returns client invoice details.
    """
    params = [('embed', 'embed_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/customers/invoices/{invoice_id}'.format(invoice_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dates(client):
    """Test case for get_dates

    Returns dates of a given client invoice.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/customers/invoices/{invoice_id}/dates'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document(client):
    """Test case for get_document

    Generates client invoice document (PDF).
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/customers/invoices/{invoice_id}/document'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_terms(client):
    """Test case for get_payment_terms

    Returns payment terms of a given client invoice.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/customers/invoices/{invoice_id}/paymentTerms'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payments(client):
    """Test case for get_payments

    Returns all payments for the client invoice.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/accounting/customers/invoices/{invoice_id}/payments'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_reminder(client):
    """Test case for send_reminder

    Sends reminder.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/customers/invoices/{invoice_id}/sendReminder'.format(invoice_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_send_reminders(client):
    """Test case for send_reminders

    Sends reminders. Returns number of sent e-mails.
    """
    body = /home-api/assets/examples/accounting/customers/invoices/sendReminders.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/accounting/customers/invoices/sendReminders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

