from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_data_tax_class_interface import TaxDataTaxClassInterface
from openapi_server import util


async def tax_tax_class_repository_v1_delete_by_id_delete(request: web.Request, tax_class_id) -> web.Response:
    """taxClasses/{taxClassId}

    Delete a tax class with the given tax class id.

    :param tax_class_id: 
    :type tax_class_id: int

    """
    return web.Response(status=200)


async def tax_tax_class_repository_v1_get_get(request: web.Request, tax_class_id) -> web.Response:
    """taxClasses/{taxClassId}

    Get a tax class with the given tax class id.

    :param tax_class_id: 
    :type tax_class_id: int

    """
    return web.Response(status=200)
