from typing import List, Dict
from aiohttp import web

from openapi_server.models.community_content_get_community_content200_response import CommunityContentGetCommunityContent200Response
from openapi_server.models.forum_get_forum_tag_suggestions200_response import ForumGetForumTagSuggestions200Response
from openapi_server.models.forum_get_recruitment_thread_summaries200_response import ForumGetRecruitmentThreadSummaries200Response
from openapi_server.models.forum_get_topic_for_content200_response import ForumGetTopicForContent200Response
from openapi_server import util


async def forum_get_core_topics_paged(request: web.Request, category_filter, page, quick_date, sort, locales=None) -> web.Response:
    """forum_get_core_topics_paged

    Gets a listing of all topics marked as part of the core group.

    :param category_filter: The category filter.
    :type category_filter: int
    :param page: Zero base page
    :type page: int
    :param quick_date: The date filter.
    :type quick_date: int
    :param sort: The sort mode.
    :type sort: int
    :param locales: Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39;
    :type locales: str

    """
    return web.Response(status=200)


async def forum_get_forum_tag_suggestions(request: web.Request, partialtag=None) -> web.Response:
    """forum_get_forum_tag_suggestions

    Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

    :param partialtag: The partial tag input to generate suggestions from.
    :type partialtag: str

    """
    return web.Response(status=200)


async def forum_get_poll(request: web.Request, topic_id) -> web.Response:
    """forum_get_poll

    Gets the specified forum poll.

    :param topic_id: The post id of the topic that has the poll.
    :type topic_id: int

    """
    return web.Response(status=200)


async def forum_get_post_and_parent(request: web.Request, child_post_id, showbanned=None) -> web.Response:
    """forum_get_post_and_parent

    Returns the post specified and its immediate parent.

    :param child_post_id: 
    :type child_post_id: int
    :param showbanned: If this value is not null or empty, banned posts are requested to be returned
    :type showbanned: str

    """
    return web.Response(status=200)


async def forum_get_post_and_parent_awaiting_approval(request: web.Request, child_post_id, showbanned=None) -> web.Response:
    """forum_get_post_and_parent_awaiting_approval

    Returns the post specified and its immediate parent of posts that are awaiting approval.

    :param child_post_id: 
    :type child_post_id: int
    :param showbanned: If this value is not null or empty, banned posts are requested to be returned
    :type showbanned: str

    """
    return web.Response(status=200)


async def forum_get_posts_threaded_paged(request: web.Request, get_parent_post, page, page_size, parent_post_id, reply_size, root_thread_mode, sort_mode, showbanned=None) -> web.Response:
    """forum_get_posts_threaded_paged

    Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

    :param get_parent_post: 
    :type get_parent_post: bool
    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int
    :param parent_post_id: 
    :type parent_post_id: int
    :param reply_size: 
    :type reply_size: int
    :param root_thread_mode: 
    :type root_thread_mode: bool
    :param sort_mode: 
    :type sort_mode: int
    :param showbanned: If this value is not null or empty, banned posts are requested to be returned
    :type showbanned: str

    """
    return web.Response(status=200)


async def forum_get_posts_threaded_paged_from_child(request: web.Request, child_post_id, page, page_size, reply_size, root_thread_mode, sort_mode, showbanned=None) -> web.Response:
    """forum_get_posts_threaded_paged_from_child

    Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

    :param child_post_id: 
    :type child_post_id: int
    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int
    :param reply_size: 
    :type reply_size: int
    :param root_thread_mode: 
    :type root_thread_mode: bool
    :param sort_mode: 
    :type sort_mode: int
    :param showbanned: If this value is not null or empty, banned posts are requested to be returned
    :type showbanned: str

    """
    return web.Response(status=200)


async def forum_get_recruitment_thread_summaries(request: web.Request, ) -> web.Response:
    """forum_get_recruitment_thread_summaries

    Allows the caller to get a list of to 25 recruitment thread summary information objects.


    """
    return web.Response(status=200)


async def forum_get_topic_for_content(request: web.Request, content_id) -> web.Response:
    """forum_get_topic_for_content

    Gets the post Id for the given content item&#39;s comments, if it exists.

    :param content_id: 
    :type content_id: int

    """
    return web.Response(status=200)


async def forum_get_topics_paged(request: web.Request, category_filter, group, page, page_size, quick_date, sort, locales=None, tagstring=None) -> web.Response:
    """forum_get_topics_paged

    Get topics from any forum.

    :param category_filter: A category filter
    :type category_filter: int
    :param group: The group, if any.
    :type group: int
    :param page: Zero paged page number
    :type page: int
    :param page_size: Unused
    :type page_size: int
    :param quick_date: A date filter.
    :type quick_date: int
    :param sort: The sort mode.
    :type sort: int
    :param locales: Comma seperated list of locales posts must match to return in the result list. Default &#39;en&#39;
    :type locales: str
    :param tagstring: The tags to search, if any.
    :type tagstring: str

    """
    return web.Response(status=200)
