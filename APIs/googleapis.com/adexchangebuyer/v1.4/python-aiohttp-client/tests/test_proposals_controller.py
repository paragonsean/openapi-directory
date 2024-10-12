# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_orders_request import CreateOrdersRequest
from openapi_server.models.create_orders_response import CreateOrdersResponse
from openapi_server.models.get_orders_response import GetOrdersResponse
from openapi_server.models.proposal import Proposal


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_proposals_get(client):
    """Test case for adexchangebuyer_proposals_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adexchangebuyer/v1.4/proposals/{proposal_id}'.format(proposal_id='proposal_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_proposals_insert(client):
    """Test case for adexchangebuyer_proposals_insert

    
    """
    body = {"webPropertyCode":"webPropertyCode","proposals":[{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"proposalState":"proposalState","revisionNumber":"revisionNumber","kind":"adexchangebuyer#proposal","hasSellerSignedOff":True,"sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"buyerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"proposalId":"proposalId","buyer":{"accountId":"accountId"},"labels":[{"accountId":"accountId","deprecatedMarketplaceDealParty":{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"buyer":{"accountId":"accountId"}},"label":"label","createTimeMs":"createTimeMs"},{"accountId":"accountId","deprecatedMarketplaceDealParty":{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"buyer":{"accountId":"accountId"}},"label":"label","createTimeMs":"createTimeMs"}],"billedBuyer":{"accountId":"accountId"},"lastUpdaterOrCommentorRole":"lastUpdaterOrCommentorRole","hasBuyerSignedOff":True,"originatorRole":"originatorRole","privateAuctionId":"privateAuctionId","name":"name","dbmAdvertiserIds":["dbmAdvertiserIds","dbmAdvertiserIds"],"isRenegotiating":True,"negotiationId":"negotiationId","revisionTimeMs":"revisionTimeMs","buyerPrivateData":{"referenceId":"referenceId","referencePayload":"referencePayload"},"inventorySource":"inventorySource","isSetupComplete":True},{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"proposalState":"proposalState","revisionNumber":"revisionNumber","kind":"adexchangebuyer#proposal","hasSellerSignedOff":True,"sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"buyerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"proposalId":"proposalId","buyer":{"accountId":"accountId"},"labels":[{"accountId":"accountId","deprecatedMarketplaceDealParty":{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"buyer":{"accountId":"accountId"}},"label":"label","createTimeMs":"createTimeMs"},{"accountId":"accountId","deprecatedMarketplaceDealParty":{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"buyer":{"accountId":"accountId"}},"label":"label","createTimeMs":"createTimeMs"}],"billedBuyer":{"accountId":"accountId"},"lastUpdaterOrCommentorRole":"lastUpdaterOrCommentorRole","hasBuyerSignedOff":True,"originatorRole":"originatorRole","privateAuctionId":"privateAuctionId","name":"name","dbmAdvertiserIds":["dbmAdvertiserIds","dbmAdvertiserIds"],"isRenegotiating":True,"negotiationId":"negotiationId","revisionTimeMs":"revisionTimeMs","buyerPrivateData":{"referenceId":"referenceId","referencePayload":"referencePayload"},"inventorySource":"inventorySource","isSetupComplete":True}]}
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
        path='/adexchangebuyer/v1.4/proposals/insert',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_proposals_patch(client):
    """Test case for adexchangebuyer_proposals_patch

    
    """
    body = {"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"proposalState":"proposalState","revisionNumber":"revisionNumber","kind":"adexchangebuyer#proposal","hasSellerSignedOff":True,"sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"buyerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"proposalId":"proposalId","buyer":{"accountId":"accountId"},"labels":[{"accountId":"accountId","deprecatedMarketplaceDealParty":{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"buyer":{"accountId":"accountId"}},"label":"label","createTimeMs":"createTimeMs"},{"accountId":"accountId","deprecatedMarketplaceDealParty":{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"buyer":{"accountId":"accountId"}},"label":"label","createTimeMs":"createTimeMs"}],"billedBuyer":{"accountId":"accountId"},"lastUpdaterOrCommentorRole":"lastUpdaterOrCommentorRole","hasBuyerSignedOff":True,"originatorRole":"originatorRole","privateAuctionId":"privateAuctionId","name":"name","dbmAdvertiserIds":["dbmAdvertiserIds","dbmAdvertiserIds"],"isRenegotiating":True,"negotiationId":"negotiationId","revisionTimeMs":"revisionTimeMs","buyerPrivateData":{"referenceId":"referenceId","referencePayload":"referencePayload"},"inventorySource":"inventorySource","isSetupComplete":True}
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
        method='PATCH',
        path='/adexchangebuyer/v1.4/proposals/{proposal_id}/{revision_number}/{update_action}'.format(proposal_id='proposal_id_example', revision_number='revision_number_example', update_action='update_action_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_proposals_search(client):
    """Test case for adexchangebuyer_proposals_search

    
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
        path='/adexchangebuyer/v1.4/proposals/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_proposals_setupcomplete(client):
    """Test case for adexchangebuyer_proposals_setupcomplete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/adexchangebuyer/v1.4/proposals/{proposal_id}/setupcomplete'.format(proposal_id='proposal_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer_proposals_update(client):
    """Test case for adexchangebuyer_proposals_update

    
    """
    body = {"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"proposalState":"proposalState","revisionNumber":"revisionNumber","kind":"adexchangebuyer#proposal","hasSellerSignedOff":True,"sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"buyerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"proposalId":"proposalId","buyer":{"accountId":"accountId"},"labels":[{"accountId":"accountId","deprecatedMarketplaceDealParty":{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"buyer":{"accountId":"accountId"}},"label":"label","createTimeMs":"createTimeMs"},{"accountId":"accountId","deprecatedMarketplaceDealParty":{"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"buyer":{"accountId":"accountId"}},"label":"label","createTimeMs":"createTimeMs"}],"billedBuyer":{"accountId":"accountId"},"lastUpdaterOrCommentorRole":"lastUpdaterOrCommentorRole","hasBuyerSignedOff":True,"originatorRole":"originatorRole","privateAuctionId":"privateAuctionId","name":"name","dbmAdvertiserIds":["dbmAdvertiserIds","dbmAdvertiserIds"],"isRenegotiating":True,"negotiationId":"negotiationId","revisionTimeMs":"revisionTimeMs","buyerPrivateData":{"referenceId":"referenceId","referencePayload":"referencePayload"},"inventorySource":"inventorySource","isSetupComplete":True}
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
        method='PUT',
        path='/adexchangebuyer/v1.4/proposals/{proposal_id}/{revision_number}/{update_action}'.format(proposal_id='proposal_id_example', revision_number='revision_number_example', update_action='update_action_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

