from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_warehouse_user_activities import DataWarehouseUserActivities
from openapi_server import util


async def data_warehouse_user_activities_get(request: web.Request, resource_group_name, server_name, database_name, data_warehouse_user_activity_name, subscription_id, api_version) -> web.Response:
    """data_warehouse_user_activities_get

    Gets the user activities of a data warehouse which includes running and suspended queries

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param data_warehouse_user_activity_name: The activity name of the data warehouse. 
    :type data_warehouse_user_activity_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
