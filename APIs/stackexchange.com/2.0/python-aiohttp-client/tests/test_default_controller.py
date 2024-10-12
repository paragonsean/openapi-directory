# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_tokens_inner import AccessTokensInner
from openapi_server.models.account_merge_inner import AccountMergeInner
from openapi_server.models.answers_inner import AnswersInner
from openapi_server.models.badges_inner import BadgesInner
from openapi_server.models.comments_inner import CommentsInner
from openapi_server.models.created_comment import CreatedComment
from openapi_server.models.error import Error
from openapi_server.models.errors_inner import ErrorsInner
from openapi_server.models.events_inner import EventsInner
from openapi_server.models.filters_inner import FiltersInner
from openapi_server.models.inbox_items_inner import InboxItemsInner
from openapi_server.models.inbox_items_inner_site import InboxItemsInnerSite
from openapi_server.models.info_object import InfoObject
from openapi_server.models.network_users_inner import NetworkUsersInner
from openapi_server.models.notifications_inner import NotificationsInner
from openapi_server.models.posts_inner import PostsInner
from openapi_server.models.privileges_inner import PrivilegesInner
from openapi_server.models.question_timeline_events_inner import QuestionTimelineEventsInner
from openapi_server.models.questions_inner import QuestionsInner
from openapi_server.models.reputation_changes_inner import ReputationChangesInner
from openapi_server.models.reputation_history_inner import ReputationHistoryInner
from openapi_server.models.revisions_inner import RevisionsInner
from openapi_server.models.single_filter import SingleFilter
from openapi_server.models.suggested_edits_inner import SuggestedEditsInner
from openapi_server.models.tag_score_objects_inner import TagScoreObjectsInner
from openapi_server.models.tag_synonyms_inner import TagSynonymsInner
from openapi_server.models.tag_wikis_inner import TagWikisInner
from openapi_server.models.tags_inner import TagsInner
from openapi_server.models.top_tag_objects_inner import TopTagObjectsInner
from openapi_server.models.user import User
from openapi_server.models.user_timeline_objects_inner import UserTimelineObjectsInner
from openapi_server.models.users_inner import UsersInner
from openapi_server.models.write_permissions_inner import WritePermissionsInner


pytestmark = pytest.mark.asyncio

async def test_access_tokens_access_tokens_get(client):
    """Test case for access_tokens_access_tokens_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/access-tokens/{access_tokens}'.format(access_tokens='access_tokens_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_access_tokens_access_tokens_invalidate_get(client):
    """Test case for access_tokens_access_tokens_invalidate_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/access-tokens/{access_tokens}/invalidate'.format(access_tokens='access_tokens_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_answers_get(client):
    """Test case for answers_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/answers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_answers_ids_comments_get(client):
    """Test case for answers_ids_comments_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/answers/{ids}/comments'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_answers_ids_get(client):
    """Test case for answers_ids_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/answers/{ids}'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_access_tokens_de_authenticate_get(client):
    """Test case for apps_access_tokens_de_authenticate_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/apps/{access_tokens}/de-authenticate'.format(access_tokens='access_tokens_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_badges_get(client):
    """Test case for badges_get

    
    """
    params = [('inname', 'inname_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/badges',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_badges_ids_get(client):
    """Test case for badges_ids_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/badges/{ids}'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_badges_ids_recipients_get(client):
    """Test case for badges_ids_recipients_get

    
    """
    params = [('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/badges/{ids}/recipients'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_badges_name_get(client):
    """Test case for badges_name_get

    
    """
    params = [('inname', 'inname_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/badges/name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_badges_recipients_get(client):
    """Test case for badges_recipients_get

    
    """
    params = [('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/badges/recipients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_badges_tags_get(client):
    """Test case for badges_tags_get

    
    """
    params = [('inname', 'inname_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/badges/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_get(client):
    """Test case for comments_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/comments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_id_delete_post(client):
    """Test case for comments_id_delete_post

    
    """
    params = [('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('preview', True)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/2.0/comments/{id}/delete'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_id_edit_post(client):
    """Test case for comments_id_edit_post

    
    """
    params = [('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('body', 'body_example'),
                    ('preview', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/2.0/comments/{id}/edit'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_ids_get(client):
    """Test case for comments_ids_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/comments/{ids}'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_get(client):
    """Test case for errors_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/errors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_errors_id_get(client):
    """Test case for errors_id_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/errors/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_get(client):
    """Test case for events_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('since', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filters_create_get(client):
    """Test case for filters_create_get

    
    """
    params = [('base', 'base_example'),
                    ('exclude', 'exclude_example'),
                    ('include', 'include_example'),
                    ('unsafe', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/filters/create',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filters_filters_get(client):
    """Test case for filters_filters_get

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/filters/{filters}'.format(filters='filters_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inbox_get(client):
    """Test case for inbox_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/inbox',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_inbox_unread_get(client):
    """Test case for inbox_unread_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('since', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/inbox/unread',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_info_get(client):
    """Test case for info_get

    
    """
    params = [('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_answers_get(client):
    """Test case for me_answers_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/answers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_associated_get(client):
    """Test case for me_associated_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/associated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_badges_get(client):
    """Test case for me_badges_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/badges',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_comments_get(client):
    """Test case for me_comments_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/comments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_comments_to_id_get(client):
    """Test case for me_comments_to_id_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/comments/{to_id}'.format(to_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_favorites_get(client):
    """Test case for me_favorites_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/favorites',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_get(client):
    """Test case for me_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_inbox_get(client):
    """Test case for me_inbox_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/inbox',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_inbox_unread_get(client):
    """Test case for me_inbox_unread_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('since', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/inbox/unread',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_mentioned_get(client):
    """Test case for me_mentioned_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/mentioned',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_merges_get(client):
    """Test case for me_merges_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/merges',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_notifications_get(client):
    """Test case for me_notifications_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_notifications_unread_get(client):
    """Test case for me_notifications_unread_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/notifications/unread',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_privileges_get(client):
    """Test case for me_privileges_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/privileges',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_questions_featured_get(client):
    """Test case for me_questions_featured_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/questions/featured',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_questions_get(client):
    """Test case for me_questions_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/questions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_questions_no_answers_get(client):
    """Test case for me_questions_no_answers_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/questions/no-answers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_questions_unaccepted_get(client):
    """Test case for me_questions_unaccepted_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/questions/unaccepted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_questions_unanswered_get(client):
    """Test case for me_questions_unanswered_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/questions/unanswered',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_reputation_get(client):
    """Test case for me_reputation_get

    
    """
    params = [('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/reputation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_reputation_history_full_get(client):
    """Test case for me_reputation_history_full_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/reputation-history/full',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_reputation_history_get(client):
    """Test case for me_reputation_history_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/reputation-history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_suggested_edits_get(client):
    """Test case for me_suggested_edits_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/suggested-edits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_tags_get(client):
    """Test case for me_tags_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_tags_tags_top_answers_get(client):
    """Test case for me_tags_tags_top_answers_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/tags/{tags}/top-answers'.format(tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_tags_tags_top_questions_get(client):
    """Test case for me_tags_tags_top_questions_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/tags/{tags}/top-questions'.format(tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_timeline_get(client):
    """Test case for me_timeline_get

    
    """
    params = [('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/timeline',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_top_answer_tags_get(client):
    """Test case for me_top_answer_tags_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/top-answer-tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_top_question_tags_get(client):
    """Test case for me_top_question_tags_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/top-question-tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_write_permissions_get(client):
    """Test case for me_write_permissions_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/me/write-permissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_get(client):
    """Test case for notifications_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_unread_get(client):
    """Test case for notifications_unread_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/notifications/unread',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_posts_get(client):
    """Test case for posts_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/posts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_posts_id_comments_add_post(client):
    """Test case for posts_id_comments_add_post

    
    """
    params = [('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('body', 'body_example'),
                    ('preview', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/2.0/posts/{id}/comments/add'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_posts_ids_comments_get(client):
    """Test case for posts_ids_comments_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/posts/{ids}/comments'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_posts_ids_get(client):
    """Test case for posts_ids_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/posts/{ids}'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_posts_ids_revisions_get(client):
    """Test case for posts_ids_revisions_get

    
    """
    params = [('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/posts/{ids}/revisions'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_posts_ids_suggested_edits_get(client):
    """Test case for posts_ids_suggested_edits_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/posts/{ids}/suggested-edits'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privileges_get(client):
    """Test case for privileges_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/privileges',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_featured_get(client):
    """Test case for questions_featured_get

    
    """
    params = [('tagged', 'tagged_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/featured',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_get(client):
    """Test case for questions_get

    
    """
    params = [('tagged', 'tagged_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_ids_answers_get(client):
    """Test case for questions_ids_answers_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/{ids}/answers'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_ids_comments_get(client):
    """Test case for questions_ids_comments_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/{ids}/comments'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_ids_get(client):
    """Test case for questions_ids_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/{ids}'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_ids_linked_get(client):
    """Test case for questions_ids_linked_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/{ids}/linked'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_ids_related_get(client):
    """Test case for questions_ids_related_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/{ids}/related'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_ids_timeline_get(client):
    """Test case for questions_ids_timeline_get

    
    """
    params = [('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/{ids}/timeline'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_no_answers_get(client):
    """Test case for questions_no_answers_get

    
    """
    params = [('tagged', 'tagged_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/no-answers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_questions_unanswered_get(client):
    """Test case for questions_unanswered_get

    
    """
    params = [('tagged', 'tagged_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/questions/unanswered',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revisions_ids_get(client):
    """Test case for revisions_ids_get

    
    """
    params = [('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/revisions/{ids}'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_advanced_get(client):
    """Test case for search_advanced_get

    
    """
    params = [('tagged', 'tagged_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('accepted', 'accepted_example'),
                    ('answers', 56),
                    ('body', 'body_example'),
                    ('closed', 'closed_example'),
                    ('migrated', 'migrated_example'),
                    ('notice', 'notice_example'),
                    ('nottagged', 'nottagged_example'),
                    ('q', 'q_example'),
                    ('title', 'title_example'),
                    ('url', 'url_example'),
                    ('user', 56),
                    ('views', 56),
                    ('wiki', 'wiki_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/search/advanced',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_get(client):
    """Test case for search_get

    
    """
    params = [('tagged', 'tagged_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('intitle', 'intitle_example'),
                    ('nottagged', 'nottagged_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_similar_get(client):
    """Test case for similar_get

    
    """
    params = [('tagged', 'tagged_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('nottagged', 'nottagged_example'),
                    ('title', 'title_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/similar',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_get(client):
    """Test case for sites_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/sites',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suggested_edits_get(client):
    """Test case for suggested_edits_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/suggested-edits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suggested_edits_ids_get(client):
    """Test case for suggested_edits_ids_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/suggested-edits/{ids}'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_get(client):
    """Test case for tags_get

    
    """
    params = [('inname', 'inname_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_moderator_only_get(client):
    """Test case for tags_moderator_only_get

    
    """
    params = [('inname', 'inname_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/moderator-only',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_required_get(client):
    """Test case for tags_required_get

    
    """
    params = [('inname', 'inname_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/required',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_synonyms_get(client):
    """Test case for tags_synonyms_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/synonyms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tag_top_answerers_period_get(client):
    """Test case for tags_tag_top_answerers_period_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/{tag}/top-answerers/{period}'.format(tag='tag_example', period='period_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tag_top_askers_period_get(client):
    """Test case for tags_tag_top_askers_period_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/{tag}/top-askers/{period}'.format(tag='tag_example', period='period_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tags_faq_get(client):
    """Test case for tags_tags_faq_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/{tags}/faq'.format(tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tags_info_get(client):
    """Test case for tags_tags_info_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/{tags}/info'.format(tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tags_related_get(client):
    """Test case for tags_tags_related_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/{tags}/related'.format(tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tags_synonyms_get(client):
    """Test case for tags_tags_synonyms_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/{tags}/synonyms'.format(tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tags_wikis_get(client):
    """Test case for tags_tags_wikis_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/tags/{tags}/wikis'.format(tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    
    """
    params = [('inname', 'inname_example'),
                    ('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_inbox_get(client):
    """Test case for users_id_inbox_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/inbox'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_inbox_unread_get(client):
    """Test case for users_id_inbox_unread_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example'),
                    ('since', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/inbox/unread'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_notifications_get(client):
    """Test case for users_id_notifications_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/notifications'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_notifications_unread_get(client):
    """Test case for users_id_notifications_unread_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/notifications/unread'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_privileges_get(client):
    """Test case for users_id_privileges_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/privileges'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_reputation_history_full_get(client):
    """Test case for users_id_reputation_history_full_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/reputation-history/full'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_tags_tags_top_answers_get(client):
    """Test case for users_id_tags_tags_top_answers_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/tags/{tags}/top-answers'.format(id=56, tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_tags_tags_top_questions_get(client):
    """Test case for users_id_tags_tags_top_questions_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/tags/{tags}/top-questions'.format(id=56, tags='tags_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_top_answer_tags_get(client):
    """Test case for users_id_top_answer_tags_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/top-answer-tags'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_top_question_tags_get(client):
    """Test case for users_id_top_question_tags_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/top-question-tags'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_write_permissions_get(client):
    """Test case for users_id_write_permissions_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{id}/write-permissions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_answers_get(client):
    """Test case for users_ids_answers_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/answers'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_associated_get(client):
    """Test case for users_ids_associated_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/associated'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_badges_get(client):
    """Test case for users_ids_badges_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/badges'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_comments_get(client):
    """Test case for users_ids_comments_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/comments'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_comments_toid_get(client):
    """Test case for users_ids_comments_toid_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/comments/{toid}'.format(ids='ids_example', toid=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_favorites_get(client):
    """Test case for users_ids_favorites_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/favorites'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_get(client):
    """Test case for users_ids_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_mentioned_get(client):
    """Test case for users_ids_mentioned_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/mentioned'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_merges_get(client):
    """Test case for users_ids_merges_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/merges'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_questions_featured_get(client):
    """Test case for users_ids_questions_featured_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/questions/featured'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_questions_get(client):
    """Test case for users_ids_questions_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/questions'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_questions_no_answers_get(client):
    """Test case for users_ids_questions_no_answers_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/questions/no-answers'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_questions_unaccepted_get(client):
    """Test case for users_ids_questions_unaccepted_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/questions/unaccepted'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_questions_unanswered_get(client):
    """Test case for users_ids_questions_unanswered_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/questions/unanswered'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_reputation_get(client):
    """Test case for users_ids_reputation_get

    
    """
    params = [('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/reputation'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_reputation_history_get(client):
    """Test case for users_ids_reputation_history_get

    
    """
    params = [('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/reputation-history'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_suggested_edits_get(client):
    """Test case for users_ids_suggested_edits_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/suggested-edits'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_tags_get(client):
    """Test case for users_ids_tags_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/tags'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ids_timeline_get(client):
    """Test case for users_ids_timeline_get

    
    """
    params = [('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/{ids}/timeline'.format(ids='ids_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_moderators_elected_get(client):
    """Test case for users_moderators_elected_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/moderators/elected',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_moderators_get(client):
    """Test case for users_moderators_get

    
    """
    params = [('order', 'order_example'),
                    ('max', 'max_example'),
                    ('min', 'min_example'),
                    ('sort', 'sort_example'),
                    ('fromdate', 56),
                    ('todate', 56),
                    ('pagesize', 56),
                    ('page', 56),
                    ('filter', 'filter_example'),
                    ('callback', 'param_callback_example'),
                    ('site', 'site_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/2.0/users/moderators',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

