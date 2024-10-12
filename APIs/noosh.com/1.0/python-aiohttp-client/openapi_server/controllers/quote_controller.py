from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.object_state_list_vo import ObjectStateListVO
from openapi_server.models.quote_expand_vo import QuoteExpandVO
from openapi_server.models.quote_list_vo import QuoteListVO
from openapi_server.models.quote_of_wg_level_simple_vo import QuoteOfWgLevelSimpleVO
from openapi_server.models.quote_put_persist_vo import QuotePutPersistVO
from openapi_server import util


async def get_quote(request: web.Request, workgroup_id, project_id, quote_id) -> web.Response:
    """Get a specific quote of project

    Get a specific quote of project

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param quote_id: 
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_quote_list(request: web.Request, workgroup_id, project_id, quote_state_id_use_filtersquote_state_id111111=None) -> web.Response:
    """List the quotes

    List the quotes

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param quote_state_id_use_filtersquote_state_id111111: Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value
    :type quote_state_id_use_filtersquote_state_id111111: str

    """
    return web.Response(status=200)


async def get_quote_state_list(request: web.Request, workgroup_id) -> web.Response:
    """List the quote states

    List the quote states

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def put_quote(request: web.Request, workgroup_id, project_id, quote_id, body=None) -> web.Response:
    """Accept / Reject a Quote

    Accept / Reject a Quote

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param quote_id: 
    :type quote_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = QuotePutPersistVO.from_dict(body)
    return web.Response(status=200)


async def v1_workgroups_workgroup_id_quotes_get(request: web.Request, workgroup_id, quote_state_id_use_filtersquote_state_id111111=None) -> web.Response:
    """List the quotes of workgroup level

    List the quotes of workgroup level

    :param workgroup_id: 
    :type workgroup_id: str
    :param quote_state_id_use_filtersquote_state_id111111: Quote Object State Id, use /workgroups/{workgroup_id}/quoteStates to get correct value
    :type quote_state_id_use_filtersquote_state_id111111: str

    """
    return web.Response(status=200)
