# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_order_notes_request import AddOrderNotesRequest
from openapi_server.models.add_order_notes_response import AddOrderNotesResponse
from openapi_server.models.get_order_notes_response import GetOrderNotesResponse


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_marketplacenotes_insert(client):
    """Test case for adexchangebuyer_marketplacenotes_insert

    
    """
    body = {"notes":[{"note":"note","proposalRevisionNumber":"proposalRevisionNumber","creatorRole":"creatorRole","dealId":"dealId","kind":"adexchangebuyer#marketplaceNote","noteId":"noteId","proposalId":"proposalId","timestampMs":"timestampMs"},{"note":"note","proposalRevisionNumber":"proposalRevisionNumber","creatorRole":"creatorRole","dealId":"dealId","kind":"adexchangebuyer#marketplaceNote","noteId":"noteId","proposalId":"proposalId","timestampMs":"timestampMs"}]}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adexchangebuyer/v1.4/proposals/{proposal_id}/notes/insert'.format(proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_marketplacenotes_list(client):
    """Test case for adexchangebuyer_marketplacenotes_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('pqlQuery', 'pql_query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.4/proposals/{proposal_id}/notes'.format(proposal_id='proposal_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

