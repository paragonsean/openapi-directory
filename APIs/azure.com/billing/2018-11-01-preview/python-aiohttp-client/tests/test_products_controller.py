# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.product_summary import ProductSummary
from openapi_server.models.products_list_result import ProductsListResult
from openapi_server.models.transfer_product_request_properties import TransferProductRequestProperties
from openapi_server.models.update_auto_renew_operation_summary import UpdateAutoRenewOperationSummary
from openapi_server.models.update_auto_renew_request import UpdateAutoRenewRequest


pytestmark = pytest.mark.asyncio

async def test_products_get(client):
    """Test case for products_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/products/{product_name}'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example', product_name='product_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_list_by_billing_account_name(client):
    """Test case for products_list_by_billing_account_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/products'.format(billing_account_name='billing_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_list_by_invoice_section_name(client):
    """Test case for products_list_by_invoice_section_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/products'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_transfer(client):
    """Test case for products_transfer

    
    """
    parameters = {"destinationInvoiceSectionId":"destinationInvoiceSectionId","destinationBillingProfileId":"destinationBillingProfileId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/products/{product_name}/transfer'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example', product_name='product_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_update_auto_renew_by_billing_account_name(client):
    """Test case for products_update_auto_renew_by_billing_account_name

    
    """
    body = {"autoRenew":"true"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/products/{product_name}/updateAutoRenew'.format(billing_account_name='billing_account_name_example', product_name='product_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_update_auto_renew_by_invoice_section_name(client):
    """Test case for products_update_auto_renew_by_invoice_section_name

    
    """
    body = {"autoRenew":"true"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/products/{product_name}/updateAutoRenew'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example', product_name='product_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

