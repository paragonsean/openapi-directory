from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def compare_station(request: web.Request, station_name) -> web.Response:
    """compare_station

    Get forecast and realtime information for known points&lt;br/&gt;None

    :param station_name: Weather station to compare, values: cnareanl|rcnp | cmsap|boyaenderrocat|areopuertopalma | EWXXX
    :type station_name: str

    """
    return web.Response(status=200)


async def get_aemet_station(request: web.Request, station_name, period) -> web.Response:
    """get_aemet_station

    Get data from the aemet stations&lt;br/&gt;None

    :param station_name: station name currently: aeropuertopalma | caboblanco 
    :type station_name: str
    :param period: Period of time to get the data. Options: lastdata lastday
    :type period: str

    """
    return web.Response(status=200)


async def get_easywind(request: web.Request, easywind_id, period) -> web.Response:
    """get_easywind

    Get data from the easywind weather stations&lt;br/&gt;None

    :param easywind_id: currently: &#39;EW013&#39;|&#39;EW008&#39;
    :type easywind_id: str
    :param period: Period of time to get the data latestdata|latesthour|latestday
    :type period: str

    """
    return web.Response(status=200)


async def get_event_stations(request: web.Request, event_id) -> web.Response:
    """get_event_stations

    Get stations in an event&lt;br/&gt;None

    :param event_id: currently: &#39;trofeoprincesasofia|palmavela&#39;
    :type event_id: str

    """
    return web.Response(status=200)


async def get_forecast_points(request: web.Request, yatchclubid, language) -> web.Response:
    """get_forecast_points

    Get forecast points of a yatchclub&lt;br/&gt;None

    :param yatchclubid: base URL for the the
    :type yatchclubid: str
    :param language: 
    :type language: str

    """
    return web.Response(status=200)


async def get_forecast_time_series(request: web.Request, latitude, longitude, weather, inittime=None, endtime=None, days=None, hours=None, wave=None, entryid=None) -> web.Response:
    """get_forecast_time_series

    Get timeseries forecast information&lt;br/&gt;None

    :param latitude: latitude for the forecast
    :type latitude: float
    :param longitude: longitude for the forecast
    :type longitude: float
    :param weather:  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&amp;wave&#x3D;height,direction,period
    :type weather: str
    :param inittime: initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
    :type inittime: str
    :param endtime: end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
    :type endtime: str
    :param days: optional number of days in string. Will be added to init forecast date
    :type days: int
    :param hours: optional number of hours in string. Will be added to init forecast date
    :type hours: int
    :param wave:  Comma separated values for the wave parameteres height,direction,period
    :type wave: str
    :param entryid: Direct file I want to extract
    :type entryid: str

    """
    return web.Response(status=200)


async def get_forecast_time_series_wrf(request: web.Request, latitude, longitude, weather, inittime=None, endtime=None, days=None, hours=None, wave=None, entryid=None) -> web.Response:
    """get_forecast_time_series_wrf

    Get timeseries forecast information&lt;br/&gt;None

    :param latitude: latitude for the forecast
    :type latitude: float
    :param longitude: longitude for the forecast
    :type longitude: float
    :param weather:  Comma separated values for the weather parameteres temperature,rain,wind_u,wind_v,gust,pressure,cloud,humidity&amp;wave&#x3D;height,direction,period
    :type weather: str
    :param inittime: initial date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
    :type inittime: str
    :param endtime: end date for the forecast ISO string YYYY-MM-DDTHH:mm:SS.SZ
    :type endtime: str
    :param days: optional number of days in string. Will be added to init forecast date
    :type days: int
    :param hours: optional number of hours in string. Will be added to init forecast date
    :type hours: int
    :param wave:  Comma separated values for the wave parameteres height,direction,period
    :type wave: str
    :param entryid: Direct file I want to extract
    :type entryid: str

    """
    return web.Response(status=200)


async def get_socib_weather_station(request: web.Request, station_name, period) -> web.Response:
    """get_socib_weather_station

    Get data from the socib bahia de palma buoy&lt;br/&gt;None

    :param station_name: station name currently: boyaenderrocat | playadepalma
    :type station_name: str
    :param period: Period of time to get the data. Options: lastdata lasthour lastday
    :type period: str

    """
    return web.Response(status=200)


async def get_weather_display(request: web.Request, station_name, period) -> web.Response:
    """get_weather_display

    Get data from the weather display software&lt;br/&gt;None

    :param station_name: currently: &#39;cnarenal&#39;|&#39;campastilla&#39; | &#39;cncg&#39;
    :type station_name: str
    :param period: Period of time to get the data latestdata|latesthour|latestday|dailylog
    :type period: str

    """
    return web.Response(status=200)


async def get_web_cams(request: web.Request, ) -> web.Response:
    """get_web_cams

    Get forecast and realtime information for known points&lt;br/&gt;None


    """
    return web.Response(status=200)
