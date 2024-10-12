# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_recipient_address200_response import AddRecipientAddress200Response
from openapi_server.models.add_recipient_address_request import AddRecipientAddressRequest
from openapi_server.models.delete_recipient200_response import DeleteRecipient200Response
from openapi_server.models.delete_recipient_request import DeleteRecipientRequest
from openapi_server.models.recipient_address import RecipientAddress
from openapi_server.models.recipients_list_request import RecipientsListRequest
from openapi_server.models.update_recipient_request import UpdateRecipientRequest


pytestmark = pytest.mark.asyncio

async def test_add_recipient_address(client):
    """Test case for add_recipient_address

    add a new recipient address
    """
    body = openapi_server.AddRecipientAddressRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/profile/profileAddRecipient',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_recipient(client):
    """Test case for delete_recipient

    deletes an existing recipient address
    """
    body = openapi_server.DeleteRecipientRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/profile/deleteRecipient',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recipients_list(client):
    """Test case for recipients_list

    list the addresses in the user's account
    """
    body = openapi_server.RecipientsListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/profile/recipientsList',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_recipient(client):
    """Test case for update_recipient

    updates an existing new recipient address
    """
    body = openapi_server.UpdateRecipientRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/profile/updateRecipient',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

