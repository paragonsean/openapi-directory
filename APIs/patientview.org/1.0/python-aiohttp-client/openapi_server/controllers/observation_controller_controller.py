from typing import List, Dict
from aiohttp import web

from openapi_server.models.fhir_observation import FhirObservation
from openapi_server.models.fhir_observation_page import FhirObservationPage
from openapi_server import util


async def get_observations_by_code(request: web.Request, user_id, code) -> web.Response:
    """Get Observations of a Certain Type For a User

    Given a User ID and observation code, retrieve all observations.

    :param user_id: userId
    :type user_id: int
    :param code: code
    :type code: str

    """
    return web.Response(status=200)


async def get_observations_by_codes(request: web.Request, user_id, code, limit, offset, order_direction) -> web.Response:
    """Get Observations of Multiple Types For a User

    Given a User ID and search parameters, retrieve a page of observations.

    :param user_id: userId
    :type user_id: int
    :param code: code
    :type code: List[str]
    :param limit: limit
    :type limit: int
    :param offset: offset
    :type offset: int
    :param order_direction: orderDirection
    :type order_direction: str

    """
    return web.Response(status=200)


async def get_patient_entered_observations_by_code(request: web.Request, user_id, code) -> web.Response:
    """Get patient entered Observations of a Certain Type For a User

    Given a User ID and observation code, retrieve patient entered observations.

    :param user_id: userId
    :type user_id: int
    :param code: code
    :type code: str

    """
    return web.Response(status=200)
