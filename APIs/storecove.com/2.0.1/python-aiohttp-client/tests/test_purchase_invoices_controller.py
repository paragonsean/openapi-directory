# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.purchase_invoice import PurchaseInvoice
from openapi_server.models.purchase_invoice_ubl import PurchaseInvoiceUbl


pytestmark = pytest.mark.asyncio

async def test_get_invoice_json(client):
    """Test case for get_invoice_json

    Get Purchase invoice data as JSON
    """
    params = [('pmv', '1.0')]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/purchase_invoices/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_ubl(client):
    """Test case for get_invoice_ubl

    Get Purchase invoice data in a selectable format
    """
    params = [('pmv', '1.0')]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/purchase_invoices/{guid}/{packaging}'.format(guid='guid_example', packaging=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_ubl_versioned(client):
    """Test case for get_invoice_ubl_versioned

    Get Purchase invoice data as JSON with a Base64-encoded UBL string in the specified version
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/purchase_invoices/{guid}/{packaging}/{package_version}'.format(guid='guid_example', packaging=ubl, package_version=si11),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

