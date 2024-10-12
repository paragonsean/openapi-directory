from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_email_histories_response import FetchEmailHistoriesResponse
from openapi_server.models.fetch_email_history_response import FetchEmailHistoryResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server import util


async def fetch_email_histories(request: web.Request, filter_receiver=None, filter_sender=None, filter_email_type=None, sort=None) -> web.Response:
    """List email histories

    Get a list of email histories

    :param filter_receiver: Fitbit Plus user id of email recipient. Required if filter[sender] is not defined.
    :type filter_receiver: str
    :param filter_sender: Fitbit Plus user id of email sender. Required if filter[receiver] is not defined.
    :type filter_sender: str
    :param filter_email_type: Type of email
    :type filter_email_type: str
    :param sort: valid sorts:   * send_time - ascending by send_time   * -send_time - descending by send_time 
    :type sort: str

    """
    return web.Response(status=200)


async def fetch_email_history(request: web.Request, id) -> web.Response:
    """Get an email history

    Get an email history by id

    :param id: Email history identifier
    :type id: str

    """
    return web.Response(status=200)
