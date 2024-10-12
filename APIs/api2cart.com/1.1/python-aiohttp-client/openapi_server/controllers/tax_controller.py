from typing import List, Dict
from aiohttp import web

from openapi_server.models.tax_class_info200_response import TaxClassInfo200Response
from openapi_server import util


async def tax_class_info(request: web.Request, tax_class_id, store_id=None, lang_id=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """tax_class_info

    Get info about tax

    :param tax_class_id: Retrieves taxes specified by class id
    :type tax_class_id: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)
