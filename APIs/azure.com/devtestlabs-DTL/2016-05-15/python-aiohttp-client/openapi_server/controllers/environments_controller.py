from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.dtl_environment import DtlEnvironment
from openapi_server.models.response_with_continuation_dtl_environment import ResponseWithContinuationDtlEnvironment
from openapi_server import util


async def environments_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, dtl_environment) -> web.Response:
    """environments_create_or_update

    Create or replace an existing environment. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the environment.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param dtl_environment: An environment, which is essentially an ARM template deployment.
    :type dtl_environment: dict | bytes

    """
    dtl_environment = DtlEnvironment.from_dict(dtl_environment)
    return web.Response(status=200)


async def environments_delete(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version) -> web.Response:
    """environments_delete

    Delete environment. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the environment.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def environments_get(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, name, api_version, expand=None) -> web.Response:
    """environments_get

    Get environment.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param name: The name of the environment.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;deploymentProperties)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def environments_list(request: web.Request, subscription_id, resource_group_name, lab_name, user_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """environments_list

    List environments in a given user profile.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param user_name: The name of the user profile.
    :type user_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;deploymentProperties)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)
