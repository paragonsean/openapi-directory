from typing import List, Dict
from aiohttp import web

from openapi_server.models.database_instance import DatabaseInstance
from openapi_server.models.database_instance_collection import DatabaseInstanceCollection
from openapi_server import util


async def database_instances_enumerate_database_instances(request: web.Request, subscription_id, resource_group_name, migrate_project_name, api_version, continuation_token=None, page_size=None, accept_language=None) -> web.Response:
    """Gets a list of database instances in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param continuation_token: The continuation token.
    :type continuation_token: str
    :param page_size: The number of items to be returned in a single page. This value is honored only if it is less than the 100.
    :type page_size: int
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)


async def database_instances_get_database_instance(request: web.Request, subscription_id, resource_group_name, migrate_project_name, database_instance_name, api_version, accept_language=None) -> web.Response:
    """Gets a database instance in the migrate project.

    

    :param subscription_id: Azure Subscription Id in which migrate project was created.
    :type subscription_id: str
    :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
    :type resource_group_name: str
    :param migrate_project_name: Name of the Azure Migrate project.
    :type migrate_project_name: str
    :param database_instance_name: Unique name of a database instance in Azure migration hub.
    :type database_instance_name: str
    :param api_version: Standard request header. Used by service to identify API version used by client.
    :type api_version: str
    :param accept_language: Standard request header. Used by service to respond to client in appropriate language.
    :type accept_language: str

    """
    return web.Response(status=200)
