# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_holder import AccountHolder
from openapi_server.models.account_holder_info import AccountHolderInfo
from openapi_server.models.paginated_balance_accounts_response import PaginatedBalanceAccountsResponse
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_get_account_holders_id(client):
    """Test case for get_account_holders_id

    Get an account holder
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/accountHolders/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_holders_id_balance_accounts(client):
    """Test case for get_account_holders_id_balance_accounts

    Get all balance accounts of an account holder
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/accountHolders/{id}/balanceAccounts'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_account_holders_id(client):
    """Test case for patch_account_holders_id

    Update an account holder
    """
    body = {"reference":"reference","capabilities":{"key":{"requested":True,"verificationStatus":"invalid","allowed":True,"allowedSettings":{"paths":[{"content":["content","content"]},{"content":["content","content"]}],"rootPath":{"content":["content","content"]}},"allowedLevel":"high","requestedLevel":"high","requestedSettings":{"paths":[{"content":["content","content"]},{"content":["content","content"]}],"rootPath":{"content":["content","content"]}},"transferInstruments":[{"requested":True,"verificationStatus":"invalid","allowed":True,"allowedLevel":"high","id":"id","requestedLevel":"high","enabled":True},{"requested":True,"verificationStatus":"invalid","allowed":True,"allowedLevel":"high","id":"id","requestedLevel":"high","enabled":True}],"enabled":True,"problems":[null,null]}},"legalEntityId":"legalEntityId","description":"description","timeZone":"timeZone","id":"id","primaryBalanceAccount":"primaryBalanceAccount","contactDetails":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phone":{"number":"number","type":"Landline"},"webAddress":"webAddress","email":"email"},"balancePlatform":"balancePlatform","status":"Active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/bcl/v1/accountHolders/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_account_holders(client):
    """Test case for post_account_holders

    Create an account holder
    """
    body = {"reference":"reference","capabilities":{"key":{"requested":True,"verificationStatus":"invalid","allowed":True,"allowedSettings":{"paths":[{"content":["content","content"]},{"content":["content","content"]}],"rootPath":{"content":["content","content"]}},"allowedLevel":"high","requestedLevel":"high","requestedSettings":{"paths":[{"content":["content","content"]},{"content":["content","content"]}],"rootPath":{"content":["content","content"]}},"transferInstruments":[{"requested":True,"verificationStatus":"invalid","allowed":True,"allowedLevel":"high","id":"id","requestedLevel":"high","enabled":True},{"requested":True,"verificationStatus":"invalid","allowed":True,"allowedLevel":"high","id":"id","requestedLevel":"high","enabled":True}],"enabled":True,"problems":[null,null]}},"legalEntityId":"legalEntityId","description":"description","timeZone":"timeZone","contactDetails":{"address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","houseNumberOrName":"houseNumberOrName","street":"street","postalCode":"postalCode"},"phone":{"number":"number","type":"Landline"},"webAddress":"webAddress","email":"email"},"balancePlatform":"balancePlatform"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bcl/v1/accountHolders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

