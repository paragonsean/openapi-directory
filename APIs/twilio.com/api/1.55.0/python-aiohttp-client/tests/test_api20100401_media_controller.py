# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_message_media import ApiV2010AccountMessageMedia
from openapi_server.models.list_media_response import ListMediaResponse


pytestmark = pytest.mark.asyncio

async def test_delete_media(client):
    """Test case for delete_media

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid_jso}'.format(account_sid='account_sid_example', message_sid='message_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_media(client):
    """Test case for fetch_media

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid_jso}'.format(account_sid='account_sid_example', message_sid='message_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_media(client):
    """Test case for list_media

    
    """
    params = [('DateCreated', '2013-10-20T19:20:30+01:00'),
                    ('DateCreated&lt;', '2013-10-20T19:20:30+01:00'),
                    ('DateCreated&gt;', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}/Media.json'.format(account_sid='account_sid_example', message_sid='message_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

