from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.formula import Formula
from openapi_server.models.response_with_continuation_formula import ResponseWithContinuationFormula
from openapi_server import util


async def formula_create_or_update_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, formula) -> web.Response:
    """formula_create_or_update_resource

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
    :param formula: 
    :type formula: dict | bytes

    """
    formula = Formula.from_dict(formula)
    return web.Response(status=200)


async def formula_delete_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """formula_delete_resource

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


async def formula_get_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """formula_get_resource

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

    """
    return web.Response(status=200)


async def formula_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """formula_list

    List formulas.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)
