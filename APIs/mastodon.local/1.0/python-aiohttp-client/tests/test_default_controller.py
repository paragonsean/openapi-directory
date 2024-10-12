# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.activity import Activity
from openapi_server.models.admin_account import AdminAccount
from openapi_server.models.admin_report import AdminReport
from openapi_server.models.announcement import Announcement
from openapi_server.models.api_v1_admin_accounts_id_action_post_request import ApiV1AdminAccountsIdActionPostRequest
from openapi_server.models.api_v1_domain_blocks_post_request import ApiV1DomainBlocksPostRequest
from openapi_server.models.api_v1_featured_tags_post_request import ApiV1FeaturedTagsPostRequest
from openapi_server.models.api_v1_filters_post_request import ApiV1FiltersPostRequest
from openapi_server.models.api_v1_lists_id_accounts_post_request import ApiV1ListsIdAccountsPostRequest
from openapi_server.models.api_v1_lists_post_request import ApiV1ListsPostRequest
from openapi_server.models.api_v1_lists_put_request import ApiV1ListsPutRequest
from openapi_server.models.api_v1_media_post_request import ApiV1MediaPostRequest
from openapi_server.models.api_v1_polls_id_post_request import ApiV1PollsIdPostRequest
from openapi_server.models.api_v1_push_subscription_post_request import ApiV1PushSubscriptionPostRequest
from openapi_server.models.api_v1_push_subscription_put_request import ApiV1PushSubscriptionPutRequest
from openapi_server.models.api_v1_reports_post_request import ApiV1ReportsPostRequest
from openapi_server.models.api_v1_scheduled_statuses_id_put_request import ApiV1ScheduledStatusesIdPutRequest
from openapi_server.models.api_v1_statuses_id_reblog_post_request import ApiV1StatusesIdReblogPostRequest
from openapi_server.models.api_v1_statuses_post200_response import ApiV1StatusesPost200Response
from openapi_server.models.api_v1_statuses_post_request_inner import ApiV1StatusesPostRequestInner
from openapi_server.models.api_v2_search_get200_response import ApiV2SearchGet200Response
from openapi_server.models.attachment import Attachment
from openapi_server.models.card import Card
from openapi_server.models.context import Context
from openapi_server.models.conversation import Conversation
from openapi_server.models.emoji import Emoji
from openapi_server.models.error import Error
from openapi_server.models.featured_tag import FeaturedTag
from openapi_server.models.filter import Filter
from openapi_server.models.identity_proof import IdentityProof
from openapi_server.models.instance import Instance
from openapi_server.models.notification import Notification
from openapi_server.models.poll import Poll
from openapi_server.models.preferences import Preferences
from openapi_server.models.push_subscription import PushSubscription
from openapi_server.models.relationship import Relationship
from openapi_server.models.report import Report
from openapi_server.models.scheduled_status import ScheduledStatus
from openapi_server.models.status import Status
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_api_oembed_get(client):
    """Test case for api_oembed_get

    
    """
    params = [('url', 'url_example'),
                    ('maxwidth', 400),
                    ('maxheight', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/oembed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_proofs_get(client):
    """Test case for api_proofs_get

    
    """
    params = [('provider', 'provider_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/proofs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_accounts_get(client):
    """Test case for api_v1_admin_accounts_get

    
    """
    params = [('local', True),
                    ('remote', True),
                    ('by_domain', 'by_domain_example'),
                    ('active', True),
                    ('pending', True),
                    ('disabled', True),
                    ('silenced', True),
                    ('suspended', True),
                    ('staff', True),
                    ('username', 'username_example'),
                    ('display_name', 'display_name_example'),
                    ('email', 'email_example'),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/admin/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_accounts_id_action_post(client):
    """Test case for api_v1_admin_accounts_id_action_post

    
    """
    body = openapi_server.ApiV1AdminAccountsIdActionPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/accounts/{id}/action'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_accounts_id_approve_post(client):
    """Test case for api_v1_admin_accounts_id_approve_post

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/accounts/{id}/approve'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_accounts_id_enable_post(client):
    """Test case for api_v1_admin_accounts_id_enable_post

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/accounts/{id}/enable'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_accounts_id_get(client):
    """Test case for api_v1_admin_accounts_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/admin/accounts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_accounts_id_reject_post(client):
    """Test case for api_v1_admin_accounts_id_reject_post

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/accounts/{id}/reject'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_accounts_id_unsilence_post(client):
    """Test case for api_v1_admin_accounts_id_unsilence_post

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/accounts/{id}/unsilence'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_accounts_id_unsuspend_post(client):
    """Test case for api_v1_admin_accounts_id_unsuspend_post

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/accounts/{id}/unsuspend'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_reports_get(client):
    """Test case for api_v1_admin_reports_get

    
    """
    params = [('resolved', True),
                    ('account_id', 'account_id_example'),
                    ('target_account_id', 'target_account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/admin/reports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_reports_id_assign_to_self_post(client):
    """Test case for api_v1_admin_reports_id_assign_to_self_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/reports/{id}/assign_to_self'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_reports_id_get(client):
    """Test case for api_v1_admin_reports_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/admin/reports/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_reports_id_reopen_post(client):
    """Test case for api_v1_admin_reports_id_reopen_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/reports/{id}/reopen'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_reports_id_resolve_post(client):
    """Test case for api_v1_admin_reports_id_resolve_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/reports/{id}/resolve'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_admin_reports_id_unassign_post(client):
    """Test case for api_v1_admin_reports_id_unassign_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/admin/reports/{id}/unassign'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_announcements_get(client):
    """Test case for api_v1_announcements_get

    
    """
    params = [('with_dismissed', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/announcements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_announcements_id_dismiss_post(client):
    """Test case for api_v1_announcements_id_dismiss_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/announcements/{id}/dismiss'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_announcements_id_reactions_name_delete(client):
    """Test case for api_v1_announcements_id_reactions_name_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/announcements/{id}/reactions/{name}'.format(id='id_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_announcements_id_reactions_name_put(client):
    """Test case for api_v1_announcements_id_reactions_name_put

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/announcements/{id}/reactions/{name}'.format(id='id_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_blocks_get(client):
    """Test case for api_v1_blocks_get

    
    """
    params = [('limit', 56),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/blocks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_bookmarks_get(client):
    """Test case for api_v1_bookmarks_get

    
    """
    params = [('limit', 56),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/bookmarks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_conversations_get(client):
    """Test case for api_v1_conversations_get

    
    """
    params = [('limit', 20),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/conversations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_conversations_id_delete(client):
    """Test case for api_v1_conversations_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/conversations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_conversations_id_read_post(client):
    """Test case for api_v1_conversations_id_read_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/conversations/{id}/read'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_custom_emojis_get(client):
    """Test case for api_v1_custom_emojis_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/custom_emojis',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_directory_get(client):
    """Test case for api_v1_directory_get

    
    """
    params = [('limit', 40),
                    ('offset', 0),
                    ('order', active),
                    ('local', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/directory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_domain_blocks_delete(client):
    """Test case for api_v1_domain_blocks_delete

    
    """
    params = [('domain', 'domain_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/domain_blocks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_domain_blocks_get(client):
    """Test case for api_v1_domain_blocks_get

    
    """
    params = [('limit', 56),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/domain_blocks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_domain_blocks_post(client):
    """Test case for api_v1_domain_blocks_post

    
    """
    body = openapi_server.ApiV1DomainBlocksPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/domain_blocks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_endorsements_get(client):
    """Test case for api_v1_endorsements_get

    
    """
    params = [('limit', 40),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/endorsements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_favourites_get(client):
    """Test case for api_v1_favourites_get

    
    """
    params = [('limit', 'limit_example'),
                    ('max_id', 'max_id_example'),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/favourites',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_featured_tags_get(client):
    """Test case for api_v1_featured_tags_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/featured_tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_featured_tags_id_delete(client):
    """Test case for api_v1_featured_tags_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/featured_tags/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_featured_tags_post(client):
    """Test case for api_v1_featured_tags_post

    
    """
    body = openapi_server.ApiV1FeaturedTagsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/featured_tags',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_featured_tags_suggestions_get(client):
    """Test case for api_v1_featured_tags_suggestions_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/featured_tags/suggestions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_filters_get(client):
    """Test case for api_v1_filters_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/filters',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_filters_id_delete(client):
    """Test case for api_v1_filters_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/filters/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_filters_id_get(client):
    """Test case for api_v1_filters_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/filters/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_filters_id_put(client):
    """Test case for api_v1_filters_id_put

    
    """
    body = openapi_server.ApiV1FiltersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/filters/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_filters_post(client):
    """Test case for api_v1_filters_post

    
    """
    body = openapi_server.ApiV1FiltersPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/filters',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_follow_requests_get(client):
    """Test case for api_v1_follow_requests_get

    
    """
    params = [('limit', 40)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/follow_requests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_follow_requests_id_authorize_post(client):
    """Test case for api_v1_follow_requests_id_authorize_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/follow_requests/{id}/authorize'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_follow_requests_id_reject_post(client):
    """Test case for api_v1_follow_requests_id_reject_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/follow_requests/{id}/reject'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_instance_activity_get(client):
    """Test case for api_v1_instance_activity_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/instance/activity',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_instance_get(client):
    """Test case for api_v1_instance_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/instance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_instance_peers_get(client):
    """Test case for api_v1_instance_peers_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/instance/peers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_lists_delete(client):
    """Test case for api_v1_lists_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/lists',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_lists_get(client):
    """Test case for api_v1_lists_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/lists',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_lists_id_accounts_delete(client):
    """Test case for api_v1_lists_id_accounts_delete

    
    """
    params = [('account_ids', ['account_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/lists/{id}/accounts'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_lists_id_accounts_get(client):
    """Test case for api_v1_lists_id_accounts_get

    
    """
    params = [('limit', 40),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/lists/{id}/accounts'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_lists_id_accounts_post(client):
    """Test case for api_v1_lists_id_accounts_post

    
    """
    body = openapi_server.ApiV1ListsIdAccountsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/lists/{id}/accounts'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_lists_id_get(client):
    """Test case for api_v1_lists_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/lists/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_lists_post(client):
    """Test case for api_v1_lists_post

    
    """
    body = openapi_server.ApiV1ListsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/lists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_lists_put(client):
    """Test case for api_v1_lists_put

    
    """
    body = openapi_server.ApiV1ListsPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/lists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_markers_get(client):
    """Test case for api_v1_markers_get

    
    """
    params = [('timeline', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/markers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_markers_post(client):
    """Test case for api_v1_markers_post

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/markers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_media_id_get(client):
    """Test case for api_v1_media_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/media/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_media_id_post(client):
    """Test case for api_v1_media_id_post

    
    """
    body = openapi_server.ApiV1MediaPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/media/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_api_v1_media_post(client):
    """Test case for api_v1_media_post

    
    """
    body = openapi_server.ApiV1MediaPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/media',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_mutes_get(client):
    """Test case for api_v1_mutes_get

    
    """
    params = [('limit', 'limit_example'),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/mutes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_notifications_clear_post(client):
    """Test case for api_v1_notifications_clear_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/notifications/clear',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_notifications_get(client):
    """Test case for api_v1_notifications_get

    
    """
    params = [('limit', 20),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('min_id', 'min_id_example'),
                    ('exclude_types', ['exclude_types_example']),
                    ('account_id', 'account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_notifications_id_dismiss_post(client):
    """Test case for api_v1_notifications_id_dismiss_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/notifications/{id}/dismiss'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_notifications_id_get(client):
    """Test case for api_v1_notifications_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/notifications/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_polls_id_get(client):
    """Test case for api_v1_polls_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/polls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_polls_id_post(client):
    """Test case for api_v1_polls_id_post

    
    """
    body = openapi_server.ApiV1PollsIdPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/polls/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_preferences_get(client):
    """Test case for api_v1_preferences_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/preferences',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_push_subscription_delete(client):
    """Test case for api_v1_push_subscription_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/push/subscription',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_push_subscription_get(client):
    """Test case for api_v1_push_subscription_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/push/subscription',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_push_subscription_post(client):
    """Test case for api_v1_push_subscription_post

    
    """
    body = openapi_server.ApiV1PushSubscriptionPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/push/subscription',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_push_subscription_put(client):
    """Test case for api_v1_push_subscription_put

    
    """
    body = openapi_server.ApiV1PushSubscriptionPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/push/subscription',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_reports_post(client):
    """Test case for api_v1_reports_post

    
    """
    body = openapi_server.ApiV1ReportsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/reports',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_scheduled_statuses_get(client):
    """Test case for api_v1_scheduled_statuses_get

    
    """
    params = [('limit', 20),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/scheduled_statuses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_scheduled_statuses_id_delete(client):
    """Test case for api_v1_scheduled_statuses_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/scheduled_statuses/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_scheduled_statuses_id_get(client):
    """Test case for api_v1_scheduled_statuses_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/scheduled_statuses/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_scheduled_statuses_id_put(client):
    """Test case for api_v1_scheduled_statuses_id_put

    
    """
    body = openapi_server.ApiV1ScheduledStatusesIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/scheduled_statuses/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_bookmark_post(client):
    """Test case for api_v1_statuses_id_bookmark_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/bookmark'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_context_get(client):
    """Test case for api_v1_statuses_id_context_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/statuses/{id}/context'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_delete(client):
    """Test case for api_v1_statuses_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/statuses/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_favourite_post(client):
    """Test case for api_v1_statuses_id_favourite_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/favourite'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_favourited_by_get(client):
    """Test case for api_v1_statuses_id_favourited_by_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/statuses/{id}/favourited_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_get(client):
    """Test case for api_v1_statuses_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/statuses/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_mute_post(client):
    """Test case for api_v1_statuses_id_mute_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/mute'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_pin_post(client):
    """Test case for api_v1_statuses_id_pin_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/pin'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_reblog_post(client):
    """Test case for api_v1_statuses_id_reblog_post

    
    """
    body = openapi_server.ApiV1StatusesIdReblogPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/reblog'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_reblogged_by_get(client):
    """Test case for api_v1_statuses_id_reblogged_by_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/statuses/{id}/reblogged_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_unbookmark_post(client):
    """Test case for api_v1_statuses_id_unbookmark_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/unbookmark'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_unfavourite_post(client):
    """Test case for api_v1_statuses_id_unfavourite_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/unfavourite'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_unmute_post(client):
    """Test case for api_v1_statuses_id_unmute_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/unmute'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_unpin_post(client):
    """Test case for api_v1_statuses_id_unpin_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/unpin'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_id_unreblog_post(client):
    """Test case for api_v1_statuses_id_unreblog_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses/{id}/unreblog'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_statuses_post(client):
    """Test case for api_v1_statuses_post

    
    """
    body = [openapi_server.ApiV1StatusesPostRequestInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/statuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_suggestions_get(client):
    """Test case for api_v1_suggestions_get

    
    """
    params = [('limit', 40)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_suggestions_id_delete(client):
    """Test case for api_v1_suggestions_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/suggestions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_timelines_home_get(client):
    """Test case for api_v1_timelines_home_get

    
    """
    params = [('local', False),
                    ('limit', 20),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/timelines/home',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_timelines_list_list_id_get(client):
    """Test case for api_v1_timelines_list_list_id_get

    
    """
    params = [('limit', 20),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/timelines/list/{list_id}'.format(list_id='list_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_timelines_public_get(client):
    """Test case for api_v1_timelines_public_get

    
    """
    params = [('local', False),
                    ('remote', False),
                    ('only_media', False),
                    ('limit', 20),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/timelines/public',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_timelines_tag_hashtag_get(client):
    """Test case for api_v1_timelines_tag_hashtag_get

    
    """
    params = [('local', False),
                    ('remote', False),
                    ('only_media', False),
                    ('limit', 20),
                    ('max_id', 'max_id_example'),
                    ('since_id', 'since_id_example'),
                    ('min_id', 'min_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/timelines/tag/{hashtag}'.format(hashtag='hashtag_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_trends_get(client):
    """Test case for api_v1_trends_get

    
    """
    params = [('limit', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/trends',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_search_get(client):
    """Test case for api_v2_search_get

    
    """
    params = [('q', 'q_example'),
                    ('limit', 20),
                    ('resolve', 'resolve_example'),
                    ('following', True),
                    ('account_id', 'account_id_example'),
                    ('max_id', 'max_id_example'),
                    ('min_id', 'min_id_example'),
                    ('type', 'type_example'),
                    ('exclude_unreviewed', True),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

