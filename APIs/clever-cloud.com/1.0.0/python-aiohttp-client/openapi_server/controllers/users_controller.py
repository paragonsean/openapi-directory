from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.user import User
from openapi_server.models.wannabe_user import WannabeUser
from openapi_server import util


async def get_users_id_0(request: web.Request, id) -> web.Response:
    """get_users_id_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_users_id_applications_1(request: web.Request, id) -> web.Response:
    """get_users_id_applications_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_users_user_id_git_info_0(request: web.Request, user_id) -> web.Response:
    """get_users_user_id_git_info_0

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def post_users_0(request: web.Request, body, invitation_key=None, addon_beta_invitation_key=None, email=None, _pass=None, url_next=None, terms=None) -> web.Response:
    """post_users_0

    

    :param body: 
    :type body: dict | bytes
    :param invitation_key: 
    :type invitation_key: str
    :param addon_beta_invitation_key: 
    :type addon_beta_invitation_key: str
    :param email: 
    :type email: str
    :param _pass: 
    :type _pass: str
    :param url_next: 
    :type url_next: str
    :param terms: 
    :type terms: str

    """
    body = WannabeUser.from_dict(body)
    return web.Response(status=200)
