# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_invoice_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_invoice import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice


pytestmark = pytest.mark.asyncio

async def test_order_api_create_invoice_0(client):
    """Test case for order_api_create_invoice_0

    Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.
    """
    params = [('includeInvoicePdf', True),
                    ('templateId', 56),
                    ('sendToCloudId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/orders/CreateInvoice/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_api_get_invoice_list_0(client):
    """Test case for order_api_get_invoice_list_0

    Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate
    """
    params = [('minInvoiceDate', '2013-10-20T19:20:30+01:00'),
                    ('maxInvoiceDate', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('pageSize', 56),
                    ('shopId', [56]),
                    ('orderStateId', [56]),
                    ('tag', ['tag_example']),
                    ('minPayDate', '2013-10-20T19:20:30+01:00'),
                    ('maxPayDate', '2013-10-20T19:20:30+01:00'),
                    ('includePositions', True),
                    ('excludeTags', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/orders/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

