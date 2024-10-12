from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_data_source200_response import CreateDataSource200Response
from openapi_server.models.datasource import Datasource
from openapi_server.models.delete_data_source200_response import DeleteDataSource200Response
from openapi_server.models.get_all_data_sources200_response import GetAllDataSources200Response
from openapi_server.models.get_data_source200_response import GetDataSource200Response
from openapi_server.models.reload_all_datasources_all_nodes200_response import ReloadAllDatasourcesAllNodes200Response
from openapi_server.models.reload_all_datasources_one_node200_response import ReloadAllDatasourcesOneNode200Response
from openapi_server.models.reload_one_datasource_all_nodes200_response import ReloadOneDatasourceAllNodes200Response
from openapi_server.models.reload_one_datasource_one_node200_response import ReloadOneDatasourceOneNode200Response
from openapi_server.models.update_data_source200_response import UpdateDataSource200Response
from openapi_server import util


async def create_data_source(request: web.Request, body=None) -> web.Response:
    """Create a data source

    Create a new data source

    :param body: 
    :type body: dict | bytes

    """
    body = Datasource.from_dict(body)
    return web.Response(status=200)


async def delete_data_source(request: web.Request, datasource_id) -> web.Response:
    """Delete a data source

    Delete a data source configuration

    :param datasource_id: Id of the data source
    :type datasource_id: str

    """
    return web.Response(status=200)


async def get_all_data_sources(request: web.Request, ) -> web.Response:
    """List all data sources

    Get the configuration of all present data sources


    """
    return web.Response(status=200)


async def get_data_source(request: web.Request, datasource_id) -> web.Response:
    """Get data source configuration

    Get the configuration of a data source

    :param datasource_id: Id of the data source
    :type datasource_id: str

    """
    return web.Response(status=200)


async def reload_all_datasources_all_nodes(request: web.Request, ) -> web.Response:
    """Update properties from data sources

    Update properties from all data source on all nodes. The call is asynchronous.


    """
    return web.Response(status=200)


async def reload_all_datasources_one_node(request: web.Request, node_id) -> web.Response:
    """Update properties for one node from all data sources

    Update properties from all data sources on one nodes. The call is asynchronous.

    :param node_id: Id of the target node
    :type node_id: str

    """
    return web.Response(status=200)


async def reload_one_datasource_all_nodes(request: web.Request, datasource_id) -> web.Response:
    """Update properties from data sources

    Update properties from all data source on all nodes. The call is asynchronous.

    :param datasource_id: Id of the data source
    :type datasource_id: str

    """
    return web.Response(status=200)


async def reload_one_datasource_one_node(request: web.Request, node_id, datasource_id) -> web.Response:
    """Update properties for one node from a data source

    Update properties from a data source on one nodes. The call is asynchronous.

    :param node_id: Id of the target node
    :type node_id: str
    :param datasource_id: Id of the data source
    :type datasource_id: str

    """
    return web.Response(status=200)


async def update_data_source(request: web.Request, datasource_id, body=None) -> web.Response:
    """Update a data source configuration

    Update the configuration of a data source

    :param datasource_id: Id of the data source
    :type datasource_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Datasource.from_dict(body)
    return web.Response(status=200)
