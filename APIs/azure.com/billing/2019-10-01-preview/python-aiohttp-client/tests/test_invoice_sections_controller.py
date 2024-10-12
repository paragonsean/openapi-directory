# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.invoice_section import InvoiceSection
from openapi_server.models.invoice_section_creation_request import InvoiceSectionCreationRequest
from openapi_server.models.invoice_section_list_result import InvoiceSectionListResult


pytestmark = pytest.mark.asyncio

async def test_invoice_sections_create(client):
    """Test case for invoice_sections_create

    
    """
    parameters = {"displayName":"displayName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_sections_elevate_to_billing_profile(client):
    """Test case for invoice_sections_elevate_to_billing_profile

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}/elevate'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_sections_get(client):
    """Test case for invoice_sections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_sections_list_by_billing_profile(client):
    """Test case for invoice_sections_list_by_billing_profile

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_sections_update(client):
    """Test case for invoice_sections_update

    
    """
    parameters = {"properties":{"displayName":"displayName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoiceSections/{invoice_section_name}'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

