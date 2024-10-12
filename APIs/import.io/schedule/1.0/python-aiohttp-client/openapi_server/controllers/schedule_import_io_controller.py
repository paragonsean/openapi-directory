from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.schedule import Schedule
from openapi_server.models.schedule_request import ScheduleRequest
from openapi_server import util


async def extractor_extractor_id_delete(request: web.Request, extractor_id) -> web.Response:
    """Delete an existing schedule

    

    :param extractor_id: the id of the extractor with a schedule
    :type extractor_id: str

    """
    return web.Response(status=200)


async def extractor_extractor_id_get(request: web.Request, extractor_id) -> web.Response:
    """Get the schedule of a particular extractor

    

    :param extractor_id: the id of the extractor with a schedule
    :type extractor_id: str

    """
    return web.Response(status=200)


async def extractor_get(request: web.Request, ) -> web.Response:
    """Get the list of schedules for all your extractors

    


    """
    return web.Response(status=200)


async def extractor_post(request: web.Request, schedule_request_body) -> web.Response:
    """Schedule and extractor to run at a specific time

    

    :param schedule_request_body: Request body with the schema defined on the left. Interval is a cron string.
    :type schedule_request_body: dict | bytes

    """
    schedule_request_body = ScheduleRequest.from_dict(schedule_request_body)
    return web.Response(status=200)
