from typing import List, Dict
from aiohttp import web

from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_patient_health_result_response import FetchPatientHealthResultResponse
from openapi_server import util


async def fetch_patient_health_result(request: web.Request, id) -> web.Response:
    """Get a patient health result

    Get patient health result by id.

    :param id: Patient health result identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_patient_health_results(request: web.Request, filter_patient, filter_actions=None, filter_start_at=None, filter_end_at=None, filter_threads=None, filter_created_at=None, filter_updated_at=None, page_number=None, page_size=None, page_limit=None, page_after=None) -> web.Response:
    """List patient health results

    Get a list of patient health results.

    :param filter_patient: Filter the patient health results for a specified patient
    :type filter_patient: str
    :param filter_actions: A comma-separated list of action identifiers
    :type filter_actions: str
    :param filter_start_at: Filter results that occurred after the passed ISO date and time string
    :type filter_start_at: str
    :param filter_end_at: Filter results that occurred before the passed ISO date and time string
    :type filter_end_at: str
    :param filter_threads: A comma-separated list of thread identifiers
    :type filter_threads: str
    :param filter_created_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_created_at: str
    :param filter_updated_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for results updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_updated_at: str
    :param page_number: Page number
    :type page_number: int
    :param page_size: Page size
    :type page_size: int
    :param page_limit: Page limit
    :type page_limit: int
    :param page_after: Page cursor
    :type page_after: str

    """
    return web.Response(status=200)
