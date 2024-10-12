# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.download_url import DownloadUrl
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_price_sheet_download(client):
    """Test case for price_sheet_download

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/invoices/{invoice_name}/pricesheet/default/download'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example', invoice_name='invoice_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_price_sheet_download_by_billing_profile(client):
    """Test case for price_sheet_download_by_billing_profile

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/billingProfiles/{billing_profile_name}/pricesheet/default/download'.format(billing_account_name='billing_account_name_example', billing_profile_name='billing_profile_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

