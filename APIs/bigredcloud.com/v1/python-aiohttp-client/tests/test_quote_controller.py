# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_quote_dto import BatchItemQuoteDto
from openapi_server.models.page_result_quote_dto import PageResultQuoteDto
from openapi_server.models.quote_dto import QuoteDto
from openapi_server.models.quote_generating_invoice_dto import QuoteGeneratingInvoiceDto


pytestmark = pytest.mark.asyncio

async def test_quote_close(client):
    """Test case for quote_close

    Close a Quote.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/quotes/close/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_delete(client):
    """Test case for quote_delete

    Removes an existing Quote.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/quotes/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_get(client):
    """Test case for quote_get

    Returns a list of company's Quotes.  Filtering is forbidden.  Ordering is allowed by \"id\".
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/quotes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_post(client):
    """Test case for quote_post

    Creates a new Quote.
    """
    body = {"comments":"Sample","companyId":40449,"customerOwnerId":70583,"customerOwnerName":"Customer 1","ddNumber":"Sample","entryDate":"2017-01-01T00:00:00","id":1,"layoutType":1,"poNumber":"Sample","procDate":"2017-01-05T00:00:00","productTrans":[{"acEntries":[{"accountCode":"sample","analysisCategoryId":40888,"companyId":40449,"id":1,"quoteProductTranId":40277,"value":100}],"amount":10,"companyId":40449,"id":40277,"percentage":0,"productCode":"PRO1","productId":20107,"quantity":1,"tranNotes":["Product"],"unitPrice":100,"vatAmount":10,"vatAnalysisTypeId":0,"vatRateId":30657}],"saleInvoiceId":30044,"saleRepId":75783,"timeStamp":"kWjsu9RD2wg=","total":110,"totalNet":100,"totalVat":10,"vatTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/quotes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_post_create_quote_with_generating_reference(client):
    """Test case for quote_post_create_quote_with_generating_reference

    Creates a new Quote with auto generating reference.
    """
    body = {"comments":"Sample","companyId":40449,"customerOwnerId":70583,"customerOwnerName":"Customer 1","ddNumber":"Sample","entryDate":"2017-01-01T00:00:00","id":1,"layoutType":1,"poNumber":"Sample","procDate":"2017-01-05T00:00:00","productTrans":[{"acEntries":[{"accountCode":"sample","analysisCategoryId":40888,"companyId":40449,"id":1,"quoteProductTranId":40277,"value":100}],"amount":10,"companyId":40449,"id":40277,"percentage":0,"productCode":"PRO1","productId":20107,"quantity":1,"tranNotes":["Product"],"unitPrice":100,"vatAmount":10,"vatAnalysisTypeId":0,"vatRateId":30657}],"saleInvoiceId":30044,"saleRepId":75783,"timeStamp":"kWjsu9RD2wg=","total":110,"totalNet":100,"totalVat":10,"vatTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/quotes/createQuoteWithGeneratingReference',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_post_generate_sale_invoice(client):
    """Test case for quote_post_generate_sale_invoice

    Generate a sale invoice from a Quote.  When sale invoice is empty, new sale invoice will be generated from Quote.
    """
    body = {"saleInvoice":{"acCode":"CUS3","bookTranTypeId":7,"customFields":[{"description":"acudf_1","id":1,"userDefinedFieldId":1,"value":"acudfv_1"},{"description":"acudf_2","id":2,"userDefinedFieldId":1,"value":"acudfv_2"}],"customerId":70585,"deliveryTo":["dt_1","dt_2"],"details":"detail_1","entryDate":"2016-06-01T00:00:00","id":75813,"loType":"1","note":"Customer 3","ourReference":"ddNumber_1","procDate":"2016-06-24T00:00:00","productTrans":[{"acEntries":[{"accountCode":"SA02","analysisCategoryId":40889,"description":"AnCat1","id":73455,"value":-200}],"amount":-220,"amountNet":-200,"id":51820,"percentage":10,"productCode":"PRO2","productId":20108,"quantity":-1,"tranNotes":["tn_1","tn_2"],"unitPrice":200,"vat":-20,"vatAnalysisTypeId":0,"vatRateId":30657}],"saleRepId":33110,"timestamp":"EQUJvNRD2wg=","total":-220,"totalNet":-200,"totalVAT":-20,"unpaid":-220,"vatTypeId":1,"yourReference":"poNumber_1"},"quoteId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/quotes/generateSaleInvoice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_process_batch(client):
    """Test case for quote_process_batch

    Processes a batch of Quote.
    """
    body = [openapi_server.BatchItemQuoteDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/quotes/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_put(client):
    """Test case for quote_put

    Updates an existing Quote.
    """
    body = {"comments":"Sample","companyId":40449,"customerOwnerId":70583,"customerOwnerName":"Customer 1","ddNumber":"Sample","entryDate":"2017-01-01T00:00:00","id":1,"layoutType":1,"poNumber":"Sample","procDate":"2017-01-05T00:00:00","productTrans":[{"acEntries":[{"accountCode":"sample","analysisCategoryId":40888,"companyId":40449,"id":1,"quoteProductTranId":40277,"value":100}],"amount":10,"companyId":40449,"id":40277,"percentage":0,"productCode":"PRO1","productId":20107,"quantity":1,"tranNotes":["Product"],"unitPrice":100,"vatAmount":10,"vatAnalysisTypeId":0,"vatRateId":30657}],"saleInvoiceId":30044,"saleRepId":75783,"timeStamp":"kWjsu9RD2wg=","total":110,"totalNet":100,"totalVat":10,"vatTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/quotes/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_reopen(client):
    """Test case for quote_reopen

    Reopen a Quote.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/quotes/reopen/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_quotes_id_get(client):
    """Test case for v1_quotes_id_get

    Returns information about a single Quote.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/quotes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

