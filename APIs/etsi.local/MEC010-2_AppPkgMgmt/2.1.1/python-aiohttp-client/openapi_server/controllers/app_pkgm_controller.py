from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_d import AppD
from openapi_server.models.app_pkg_info import AppPkgInfo
from openapi_server.models.app_pkg_info_modifications import AppPkgInfoModifications
from openapi_server.models.app_pkg_subscription import AppPkgSubscription
from openapi_server.models.app_pkg_subscription_info import AppPkgSubscriptionInfo
from openapi_server.models.app_pkg_subscription_link_list import AppPkgSubscriptionLinkList
from openapi_server.models.create_app_pkg import CreateAppPkg
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def app_dget(request: web.Request, app_did, filter=None, all_fields=None, fields=None, exclude_fields=None, exclude_default=None) -> web.Response:
    """Reads the content of the AppD of on-boarded individual application package resources.

    Reads the content of the AppD of on-boarded individual application package resources.

    :param app_did: Identifier of an application descriptor
    :type app_did: str
    :param filter: Attribute-based filtering parameters according to ETSI GS MEC 009
    :type filter: str
    :param all_fields: Include all complex attributes in the response.
    :type all_fields: str
    :param fields: Complex attributes of AppPkgInfo to be included into the response
    :type fields: str
    :param exclude_fields: Complex attributes of AppPkgInfo to be excluded from the response.
    :type exclude_fields: str
    :param exclude_default: Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    :type exclude_default: str

    """
    return web.Response(status=200)


async def app_did_get(request: web.Request, app_did) -> web.Response:
    """Fetch the onboarded application package content identified by appPkgId or appDId.

    Fetch the onboarded application package content identified by appPkgId or appDId.

    :param app_did: Identifier of an application descriptor
    :type app_did: str

    """
    return web.Response(status=200)


async def app_did_put(request: web.Request, app_did, body=None) -> web.Response:
    """Uploads the content of application package.

    Uploads the content of application package.

    :param app_did: Identifier of an application descriptor
    :type app_did: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def app_package_delete(request: web.Request, app_pkg_id) -> web.Response:
    """Deletes an individual application package resources

    Deletes an individual application package resources

    :param app_pkg_id: Identifier of an individual application package resource
    :type app_pkg_id: str

    """
    return web.Response(status=200)


async def app_package_get(request: web.Request, app_pkg_id) -> web.Response:
    """Queries the information related to individual application package resources

    Queries the information related to individual application package resources

    :param app_pkg_id: Identifier of an individual application package resource
    :type app_pkg_id: str

    """
    return web.Response(status=200)


async def app_package_patch(request: web.Request, app_pkg_id, body) -> web.Response:
    """Updates the operational state of an individual application package resource

    Updates the operational state of an individual application package resources

    :param app_pkg_id: Identifier of an individual application package resource
    :type app_pkg_id: str
    :param body: Operational state to be set
    :type body: dict | bytes

    """
    body = AppPkgInfoModifications.from_dict(body)
    return web.Response(status=200)


async def app_packages_get(request: web.Request, filter=None, all_fields=None, fields=None, exclude_fields=None, exclude_default=None) -> web.Response:
    """Queries information relating to on-boarded application packages in the MEO

    queries information relating to on-boarded application packages in the MEO

    :param filter: Attribute-based filtering parameters according to ETSI GS MEC 009
    :type filter: str
    :param all_fields: Include all complex attributes in the response.
    :type all_fields: str
    :param fields: Complex attributes of AppPkgInfo to be included into the response
    :type fields: str
    :param exclude_fields: Complex attributes of AppPkgInfo to be excluded from the response.
    :type exclude_fields: str
    :param exclude_default: Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    :type exclude_default: str

    """
    return web.Response(status=200)


async def app_packages_post(request: web.Request, body) -> web.Response:
    """Create a resource for on-boarding an application package to a MEO

    Create a resource for on-boarding an application package to a MEO

    :param body: Resource to be created
    :type body: dict | bytes

    """
    body = CreateAppPkg.from_dict(body)
    return web.Response(status=200)


async def app_pkg_get(request: web.Request, app_pkg_id) -> web.Response:
    """Fetch the onboarded application package content identified by appPkgId or appDId.

    Fetch the onboarded application package content identified by appPkgId or appDId.

    :param app_pkg_id: Identifier of an on-boarded individual application package
    :type app_pkg_id: str

    """
    return web.Response(status=200)


async def app_pkg_id_get(request: web.Request, app_pkg_id, filter=None, all_fields=None, fields=None, exclude_fields=None, exclude_default=None) -> web.Response:
    """Reads the content of the AppD of on-boarded individual application package resources.

    Reads the content of the AppD of on-boarded individual application package resources.

    :param app_pkg_id: Identifier of an on-boarded individual application package
    :type app_pkg_id: str
    :param filter: Attribute-based filtering parameters according to ETSI GS MEC 009
    :type filter: str
    :param all_fields: Include all complex attributes in the response.
    :type all_fields: str
    :param fields: Complex attributes of AppPkgInfo to be included into the response
    :type fields: str
    :param exclude_fields: Complex attributes of AppPkgInfo to be excluded from the response.
    :type exclude_fields: str
    :param exclude_default: Indicates to exclude the following complex attributes of AppPkgInfo from the response.
    :type exclude_default: str

    """
    return web.Response(status=200)


async def app_pkg_put(request: web.Request, app_pkg_id, body=None) -> web.Response:
    """Uploads the content of application package.

    Uploads the content of application package.

    :param app_pkg_id: Identifier of an on-boarded individual application package
    :type app_pkg_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def individual_subscription_delete(request: web.Request, subscription_id) -> web.Response:
    """Deletes the individual subscription to notifications about application package changes in MEO.

    Deletes the individual subscription to notifications about application package changes in MEO.

    :param subscription_id: Identifier of an individual subscription to notifications about application package changes
    :type subscription_id: str

    """
    return web.Response(status=200)


async def individual_subscription_get(request: web.Request, subscription_id) -> web.Response:
    """Used to represent an individual subscription to notifications about application package changes.

    Used to represent an individual subscription to notifications about application package changes.

    :param subscription_id: Identifier of an individual subscription to notifications about application package changes
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_get(request: web.Request, ) -> web.Response:
    """used to retrieve the information of subscriptions to individual application package resource in MEO

    used to retrieve the information of subscriptions to individual application package resource in MEO package


    """
    return web.Response(status=200)


async def subscriptions_post(request: web.Request, body) -> web.Response:
    """Subscribe to notifications about on-boarding an application package

    Subscribe to notifications about on-boarding an application package

    :param body: The input parameters of subscribe operation to notifications
    :type body: dict | bytes

    """
    body = AppPkgSubscription.from_dict(body)
    return web.Response(status=200)
