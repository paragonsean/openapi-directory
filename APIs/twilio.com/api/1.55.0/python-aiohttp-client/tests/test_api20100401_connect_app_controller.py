# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_connect_app import ApiV2010AccountConnectApp
from openapi_server.models.connect_app_enum_permission import ConnectAppEnumPermission
from openapi_server.models.list_connect_app_response import ListConnectAppResponse


pytestmark = pytest.mark.asyncio

async def test_delete_connect_app(client):
    """Test case for delete_connect_app

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_connect_app(client):
    """Test case for fetch_connect_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_connect_app(client):
    """Test case for list_connect_app

    
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
        path='/2010-04-01/Accounts/{account_sid}/ConnectApps.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_connect_app(client):
    """Test case for update_connect_app

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'authorize_redirect_url': 'authorize_redirect_url_example',
        'company_name': 'company_name_example',
        'deauthorize_callback_method': 'deauthorize_callback_method_example',
        'deauthorize_callback_url': 'deauthorize_callback_url_example',
        'description': 'description_example',
        'friendly_name': 'friendly_name_example',
        'homepage_url': 'homepage_url_example',
        'permissions': [openapi_server.ConnectAppEnumPermission()]
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/ConnectApps/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

