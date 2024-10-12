# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_detail import AccountDetail
from openapi_server.models.asset_type import AssetType
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_account import CreateAccount


pytestmark = pytest.mark.asyncio

async def test_create_account(client):
    """Test case for create_account

    Create a new account
    """
    body = {"ftp_password":"ftp_password","identifier":"identifier","servicepack_id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    Get a specific account
    """
    params = [('account_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/accounts/{account_id}'.format(account_id2='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_accounts(client):
    """Test case for get_accounts

    Overview of accounts
    """
    params = [('skip', 56),
                    ('take', 56),
                    ('asset_type', openapi_server.AssetType()),
                    ('identifier', 'identifier_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

