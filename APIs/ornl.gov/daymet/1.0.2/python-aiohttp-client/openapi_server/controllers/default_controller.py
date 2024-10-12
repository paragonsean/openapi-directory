from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_data_get(request: web.Request, lat, lon, format, vars=None, years=None, start=None, end=None) -> web.Response:
    """Download Daymet Data

    Returns a csv or json of the requested data to local machine

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param format: Specify a format for data retrieval.
    :type format: str
    :param vars: Daymet Daily weather estimates.
    :type vars: List[str]
    :param years: Subset on years [1980..2019].
    :type years: List[str]
    :param start: Subset on dates (start date).
    :type start: str
    :param end: Subset on dates (end date).
    :type end: str

    """
    start = util.deserialize_date(start)
    end = util.deserialize_date(end)
    return web.Response(status=200)


async def preview_get(request: web.Request, lat, lon, format, vars=None, years=None, start=None, end=None) -> web.Response:
    """Preview Daymet Data in a web browser

    Returns a table to the browser displaying requested data

    :param lat: Latitude component of location
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param format: Specify a format for data retrieval.
    :type format: str
    :param vars: Daymet Daily weather estimates.
    :type vars: List[str]
    :param years: Subset on years [1980..2019].
    :type years: List[str]
    :param start: Subset on dates (start date).
    :type start: str
    :param end: Subset on dates (end date).
    :type end: str

    """
    start = util.deserialize_date(start)
    end = util.deserialize_date(end)
    return web.Response(status=200)


async def send_save_data_get(request: web.Request, lat, lon, format, vars=None, years=None, start=None, end=None) -> web.Response:
    """Download Daymet Data

    Returns a csv or json of the requested data to local machine

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param format: Specify a format for data retrieval.
    :type format: str
    :param vars: Daymet Daily weather estimates.
    :type vars: List[str]
    :param years: Subset on years [1980..2019].
    :type years: List[str]
    :param start: Subset on dates (start date).
    :type start: str
    :param end: Subset on dates (end date).
    :type end: str

    """
    start = util.deserialize_date(start)
    end = util.deserialize_date(end)
    return web.Response(status=200)


async def visualize_get(request: web.Request, lat, lon, format, vars=None, years=None, start=None, end=None) -> web.Response:
    """Visualize Daymet Data in a web browser

    Returns plots to a web browser of requested data using Plotly

    :param lat: Latitude component of location.
    :type lat: float
    :param lon: Longitude component of location.
    :type lon: float
    :param format: Specify a format for data retrieval.
    :type format: str
    :param vars: Daymet Daily weather estimates.
    :type vars: List[str]
    :param years: Subset on years [1980..2019].
    :type years: List[str]
    :param start: Subset on dates (start date).
    :type start: str
    :param end: Subset on dates (end date).
    :type end: str

    """
    start = util.deserialize_date(start)
    end = util.deserialize_date(end)
    return web.Response(status=200)
