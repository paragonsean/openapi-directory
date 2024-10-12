# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_recording_recording_add_on_result_recording_add_on_result_payload import ApiV2010AccountRecordingRecordingAddOnResultRecordingAddOnResultPayload
from openapi_server.models.list_recording_add_on_result_payload_response import ListRecordingAddOnResultPayloadResponse


pytestmark = pytest.mark.asyncio

async def test_delete_recording_add_on_result_payload(client):
    """Test case for delete_recording_add_on_result_payload

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid_jso}'.format(account_sid='account_sid_example', reference_sid='reference_sid_example', add_on_result_sid='add_on_result_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_recording_add_on_result_payload(client):
    """Test case for fetch_recording_add_on_result_payload

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid_jso}'.format(account_sid='account_sid_example', reference_sid='reference_sid_example', add_on_result_sid='add_on_result_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_recording_add_on_result_payload(client):
    """Test case for list_recording_add_on_result_payload

    
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
        path='/2010-04-01/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads.json'.format(account_sid='account_sid_example', reference_sid='reference_sid_example', add_on_result_sid='add_on_result_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

