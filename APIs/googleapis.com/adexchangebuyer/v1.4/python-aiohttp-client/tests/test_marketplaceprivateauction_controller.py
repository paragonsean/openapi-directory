# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_private_auction_proposal_request import UpdatePrivateAuctionProposalRequest


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_marketplaceprivateauction_updateproposal(client):
    """Test case for adexchangebuyer_marketplaceprivateauction_updateproposal

    
    """
    body = {"updateAction":"updateAction","note":{"note":"note","proposalRevisionNumber":"proposalRevisionNumber","creatorRole":"creatorRole","dealId":"dealId","kind":"adexchangebuyer#marketplaceNote","noteId":"noteId","proposalId":"proposalId","timestampMs":"timestampMs"},"proposalRevisionNumber":"proposalRevisionNumber","externalDealId":"externalDealId"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adexchangebuyer/v1.4/privateauction/{private_auction_id}/updateproposal'.format(private_auction_id='private_auction_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

