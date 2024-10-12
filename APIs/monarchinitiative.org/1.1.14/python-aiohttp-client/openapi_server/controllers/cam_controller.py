from typing import List, Dict
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server import util


async def get_activity_collection(request: web.Request, title=None, contributor=None) -> web.Response:
    """Returns list of models

    

    :param title: string to search for in title of model
    :type title: str
    :param contributor: string to search for in contributor of model
    :type contributor: str

    """
    return web.Response(status=200)


async def get_instance_object(request: web.Request, id, title=None, contributor=None) -> web.Response:
    """Returns list of matches

    

    :param id: 
    :type id: str
    :param title: string to search for in title of model
    :type title: str
    :param contributor: string to search for in contributor of model
    :type contributor: str

    """
    return web.Response(status=200)


async def get_model_collection(request: web.Request, ) -> web.Response:
    """Returns list of ALL models

    


    """
    return web.Response(status=200)


async def get_model_contributors(request: web.Request, ) -> web.Response:
    """Returns list of all contributors across all models

    


    """
    return web.Response(status=200)


async def get_model_instances(request: web.Request, ) -> web.Response:
    """Returns list of all instances

    


    """
    return web.Response(status=200)


async def get_model_object(request: web.Request, id) -> web.Response:
    """Returns a complete model

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_model_properties(request: web.Request, title=None, contributor=None) -> web.Response:
    """Returns list of all properties used across all models

    

    :param title: string to search for in title of model
    :type title: str
    :param contributor: string to search for in contributor of model
    :type contributor: str

    """
    return web.Response(status=200)


async def get_model_property_values(request: web.Request, title=None, contributor=None) -> web.Response:
    """Returns list property-values for all models

    

    :param title: string to search for in title of model
    :type title: str
    :param contributor: string to search for in contributor of model
    :type contributor: str

    """
    return web.Response(status=200)


async def get_model_query(request: web.Request, title=None, contributor=None) -> web.Response:
    """Returns list of models matching query

    

    :param title: string to search for in title of model
    :type title: str
    :param contributor: string to search for in contributor of model
    :type contributor: str

    """
    return web.Response(status=200)


async def get_physical_interaction(request: web.Request, title=None, contributor=None) -> web.Response:
    """Returns list of models

    

    :param title: string to search for in title of model
    :type title: str
    :param contributor: string to search for in contributor of model
    :type contributor: str

    """
    return web.Response(status=200)
