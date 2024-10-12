from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_bulk_data_exporter_configs200_response_inner import CreateBulkDataExporterConfigs200ResponseInner
from openapi_server.models.data_exporter_config import DataExporterConfig
from openapi_server.models.deletebulk_data_exporter_config200_response_inner import DeletebulkDataExporterConfig200ResponseInner
from openapi_server.models.deleted import Deleted
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.update_bulk_data_exporter_config200_response_inner import UpdateBulkDataExporterConfig200ResponseInner
from openapi_server import util


async def create_bulk_data_exporter_configs(request: web.Request, body=None) -> web.Response:
    """Create a new data exporter configs

    Create a new data exporter configs

    :param body: 
    :type body: dict | bytes

    """
    body = DataExporterConfig.from_dict(body)
    return web.Response(status=200)


async def create_data_exporter_config(request: web.Request, body=None) -> web.Response:
    """Create a new data exporter config

    Create a new data exporter config

    :param body: 
    :type body: dict | bytes

    """
    body = DataExporterConfig.from_dict(body)
    return web.Response(status=200)


async def data_exporter_template(request: web.Request, type=None) -> web.Response:
    """Get all data exporter configs

    Get all data exporter configs

    :param type: The data exporter config type
    :type type: str

    """
    return web.Response(status=200)


async def delete_data_exporter_config(request: web.Request, data_exporter_config_id) -> web.Response:
    """Delete a data exporter config

    Delete a data exporter config

    :param data_exporter_config_id: The data exporter config id
    :type data_exporter_config_id: str

    """
    return web.Response(status=200)


async def deletebulk_data_exporter_config(request: web.Request, body=None) -> web.Response:
    """Delete a data exporter config

    Delete a data exporter config

    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def find_all_data_exporters(request: web.Request, ) -> web.Response:
    """Get all data exporter configs

    Get all data exporter configs


    """
    return web.Response(status=200)


async def find_data_exporter_config_by_id(request: web.Request, data_exporter_config_id) -> web.Response:
    """Get a data exporter config

    Get a data exporter config

    :param data_exporter_config_id: The data exporter config id
    :type data_exporter_config_id: str

    """
    return web.Response(status=200)


async def patch_bulk_data_exporter_config(request: web.Request, body=None) -> web.Response:
    """Update a data exporter configs with a diff

    Update a data exporter configs with a diff

    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def patch_data_exporter_config(request: web.Request, data_exporter_config_id, body=None) -> web.Response:
    """Update a data exporter config with a diff

    Update a data exporter config with a diff

    :param data_exporter_config_id: The data exporter config id
    :type data_exporter_config_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PatchInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_bulk_data_exporter_config(request: web.Request, body=None) -> web.Response:
    """Update a data exporter configs

    Update a data exporter configs

    :param body: 
    :type body: dict | bytes

    """
    body = DataExporterConfig.from_dict(body)
    return web.Response(status=200)


async def update_data_exporter_config(request: web.Request, data_exporter_config_id, body=None) -> web.Response:
    """Update a data exporter config

    Update a data exporter config

    :param data_exporter_config_id: The data exporter config id
    :type data_exporter_config_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DataExporterConfig.from_dict(body)
    return web.Response(status=200)
