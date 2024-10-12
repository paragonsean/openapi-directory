from typing import List, Dict
from aiohttp import web

from openapi_server.models.comment_for_api_contract import CommentForApiContract
from openapi_server.models.discussion_folder_contract import DiscussionFolderContract
from openapi_server.models.discussion_folder_optional_fields import DiscussionFolderOptionalFields
from openapi_server.models.discussion_topic_contract import DiscussionTopicContract
from openapi_server.models.discussion_topic_contract_partial_find_result import DiscussionTopicContractPartialFindResult
from openapi_server.models.discussion_topic_optional_fields import DiscussionTopicOptionalFields
from openapi_server.models.discussion_topic_sort_rule import DiscussionTopicSortRule
from openapi_server import util


async def api_discussions_comments_comment_id_delete(request: web.Request, comment_id) -> web.Response:
    """api_discussions_comments_comment_id_delete

    

    :param comment_id: 
    :type comment_id: int

    """
    return web.Response(status=200)


async def api_discussions_comments_comment_id_post(request: web.Request, comment_id, body=None) -> web.Response:
    """api_discussions_comments_comment_id_post

    

    :param comment_id: 
    :type comment_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_discussions_folders_folder_id_topics_get(request: web.Request, folder_id, fields=None) -> web.Response:
    """api_discussions_folders_folder_id_topics_get

    

    :param folder_id: 
    :type folder_id: int
    :param fields: 
    :type fields: dict | bytes

    """
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_discussions_folders_folder_id_topics_post(request: web.Request, folder_id, body=None) -> web.Response:
    """api_discussions_folders_folder_id_topics_post

    

    :param folder_id: 
    :type folder_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DiscussionTopicContract.from_dict(body)
    return web.Response(status=200)


async def api_discussions_folders_get(request: web.Request, fields=None) -> web.Response:
    """api_discussions_folders_get

    

    :param fields: 
    :type fields: dict | bytes

    """
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_discussions_folders_post(request: web.Request, body=None) -> web.Response:
    """api_discussions_folders_post

    

    :param body: 
    :type body: dict | bytes

    """
    body = DiscussionFolderContract.from_dict(body)
    return web.Response(status=200)


async def api_discussions_topics_get(request: web.Request, folder_id=None, start=None, max_results=None, get_total_count=None, sort=None, fields=None) -> web.Response:
    """api_discussions_topics_get

    

    :param folder_id: 
    :type folder_id: int
    :param start: 
    :type start: int
    :param max_results: 
    :type max_results: int
    :param get_total_count: 
    :type get_total_count: bool
    :param sort: 
    :type sort: dict | bytes
    :param fields: 
    :type fields: dict | bytes

    """
    sort = .from_dict(sort)
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_discussions_topics_topic_id_comments_post(request: web.Request, topic_id, body=None) -> web.Response:
    """api_discussions_topics_topic_id_comments_post

    

    :param topic_id: 
    :type topic_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CommentForApiContract.from_dict(body)
    return web.Response(status=200)


async def api_discussions_topics_topic_id_delete(request: web.Request, topic_id) -> web.Response:
    """api_discussions_topics_topic_id_delete

    

    :param topic_id: 
    :type topic_id: int

    """
    return web.Response(status=200)


async def api_discussions_topics_topic_id_get(request: web.Request, topic_id, fields=None) -> web.Response:
    """api_discussions_topics_topic_id_get

    

    :param topic_id: 
    :type topic_id: int
    :param fields: 
    :type fields: dict | bytes

    """
    fields = .from_dict(fields)
    return web.Response(status=200)


async def api_discussions_topics_topic_id_post(request: web.Request, topic_id, body=None) -> web.Response:
    """api_discussions_topics_topic_id_post

    

    :param topic_id: 
    :type topic_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DiscussionTopicContract.from_dict(body)
    return web.Response(status=200)
