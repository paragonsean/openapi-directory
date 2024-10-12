from typing import List, Dict
from aiohttp import web

from openapi_server.models.input_date_time_conversion import InputDateTimeConversion
from openapi_server.models.input_date_time_difference import InputDateTimeDifference
from openapi_server.models.input_date_time_format import InputDateTimeFormat
from openapi_server.models.input_date_time_info import InputDateTimeInfo
from openapi_server.models.output_date_difference import OutputDateDifference
from openapi_server.models.output_date_info import OutputDateInfo
from openapi_server.models.output_string import OutputString
from openapi_server import util


async def date_time_difference(request: web.Request, date_time_difference=None) -> web.Response:
    """DateTime - DateTime difference

    Calculate the difference between two dates

    :param date_time_difference: 
    :type date_time_difference: dict | bytes

    """
    date_time_difference = InputDateTimeDifference.from_dict(date_time_difference)
    return web.Response(status=200)


async def date_time_info(request: web.Request, date_time_info=None) -> web.Response:
    """DateTime - Get date and time information

    Retrieve useful date and time information, such as day of year, total seconds and ticks

    :param date_time_info: 
    :type date_time_info: dict | bytes

    """
    date_time_info = InputDateTimeInfo.from_dict(date_time_info)
    return web.Response(status=200)


async def format_date_time(request: web.Request, date_time_format=None) -> web.Response:
    """DateTime - Format date and time

    Create a date/time string in a specific format

    :param date_time_format: 
    :type date_time_format: dict | bytes

    """
    date_time_format = InputDateTimeFormat.from_dict(date_time_format)
    return web.Response(status=200)


async def world_time(request: web.Request, date_time_conversion=None) -> web.Response:
    """DateTime - Get world time

    Convert date and time from one time zone to another

    :param date_time_conversion: 
    :type date_time_conversion: dict | bytes

    """
    date_time_conversion = InputDateTimeConversion.from_dict(date_time_conversion)
    return web.Response(status=200)
