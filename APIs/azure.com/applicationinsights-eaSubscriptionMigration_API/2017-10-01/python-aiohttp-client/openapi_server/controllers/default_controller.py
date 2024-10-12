from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.ea_subscription_migration_date import EASubscriptionMigrationDate
from openapi_server import util


async def e_a_subscription_list_migration_date_post(request: web.Request, api_version, subscription_id) -> web.Response:
    """e_a_subscription_list_migration_date_post

    list date to migrate to new pricing model.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def e_a_subscription_migrate_to_new_pricing_model_post(request: web.Request, api_version, subscription_id) -> web.Response:
    """e_a_subscription_migrate_to_new_pricing_model_post

    Enterprise Agreement Customer opted to use new pricing model.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def e_a_subscription_rollback_to_legacy_pricing_model_post(request: web.Request, api_version, subscription_id) -> web.Response:
    """e_a_subscription_rollback_to_legacy_pricing_model_post

    Enterprise Agreement Customer roll back to use legacy pricing model.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
