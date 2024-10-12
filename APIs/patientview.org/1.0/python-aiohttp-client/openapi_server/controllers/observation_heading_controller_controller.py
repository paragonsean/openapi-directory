from typing import List, Dict
from aiohttp import web

from openapi_server.models.observation_heading import ObservationHeading
from openapi_server import util


async def get_available_observation_headings(request: web.Request, user_id) -> web.Response:
    """Get Available Observations Types For a User

    Given a User ID retrieve a list of available observation types for that user (where they have observation data).

    :param user_id: userId
    :type user_id: int

    """
    return web.Response(status=200)


async def get_patient_entered_observation_headings(request: web.Request, user_id) -> web.Response:
    """Get Available Patient Entered Observations Types For a User

    Given a User ID retrieve a list of available observation types for that user (where they have patient entered observation data).

    :param user_id: userId
    :type user_id: int

    """
    return web.Response(status=200)
