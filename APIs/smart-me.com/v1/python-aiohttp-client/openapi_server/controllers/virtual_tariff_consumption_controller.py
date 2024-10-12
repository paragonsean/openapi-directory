from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_tariff_consumption_data import VirtualTariffConsumptionData
from openapi_server import util


async def virtual_tariff_consumption_get(request: web.Request, folder_id, start_date, end_date) -> web.Response:
    """Gets the consumption of a folder with a virtuall tariffs.

    Gets the consumption of a folder with a virtuall tariffs.

    :param folder_id: The ID of the Folder
    :type folder_id: str
    :param start_date: The start date (UTC)
    :type start_date: str
    :param end_date: The end date (UTC)
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)
