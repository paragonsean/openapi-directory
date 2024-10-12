from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_schedule200_response import CreateSchedule200Response
from openapi_server.models.disable_schedule200_response import DisableSchedule200Response
from openapi_server.models.enable_schedule200_response import EnableSchedule200Response
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.error422 import Error422
from openapi_server.models.schedule_create_input import ScheduleCreateInput
from openapi_server.models.schedule_update_input import ScheduleUpdateInput
from openapi_server.models.schedules import Schedules
from openapi_server import util


async def create_schedule(request: web.Request, schedule) -> web.Response:
    """Create a schedule

    This operation creates a schedule.

    :param schedule: Provide the details of the schedule to create in the body of the request.
    :type schedule: dict | bytes

    """
    schedule = ScheduleCreateInput.from_dict(schedule)
    return web.Response(status=200)


async def delete_schedule(request: web.Request, id) -> web.Response:
    """Delete a schedule

    This operation deletes a schedule.

    :param id: The unique alphanumeric string that identifies the schedule.
    :type id: str

    """
    return web.Response(status=200)


async def disable_schedule(request: web.Request, id) -> web.Response:
    """Disable a schedule

    This operation disables a schedule.

    :param id: The unique alphanumeric string that identifies the schedule.
    :type id: str

    """
    return web.Response(status=200)


async def enable_schedule(request: web.Request, id) -> web.Response:
    """Enable a schedule

    This operation enables a schedule.

    :param id: The unique alphanumeric string that identifies the schedule.
    :type id: str

    """
    return web.Response(status=200)


async def list_schedules(request: web.Request, page=None, per_page=None) -> web.Response:
    """Fetch all schedules

    This operation shows the details of all of your schedules.

    :param page: Returns a paginated view of results from the HTTP request. Specify a positive integer to indicate which page of the results should be displayed first. &lt;strong&gt;Next&lt;/strong&gt; and &lt;strong&gt;Previous&lt;/strong&gt; links allow you to navigate multiple pages of results. Omit the &lt;em&gt;page&lt;/em&gt; parameter or specify an integer that&#39;s less than or equal to &lt;strong&gt;0&lt;/strong&gt; to view all (unpaginated) results.
    :type page: int
    :param per_page: For use with the &lt;em&gt;page&lt;/em&gt; parameter. Indicates how many records should be included on each page of results. A valid value is any positive integer. The default is &lt;strong&gt;10&lt;/strong&gt;.
    :type per_page: int

    """
    return web.Response(status=200)


async def show_schedule(request: web.Request, id) -> web.Response:
    """Fetch a schedule

    This operation shows the details of a specific schedule.

    :param id: The unique alphanumeric string that identifies the schedule.
    :type id: str

    """
    return web.Response(status=200)


async def show_schedule_state(request: web.Request, id) -> web.Response:
    """Fetch the state of a schedule

    This operation shows the current state of a schedule.

    :param id: The unique alphanumeric string that identifies the schedule.
    :type id: str

    """
    return web.Response(status=200)


async def update_schedule(request: web.Request, id, schedule) -> web.Response:
    """Update a schedule

    This operation updates a schedule.

    :param id: The unique alphanumeric string that identifies the schedule.
    :type id: str
    :param schedule: Provide the details of the schedule to update in the body of the request.
    :type schedule: dict | bytes

    """
    schedule = ScheduleUpdateInput.from_dict(schedule)
    return web.Response(status=200)
