from typing import List, Dict
from aiohttp import web

from openapi_server.models.patient import Patient
from openapi_server import util


async def get_basic_patient_details(request: web.Request, user_id) -> web.Response:
    """Get Basic Patient Information

    Given a User ID, get basic patient information for a user from clinical data stored in FHIR

    :param user_id: userId
    :type user_id: int

    """
    return web.Response(status=200)
