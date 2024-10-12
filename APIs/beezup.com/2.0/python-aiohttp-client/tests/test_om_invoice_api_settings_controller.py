# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.get_order_invoice_design_preview_response import GetOrderInvoiceDesignPreviewResponse
from openapi_server.models.get_order_invoice_general_settings_response import GetOrderInvoiceGeneralSettingsResponse
from openapi_server.models.order_invoice_design_settings import OrderInvoiceDesignSettings
from openapi_server.models.order_invoice_general_settings import OrderInvoiceGeneralSettings


pytestmark = pytest.mark.asyncio

async def test_get_order_invoice_design_settings(client):
    """Test case for get_order_invoice_design_settings

    Get Order Invoice design settings
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/invoices/settings/design',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_invoice_design_settings_preview(client):
    """Test case for get_order_invoice_design_settings_preview

    View a preview an Order Invoice using custom design settings
    """
    body = openapi_server.OrderInvoiceDesignSettings()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_encoding': ['accept_encoding_example'],
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/invoices/settings/design/preview',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order_invoice_general_settings(client):
    """Test case for get_order_invoice_general_settings

    Get Order Invoice general settings
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/invoices/settings/general',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_order_invoice_design_settings(client):
    """Test case for save_order_invoice_design_settings

    Save Order Invoice design settings
    """
    body = openapi_server.OrderInvoiceDesignSettings()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/marketplaces/orders/invoices/settings/design',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_order_invoice_general_settings(client):
    """Test case for save_order_invoice_general_settings

    Save Order Invoice general settings
    """
    body = openapi_server.OrderInvoiceGeneralSettings()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/marketplaces/orders/invoices/settings/general',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

