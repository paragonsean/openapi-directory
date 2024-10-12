from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.formula import Formula
from openapi_server.models.response_with_continuation_formula import ResponseWithContinuationFormula
from openapi_server import util


async def formulas_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, formula) -> web.Response:
    """formulas_create_or_update

    Create or replace an existing Formula. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the formula.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param formula: A formula for creating a VM, specifying an image base and other parameters
    :type formula: dict | bytes

    """
    formula = Formula.from_dict(formula)
    return web.Response(status=200)


async def formulas_delete(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """formulas_delete

    Delete formula.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the formula.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def formulas_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, expand=None) -> web.Response:
    """formulas_get

    Get formula.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the formula.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;description)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def formulas_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """formulas_list

    List formulas in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;description)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)
