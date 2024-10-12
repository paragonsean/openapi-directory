from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_patient_request import CreatePatientRequest
from openapi_server.models.create_patient_response import CreatePatientResponse
from openapi_server.models.fetch_coaches_response import FetchCoachesResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_groups_response import FetchGroupsResponse
from openapi_server.models.fetch_patient_response import FetchPatientResponse
from openapi_server.models.fetch_patients_response import FetchPatientsResponse
from openapi_server.models.update_patient_request import UpdatePatientRequest
from openapi_server.models.update_patient_response import UpdatePatientResponse
from openapi_server.models.upsert_patient_request import UpsertPatientRequest
from openapi_server import util


async def create_patient(request: web.Request, body) -> web.Response:
    """Create a patient

    Create a patient record.  Example for creating a patient with a group specified using &#x60;meta.query&#x60; instead of &#x60;id&#x60;:  &#x60;&#x60;&#x60;JSON {   \&quot;data\&quot;: {     \&quot;type\&quot;: \&quot;patient\&quot;,     \&quot;attributes\&quot;: {       \&quot;first_name\&quot;: \&quot;Andrew\&quot;,       \&quot;last_name\&quot;: \&quot;Smith\&quot;     },     \&quot;relationships\&quot;: {       \&quot;groups\&quot;: {         \&quot;data\&quot;: [           {             \&quot;type\&quot;: \&quot;group\&quot;,             \&quot;meta\&quot;: {               \&quot;query\&quot;: {                 \&quot;organization\&quot;: \&quot;58c88de7c93eb96357a87033\&quot;,                 \&quot;name\&quot;: \&quot;Patients Lead\&quot;               }             }           }         ]       }     }   } } &#x60;&#x60;&#x60; 

    :param body: 
    :type body: dict | bytes

    """
    body = CreatePatientRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_patient(request: web.Request, id) -> web.Response:
    """Get a patient

    Gets a patient record by id.

    :param id: Patient identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_patient_coaches(request: web.Request, id) -> web.Response:
    """List coaches for a patient

    Get the list of coaches for a patient.

    :param id: Patient identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_patient_groups(request: web.Request, id) -> web.Response:
    """List groups for a patient

    Get the list of groups for a patient.

    :param id: Patient identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_patients(request: web.Request, filter_groups=None, filter_organization=None, filter_identifier_system=None, filter_identifier_value=None, filter_archived=None, filter_created_at=None, filter_updated_at=None, page_number=None, page_size=None, page_limit=None, page_cursor=None) -> web.Response:
    """List patients

    Get a list of patients.

    :param filter_groups: Comma-separated list of group ids. Note that either &#x60;filter[group]&#x60; or &#x60;filter[organization]&#x60; must be specified.
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that either &#x60;filter[group]&#x60; or &#x60;filter[organization]&#x60; must be specified.
    :type filter_organization: str
    :param filter_identifier_system: Identifier system (example: \&quot;MyEHR\&quot;) - requires a \&quot;filter[identifier][value]\&quot; parameter
    :type filter_identifier_system: str
    :param filter_identifier_value: Identifier value (example: \&quot;12345\&quot;) - requires a \&quot;filter[identifier][system]\&quot; parameter
    :type filter_identifier_value: str
    :param filter_archived: If not specified, return all patients. If set to &#39;true&#39; return only archived patients, if set to &#39;false&#39;, return only patients who are not archived.
    :type filter_archived: bool
    :param filter_created_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for patients created in November 2017 (America/New_York): &#x60;filter[created_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_created_at: str
    :param filter_updated_at: The start (inclusive) and end (exclusive) dates are ISO date and time strings separated by &#x60;..&#x60;. Example for patients updated in November 2017 (America/New_York): &#x60;filter[updated_at]&#x3D;2017-11-01T00:00:00-04:00..2017-12-01T00:00:00-05:00&#x60; 
    :type filter_updated_at: str
    :param page_number: Page number
    :type page_number: int
    :param page_size: Page size
    :type page_size: int
    :param page_limit: Page limit
    :type page_limit: int
    :param page_cursor: Page cursor
    :type page_cursor: str

    """
    return web.Response(status=200)


async def update_patient(request: web.Request, id, body) -> web.Response:
    """Update a patient

    Update a patient record.

    :param id: Patient identifier
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePatientRequest.from_dict(body)
    return web.Response(status=200)


async def upsert_patient(request: web.Request, body) -> web.Response:
    """Upsert patient

    Create a new patient or update an existing patient

    :param body: 
    :type body: dict | bytes

    """
    body = UpsertPatientRequest.from_dict(body)
    return web.Response(status=200)
