from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_deployment_resource_entity import ProductDeploymentResourceEntity
from openapi_server.models.product_deployments_boot_strap_request import ProductDeploymentsBootStrapRequest
from openapi_server.models.product_deployments_deploy_request import ProductDeploymentsDeployRequest
from openapi_server.models.product_deployments_list import ProductDeploymentsList
from openapi_server.models.product_deployments_unlock_request import ProductDeploymentsUnlockRequest
from openapi_server import util


async def product_deployments_boot_strap(request: web.Request, subscription_id, product_id, api_version, bootstrap_action_parameter) -> web.Response:
    """product_deployments_boot_strap

    Invokes bootstrap action on the product deployment

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param bootstrap_action_parameter: Represents bootstrap action parameter
    :type bootstrap_action_parameter: dict | bytes

    """
    bootstrap_action_parameter = ProductDeploymentsBootStrapRequest.from_dict(bootstrap_action_parameter)
    return web.Response(status=200)


async def product_deployments_deploy(request: web.Request, subscription_id, product_id, api_version, deploy_action_parameter) -> web.Response:
    """product_deployments_deploy

    Invokes deploy action on the product

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param deploy_action_parameter: Represents bootstrap action parameter
    :type deploy_action_parameter: dict | bytes

    """
    deploy_action_parameter = ProductDeploymentsDeployRequest.from_dict(deploy_action_parameter)
    return web.Response(status=200)


async def product_deployments_get(request: web.Request, subscription_id, api_version, product_id) -> web.Response:
    """product_deployments_get

    Invokes bootstrap action on the product deployment

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param product_id: The product identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def product_deployments_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """product_deployments_list

    Invokes bootstrap action on the product deployment

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_deployments_lock(request: web.Request, subscription_id, product_id, api_version) -> web.Response:
    """product_deployments_lock

    locks the product subscription

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_deployments_remove(request: web.Request, subscription_id, product_id, api_version) -> web.Response:
    """product_deployments_remove

    Invokes remove action on the product deployment

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_deployments_rotate_secrets(request: web.Request, subscription_id, product_id, api_version) -> web.Response:
    """product_deployments_rotate_secrets

    Invokes rotate secrets action on the product deployment

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_deployments_unlock(request: web.Request, subscription_id, product_id, api_version, unlock_action_parameter) -> web.Response:
    """product_deployments_unlock

    Unlocks the product subscription

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param unlock_action_parameter: Represents bootstrap action parameter
    :type unlock_action_parameter: dict | bytes

    """
    unlock_action_parameter = ProductDeploymentsUnlockRequest.from_dict(unlock_action_parameter)
    return web.Response(status=200)
