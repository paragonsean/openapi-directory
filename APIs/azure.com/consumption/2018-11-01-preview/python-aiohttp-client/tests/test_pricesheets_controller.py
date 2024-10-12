# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.pricesheet_download_response import PricesheetDownloadResponse


pytestmark = pytest.mark.asyncio

async def test_billing_profile_pricesheet_download(client):
    """Test case for billing_profile_pricesheet_download

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Consumption/billingAccounts/{billing_account_id}/billingProfiles/{billing_profile_id}/pricesheet/default/download'.format(billing_account_id='billing_account_id_example', billing_profile_id='billing_profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_pricesheet_download(client):
    """Test case for invoice_pricesheet_download

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Consumption/billingAccounts/{billing_account_id}/invoices/{invoice_name}/pricesheet/default/download'.format(billing_account_id='billing_account_id_example', invoice_name='invoice_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

