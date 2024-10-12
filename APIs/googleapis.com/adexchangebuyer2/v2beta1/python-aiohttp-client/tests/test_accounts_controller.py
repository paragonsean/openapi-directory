# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accept_proposal_request import AcceptProposalRequest
from openapi_server.models.add_deal_association_request import AddDealAssociationRequest
from openapi_server.models.add_note_request import AddNoteRequest
from openapi_server.models.client import Client
from openapi_server.models.client_user import ClientUser
from openapi_server.models.client_user_invitation import ClientUserInvitation
from openapi_server.models.creative import Creative
from openapi_server.models.list_client_user_invitations_response import ListClientUserInvitationsResponse
from openapi_server.models.list_client_users_response import ListClientUsersResponse
from openapi_server.models.list_clients_response import ListClientsResponse
from openapi_server.models.list_creatives_response import ListCreativesResponse
from openapi_server.models.list_deal_associations_response import ListDealAssociationsResponse
from openapi_server.models.list_products_response import ListProductsResponse
from openapi_server.models.list_proposals_response import ListProposalsResponse
from openapi_server.models.list_publisher_profiles_response import ListPublisherProfilesResponse
from openapi_server.models.note import Note
from openapi_server.models.pause_proposal_deals_request import PauseProposalDealsRequest
from openapi_server.models.pause_proposal_request import PauseProposalRequest
from openapi_server.models.product import Product
from openapi_server.models.proposal import Proposal
from openapi_server.models.publisher_profile import PublisherProfile
from openapi_server.models.remove_deal_association_request import RemoveDealAssociationRequest
from openapi_server.models.resume_proposal_deals_request import ResumeProposalDealsRequest
from openapi_server.models.watch_creative_request import WatchCreativeRequest


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_create(client):
    """Test case for adexchangebuyer2_accounts_clients_create

    
    """
    body = {"role":"CLIENT_ROLE_UNSPECIFIED","clientName":"clientName","entityName":"entityName","entityType":"ENTITY_TYPE_UNSPECIFIED","partnerClientId":"partnerClientId","entityId":"entityId","visibleToSeller":True,"clientAccountId":"clientAccountId","status":"CLIENT_STATUS_UNSPECIFIED"}
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
        path='/v2beta1/accounts/{account_id}/clients'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_get(client):
    """Test case for adexchangebuyer2_accounts_clients_get

    
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
        path='/v2beta1/accounts/{account_id}/clients/{client_account_id}'.format(account_id='account_id_example', client_account_id='client_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_invitations_create(client):
    """Test case for adexchangebuyer2_accounts_clients_invitations_create

    
    """
    body = {"clientAccountId":"clientAccountId","invitationId":"invitationId","email":"email"}
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
        path='/v2beta1/accounts/{account_id}/clients/{client_account_id}/invitations'.format(account_id='account_id_example', client_account_id='client_account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_invitations_get(client):
    """Test case for adexchangebuyer2_accounts_clients_invitations_get

    
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
        path='/v2beta1/accounts/{account_id}/clients/{client_account_id}/invitations/{invitation_id}'.format(account_id='account_id_example', client_account_id='client_account_id_example', invitation_id='invitation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_invitations_list(client):
    """Test case for adexchangebuyer2_accounts_clients_invitations_list

    
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
        path='/v2beta1/accounts/{account_id}/clients/{client_account_id}/invitations'.format(account_id='account_id_example', client_account_id='client_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_list(client):
    """Test case for adexchangebuyer2_accounts_clients_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('partnerClientId', 'partner_client_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta1/accounts/{account_id}/clients'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_update(client):
    """Test case for adexchangebuyer2_accounts_clients_update

    
    """
    body = {"role":"CLIENT_ROLE_UNSPECIFIED","clientName":"clientName","entityName":"entityName","entityType":"ENTITY_TYPE_UNSPECIFIED","partnerClientId":"partnerClientId","entityId":"entityId","visibleToSeller":True,"clientAccountId":"clientAccountId","status":"CLIENT_STATUS_UNSPECIFIED"}
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
        method='PUT',
        path='/v2beta1/accounts/{account_id}/clients/{client_account_id}'.format(account_id='account_id_example', client_account_id='client_account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_users_get(client):
    """Test case for adexchangebuyer2_accounts_clients_users_get

    
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
        path='/v2beta1/accounts/{account_id}/clients/{client_account_id}/users/{user_id}'.format(account_id='account_id_example', client_account_id='client_account_id_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_users_list(client):
    """Test case for adexchangebuyer2_accounts_clients_users_list

    
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
        path='/v2beta1/accounts/{account_id}/clients/{client_account_id}/users'.format(account_id='account_id_example', client_account_id='client_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_clients_users_update(client):
    """Test case for adexchangebuyer2_accounts_clients_users_update

    
    """
    body = {"clientAccountId":"clientAccountId","userId":"userId","email":"email","status":"USER_STATUS_UNSPECIFIED"}
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
        method='PUT',
        path='/v2beta1/accounts/{account_id}/clients/{client_account_id}/users/{user_id}'.format(account_id='account_id_example', client_account_id='client_account_id_example', user_id='user_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_create(client):
    """Test case for adexchangebuyer2_accounts_creatives_create

    
    """
    body = {"dealsStatus":"STATUS_UNSPECIFIED","servingRestrictions":[{"disapprovalReasons":[{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]},{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]}],"disapproval":{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]},"contexts":[{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}},{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}}],"status":"STATUS_UNSPECIFIED"},{"disapprovalReasons":[{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]},{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]}],"disapproval":{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]},"contexts":[{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}},{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}}],"status":"STATUS_UNSPECIFIED"}],"agencyId":"agencyId","video":{"videoUrl":"videoUrl","videoVastXml":"videoVastXml"},"adTechnologyProviders":{"hasUnidentifiedProvider":True,"detectedProviderIds":["detectedProviderIds","detectedProviderIds"]},"advertiserName":"advertiserName","creativeId":"creativeId","detectedProductCategories":[6,6],"detectedDomains":["detectedDomains","detectedDomains"],"native":{"image":{"width":7,"url":"url","height":2},"clickLinkUrl":"clickLinkUrl","body":"body","advertiserName":"advertiserName","callToAction":"callToAction","appIcon":{"width":7,"url":"url","height":2},"clickTrackingUrl":"clickTrackingUrl","videoUrl":"videoUrl","storeUrl":"storeUrl","logo":{"width":7,"url":"url","height":2},"starRating":9.301444243932576,"headline":"headline","priceDisplayText":"priceDisplayText"},"vendorIds":[3,3],"clickThroughUrls":["clickThroughUrls","clickThroughUrls"],"html":{"snippet":"snippet","width":5,"height":5},"detectedLanguages":["detectedLanguages","detectedLanguages"],"impressionTrackingUrls":["impressionTrackingUrls","impressionTrackingUrls"],"apiUpdateTime":"apiUpdateTime","version":2,"restrictedCategories":["NO_RESTRICTED_CATEGORIES","NO_RESTRICTED_CATEGORIES"],"accountId":"accountId","detectedSensitiveCategories":[1,1],"corrections":[{"details":["details","details"],"contexts":[{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}},{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}}],"type":"CORRECTION_TYPE_UNSPECIFIED"},{"details":["details","details"],"contexts":[{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}},{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}}],"type":"CORRECTION_TYPE_UNSPECIFIED"}],"adChoicesDestinationUrl":"adChoicesDestinationUrl","declaredClickThroughUrls":["declaredClickThroughUrls","declaredClickThroughUrls"],"attributes":["ATTRIBUTE_UNSPECIFIED","ATTRIBUTE_UNSPECIFIED"],"detectedAdvertiserIds":["detectedAdvertiserIds","detectedAdvertiserIds"],"openAuctionStatus":"STATUS_UNSPECIFIED"}
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
                    ('duplicateIdMode', 'duplicate_id_mode_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2beta1/accounts/{account_id}/creatives'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_deal_associations_add(client):
    """Test case for adexchangebuyer2_accounts_creatives_deal_associations_add

    
    """
    body = {"association":{"dealsId":"dealsId","accountId":"accountId","creativeId":"creativeId"}}
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
        path='/v2beta1/accounts/{account_id}/creatives/{creative_id}/dealAssociations:add'.format(account_id='account_id_example', creative_id='creative_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_deal_associations_list(client):
    """Test case for adexchangebuyer2_accounts_creatives_deal_associations_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta1/accounts/{account_id}/creatives/{creative_id}/dealAssociations'.format(account_id='account_id_example', creative_id='creative_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_deal_associations_remove(client):
    """Test case for adexchangebuyer2_accounts_creatives_deal_associations_remove

    
    """
    body = {"association":{"dealsId":"dealsId","accountId":"accountId","creativeId":"creativeId"}}
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
        path='/v2beta1/accounts/{account_id}/creatives/{creative_id}/dealAssociations:remove'.format(account_id='account_id_example', creative_id='creative_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_get(client):
    """Test case for adexchangebuyer2_accounts_creatives_get

    
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
        path='/v2beta1/accounts/{account_id}/creatives/{creative_id}'.format(account_id='account_id_example', creative_id='creative_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_list(client):
    """Test case for adexchangebuyer2_accounts_creatives_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta1/accounts/{account_id}/creatives'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_stop_watching(client):
    """Test case for adexchangebuyer2_accounts_creatives_stop_watching

    
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
        path='/v2beta1/accounts/{account_id}/creatives/{creative_idstop_watchin}'.format(account_id='account_id_example', creative_id='creative_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_update(client):
    """Test case for adexchangebuyer2_accounts_creatives_update

    
    """
    body = {"dealsStatus":"STATUS_UNSPECIFIED","servingRestrictions":[{"disapprovalReasons":[{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]},{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]}],"disapproval":{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]},"contexts":[{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}},{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}}],"status":"STATUS_UNSPECIFIED"},{"disapprovalReasons":[{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]},{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]}],"disapproval":{"reason":"LENGTH_OF_IMAGE_ANIMATION","details":["details","details"]},"contexts":[{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}},{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}}],"status":"STATUS_UNSPECIFIED"}],"agencyId":"agencyId","video":{"videoUrl":"videoUrl","videoVastXml":"videoVastXml"},"adTechnologyProviders":{"hasUnidentifiedProvider":True,"detectedProviderIds":["detectedProviderIds","detectedProviderIds"]},"advertiserName":"advertiserName","creativeId":"creativeId","detectedProductCategories":[6,6],"detectedDomains":["detectedDomains","detectedDomains"],"native":{"image":{"width":7,"url":"url","height":2},"clickLinkUrl":"clickLinkUrl","body":"body","advertiserName":"advertiserName","callToAction":"callToAction","appIcon":{"width":7,"url":"url","height":2},"clickTrackingUrl":"clickTrackingUrl","videoUrl":"videoUrl","storeUrl":"storeUrl","logo":{"width":7,"url":"url","height":2},"starRating":9.301444243932576,"headline":"headline","priceDisplayText":"priceDisplayText"},"vendorIds":[3,3],"clickThroughUrls":["clickThroughUrls","clickThroughUrls"],"html":{"snippet":"snippet","width":5,"height":5},"detectedLanguages":["detectedLanguages","detectedLanguages"],"impressionTrackingUrls":["impressionTrackingUrls","impressionTrackingUrls"],"apiUpdateTime":"apiUpdateTime","version":2,"restrictedCategories":["NO_RESTRICTED_CATEGORIES","NO_RESTRICTED_CATEGORIES"],"accountId":"accountId","detectedSensitiveCategories":[1,1],"corrections":[{"details":["details","details"],"contexts":[{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}},{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}}],"type":"CORRECTION_TYPE_UNSPECIFIED"},{"details":["details","details"],"contexts":[{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}},{"all":"SIMPLE_CONTEXT","appType":{"appTypes":["NATIVE","NATIVE"]},"securityType":{"securities":["INSECURE","INSECURE"]},"location":{"geoCriteriaIds":[0,0]},"auctionType":{"auctionTypes":["OPEN_AUCTION","OPEN_AUCTION"]},"platform":{"platforms":["DESKTOP","DESKTOP"]}}],"type":"CORRECTION_TYPE_UNSPECIFIED"}],"adChoicesDestinationUrl":"adChoicesDestinationUrl","declaredClickThroughUrls":["declaredClickThroughUrls","declaredClickThroughUrls"],"attributes":["ATTRIBUTE_UNSPECIFIED","ATTRIBUTE_UNSPECIFIED"],"detectedAdvertiserIds":["detectedAdvertiserIds","detectedAdvertiserIds"],"openAuctionStatus":"STATUS_UNSPECIFIED"}
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
        method='PUT',
        path='/v2beta1/accounts/{account_id}/creatives/{creative_id}'.format(account_id='account_id_example', creative_id='creative_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_creatives_watch(client):
    """Test case for adexchangebuyer2_accounts_creatives_watch

    
    """
    body = {"topic":"topic"}
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
        path='/v2beta1/accounts/{account_id}/creatives/{creative_idwatc}'.format(account_id='account_id_example', creative_id='creative_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_finalized_proposals_list(client):
    """Test case for adexchangebuyer2_accounts_finalized_proposals_list

    
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
                    ('filterSyntax', 'filter_syntax_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta1/accounts/{account_id}/finalizedProposals'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_finalized_proposals_pause(client):
    """Test case for adexchangebuyer2_accounts_finalized_proposals_pause

    
    """
    body = {"reason":"reason","externalDealIds":["externalDealIds","externalDealIds"]}
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
        path='/v2beta1/accounts/{account_id}/finalizedProposals/{proposal_idpaus}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_finalized_proposals_resume(client):
    """Test case for adexchangebuyer2_accounts_finalized_proposals_resume

    
    """
    body = {"externalDealIds":["externalDealIds","externalDealIds"]}
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
        path='/v2beta1/accounts/{account_id}/finalizedProposals/{proposal_idresum}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_products_get(client):
    """Test case for adexchangebuyer2_accounts_products_get

    
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
        path='/v2beta1/accounts/{account_id}/products/{product_id}'.format(account_id='account_id_example', product_id='product_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_products_list(client):
    """Test case for adexchangebuyer2_accounts_products_list

    
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
        path='/v2beta1/accounts/{account_id}/products'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_accept(client):
    """Test case for adexchangebuyer2_accounts_proposals_accept

    
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
        path='/v2beta1/accounts/{account_id}/proposals/{proposal_idaccep}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_add_note(client):
    """Test case for adexchangebuyer2_accounts_proposals_add_note

    
    """
    body = {"note":{"note":"note","creatorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","createTime":"createTime","proposalRevision":"proposalRevision","noteId":"noteId"}}
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
        path='/v2beta1/accounts/{account_id}/proposals/{proposal_idadd_not}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_cancel_negotiation(client):
    """Test case for adexchangebuyer2_accounts_proposals_cancel_negotiation

    
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
        path='/v2beta1/accounts/{account_id}/proposals/{proposal_idcancel_negotiatio}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_complete_setup(client):
    """Test case for adexchangebuyer2_accounts_proposals_complete_setup

    
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
        path='/v2beta1/accounts/{account_id}/proposals/{proposal_idcomplete_setu}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_create(client):
    """Test case for adexchangebuyer2_accounts_proposals_create

    
    """
    body = {"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"notes":[{"note":"note","creatorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","createTime":"createTime","proposalRevision":"proposalRevision","noteId":"noteId"},{"note":"note","creatorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","createTime":"createTime","proposalRevision":"proposalRevision","noteId":"noteId"}],"proposalState":"PROPOSAL_STATE_UNSPECIFIED","proposalRevision":"proposalRevision","displayName":"displayName","sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"buyerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"updateTime":"updateTime","proposalId":"proposalId","buyer":{"accountId":"accountId"},"termsAndConditions":"termsAndConditions","billedBuyer":{"accountId":"accountId"},"lastUpdaterOrCommentorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","originatorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","privateAuctionId":"privateAuctionId","deals":[{"dealServingMetadata":{"dealPauseStatus":{"hasSellerPaused":True,"sellerPauseReason":"sellerPauseReason","firstPausedBy":"BUYER_SELLER_ROLE_UNSPECIFIED","hasBuyerPaused":True,"buyerPauseReason":"buyerPauseReason"}},"dealId":"dealId","displayName":"displayName","creativeRestrictions":{"creativeSpecifications":[{"creativeCompanionSizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"creativeSize":{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}},{"creativeCompanionSizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"creativeSize":{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}}],"creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"description":"description","sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"createProductRevision":"createProductRevision","availableStartTime":"availableStartTime","proposalId":"proposalId","dealTerms":{"guaranteedFixedPriceTerms":{"minimumDailyLooks":"minimumDailyLooks","percentShareOfVoice":"percentShareOfVoice","reservationType":"RESERVATION_TYPE_UNSPECIFIED","guaranteedLooks":"guaranteedLooks","impressionCap":"impressionCap","fixedPrices":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}],"guaranteedImpressions":"guaranteedImpressions"},"brandingType":"BRANDING_TYPE_UNSPECIFIED","nonGuaranteedAuctionTerms":{"autoOptimizePrivateAuction":True,"reservePricesPerBuyer":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}]},"sellerTimeZone":"sellerTimeZone","description":"description","estimatedImpressionsPerDay":"estimatedImpressionsPerDay","nonGuaranteedFixedPriceTerms":{"fixedPrices":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}]},"estimatedGrossSpend":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"}},"targeting":{"geoTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"placementTargeting":{"urlTargeting":{"targetedUrls":["targetedUrls","targetedUrls"],"excludedUrls":["excludedUrls","excludedUrls"]},"mobileApplicationTargeting":{"firstPartyTargeting":{"excludedAppIds":["excludedAppIds","excludedAppIds"],"targetedAppIds":["targetedAppIds","targetedAppIds"]}}},"technologyTargeting":{"operatingSystemTargeting":{"operatingSystemCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"operatingSystemVersionCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"deviceCategoryTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"deviceCapabilityTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"videoTargeting":{"targetedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"],"excludedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"]},"inventorySizeTargeting":{"targetedInventorySizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"excludedInventorySizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}]}},"deliveryControl":{"deliveryRateType":"DELIVERY_RATE_TYPE_UNSPECIFIED","frequencyCaps":[{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":6,"numTimeUnits":1},{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":6,"numTimeUnits":1}],"creativeBlockingLevel":"CREATIVE_BLOCKING_LEVEL_UNSPECIFIED"},"targetingCriterion":[{"exclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"inclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"key":"key"},{"exclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"inclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"key":"key"}],"externalDealId":"externalDealId","updateTime":"updateTime","programmaticCreativeSource":"PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED","syndicationProduct":"SYNDICATION_PRODUCT_UNSPECIFIED","creativePreApprovalPolicy":"CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED","createProductId":"createProductId","createTime":"createTime","webPropertyCode":"webPropertyCode","availableEndTime":"availableEndTime","creativeSafeFrameCompatibility":"CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED","buyerPrivateData":{"referenceId":"referenceId"},"isSetupComplete":True},{"dealServingMetadata":{"dealPauseStatus":{"hasSellerPaused":True,"sellerPauseReason":"sellerPauseReason","firstPausedBy":"BUYER_SELLER_ROLE_UNSPECIFIED","hasBuyerPaused":True,"buyerPauseReason":"buyerPauseReason"}},"dealId":"dealId","displayName":"displayName","creativeRestrictions":{"creativeSpecifications":[{"creativeCompanionSizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"creativeSize":{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}},{"creativeCompanionSizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"creativeSize":{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}}],"creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"description":"description","sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"createProductRevision":"createProductRevision","availableStartTime":"availableStartTime","proposalId":"proposalId","dealTerms":{"guaranteedFixedPriceTerms":{"minimumDailyLooks":"minimumDailyLooks","percentShareOfVoice":"percentShareOfVoice","reservationType":"RESERVATION_TYPE_UNSPECIFIED","guaranteedLooks":"guaranteedLooks","impressionCap":"impressionCap","fixedPrices":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}],"guaranteedImpressions":"guaranteedImpressions"},"brandingType":"BRANDING_TYPE_UNSPECIFIED","nonGuaranteedAuctionTerms":{"autoOptimizePrivateAuction":True,"reservePricesPerBuyer":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}]},"sellerTimeZone":"sellerTimeZone","description":"description","estimatedImpressionsPerDay":"estimatedImpressionsPerDay","nonGuaranteedFixedPriceTerms":{"fixedPrices":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}]},"estimatedGrossSpend":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"}},"targeting":{"geoTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"placementTargeting":{"urlTargeting":{"targetedUrls":["targetedUrls","targetedUrls"],"excludedUrls":["excludedUrls","excludedUrls"]},"mobileApplicationTargeting":{"firstPartyTargeting":{"excludedAppIds":["excludedAppIds","excludedAppIds"],"targetedAppIds":["targetedAppIds","targetedAppIds"]}}},"technologyTargeting":{"operatingSystemTargeting":{"operatingSystemCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"operatingSystemVersionCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"deviceCategoryTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"deviceCapabilityTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"videoTargeting":{"targetedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"],"excludedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"]},"inventorySizeTargeting":{"targetedInventorySizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"excludedInventorySizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}]}},"deliveryControl":{"deliveryRateType":"DELIVERY_RATE_TYPE_UNSPECIFIED","frequencyCaps":[{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":6,"numTimeUnits":1},{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":6,"numTimeUnits":1}],"creativeBlockingLevel":"CREATIVE_BLOCKING_LEVEL_UNSPECIFIED"},"targetingCriterion":[{"exclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"inclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"key":"key"},{"exclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"inclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"key":"key"}],"externalDealId":"externalDealId","updateTime":"updateTime","programmaticCreativeSource":"PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED","syndicationProduct":"SYNDICATION_PRODUCT_UNSPECIFIED","creativePreApprovalPolicy":"CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED","createProductId":"createProductId","createTime":"createTime","webPropertyCode":"webPropertyCode","availableEndTime":"availableEndTime","creativeSafeFrameCompatibility":"CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED","buyerPrivateData":{"referenceId":"referenceId"},"isSetupComplete":True}],"isRenegotiating":True,"buyerPrivateData":{"referenceId":"referenceId"},"isSetupComplete":True}
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
        path='/v2beta1/accounts/{account_id}/proposals'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_get(client):
    """Test case for adexchangebuyer2_accounts_proposals_get

    
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
        path='/v2beta1/accounts/{account_id}/proposals/{proposal_id}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_list(client):
    """Test case for adexchangebuyer2_accounts_proposals_list

    
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
                    ('filterSyntax', 'filter_syntax_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2beta1/accounts/{account_id}/proposals'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_pause(client):
    """Test case for adexchangebuyer2_accounts_proposals_pause

    
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
        path='/v2beta1/accounts/{account_id}/proposals/{proposal_idpaus}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_resume(client):
    """Test case for adexchangebuyer2_accounts_proposals_resume

    
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
        path='/v2beta1/accounts/{account_id}/proposals/{proposal_idresum}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_proposals_update(client):
    """Test case for adexchangebuyer2_accounts_proposals_update

    
    """
    body = {"seller":{"accountId":"accountId","subAccountId":"subAccountId"},"notes":[{"note":"note","creatorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","createTime":"createTime","proposalRevision":"proposalRevision","noteId":"noteId"},{"note":"note","creatorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","createTime":"createTime","proposalRevision":"proposalRevision","noteId":"noteId"}],"proposalState":"PROPOSAL_STATE_UNSPECIFIED","proposalRevision":"proposalRevision","displayName":"displayName","sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"buyerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"updateTime":"updateTime","proposalId":"proposalId","buyer":{"accountId":"accountId"},"termsAndConditions":"termsAndConditions","billedBuyer":{"accountId":"accountId"},"lastUpdaterOrCommentorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","originatorRole":"BUYER_SELLER_ROLE_UNSPECIFIED","privateAuctionId":"privateAuctionId","deals":[{"dealServingMetadata":{"dealPauseStatus":{"hasSellerPaused":True,"sellerPauseReason":"sellerPauseReason","firstPausedBy":"BUYER_SELLER_ROLE_UNSPECIFIED","hasBuyerPaused":True,"buyerPauseReason":"buyerPauseReason"}},"dealId":"dealId","displayName":"displayName","creativeRestrictions":{"creativeSpecifications":[{"creativeCompanionSizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"creativeSize":{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}},{"creativeCompanionSizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"creativeSize":{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}}],"creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"description":"description","sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"createProductRevision":"createProductRevision","availableStartTime":"availableStartTime","proposalId":"proposalId","dealTerms":{"guaranteedFixedPriceTerms":{"minimumDailyLooks":"minimumDailyLooks","percentShareOfVoice":"percentShareOfVoice","reservationType":"RESERVATION_TYPE_UNSPECIFIED","guaranteedLooks":"guaranteedLooks","impressionCap":"impressionCap","fixedPrices":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}],"guaranteedImpressions":"guaranteedImpressions"},"brandingType":"BRANDING_TYPE_UNSPECIFIED","nonGuaranteedAuctionTerms":{"autoOptimizePrivateAuction":True,"reservePricesPerBuyer":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}]},"sellerTimeZone":"sellerTimeZone","description":"description","estimatedImpressionsPerDay":"estimatedImpressionsPerDay","nonGuaranteedFixedPriceTerms":{"fixedPrices":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}]},"estimatedGrossSpend":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"}},"targeting":{"geoTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"placementTargeting":{"urlTargeting":{"targetedUrls":["targetedUrls","targetedUrls"],"excludedUrls":["excludedUrls","excludedUrls"]},"mobileApplicationTargeting":{"firstPartyTargeting":{"excludedAppIds":["excludedAppIds","excludedAppIds"],"targetedAppIds":["targetedAppIds","targetedAppIds"]}}},"technologyTargeting":{"operatingSystemTargeting":{"operatingSystemCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"operatingSystemVersionCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"deviceCategoryTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"deviceCapabilityTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"videoTargeting":{"targetedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"],"excludedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"]},"inventorySizeTargeting":{"targetedInventorySizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"excludedInventorySizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}]}},"deliveryControl":{"deliveryRateType":"DELIVERY_RATE_TYPE_UNSPECIFIED","frequencyCaps":[{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":6,"numTimeUnits":1},{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":6,"numTimeUnits":1}],"creativeBlockingLevel":"CREATIVE_BLOCKING_LEVEL_UNSPECIFIED"},"targetingCriterion":[{"exclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"inclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"key":"key"},{"exclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"inclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"key":"key"}],"externalDealId":"externalDealId","updateTime":"updateTime","programmaticCreativeSource":"PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED","syndicationProduct":"SYNDICATION_PRODUCT_UNSPECIFIED","creativePreApprovalPolicy":"CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED","createProductId":"createProductId","createTime":"createTime","webPropertyCode":"webPropertyCode","availableEndTime":"availableEndTime","creativeSafeFrameCompatibility":"CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED","buyerPrivateData":{"referenceId":"referenceId"},"isSetupComplete":True},{"dealServingMetadata":{"dealPauseStatus":{"hasSellerPaused":True,"sellerPauseReason":"sellerPauseReason","firstPausedBy":"BUYER_SELLER_ROLE_UNSPECIFIED","hasBuyerPaused":True,"buyerPauseReason":"buyerPauseReason"}},"dealId":"dealId","displayName":"displayName","creativeRestrictions":{"creativeSpecifications":[{"creativeCompanionSizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"creativeSize":{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}},{"creativeCompanionSizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"creativeSize":{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}}],"creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"description":"description","sellerContacts":[{"name":"name","email":"email"},{"name":"name","email":"email"}],"createProductRevision":"createProductRevision","availableStartTime":"availableStartTime","proposalId":"proposalId","dealTerms":{"guaranteedFixedPriceTerms":{"minimumDailyLooks":"minimumDailyLooks","percentShareOfVoice":"percentShareOfVoice","reservationType":"RESERVATION_TYPE_UNSPECIFIED","guaranteedLooks":"guaranteedLooks","impressionCap":"impressionCap","fixedPrices":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}],"guaranteedImpressions":"guaranteedImpressions"},"brandingType":"BRANDING_TYPE_UNSPECIFIED","nonGuaranteedAuctionTerms":{"autoOptimizePrivateAuction":True,"reservePricesPerBuyer":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}]},"sellerTimeZone":"sellerTimeZone","description":"description","estimatedImpressionsPerDay":"estimatedImpressionsPerDay","nonGuaranteedFixedPriceTerms":{"fixedPrices":[{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}},{"advertiserIds":["advertiserIds","advertiserIds"],"price":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"},"buyer":{"accountId":"accountId"}}]},"estimatedGrossSpend":{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"pricingType":"PRICING_TYPE_UNSPECIFIED"}},"targeting":{"geoTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"placementTargeting":{"urlTargeting":{"targetedUrls":["targetedUrls","targetedUrls"],"excludedUrls":["excludedUrls","excludedUrls"]},"mobileApplicationTargeting":{"firstPartyTargeting":{"excludedAppIds":["excludedAppIds","excludedAppIds"],"targetedAppIds":["targetedAppIds","targetedAppIds"]}}},"technologyTargeting":{"operatingSystemTargeting":{"operatingSystemCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"operatingSystemVersionCriteria":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"deviceCategoryTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]},"deviceCapabilityTargeting":{"targetedCriteriaIds":["targetedCriteriaIds","targetedCriteriaIds"],"excludedCriteriaIds":["excludedCriteriaIds","excludedCriteriaIds"]}},"videoTargeting":{"targetedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"],"excludedPositionTypes":["POSITION_TYPE_UNSPECIFIED","POSITION_TYPE_UNSPECIFIED"]},"inventorySizeTargeting":{"targetedInventorySizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}],"excludedInventorySizes":[{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"},{"sizeType":"SIZE_TYPE_UNSPECIFIED","width":"width","height":"height"}]}},"deliveryControl":{"deliveryRateType":"DELIVERY_RATE_TYPE_UNSPECIFIED","frequencyCaps":[{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":6,"numTimeUnits":1},{"timeUnitType":"TIME_UNIT_TYPE_UNSPECIFIED","maxImpressions":6,"numTimeUnits":1}],"creativeBlockingLevel":"CREATIVE_BLOCKING_LEVEL_UNSPECIFIED"},"targetingCriterion":[{"exclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"inclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"key":"key"},{"exclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"inclusions":[{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"},{"stringValue":"stringValue","dayPartTargetingValue":{"dayParts":[{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}},{"dayOfWeek":"DAY_OF_WEEK_UNSPECIFIED","startTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7},"endTime":{"hours":2,"seconds":3,"nanos":9,"minutes":7}}],"timeZoneType":"TIME_ZONE_SOURCE_UNSPECIFIED"},"creativeSizeValue":{"size":{"width":5,"height":5},"creativeSizeType":"CREATIVE_SIZE_TYPE_UNSPECIFIED","nativeTemplate":"UNKNOWN_NATIVE_TEMPLATE","allowedFormats":["UNKNOWN","UNKNOWN"],"companionSizes":[{"width":5,"height":5},{"width":5,"height":5}],"skippableAdType":"SKIPPABLE_AD_TYPE_UNSPECIFIED"},"longValue":"longValue"}],"key":"key"}],"externalDealId":"externalDealId","updateTime":"updateTime","programmaticCreativeSource":"PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED","syndicationProduct":"SYNDICATION_PRODUCT_UNSPECIFIED","creativePreApprovalPolicy":"CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED","createProductId":"createProductId","createTime":"createTime","webPropertyCode":"webPropertyCode","availableEndTime":"availableEndTime","creativeSafeFrameCompatibility":"CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED","buyerPrivateData":{"referenceId":"referenceId"},"isSetupComplete":True}],"isRenegotiating":True,"buyerPrivateData":{"referenceId":"referenceId"},"isSetupComplete":True}
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
        method='PUT',
        path='/v2beta1/accounts/{account_id}/proposals/{proposal_id}'.format(account_id='account_id_example', proposal_id='proposal_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_publisher_profiles_get(client):
    """Test case for adexchangebuyer2_accounts_publisher_profiles_get

    
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
        path='/v2beta1/accounts/{account_id}/publisherProfiles/{publisher_profile_id}'.format(account_id='account_id_example', publisher_profile_id='publisher_profile_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adexchangebuyer2_accounts_publisher_profiles_list(client):
    """Test case for adexchangebuyer2_accounts_publisher_profiles_list

    
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
        path='/v2beta1/accounts/{account_id}/publisherProfiles'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

