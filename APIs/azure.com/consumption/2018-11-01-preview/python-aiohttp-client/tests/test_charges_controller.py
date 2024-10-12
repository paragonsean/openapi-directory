# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.charges_list_by_billing_account import ChargesListByBillingAccount
from openapi_server.models.charges_list_by_billing_profile import ChargesListByBillingProfile
from openapi_server.models.charges_list_by_invoice_section import ChargesListByInvoiceSection
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_charges_by_billing_account_list(client):
    """Test case for charges_by_billing_account_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('$apply', 'apply_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.Consumption/charges'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charges_by_billing_profile_list(client):
    """Test case for charges_by_billing_profile_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/billingProfiles/{billing_profile_id}/providers/Microsoft.Consumption/charges'.format(billing_account_id='billing_account_id_example', billing_profile_id='billing_profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_charges_by_invoice_section_list(client):
    """Test case for charges_by_invoice_section_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('$apply', 'apply_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/invoiceSections/{invoice_section_id}/providers/Microsoft.Consumption/charges'.format(billing_account_id='billing_account_id_example', invoice_section_id='invoice_section_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

