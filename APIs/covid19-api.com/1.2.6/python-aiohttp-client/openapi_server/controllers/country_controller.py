from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_daily_report_all_countries200_response_inner import GetDailyReportAllCountries200ResponseInner
from openapi_server.models.get_latest_country_data_by_name200_response_inner import GetLatestCountryDataByName200ResponseInner
from openapi_server import util


async def get_daily_report_all_countries(request: web.Request, _date, date_format=None, format=None) -> web.Response:
    """getDailyReportAllCountries

    Get daily report for all countries. Date is mandatory parametar. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter.

    :param _date: Date of the report.
    :type _date: str
    :param date_format: Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
    :type date_format: str
    :param format: Format of the response
    :type format: str

    """
    return web.Response(status=200)


async def get_daily_report_by_country_code(request: web.Request, code, _date, date_format=None, format=None) -> web.Response:
    """getDailyReportByCountryCode

    Get daily report for specific country. Country code and date are mandatory in parametars. Country code is in ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter

    :param code: Country code. Country code is by ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type.
    :type code: str
    :param _date: Date of the report.
    :type _date: str
    :param date_format: Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
    :type date_format: str
    :param format: Format of the response
    :type format: str

    """
    return web.Response(status=200)


async def get_daily_report_by_country_name(request: web.Request, name, _date, date_format=None, format=None) -> web.Response:
    """getDailyReportByCountryName

    Get daily report for specific country. Country name and date are mandatory in parametars. Date format is by ISO 8601 standard, but you can provide different format with date-format parameter

    :param name: Country name.
    :type name: str
    :param _date: Date of the report.
    :type _date: str
    :param date_format: Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
    :type date_format: str
    :param format: Format of the response
    :type format: str

    """
    return web.Response(status=200)


async def get_latest_all_countries(request: web.Request, format=None) -> web.Response:
    """getLatestAllCountries

    Get latest data from all countries.

    :param format: Format of the response
    :type format: str

    """
    return web.Response(status=200)


async def get_latest_country_data_by_code(request: web.Request, code, format=None) -> web.Response:
    """getLatestCountryDataByCode

    Get latest data for specific country. Country code and format are in parametars. Country code is in ISO 3166-1 standard. It can be 2 chars (Alpha-2) or 3 chars (Alpha-3) type.

    :param code: Country code
    :type code: str
    :param format: Format of the response
    :type format: str

    """
    return web.Response(status=200)


async def get_latest_country_data_by_name(request: web.Request, name, format=None) -> web.Response:
    """getLatestCountryDataByName

    Get latest data for specific country. Country name and format are in parametars.

    :param name: Name of the country
    :type name: str
    :param format: Format of the response
    :type format: str

    """
    return web.Response(status=200)
