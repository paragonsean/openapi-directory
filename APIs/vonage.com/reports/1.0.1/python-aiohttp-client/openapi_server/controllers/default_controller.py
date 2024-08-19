from typing import List, Dict
from aiohttp import web

from openapi_server.models.call_logs_hal_response import CallLogsHalResponse
from openapi_server.models.validation_errors_response import ValidationErrorsResponse
from openapi_server import util


async def get_call_logs(request: web.Request, account_id, startgte, startlte, page_size, page, endgte=None, endlte=None, to=None, _from=None, source_user=None, destination_user=None, direction=None) -> web.Response:
    """Retrieve call logs for your account

    Retrieve call logs for your account

    :param account_id: The Vonage Business Cloud account ID
    :type account_id: str
    :param startgte: Filter records by start date (greater equal or equal to)
    :type startgte: str
    :param startlte: Filter records by start date (less equal or equal to)
    :type startlte: str
    :param page_size: Number of records per page
    :type page_size: 
    :param page: Current page number
    :type page: 
    :param endgte: Filter records by end date (greater equal or equal to)
    :type endgte: str
    :param endlte: Filter records by end date (less equal or equal to)
    :type endlte: str
    :param to: Filter by called number
    :type to: str
    :param _from: Filter by source number
    :type _from: str
    :param source_user: Filter by source user
    :type source_user: str
    :param destination_user: Filter by destination user
    :type destination_user: str
    :param direction: Filter by call direction.
    :type direction: str

    """
    return web.Response(status=200)
