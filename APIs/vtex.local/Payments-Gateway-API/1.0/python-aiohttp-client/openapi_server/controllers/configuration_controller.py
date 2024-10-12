from typing import List, Dict
from aiohttp import web

from openapi_server.models.insert_affiliation_request import InsertAffiliationRequest
from openapi_server.models.insert_rule_request import InsertRuleRequest
from openapi_server.models.payment_systems_response import PaymentSystemsResponse
from openapi_server.models.rule_by_id_request import RuleByIdRequest
from openapi_server.models.update_affiliation_request import UpdateAffiliationRequest
from openapi_server import util


async def affiliation_by_id(request: web.Request, affiliation_id, x_provider_api_app_key, x_provider_api_app_token, content_type, accept) -> web.Response:
    """Affiliation By Id

    Returns associated data for the specified affiliation Id, like name and implementation, for example.

    :param affiliation_id: 
    :type affiliation_id: str
    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str

    """
    return web.Response(status=200)


async def affiliations(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept) -> web.Response:
    """Affiliations

    Returns all affiliations that your provider can handle.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str

    """
    return web.Response(status=200)


async def available_payment_methods(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept) -> web.Response:
    """Available Payment Methods

    Returns enabled payment methods, like visa, master, bankissueinvoice that are shown for the final user and enabled to receive payment.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str

    """
    return web.Response(status=200)


async def insert_affiliation(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept, body) -> web.Response:
    """Insert Affiliation

    Creates a new affiliation and returns a successful response.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = InsertAffiliationRequest.from_dict(body)
    return web.Response(status=200)


async def insert_rule(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, body) -> web.Response:
    """Insert Rule

    Creates a new rule and returns a successful response.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = InsertRuleRequest.from_dict(body)
    return web.Response(status=200)


async def put_rule_by_id(request: web.Request, accept, content_type, x_provider_api_app_key, x_provider_api_app_token, rule_id, body) -> web.Response:
    """Rule By Id

    Update Rule.

    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param rule_id: 
    :type rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RuleByIdRequest.from_dict(body)
    return web.Response(status=200)


async def rule(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept, rule_id) -> web.Response:
    """Delete Rule

    Deletes rules by specified Id.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param rule_id: 
    :type rule_id: str

    """
    return web.Response(status=200)


async def rule_by_id(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept, rule_id) -> web.Response:
    """Rule By Id

    Returns rule by specified RuleId.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param rule_id: 
    :type rule_id: str

    """
    return web.Response(status=200)


async def rules(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, content_type, accept) -> web.Response:
    """Rules

    Returns all rules conditions your provider can handle.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str

    """
    return web.Response(status=200)


async def update_affiliation(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, affiliation_id, body) -> web.Response:
    """Update Affiliation

    Returns all affiliations.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param affiliation_id: 
    :type affiliation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAffiliationRequest.from_dict(body)
    return web.Response(status=200)
