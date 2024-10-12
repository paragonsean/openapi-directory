from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill import Bill
from openapi_server.models.bill_include import BillInclude
from openapi_server.models.bill_list import BillList
from openapi_server.models.bill_sort_option import BillSortOption
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def bill_detail_bills_jurisdiction_session_bill_id_get(request: web.Request, jurisdiction, session, bill_id, include=None, apikey=None, x_api_key=None) -> web.Response:
    """Bill Detail

    Obtain bill information based on (state, session, bill_id).

    :param jurisdiction: 
    :type jurisdiction: str
    :param session: 
    :type session: str
    :param bill_id: 
    :type bill_id: str
    :param include: 
    :type include: list | bytes
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    include = [BillInclude.from_dict(d) for d in include]
    return web.Response(status=200)


async def bill_detail_by_id_bills_ocd_bill_openstates_bill_id_get(request: web.Request, openstates_bill_id, include=None, apikey=None, x_api_key=None) -> web.Response:
    """Bill Detail By Id

    Obtain bill information by internal ID in the format ocd-bill/*uuid*.

    :param openstates_bill_id: 
    :type openstates_bill_id: str
    :param include: 
    :type include: list | bytes
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    include = [BillInclude.from_dict(d) for d in include]
    return web.Response(status=200)


async def bills_search_bills_get(request: web.Request, jurisdiction=None, session=None, chamber=None, identifier=None, classification=None, subject=None, updated_since=None, created_since=None, action_since=None, sort=None, sponsor=None, sponsor_classification=None, q=None, include=None, page=None, per_page=None, apikey=None, x_api_key=None) -> web.Response:
    """Bills Search

    Search for bills matching given criteria.  Must either specify a jurisdiction or a full text query (q).  Additional parameters will futher restrict bills returned.

    :param jurisdiction: Filter by jurisdiction name or ID.
    :type jurisdiction: str
    :param session: Filter by session identifier.
    :type session: str
    :param chamber: Filter by chamber of origination.
    :type chamber: str
    :param identifier: Filter to only include bills with this identifier.
    :type identifier: List[str]
    :param classification: Filter by classification, e.g. bill or resolution
    :type classification: str
    :param subject: Filter by one or more subjects.
    :type subject: List[str]
    :param updated_since: Filter to only include bills with updates since a given date.
    :type updated_since: str
    :param created_since: Filter to only include bills created since a given date.
    :type created_since: str
    :param action_since: Filter to only include bills with an action since a given date.
    :type action_since: str
    :param sort: Desired sort order for bill results.
    :type sort: dict | bytes
    :param sponsor: Filter to only include bills sponsored by a given name or person ID.
    :type sponsor: str
    :param sponsor_classification: Filter matched sponsors to only include particular types of sponsorships.
    :type sponsor_classification: str
    :param q: Filter by full text search term.
    :type q: str
    :param include: Additional information to include in response.
    :type include: list | bytes
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    sort = .from_dict(sort)
    include = [BillInclude.from_dict(d) for d in include]
    return web.Response(status=200)
