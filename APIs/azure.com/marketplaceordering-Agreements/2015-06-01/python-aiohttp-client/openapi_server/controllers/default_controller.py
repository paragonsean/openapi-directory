from typing import List, Dict
from aiohttp import web

from openapi_server.models.agreement_terms import AgreementTerms
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def marketplace_agreements_cancel(request: web.Request, api_version, subscription_id, publisher_id, offer_id, plan_id) -> web.Response:
    """marketplace_agreements_cancel

    Cancel marketplace terms.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param publisher_id: Publisher identifier string of image being deployed.
    :type publisher_id: str
    :param offer_id: Offer identifier string of image being deployed.
    :type offer_id: str
    :param plan_id: Plan identifier string of image being deployed.
    :type plan_id: str

    """
    return web.Response(status=200)


async def marketplace_agreements_create(request: web.Request, api_version, offer_type, subscription_id, publisher_id, offer_id, plan_id, parameters) -> web.Response:
    """marketplace_agreements_create

    Save marketplace terms.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param offer_type: Offer Type, currently only virtualmachine type is supported.
    :type offer_type: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param publisher_id: Publisher identifier string of image being deployed.
    :type publisher_id: str
    :param offer_id: Offer identifier string of image being deployed.
    :type offer_id: str
    :param plan_id: Plan identifier string of image being deployed.
    :type plan_id: str
    :param parameters: Parameters supplied to the Create Marketplace Terms operation.
    :type parameters: dict | bytes

    """
    parameters = AgreementTerms.from_dict(parameters)
    return web.Response(status=200)


async def marketplace_agreements_get(request: web.Request, api_version, subscription_id, offer_type, publisher_id, offer_id, plan_id) -> web.Response:
    """marketplace_agreements_get

    Get marketplace terms.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param offer_type: Offer Type, currently only virtualmachine type is supported.
    :type offer_type: str
    :param publisher_id: Publisher identifier string of image being deployed.
    :type publisher_id: str
    :param offer_id: Offer identifier string of image being deployed.
    :type offer_id: str
    :param plan_id: Plan identifier string of image being deployed.
    :type plan_id: str

    """
    return web.Response(status=200)


async def marketplace_agreements_get_agreement(request: web.Request, api_version, subscription_id, publisher_id, offer_id, plan_id) -> web.Response:
    """marketplace_agreements_get_agreement

    Get marketplace agreement.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param publisher_id: Publisher identifier string of image being deployed.
    :type publisher_id: str
    :param offer_id: Offer identifier string of image being deployed.
    :type offer_id: str
    :param plan_id: Plan identifier string of image being deployed.
    :type plan_id: str

    """
    return web.Response(status=200)


async def marketplace_agreements_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """marketplace_agreements_list

    List marketplace agreements in the subscription.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def marketplace_agreements_sign(request: web.Request, api_version, subscription_id, publisher_id, offer_id, plan_id) -> web.Response:
    """marketplace_agreements_sign

    Sign marketplace terms.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param publisher_id: Publisher identifier string of image being deployed.
    :type publisher_id: str
    :param offer_id: Offer identifier string of image being deployed.
    :type offer_id: str
    :param plan_id: Plan identifier string of image being deployed.
    :type plan_id: str

    """
    return web.Response(status=200)
