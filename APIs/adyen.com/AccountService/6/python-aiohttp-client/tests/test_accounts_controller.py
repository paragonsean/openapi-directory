# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.close_account_request import CloseAccountRequest
from openapi_server.models.close_account_response import CloseAccountResponse
from openapi_server.models.create_account_request import CreateAccountRequest
from openapi_server.models.create_account_response import CreateAccountResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.update_account_request import UpdateAccountRequest
from openapi_server.models.update_account_response import UpdateAccountResponse


pytestmark = pytest.mark.asyncio

async def test_post_close_account(client):
    """Test case for post_close_account

    Close an account
    """
    body = {"accountCode":"accountCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v6/closeAccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_create_account(client):
    """Test case for post_create_account

    Create an account
    """
    body = {"accountHolderCode":"accountHolderCode","metadata":{"key":"metadata"},"bankAccountUUID":"bankAccountUUID","payoutMethodCode":"payoutMethodCode","description":"description","payoutScheduleReason":"payoutScheduleReason","payoutSchedule":"BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT","payoutSpeed":"STANDARD"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v6/createAccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_update_account(client):
    """Test case for post_update_account

    Update an account
    """
    body = {"accountCode":"accountCode","metadata":{"key":"metadata"},"bankAccountUUID":"bankAccountUUID","payoutMethodCode":"payoutMethodCode","description":"description","payoutSchedule":{"reason":"reason","schedule":"BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT","action":"CLOSE"},"payoutSpeed":"INSTANT"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Account/v6/updateAccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

