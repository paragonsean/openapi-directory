# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_queue_member import ApiV2010AccountQueueMember
from openapi_server.models.list_member_response import ListMemberResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_member(client):
    """Test case for fetch_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid_jso}'.format(account_sid='account_sid_example', queue_sid='queue_sid_example', call_sid='call_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_member(client):
    """Test case for list_member

    
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
        path='/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members.json'.format(account_sid='account_sid_example', queue_sid='queue_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_member(client):
    """Test case for update_member

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'method': 'method_example',
        'url': 'url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid_jso}'.format(account_sid='account_sid_example', queue_sid='queue_sid_example', call_sid='call_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

