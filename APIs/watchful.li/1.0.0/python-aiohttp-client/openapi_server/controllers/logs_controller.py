from typing import List, Dict
from aiohttp import web

from openapi_server.models.log import Log
from openapi_server import util


async def delete_log_by_id(request: web.Request, id) -> web.Response:
    """Delete a specific log

    Delete a specific log

    :param id: ID of log that needs to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def get_export_logs(request: web.Request, format, site=None, filter_type=None, search=None, startdate=None, enddate=None, limit=None, startid=None) -> web.Response:
    """Get a CSV or PDF file contain the list of logs

    Returns a file contain the list of logs

    :param format: Format of exported file (PDF or CSV)
    :type format: str
    :param site: Site id of the log
    :type site: int
    :param filter_type: Type of the log
    :type filter_type: str
    :param search: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type search: str
    :param startdate: Logs after this date, format YYYY-MM-DD HH:MM:SS
    :type startdate: str
    :param enddate: Logs before this date, format YYYY-MM-DD HH:MM:SS
    :type enddate: str
    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param startid: Start of the return (default 0)
    :type startid: int

    """
    return web.Response(status=200)


async def get_fields_logs(request: web.Request, ) -> web.Response:
    """Get the list of fields

    Returns a list of fields


    """
    return web.Response(status=200)


async def get_types_logs(request: web.Request, ) -> web.Response:
    """Get the list of log types

    Returns a list of log types


    """
    return web.Response(status=200)


async def logs_get(request: web.Request, log_type=None, log_entry=None, _from=None, to=None, fields=None, limit=None, limitstart=None, order=None) -> web.Response:
    """Get a list of logs

    Returns a list of logs

    :param log_type: Type of the log
    :type log_type: str
    :param log_entry: Do a &#39;LIKE&#39; search, you can also use &#39;%&#39;
    :type log_entry: str
    :param _from: Logs after this date, format YYYY-MM-DD HH:MM:SS
    :type _from: str
    :param to: Logs before this date, format YYYY-MM-DD HH:MM:SS
    :type to: str
    :param fields: Fields to return separate by comas: name,id
    :type fields: str
    :param limit: Number of object to return (max 100, default 25)
    :type limit: int
    :param limitstart: Start of the return (default 0)
    :type limitstart: int
    :param order: ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
    :type order: str

    """
    return web.Response(status=200)
