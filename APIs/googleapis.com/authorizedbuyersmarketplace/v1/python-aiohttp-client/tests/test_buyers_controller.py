# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_proposal_request import AcceptProposalRequest
from openapi_server.models.add_creative_request import AddCreativeRequest
from openapi_server.models.add_note_request import AddNoteRequest
from openapi_server.models.auction_package import AuctionPackage
from openapi_server.models.batch_update_deals_request import BatchUpdateDealsRequest
from openapi_server.models.batch_update_deals_response import BatchUpdateDealsResponse
from openapi_server.models.client import Client
from openapi_server.models.client_user import ClientUser
from openapi_server.models.deal import Deal
from openapi_server.models.finalized_deal import FinalizedDeal
from openapi_server.models.list_auction_packages_response import ListAuctionPackagesResponse
from openapi_server.models.list_client_users_response import ListClientUsersResponse
from openapi_server.models.list_clients_response import ListClientsResponse
from openapi_server.models.list_deals_response import ListDealsResponse
from openapi_server.models.list_finalized_deals_response import ListFinalizedDealsResponse
from openapi_server.models.list_proposals_response import ListProposalsResponse
from openapi_server.models.list_publisher_profiles_response import ListPublisherProfilesResponse
from openapi_server.models.pause_finalized_deal_request import PauseFinalizedDealRequest
from openapi_server.models.proposal import Proposal
from openapi_server.models.publisher_profile import PublisherProfile
from openapi_server.models.send_rfp_request import SendRfpRequest
from openapi_server.models.subscribe_clients_request import SubscribeClientsRequest
from openapi_server.models.unsubscribe_clients_request import UnsubscribeClientsRequest


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_auction_packages_list(client):
    """Test case for authorizedbuyersmarketplace_buyers_auction_packages_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/auctionPackages'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_auction_packages_subscribe(client):
    """Test case for authorizedbuyersmarketplace_buyers_auction_packages_subscribe

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namesubscrib}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_auction_packages_subscribe_clients(client):
    """Test case for authorizedbuyersmarketplace_buyers_auction_packages_subscribe_clients

    
    """
    body = {"clients":["clients","clients"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{auction_packagesubscribe_client}'.format(auction_package='auction_package_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_auction_packages_unsubscribe(client):
    """Test case for authorizedbuyersmarketplace_buyers_auction_packages_unsubscribe

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameunsubscrib}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_auction_packages_unsubscribe_clients(client):
    """Test case for authorizedbuyersmarketplace_buyers_auction_packages_unsubscribe_clients

    
    """
    body = {"clients":["clients","clients"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{auction_packageunsubscribe_client}'.format(auction_package='auction_package_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_clients_create(client):
    """Test case for authorizedbuyersmarketplace_buyers_clients_create

    
    """
    body = {"role":"CLIENT_ROLE_UNSPECIFIED","displayName":"displayName","name":"name","partnerClientId":"partnerClientId","sellerVisible":True,"state":"STATE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/clients'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_clients_list(client):
    """Test case for authorizedbuyersmarketplace_buyers_clients_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/clients'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_clients_users_activate(client):
    """Test case for authorizedbuyersmarketplace_buyers_clients_users_activate

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameactivat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_clients_users_create(client):
    """Test case for authorizedbuyersmarketplace_buyers_clients_users_create

    
    """
    body = {"name":"name","state":"STATE_UNSPECIFIED","email":"email"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/users'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_clients_users_deactivate(client):
    """Test case for authorizedbuyersmarketplace_buyers_clients_users_deactivate

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namedeactivat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_clients_users_delete(client):
    """Test case for authorizedbuyersmarketplace_buyers_clients_users_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_clients_users_list(client):
    """Test case for authorizedbuyersmarketplace_buyers_clients_users_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/users'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_finalized_deals_add_creative(client):
    """Test case for authorizedbuyersmarketplace_buyers_finalized_deals_add_creative

    
    """
    body = {"creative":"creative"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{dealadd_creativ}'.format(deal='deal_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_finalized_deals_list(client):
    """Test case for authorizedbuyersmarketplace_buyers_finalized_deals_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/finalizedDeals'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_finalized_deals_pause(client):
    """Test case for authorizedbuyersmarketplace_buyers_finalized_deals_pause

    
    """
    body = {"reason":"reason"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namepaus}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_finalized_deals_resume(client):
    """Test case for authorizedbuyersmarketplace_buyers_finalized_deals_resume

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameresum}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_finalized_deals_set_ready_to_serve(client):
    """Test case for authorizedbuyersmarketplace_buyers_finalized_deals_set_ready_to_serve

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{dealset_ready_to_serv}'.format(deal='deal_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_proposals_accept(client):
    """Test case for authorizedbuyersmarketplace_buyers_proposals_accept

    
    """
    body = {"proposalRevision":"proposalRevision"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameaccep}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_proposals_add_note(client):
    """Test case for authorizedbuyersmarketplace_buyers_proposals_add_note

    
    """
    body = {"note":{"note":"note","creatorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","createTime":"createTime"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{proposaladd_not}'.format(proposal='proposal_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_proposals_cancel_negotiation(client):
    """Test case for authorizedbuyersmarketplace_buyers_proposals_cancel_negotiation

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{proposalcancel_negotiatio}'.format(proposal='proposal_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_proposals_deals_batch_update(client):
    """Test case for authorizedbuyersmarketplace_buyers_proposals_deals_batch_update

    
    """
    body = {"requests":[{"deal":{"proposalRevision":"proposalRevision","displayName":"displayName","sellerTimeZone":{"id":"id","version":"version"},"description":"description","updateTime":"updateTime","dealType":"DEAL_TYPE_UNSPECIFIED","estimatedGrossSpend":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"buyer":"buyer","publisherProfile":"publisherProfile","billedBuyer":"billedBuyer","preferredDealTerms":{"fixedPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"}},"targeting":{"geoTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"placementTargeting":{"uriTargeting":{"targetedUris":["targetedUris","targetedUris"],"excludedUris":["excludedUris","excludedUris"]},"mobileApplicationTargeting":{"firstPartyTargeting":{"excludedAppIds":["excludedAppIds","excludedAppIds"],"targetedAppIds":["targetedAppIds","targetedAppIds"]}}},"technologyTargeting":{"operatingSystemTargeting":{"operatingSystemCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"operatingSystemVersionCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"deviceCategoryTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"deviceCapabilityTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"userListTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"videoTargeting":{"targetedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"],"excludedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"]},"daypartTargeting":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"endTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"endTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}}],"timeZoneType":"TIME_ZONE_TYPE_UNSPECIFIED"},"inventoryTypeTargeting":{"inventoryTypes":["INVENTORY_TYPE_UNSPECIFIED","INVENTORY_TYPE_UNSPECIFIED"]},"inventorySizeTargeting":{"targetedInventorySizes":[{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"},{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"}],"excludedInventorySizes":[{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"},{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"}]}},"flightStartTime":"flightStartTime","createTime":"createTime","name":"name","client":"client","flightEndTime":"flightEndTime","deliveryControl":{"deliveryRateType":"DELIVERY_RATE_TYPE_UNSPECIFIED","creativeRotationType":"CREATIVE_ROTATION_TYPE_UNSPECIFIED","companionDeliveryType":"COMPANION_DELIVERY_TYPE_UNSPECIFIED","frequencyCap":[{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":0,"timeUnitsCount":6},{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":0,"timeUnitsCount":6}],"roadblockingType":"ROADBLOCKING_TYPE_UNSPECIFIED"},"privateAuctionTerms":{"floorPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"},"openAuctionAllowed":True},"creativeRequirements":{"creativePreApprovalPolicy":"CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED","creativeSafeFrameCompatibility":"CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED","maxAdDurationMs":"maxAdDurationMs","programmaticCreativeSource":"PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED","creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"programmaticGuaranteedTerms":{"minimumDailyLooks":"minimumDailyLooks","percentShareOfVoice":"percentShareOfVoice","reservationType":"RESERVATION_TYPE_UNSPECIFIED","guaranteedLooks":"guaranteedLooks","impressionCap":"impressionCap","fixedPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"}}},"updateMask":"updateMask"},{"deal":{"proposalRevision":"proposalRevision","displayName":"displayName","sellerTimeZone":{"id":"id","version":"version"},"description":"description","updateTime":"updateTime","dealType":"DEAL_TYPE_UNSPECIFIED","estimatedGrossSpend":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"buyer":"buyer","publisherProfile":"publisherProfile","billedBuyer":"billedBuyer","preferredDealTerms":{"fixedPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"}},"targeting":{"geoTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"placementTargeting":{"uriTargeting":{"targetedUris":["targetedUris","targetedUris"],"excludedUris":["excludedUris","excludedUris"]},"mobileApplicationTargeting":{"firstPartyTargeting":{"excludedAppIds":["excludedAppIds","excludedAppIds"],"targetedAppIds":["targetedAppIds","targetedAppIds"]}}},"technologyTargeting":{"operatingSystemTargeting":{"operatingSystemCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"operatingSystemVersionCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"deviceCategoryTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"deviceCapabilityTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"userListTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"videoTargeting":{"targetedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"],"excludedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"]},"daypartTargeting":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"endTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"endTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}}],"timeZoneType":"TIME_ZONE_TYPE_UNSPECIFIED"},"inventoryTypeTargeting":{"inventoryTypes":["INVENTORY_TYPE_UNSPECIFIED","INVENTORY_TYPE_UNSPECIFIED"]},"inventorySizeTargeting":{"targetedInventorySizes":[{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"},{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"}],"excludedInventorySizes":[{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"},{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"}]}},"flightStartTime":"flightStartTime","createTime":"createTime","name":"name","client":"client","flightEndTime":"flightEndTime","deliveryControl":{"deliveryRateType":"DELIVERY_RATE_TYPE_UNSPECIFIED","creativeRotationType":"CREATIVE_ROTATION_TYPE_UNSPECIFIED","companionDeliveryType":"COMPANION_DELIVERY_TYPE_UNSPECIFIED","frequencyCap":[{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":0,"timeUnitsCount":6},{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":0,"timeUnitsCount":6}],"roadblockingType":"ROADBLOCKING_TYPE_UNSPECIFIED"},"privateAuctionTerms":{"floorPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"},"openAuctionAllowed":True},"creativeRequirements":{"creativePreApprovalPolicy":"CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED","creativeSafeFrameCompatibility":"CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED","maxAdDurationMs":"maxAdDurationMs","programmaticCreativeSource":"PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED","creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"programmaticGuaranteedTerms":{"minimumDailyLooks":"minimumDailyLooks","percentShareOfVoice":"percentShareOfVoice","reservationType":"RESERVATION_TYPE_UNSPECIFIED","guaranteedLooks":"guaranteedLooks","impressionCap":"impressionCap","fixedPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"}}},"updateMask":"updateMask"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/deals:batchUpdate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_proposals_deals_list(client):
    """Test case for authorizedbuyersmarketplace_buyers_proposals_deals_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/deals'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_proposals_deals_patch(client):
    """Test case for authorizedbuyersmarketplace_buyers_proposals_deals_patch

    
    """
    body = {"proposalRevision":"proposalRevision","displayName":"displayName","sellerTimeZone":{"id":"id","version":"version"},"description":"description","updateTime":"updateTime","dealType":"DEAL_TYPE_UNSPECIFIED","estimatedGrossSpend":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"buyer":"buyer","publisherProfile":"publisherProfile","billedBuyer":"billedBuyer","preferredDealTerms":{"fixedPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"}},"targeting":{"geoTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"placementTargeting":{"uriTargeting":{"targetedUris":["targetedUris","targetedUris"],"excludedUris":["excludedUris","excludedUris"]},"mobileApplicationTargeting":{"firstPartyTargeting":{"excludedAppIds":["excludedAppIds","excludedAppIds"],"targetedAppIds":["targetedAppIds","targetedAppIds"]}}},"technologyTargeting":{"operatingSystemTargeting":{"operatingSystemCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"operatingSystemVersionCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"deviceCategoryTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"deviceCapabilityTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"userListTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"videoTargeting":{"targetedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"],"excludedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"]},"daypartTargeting":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"endTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"endTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}}],"timeZoneType":"TIME_ZONE_TYPE_UNSPECIFIED"},"inventoryTypeTargeting":{"inventoryTypes":["INVENTORY_TYPE_UNSPECIFIED","INVENTORY_TYPE_UNSPECIFIED"]},"inventorySizeTargeting":{"targetedInventorySizes":[{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"},{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"}],"excludedInventorySizes":[{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"},{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"}]}},"flightStartTime":"flightStartTime","createTime":"createTime","name":"name","client":"client","flightEndTime":"flightEndTime","deliveryControl":{"deliveryRateType":"DELIVERY_RATE_TYPE_UNSPECIFIED","creativeRotationType":"CREATIVE_ROTATION_TYPE_UNSPECIFIED","companionDeliveryType":"COMPANION_DELIVERY_TYPE_UNSPECIFIED","frequencyCap":[{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":0,"timeUnitsCount":6},{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":0,"timeUnitsCount":6}],"roadblockingType":"ROADBLOCKING_TYPE_UNSPECIFIED"},"privateAuctionTerms":{"floorPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"},"openAuctionAllowed":True},"creativeRequirements":{"creativePreApprovalPolicy":"CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED","creativeSafeFrameCompatibility":"CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED","maxAdDurationMs":"maxAdDurationMs","programmaticCreativeSource":"PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED","creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"programmaticGuaranteedTerms":{"minimumDailyLooks":"minimumDailyLooks","percentShareOfVoice":"percentShareOfVoice","reservationType":"RESERVATION_TYPE_UNSPECIFIED","guaranteedLooks":"guaranteedLooks","impressionCap":"impressionCap","fixedPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_proposals_list(client):
    """Test case for authorizedbuyersmarketplace_buyers_proposals_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/proposals'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_proposals_send_rfp(client):
    """Test case for authorizedbuyersmarketplace_buyers_proposals_send_rfp

    
    """
    body = {"geoTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"note":"note","preferredDealTerms":{"fixedPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"}},"flightStartTime":"flightStartTime","displayName":"displayName","client":"client","flightEndTime":"flightEndTime","buyerContacts":[{"displayName":"displayName","email":"email"},{"displayName":"displayName","email":"email"}],"inventorySizeTargeting":{"targetedInventorySizes":[{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"},{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"}],"excludedInventorySizes":[{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"},{"width":"width","type":"TYPE_UNSPECIFIED","height":"height"}]},"estimatedGrossSpend":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"programmaticGuaranteedTerms":{"minimumDailyLooks":"minimumDailyLooks","percentShareOfVoice":"percentShareOfVoice","reservationType":"RESERVATION_TYPE_UNSPECIFIED","guaranteedLooks":"guaranteedLooks","impressionCap":"impressionCap","fixedPrice":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"type":"TYPE_UNSPECIFIED"}},"publisherProfile":"publisherProfile"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{buyer}/proposals:sendRfp'.format(buyer='buyer_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_publisher_profiles_get(client):
    """Test case for authorizedbuyersmarketplace_buyers_publisher_profiles_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorizedbuyersmarketplace_buyers_publisher_profiles_list(client):
    """Test case for authorizedbuyersmarketplace_buyers_publisher_profiles_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/publisherProfiles'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

