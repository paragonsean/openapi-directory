from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_users_payload import AddUsersPayload
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.lab import Lab
from openapi_server.models.lab_fragment import LabFragment
from openapi_server.models.response_with_continuation_lab import ResponseWithContinuationLab
from openapi_server import util


async def labs_add_users(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, api_version, add_users_payload) -> web.Response:
    """labs_add_users

    Add users to a lab

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param add_users_payload: Payload for Add Users operation on a Lab.
    :type add_users_payload: dict | bytes

    """
    add_users_payload = AddUsersPayload.from_dict(add_users_payload)
    return web.Response(status=200)


async def labs_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, api_version, lab) -> web.Response:
    """labs_create_or_update

    Create or replace an existing Lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab: Represents a lab.
    :type lab: dict | bytes

    """
    lab = Lab.from_dict(lab)
    return web.Response(status=200)


async def labs_delete(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, api_version) -> web.Response:
    """labs_delete

    Delete lab. This operation can take a while to complete

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def labs_get(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, api_version, expand=None) -> web.Response:
    """labs_get

    Get lab

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;maxUsersInLab)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def labs_list(request: web.Request, subscription_id, resource_group_name, lab_account_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """labs_list

    List labs in a given lab account.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;maxUsersInLab)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def labs_register(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, api_version) -> web.Response:
    """labs_register

    Register to managed lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def labs_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, lab_name, api_version, lab) -> web.Response:
    """labs_update

    Modify properties of labs.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param lab: Represents a lab.
    :type lab: dict | bytes

    """
    lab = LabFragment.from_dict(lab)
    return web.Response(status=200)
