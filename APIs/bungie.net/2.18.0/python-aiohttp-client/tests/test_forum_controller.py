# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.community_content_get_community_content200_response import CommunityContentGetCommunityContent200Response
from openapi_server.models.forum_get_forum_tag_suggestions200_response import ForumGetForumTagSuggestions200Response
from openapi_server.models.forum_get_recruitment_thread_summaries200_response import ForumGetRecruitmentThreadSummaries200Response
from openapi_server.models.forum_get_topic_for_content200_response import ForumGetTopicForContent200Response


pytestmark = pytest.mark.asyncio

async def test_forum_get_core_topics_paged(client):
    """Test case for forum_get_core_topics_paged

    
    """
    params = [('locales', 'locales_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/GetCoreTopicsPaged/{page}/{sort}/{quick_date}/{category_filter}'.format(category_filter=56, page=56, quick_date=56, sort=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_forum_tag_suggestions(client):
    """Test case for forum_get_forum_tag_suggestions

    
    """
    params = [('partialtag', 'partialtag_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/GetForumTagSuggestions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_poll(client):
    """Test case for forum_get_poll

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/Poll/{topic_id}'.format(topic_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_post_and_parent(client):
    """Test case for forum_get_post_and_parent

    
    """
    params = [('showbanned', 'showbanned_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/GetPostAndParent/{child_post_id}'.format(child_post_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_post_and_parent_awaiting_approval(client):
    """Test case for forum_get_post_and_parent_awaiting_approval

    
    """
    params = [('showbanned', 'showbanned_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/GetPostAndParentAwaitingApproval/{child_post_id}'.format(child_post_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_posts_threaded_paged(client):
    """Test case for forum_get_posts_threaded_paged

    
    """
    params = [('showbanned', 'showbanned_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/GetPostsThreadedPaged/{parent_post_id}/{page}/{page_size}/{reply_size}/{get_parent_post}/{root_thread_mode}/{sort_mode}'.format(get_parent_post=True, page=56, page_size=56, parent_post_id=56, reply_size=56, root_thread_mode=True, sort_mode=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_posts_threaded_paged_from_child(client):
    """Test case for forum_get_posts_threaded_paged_from_child

    
    """
    params = [('showbanned', 'showbanned_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/GetPostsThreadedPagedFromChild/{child_post_id}/{page}/{page_size}/{reply_size}/{root_thread_mode}/{sort_mode}'.format(child_post_id=56, page=56, page_size=56, reply_size=56, root_thread_mode=True, sort_mode=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_recruitment_thread_summaries(client):
    """Test case for forum_get_recruitment_thread_summaries

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/Platform/Forum/Recruit/Summaries/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_topic_for_content(client):
    """Test case for forum_get_topic_for_content

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/GetTopicForContent/{content_id}'.format(content_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forum_get_topics_paged(client):
    """Test case for forum_get_topics_paged

    
    """
    params = [('locales', 'locales_example'),
                    ('tagstring', 'tagstring_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/Forum/GetTopicsPaged/{page}/{page_size}/{group}/{sort}/{quick_date}/{category_filter}'.format(category_filter=56, group=56, page=56, page_size=56, quick_date=56, sort=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

