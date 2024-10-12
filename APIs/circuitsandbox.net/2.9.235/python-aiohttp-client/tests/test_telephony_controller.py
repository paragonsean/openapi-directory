# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conversation_item import ConversationItem
from openapi_server.models.v2_distributed_client_info import V2DistributedClientInfo


pytestmark = pytest.mark.asyncio

async def test_get_journal_entries(client):
    """Test case for get_journal_entries

    Get journal
    """
    params = [('timestamp', 0),
                    ('numberOfEntries', 25),
                    ('direction', AFTER),
                    ('journalFilter', ALL)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/telephony/{telephony_conversation_id}/journal'.format(telephony_conversation_id='telephony_conversation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_get_device_infos(client):
    """Test case for v2_get_device_infos

    Get devices infos
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/telephony/deviceInfos',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_get_telephony_conversation_id(client):
    """Test case for v2_get_telephony_conversation_id

    Get telephony conversation id
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/telephony/telephonyConversationId',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

