from typing import List, Dict
from aiohttp import web

from openapi_server.models.job_recurrence_information import JobRecurrenceInformation
from openapi_server.models.job_recurrence_information_list_result import JobRecurrenceInformationListResult
from openapi_server import util


async def recurrence_get(request: web.Request, recurrence_identity, api_version, start_date_time=None, end_date_time=None) -> web.Response:
    """recurrence_get

    Gets the recurrence information for the specified recurrence ID.

    :param recurrence_identity: Recurrence ID.
    :type recurrence_identity: str
    :type recurrence_identity: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param start_date_time: The start date for when to get the recurrence and aggregate its data. The startDateTime and endDateTime can be no more than 30 days apart.
    :type start_date_time: str
    :param end_date_time: The end date for when to get recurrence and aggregate its data. The startDateTime and endDateTime can be no more than 30 days apart.
    :type end_date_time: str

    """
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    return web.Response(status=200)


async def recurrence_list(request: web.Request, api_version, start_date_time=None, end_date_time=None) -> web.Response:
    """recurrence_list

    Lists all recurrences.

    :param api_version: Client Api Version.
    :type api_version: str
    :param start_date_time: The start date for when to get the list of recurrences. The startDateTime and endDateTime can be no more than 30 days apart.
    :type start_date_time: str
    :param end_date_time: The end date for when to get the list of recurrences. The startDateTime and endDateTime can be no more than 30 days apart.
    :type end_date_time: str

    """
    start_date_time = util.deserialize_datetime(start_date_time)
    end_date_time = util.deserialize_datetime(end_date_time)
    return web.Response(status=200)
