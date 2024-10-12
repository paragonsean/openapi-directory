from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.company_board_members_multi import CompanyBoardMembersMulti
from openapi_server.models.company_board_members_result import CompanyBoardMembersResult
from openapi_server.models.company_credit_decision_result import CompanyCreditDecisionResult
from openapi_server.models.company_economy_overview_multi import CompanyEconomyOverviewMulti
from openapi_server.models.company_economy_overview_result import CompanyEconomyOverviewResult
from openapi_server.models.company_event_request_body import CompanyEventRequestBody
from openapi_server.models.company_event_result import CompanyEventResult
from openapi_server.models.company_lookup_request_body import CompanyLookupRequestBody
from openapi_server.models.company_overview_multi import CompanyOverviewMulti
from openapi_server.models.company_overview_result import CompanyOverviewResult
from openapi_server.models.company_signatory_multi import CompanySignatoryMulti
from openapi_server.models.company_signatory_result import CompanySignatoryResult
from openapi_server.models.not_found import NotFound
from openapi_server.models.server_error import ServerError
from openapi_server import util


async def company_board_members_get(request: web.Request, country_code, company_id) -> web.Response:
    """company_board_members_get

    

    :param country_code: Country code for the company
    :type country_code: str
    :param company_id: Company identification for the company
    :type company_id: str

    """
    return web.Response(status=200)


async def company_board_members_post(request: web.Request, country_code, body) -> web.Response:
    """company_board_members_post

    

    :param country_code: Country code for the company
    :type country_code: str
    :param body: Request body with company identifiers to lookup
    :type body: dict | bytes

    """
    body = CompanyLookupRequestBody.from_dict(body)
    return web.Response(status=200)


async def company_credit_decision_get(request: web.Request, country_code, company_id, template) -> web.Response:
    """company_credit_decision_get

    

    :param country_code: Country code for the company
    :type country_code: str
    :param company_id: Company identification for the company
    :type company_id: str
    :param template: Template for credit decision
    :type template: str

    """
    return web.Response(status=200)


async def company_economy_overview_get(request: web.Request, country_code, company_id) -> web.Response:
    """company_economy_overview_get

    

    :param country_code: Country code for the company
    :type country_code: str
    :param company_id: Company identification for the company
    :type company_id: str

    """
    return web.Response(status=200)


async def company_economy_overview_post(request: web.Request, country_code, body) -> web.Response:
    """company_economy_overview_post

    

    :param country_code: Country code for the company
    :type country_code: str
    :param body: Request body with company identifiers to lookup
    :type body: dict | bytes

    """
    body = CompanyLookupRequestBody.from_dict(body)
    return web.Response(status=200)


async def company_event_post(request: web.Request, country_code, body) -> web.Response:
    """company_event_post

    

    :param country_code: Country code for the company
    :type country_code: str
    :param body: Request body with company identifiers to lookup
    :type body: dict | bytes

    """
    body = CompanyEventRequestBody.from_dict(body)
    return web.Response(status=200)


async def company_overview_get(request: web.Request, country_code, company_id) -> web.Response:
    """company_overview_get

    

    :param country_code: Country code for the company
    :type country_code: str
    :param company_id: Company identification for the company
    :type company_id: str

    """
    return web.Response(status=200)


async def company_overview_post(request: web.Request, country_code, body) -> web.Response:
    """company_overview_post

    

    :param country_code: Country code for the company
    :type country_code: str
    :param body: Request body with company identifiers to lookup
    :type body: dict | bytes

    """
    body = CompanyLookupRequestBody.from_dict(body)
    return web.Response(status=200)


async def company_signatory_get(request: web.Request, country_code, company_id) -> web.Response:
    """company_signatory_get

    

    :param country_code: Country code for the company
    :type country_code: str
    :param company_id: Company identification for the company
    :type company_id: str

    """
    return web.Response(status=200)


async def company_signatory_post(request: web.Request, country_code, body) -> web.Response:
    """company_signatory_post

    

    :param country_code: Country code for the company
    :type country_code: str
    :param body: Request body with company identifiers to lookup
    :type body: dict | bytes

    """
    body = CompanyLookupRequestBody.from_dict(body)
    return web.Response(status=200)


async def company_simple_search_get(request: web.Request, country_code, company_name=None, town=None) -> web.Response:
    """company_simple_search_get

    

    :param country_code: Country code for the company
    :type country_code: str
    :param company_name: Company name
    :type company_name: str
    :param town: Town
    :type town: str

    """
    return web.Response(status=200)
