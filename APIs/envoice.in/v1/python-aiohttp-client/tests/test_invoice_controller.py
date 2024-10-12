# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_status_api_model import ChangeStatusApiModel
from openapi_server.models.invoice_category_api_model import InvoiceCategoryApiModel
from openapi_server.models.invoice_category_create_api_model import InvoiceCategoryCreateApiModel
from openapi_server.models.invoice_category_delete_api_model import InvoiceCategoryDeleteApiModel
from openapi_server.models.invoice_category_update_api_model import InvoiceCategoryUpdateApiModel
from openapi_server.models.invoice_create_api_model import InvoiceCreateApiModel
from openapi_server.models.invoice_delete_api_model import InvoiceDeleteApiModel
from openapi_server.models.invoice_full_details_api_model import InvoiceFullDetailsApiModel
from openapi_server.models.invoice_update_api_model import InvoiceUpdateApiModel
from openapi_server.models.invoice_uri_api_model import InvoiceUriApiModel
from openapi_server.models.list_result_invoice_category_api_model import ListResultInvoiceCategoryApiModel
from openapi_server.models.list_result_invoice_details_api_model import ListResultInvoiceDetailsApiModel
from openapi_server.models.send_invoice_to_accountant_api_model import SendInvoiceToAccountantApiModel
from openapi_server.models.send_invoice_to_client_api_model import SendInvoiceToClientApiModel


pytestmark = pytest.mark.asyncio

async def test_api_invoice_allcategories_get(client):
    """Test case for api_invoice_allcategories_get

    Return all invoice categories for the account
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/invoice/allcategories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_invoice_deletecategory_post(client):
    """Test case for api_invoice_deletecategory_post

    Delete an existing invoice category
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/deletecategory',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_invoice_newcategory_post(client):
    """Test case for api_invoice_newcategory_post

    Create an invoice category
    """
    body = {"Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/newcategory',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_api_invoice_updatecategory_post(client):
    """Test case for api_invoice_updatecategory_post

    Update an existing invoice category
    """
    body = {"Id":0,"Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/updatecategory',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_api_all(client):
    """Test case for invoice_api_all

    Return all invoices for the account
    """
    params = [('queryOptions.page', 56),
                    ('queryOptions.pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/invoice/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_invoice_api_change_status(client):
    """Test case for invoice_api_change_status

    Change invoice status
    """
    body = {"Status":"Draft","Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/changestatus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_invoice_api_delete(client):
    """Test case for invoice_api_delete

    Delete an existing invoice
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_api_details(client):
    """Test case for invoice_api_details

    Return invoice data
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/invoice/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_invoice_api_new(client):
    """Test case for invoice_api_new

    Create an invoice
    """
    body = {"Status":"Draft","ClonedFromId":1,"ShouldSendReminders":True,"PoNumber":"PoNumber","RecurringProfile":{"Status":"Pending","DayOfWeek":"Sunday","Month":6,"EndOfRecurrance":"2000-01-23T04:56:07.000+00:00","RecurranceValue":8,"DayOfMonth":9,"DueDateInDays":9,"Title":"Title","RecurrancePattern":"Daily","StartOfRecurrance":"2000-01-23T04:56:07.000+00:00"},"Terms":"Terms","InvoiceCategoryId":5,"Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":5,"Duedate":"2000-01-23T04:56:07.000+00:00","Number":"Number","IssuedOn":"2000-01-23T04:56:07.000+00:00","PaymentGateways":[{"Name":"Name"},{"Name":"Name"}],"RecurringProfileId":7,"ClientId":6,"Items":[{"WorkTypeId":4,"Description":"Description","DiscountPercentage":7.061401241503109,"TaxPercentage":2.027123023002322,"Quantity":9.301444243932576,"TaxId":3,"Cost":2.3021358869347655},{"WorkTypeId":4,"Description":"Description","DiscountPercentage":7.061401241503109,"TaxPercentage":2.027123023002322,"Quantity":9.301444243932576,"TaxId":3,"Cost":2.3021358869347655}],"Notes":"Notes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_api_pdf(client):
    """Test case for invoice_api_pdf

    Return the PDF for the invoice
    """
    params = [('id', 56),
                    ('signedVersion', True)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/invoice/pdf',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_invoice_api_send_to_accountant(client):
    """Test case for invoice_api_send_to_accountant

    Send the provided invoice to the accountant
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/sendtoaccountant',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_invoice_api_send_to_client(client):
    """Test case for invoice_api_send_to_client

    Send the provided invoice to the client
    """
    body = {"Message":"Message","SendToSelf":True,"AttachPdf":True,"Id":0,"InvoiceId":6,"Subject":"Subject"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/sendtoclient',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_api_status(client):
    """Test case for invoice_api_status

    Retrieve the status of the invoice
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/invoice/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_invoice_api_update(client):
    """Test case for invoice_api_update

    Update an existing invoice
    """
    body = {"Status":"Draft","ClonedFromId":5,"ShouldSendReminders":True,"PoNumber":"PoNumber","RecurringProfile":{"Status":"Pending","DayOfWeek":"Sunday","Month":6,"EndOfRecurrance":"2000-01-23T04:56:07.000+00:00","RecurranceValue":8,"DayOfMonth":9,"DueDateInDays":9,"Title":"Title","RecurrancePattern":"Daily","StartOfRecurrance":"2000-01-23T04:56:07.000+00:00"},"Terms":"Terms","InvoiceCategoryId":7,"Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":6,"Id":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":6,"Id":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":5,"Duedate":"2000-01-23T04:56:07.000+00:00","Number":"Number","IssuedOn":"2000-01-23T04:56:07.000+00:00","PaymentGateways":[{"Name":"Name"},{"Name":"Name"}],"RecurringProfileId":1,"ClientId":1,"Items":[{"WorkTypeId":1,"Description":"Description","DiscountPercentage":3.616076749251911,"TaxPercentage":1.2315135367772556,"Quantity":4.145608029883936,"Id":2,"TaxId":7,"Cost":9.301444243932576},{"WorkTypeId":1,"Description":"Description","DiscountPercentage":3.616076749251911,"TaxPercentage":1.2315135367772556,"Quantity":4.145608029883936,"Id":2,"TaxId":7,"Cost":9.301444243932576}],"Id":2,"Notes":"Notes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/invoice/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_api_uri(client):
    """Test case for invoice_api_uri

    Return the unique url to the client's invoice
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/invoice/uri',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

