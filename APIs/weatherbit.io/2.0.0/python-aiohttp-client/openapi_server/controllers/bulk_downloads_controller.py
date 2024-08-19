from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def bulk_files_file_get(request: web.Request, file, key) -> web.Response:
    """Download pre-generated bulk datasets

    Downloads bulk data files - OPTIONS: ( current.csv.gz, forecast_hourly.csv.gz, forecast_daily.csv.gz). Units are Metric (Celcius, m/s, etc).

    :param file: Filename (ie. current.csv.gz)
    :type file: str
    :param key: Your registered API key.
    :type key: str

    """
    return web.Response(status=200)
