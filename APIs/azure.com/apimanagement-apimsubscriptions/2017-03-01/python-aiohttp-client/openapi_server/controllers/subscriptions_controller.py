from typing import List, Dict
from aiohttp import web

from openapi_server.models.subscription_collection import SubscriptionCollection
from openapi_server.models.subscription_contract import SubscriptionContract
from openapi_server.models.subscription_create_parameters import SubscriptionCreateParameters
from openapi_server.models.subscription_list_default_response import SubscriptionListDefaultResponse
from openapi_server.models.subscription_update_parameters import SubscriptionUpdateParameters
from openapi_server import util


async def subscription_create_or_update(request: web.Request, sid, api_version, parameters, notify=None) -> web.Response:
    """subscription_create_or_update

    Creates or updates the subscription of specified user to the specified product.

    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes
    :param notify: Notify the subscriber of the subscription state change to Submitted or Active state.
    :type notify: str

    """
    parameters = SubscriptionCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def subscription_delete(request: web.Request, sid, if_match, api_version) -> web.Response:
    """subscription_delete

    Deletes the specified subscription.

    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param if_match: ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscription_get(request: web.Request, sid, api_version) -> web.Response:
    """subscription_get

    Gets the specified Subscription entity.

    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscription_list(request: web.Request, api_version, filter=None, top=None, skip=None) -> web.Response:
    """subscription_list

    Lists all subscriptions of the API Management service instance.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param filter: | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def subscription_regenerate_primary_key(request: web.Request, sid, api_version) -> web.Response:
    """subscription_regenerate_primary_key

    Regenerates primary key of existing subscription of the API Management service instance.

    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscription_regenerate_secondary_key(request: web.Request, sid, api_version) -> web.Response:
    """subscription_regenerate_secondary_key

    Regenerates secondary key of existing subscription of the API Management service instance.

    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def subscription_update(request: web.Request, sid, if_match, api_version, parameters, notify=None) -> web.Response:
    """subscription_update

    Updates the details of a subscription specified by its identifier.

    :param sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    :type sid: str
    :param if_match: ETag of the Subscription Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes
    :param notify: Notify the subscriber of the subscription state change to Submitted or Active state.
    :type notify: str

    """
    parameters = SubscriptionUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
