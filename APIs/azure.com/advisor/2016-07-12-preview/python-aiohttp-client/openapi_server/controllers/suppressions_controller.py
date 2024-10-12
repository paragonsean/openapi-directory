from typing import List, Dict
from aiohttp import web

from openapi_server.models.suppression_contract import SuppressionContract
from openapi_server import util


async def suppressions_create(request: web.Request, resource_uri, recommendation_id, name, api_version, suppression_contract) -> web.Response:
    """suppressions_create

    Enables the snoozed or dismissed attribute of a recommendation. The snoozed or dismissed attribute is referred to as a suppression. Use this API to create or update the snoozed or dismissed status of a recommendation.

    :param resource_uri: The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    :type resource_uri: str
    :param recommendation_id: The recommendation ID.
    :type recommendation_id: str
    :param name: The name of the suppression.
    :type name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param suppression_contract: The snoozed or dismissed attribute; for example, the snooze duration.
    :type suppression_contract: dict | bytes

    """
    suppression_contract = SuppressionContract.from_dict(suppression_contract)
    return web.Response(status=200)


async def suppressions_delete(request: web.Request, resource_uri, recommendation_id, name, api_version) -> web.Response:
    """suppressions_delete

    Enables the activation of a snoozed or dismissed recommendation. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.

    :param resource_uri: The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    :type resource_uri: str
    :param recommendation_id: The recommendation ID.
    :type recommendation_id: str
    :param name: The name of the suppression.
    :type name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def suppressions_get(request: web.Request, resource_uri, recommendation_id, name, api_version) -> web.Response:
    """suppressions_get

    Obtains the details of a suppression.

    :param resource_uri: The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    :type resource_uri: str
    :param recommendation_id: The recommendation ID.
    :type recommendation_id: str
    :param name: The name of the suppression.
    :type name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def suppressions_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """suppressions_list

    Retrieves the list of snoozed or dismissed suppressions for a subscription. The snoozed or dismissed attribute of a recommendation is referred to as a suppression.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
