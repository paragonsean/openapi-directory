from typing import List, Dict
from aiohttp import web

from openapi_server.models.post import Post
from openapi_server.models.post_input import PostInput
from openapi_server.models.postresponse import Postresponse
from openapi_server.models.posts import Posts
from openapi_server import util


async def create_post(request: web.Request, vestorly_auth, post, access_token=None) -> web.Response:
    """create_post

    Create a new post in the Vestorly Platform

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param post: Post you want to create
    :type post: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    post = PostInput.from_dict(post)
    return web.Response(status=200)


async def find_posts(request: web.Request, vestorly_auth, access_token=None, text_query=None, external_url=None, is_published=None) -> web.Response:
    """find_posts

    Query all posts

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str
    :param text_query: Filter post by parameters
    :type text_query: str
    :param external_url: Filter by External URL
    :type external_url: str
    :param is_published: Filter by is_published boolean
    :type is_published: str

    """
    return web.Response(status=200)


async def get_post_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """get_post_by_id

    Query all posts

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: ID of post to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def update_post_by_id(request: web.Request, vestorly_auth, id, post, access_token=None) -> web.Response:
    """update_post_by_id

    Update A Post

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of post to update
    :type id: str
    :param post: Post you want to update
    :type post: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    post = Post.from_dict(post)
    return web.Response(status=200)
