# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.initiate_transfer_request import InitiateTransferRequest
from openapi_server.models.transfer_details import TransferDetails
from openapi_server.models.transfer_details_list_result import TransferDetailsListResult


pytestmark = pytest.mark.asyncio

async def test_transfers_cancel(client):
    """Test case for transfers_cancel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/transfers/{transfer_name}'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example', transfer_name='transfer_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfers_get(client):
    """Test case for transfers_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/transfers/{transfer_name}'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example', transfer_name='transfer_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfers_initiate(client):
    """Test case for transfers_initiate

    
    """
    body = {"properties":{"recipientEmailId":"recipientEmailId","billingProfileId":"billingProfileId"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/initiateTransfer'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transfers_list(client):
    """Test case for transfers_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_name}/invoiceSections/{invoice_section_name}/transfers'.format(billing_account_name='billing_account_name_example', invoice_section_name='invoice_section_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

