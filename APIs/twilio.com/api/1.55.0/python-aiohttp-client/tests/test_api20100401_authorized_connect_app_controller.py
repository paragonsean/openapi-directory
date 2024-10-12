# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_authorized_connect_app import ApiV2010AccountAuthorizedConnectApp
from openapi_server.models.list_authorized_connect_app_response import ListAuthorizedConnectAppResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_authorized_connect_app(client):
    """Test case for fetch_authorized_connect_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/AuthorizedConnectApps/{connect_app_sid_jso}'.format(account_sid='account_sid_example', connect_app_sid='connect_app_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_authorized_connect_app(client):
    """Test case for list_authorized_connect_app

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/AuthorizedConnectApps.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

