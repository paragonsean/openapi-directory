from typing import List, Dict
from aiohttp import web

from openapi_server.models.forecast import Forecast
from openapi_server.models.protection_result import ProtectionResult
from openapi_server.models.uv_index_result import UvIndexResult
from openapi_server import util


async def forecast_get(request: web.Request, lat, lng, x_access_token, alt=None, ozone=None, dt=None) -> web.Response:
    """forecast_get

    Get hourly UV Index Forecast by location and date. Optional altitude, ozone level and datetime could be provided.

    :param lat: latitude, from -90.00 to 90.00
    :type lat: 
    :param lng: longitude, from -180.00 to 180.00
    :type lng: 
    :param x_access_token: This header is used to send data that contains your OpenUV API key
    :type x_access_token: str
    :param alt: Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
    :type alt: 
    :param ozone: Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
    :type ozone: 
    :param dt: UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time.
    :type dt: str

    """
    dt = util.deserialize_datetime(dt)
    return web.Response(status=200)


async def protection_get(request: web.Request, lat, lng, _from, to, x_access_token, alt=None, ozone=None) -> web.Response:
    """protection_get

    Get daily protection time by location, UV Index from and UV Index to with 10 minutes accuracy. Optional altitide and ozone level could be provided.

    :param lat: latitude, from -90.00 to 90.00
    :type lat: 
    :param lng: longitude, from -180.00 to 180.00
    :type lng: 
    :param _from: UV Index from value for protection datetime lookup. From 0 to 40.
    :type _from: 
    :param to: UV Index to value for protection datetime lookup. From 0 to 40.
    :type to: 
    :param x_access_token: This header is used to send data that contains your OpenUV API key
    :type x_access_token: str
    :param alt: Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
    :type alt: 
    :param ozone: Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
    :type ozone: 

    """
    return web.Response(status=200)


async def uv_get(request: web.Request, lat, lng, x_access_token, alt=None, ozone=None, dt=None) -> web.Response:
    """uv_get

    Get real-time UV Index by location. Optional altitude, ozone level and datetime could be provided.

    :param lat: latitude, from -90.00 to 90.00
    :type lat: 
    :param lng: longitude, from -180.00 to 180.00
    :type lng: 
    :param x_access_token: This header is used to send data that contains your OpenUV API key
    :type x_access_token: str
    :param alt: Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
    :type alt: 
    :param ozone: Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
    :type ozone: 
    :param dt: UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time.
    :type dt: str

    """
    dt = util.deserialize_datetime(dt)
    return web.Response(status=200)
