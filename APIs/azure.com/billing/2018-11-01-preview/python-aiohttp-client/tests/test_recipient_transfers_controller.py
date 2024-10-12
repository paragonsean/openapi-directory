# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_transfer_request import AcceptTransferRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.recipient_transfer_details import RecipientTransferDetails
from openapi_server.models.recipient_transfer_details_list_result import RecipientTransferDetailsListResult


pytestmark = pytest.mark.asyncio

async def test_recipient_transfers_accept(client):
    """Test case for recipient_transfers_accept

    Accepts the transfer with given transfer Id.
    """
    body = {"properties":{"productDetails":[{"productId":"productId","productType":"AzureSubscription"},{"productId":"productId","productType":"AzureSubscription"}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/transfers/{transfer_name}/acceptTransfer'.format(transfer_name='transfer_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipient_transfers_decline(client):
    """Test case for recipient_transfers_decline

    Declines the transfer with given transfer Id.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Billing/transfers/{transfer_name}/declineTransfer'.format(transfer_name='transfer_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipient_transfers_get(client):
    """Test case for recipient_transfers_get

    Gets the transfer with given transfer Id.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/transfers/{transfer_name}'.format(transfer_name='transfer_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipient_transfers_list(client):
    """Test case for recipient_transfers_list

    Lists the transfers received by caller.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/transfers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

