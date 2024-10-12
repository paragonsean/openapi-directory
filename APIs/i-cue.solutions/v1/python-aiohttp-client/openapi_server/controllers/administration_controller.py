from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_response import EntityResponse
from openapi_server.models.json_forecast_response import JsonForecastResponse
from openapi_server.models.method_dto import MethodDto
from openapi_server.models.new_entity_request import NewEntityRequest
from openapi_server.models.new_model_request import NewModelRequest
from openapi_server.models.new_token_request import NewTokenRequest
from openapi_server.models.new_user_request import NewUserRequest
from openapi_server.models.toggle_request import ToggleRequest
from openapi_server.models.toggle_user_request import ToggleUserRequest
from openapi_server import util


async def administration_entity_get(request: web.Request, token=None) -> web.Response:
    """Get all organizations

    This is an iCUE only endpoint or Enterprise feature.

    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_entity_id_delete(request: web.Request, id, token=None) -> web.Response:
    """Delete organization

    This is an iCUE only endpoint or Enterprise feature.

    :param id: 
    :type id: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_entity_post(request: web.Request, token=None, body=None) -> web.Response:
    """Create organization

    This is an iCUE only endpoint or Enterprise feature.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewEntityRequest.from_dict(body)
    return web.Response(status=200)


async def administration_entity_put(request: web.Request, token=None, body=None) -> web.Response:
    """Pause organization

    This is an iCUE only endpoint or Enterprise feature.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ToggleRequest.from_dict(body)
    return web.Response(status=200)


async def administration_file_to_json_post(request: web.Request, file, periodicity, token=None) -> web.Response:
    """Transform data file to JSON format

    Transform data file to JSON format

    :param file: 
    :type file: str
    :param periodicity: 
    :type periodicity: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_model_entity_id_get(request: web.Request, entity_id, token=None) -> web.Response:
    """Get Models for Organization

    Returns models registered for Organization

    :param entity_id: 
    :type entity_id: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_model_entity_id_post(request: web.Request, entity_id, token=None, body=None) -> web.Response:
    """Register new forecasting model

    Register new forecasting model for single organziation

    :param entity_id: 
    :type entity_id: int
    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewModelRequest.from_dict(body)
    return web.Response(status=200)


async def administration_model_get(request: web.Request, token=None) -> web.Response:
    """Get all common Models

    Returns models that are common for all Organizations

    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_model_post(request: web.Request, token=None, body=None) -> web.Response:
    """Register new forecasting model

    Register new forecasting model for all organziations

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewModelRequest.from_dict(body)
    return web.Response(status=200)


async def administration_planning_level_entity_id_id_delete(request: web.Request, entity_id, id, token=None) -> web.Response:
    """Delete planning level

    Delete planning level. This is an Enterprise feature.

    :param entity_id: 
    :type entity_id: int
    :param id: 
    :type id: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_planning_level_lock_post(request: web.Request, token=None) -> web.Response:
    """Lock planning level

    Lock planning level against modification. This is an Enterprise feature.

    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_token_post(request: web.Request, token=None, body=None) -> web.Response:
    """Issue a token

    This is an iCUE only endpoint.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewTokenRequest.from_dict(body)
    return web.Response(status=200)


async def administration_user_entity_id_get(request: web.Request, entity_id, token=None) -> web.Response:
    """Get all users

    Get all users

    :param entity_id: 
    :type entity_id: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_user_entity_id_id_delete(request: web.Request, entity_id, id, token=None) -> web.Response:
    """Delete user

    Delete user

    :param entity_id: 
    :type entity_id: int
    :param id: 
    :type id: int
    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)


async def administration_user_lock_put(request: web.Request, token=None, body=None) -> web.Response:
    """Lock user

    After lock user won&#39;t be able to use iCUE API endpoints.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ToggleUserRequest.from_dict(body)
    return web.Response(status=200)


async def administration_user_post(request: web.Request, token=None, body=None) -> web.Response:
    """Create user

    Create new user for entity/organization. This can be done by entity administrator.

    :param token: User Authentication Token
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewUserRequest.from_dict(body)
    return web.Response(status=200)


async def administration_user_put(request: web.Request, token=None) -> web.Response:
    """Update user

    Update user

    :param token: User Authentication Token
    :type token: str

    """
    return web.Response(status=200)
