from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_column_configuration import BeezUPColumnConfiguration
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.catalog_index import CatalogIndex
from openapi_server import util


async def catalog_get_beez_up_columns(request: web.Request, ) -> web.Response:
    """Get the BeezUP columns

    Get the BeezUP columns, this columns are used for mapping during the manual catalog importation process.


    """
    return web.Response(status=200)


async def catalog_index(request: web.Request, ) -> web.Response:
    """Get the index of the catalog API

    The operation will give you all the operations you will be able to do and all the LOV used in this API.


    """
    return web.Response(status=200)
