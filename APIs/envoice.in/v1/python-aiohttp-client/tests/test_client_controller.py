# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_create_api_model import ClientCreateApiModel
from openapi_server.models.client_delete_api_model import ClientDeleteApiModel
from openapi_server.models.client_details_api_model import ClientDetailsApiModel
from openapi_server.models.client_update_api_model import ClientUpdateApiModel


pytestmark = pytest.mark.asyncio

async def test_client_api_all(client):
    """Test case for client_api_all

    Return all clients for the account
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/client/all',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_api_can_delete(client):
    """Test case for client_api_can_delete

    Check if the provided client can be deleted
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/client/candelete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_client_api_delete(client):
    """Test case for client_api_delete

    Delete an existing client
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/client/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_api_details(client):
    """Test case for client_api_details

    Return client details. Activities and invoices included.
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/client/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_client_api_new(client):
    """Test case for client_api_new

    Create a client
    """
    body = {"UiLanguageId":5,"Email":"Email","AdditionalEmails":[{"Email":"Email"},{"Email":"Email"}],"Address":"Address","ClientCurrencyId":6,"Vat":"Vat","ClientCountryId":0,"DefaultDueDateInDays":1,"PhoneNumber":"PhoneNumber","CompanyRegistrationNumber":"CompanyRegistrationNumber","Name":"Name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/client/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_client_api_update(client):
    """Test case for client_api_update

    Update an existing client
    """
    body = {"UiLanguageId":5,"Email":"Email","AdditionalEmails":[{"Email":"Email"},{"Email":"Email"}],"Address":"Address","ClientCurrencyId":6,"Vat":"Vat","ClientCountryId":0,"DefaultDueDateInDays":1,"PhoneNumber":"PhoneNumber","Id":5,"CompanyRegistrationNumber":"CompanyRegistrationNumber","Name":"Name"}
    headers = { 
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/client/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

