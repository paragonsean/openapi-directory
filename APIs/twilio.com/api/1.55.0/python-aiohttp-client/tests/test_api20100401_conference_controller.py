# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_conference import ApiV2010AccountConference
from openapi_server.models.conference_enum_status import ConferenceEnumStatus
from openapi_server.models.conference_enum_update_status import ConferenceEnumUpdateStatus
from openapi_server.models.list_conference_response import ListConferenceResponse


pytestmark = pytest.mark.asyncio

async def test_fetch_conference(client):
    """Test case for fetch_conference

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conference(client):
    """Test case for list_conference

    
    """
    params = [('DateCreated', '2013-10-20'),
                    ('DateCreated&lt;', '2013-10-20'),
                    ('DateCreated&gt;', '2013-10-20'),
                    ('DateUpdated', '2013-10-20'),
                    ('DateUpdated&lt;', '2013-10-20'),
                    ('DateUpdated&gt;', '2013-10-20'),
                    ('FriendlyName', 'friendly_name_example'),
                    ('Status', openapi_server.ConferenceEnumStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Conferences.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_conference(client):
    """Test case for update_conference

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'announce_method': 'announce_method_example',
        'announce_url': 'announce_url_example',
        'status': openapi_server.ConferenceEnumUpdateStatus()
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

