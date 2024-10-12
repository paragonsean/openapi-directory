from typing import List, Dict
from aiohttp import web

from openapi_server.models.actor import Actor
from openapi_server.models.actor_post import ActorPost
from openapi_server.models.crew import Crew
from openapi_server.models.post_result import PostResult
from openapi_server.models.tv_show_actor import TVShowActor
from openapi_server import util


async def actor_get(request: web.Request, accesstoken, query) -> web.Response:
    """Returns data on queried actor/actress. Result set limited to 5 records

    

    :param accesstoken: 
    :type accesstoken: str
    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def actor_in_shows_get(request: web.Request, access_token, actor) -> web.Response:
    """Returns all shows queried actor/actress is or has been in

    

    :param access_token: 
    :type access_token: str
    :param actor: Part of, or full name of actor
    :type actor: str

    """
    return web.Response(status=200)


async def actors_in_tv_show_get(request: web.Request, accesstoken, show_name) -> web.Response:
    """Returns all actors in queried tvshow

    

    :param accesstoken: 
    :type accesstoken: str
    :param show_name: 
    :type show_name: str

    """
    return web.Response(status=200)


async def add_actor_post(request: web.Request, value) -> web.Response:
    """Add new actor or actress to database

    

    :param value: 
    :type value: dict | bytes

    """
    value = ActorPost.from_dict(value)
    return web.Response(status=200)


async def cast_by_actor_get(request: web.Request, access_token, actor) -> web.Response:
    """Returns list of show actor is appearing in

    

    :param access_token: 
    :type access_token: str
    :param actor: Full name of actor
    :type actor: str

    """
    return web.Response(status=200)


async def crew_by_id_get(request: web.Request, access_token, id) -> web.Response:
    """Get crew list by ID

    

    :param access_token: 
    :type access_token: str
    :param id: IMDBID, TVmazeID, or TVDBID
    :type id: str

    """
    return web.Response(status=200)


async def crew_by_person_get(request: web.Request, access_token, person_name) -> web.Response:
    """Gets list of productions searched person is/was involved in.

    

    :param access_token: 
    :type access_token: str
    :param person_name: 
    :type person_name: str

    """
    return web.Response(status=200)


async def crew_get(request: web.Request, access_token, phrase) -> web.Response:
    """Returns crew for queried show.

    

    :param access_token: 
    :type access_token: str
    :param phrase: Part of, or full showname to search for
    :type phrase: str

    """
    return web.Response(status=200)


async def crewby_showname_get(request: web.Request, access_token, show_name) -> web.Response:
    """Get crew list by showname

    

    :param access_token: 
    :type access_token: str
    :param show_name: Full exact showname
    :type show_name: str

    """
    return web.Response(status=200)
