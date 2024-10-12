# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_messenger_account400_response import CreateMessengerAccount400Response
from openapi_server.models.create_messenger_account_request import CreateMessengerAccountRequest
from openapi_server.models.messenger_account_response import MessengerAccountResponse
from openapi_server.models.model401_response import Model401Response
from openapi_server.models.model403_response import Model403Response
from openapi_server.models.update_messenger_account200_response import UpdateMessengerAccount200Response
from openapi_server.models.update_messenger_account400_response import UpdateMessengerAccount400Response
from openapi_server.models.update_messenger_account_request import UpdateMessengerAccountRequest


pytestmark = pytest.mark.asyncio

async def test_create_messenger_account(client):
    """Test case for create_messenger_account

    Create a Messenger account
    """
    body = openapi_server.CreateMessengerAccountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/beta/chatapp-accounts/messenger',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_messenger_account(client):
    """Test case for delete_messenger_account

    Delete a Messenger account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/beta/chatapp-accounts/messenger/{external_id}'.format(external_id='external_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_messenger_account(client):
    """Test case for get_messenger_account

    Retrieve a Messenger account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/beta/chatapp-accounts/messenger/{external_id}'.format(external_id='external_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_messenger_account(client):
    """Test case for update_messenger_account

    Update a Messenger account
    """
    body = openapi_server.UpdateMessengerAccountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/beta/chatapp-accounts/messenger/{external_id}'.format(external_id='external_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

