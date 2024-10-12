from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_patient_health_metric_request import CreatePatientHealthMetricRequest
from openapi_server.models.create_patient_health_metric_response import CreatePatientHealthMetricResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_patient_health_metric_response import FetchPatientHealthMetricResponse
from openapi_server import util


async def create_patient_health_metric(request: web.Request, body) -> web.Response:
    """Create patient health metrics

    Create one or more patient health metrics.  Example for creating a patient health result with a patient specified using &#x60;meta.query&#x60; instead of &#x60;id&#x60;:  &#x60;&#x60;&#x60;JSON   {     \&quot;data\&quot;: {       \&quot;type\&quot;: \&quot;patient_health_metric\&quot;,        \&quot;attributes\&quot;: {          \&quot;code\&quot;: {            \&quot;system\&quot;: \&quot;LOINC\&quot;,            \&quot;value\&quot;: \&quot;13457-7\&quot;          },          \&quot;type\&quot;: \&quot;ldl_cholesterol\&quot;,          \&quot;occurred_at\&quot;: \&quot;2017-03-14T11:00:57.000Z\&quot;,          \&quot;value\&quot;: 121,          \&quot;unit\&quot;: \&quot;mg/dl\&quot;       },       \&quot;relationships\&quot;: {         \&quot;patient\&quot;: {           \&quot;data\&quot;: {             \&quot;type\&quot;: \&quot;patient\&quot;,             \&quot;meta\&quot;: {               \&quot;query\&quot;: {                 \&quot;identifier\&quot;: {                   \&quot;system\&quot;: \&quot;medical-record-number\&quot;,                   \&quot;value\&quot;: \&quot;121212\&quot;                 },                 \&quot;organization\&quot;: \&quot;58c4554710123c5c40dbab81\&quot;               }             }           }         }       }     }   } &#x60;&#x60;&#x60; 

    :param body: 
    :type body: dict | bytes

    """
    body = CreatePatientHealthMetricRequest.from_dict(body)
    return web.Response(status=200)


async def fetch_patient_health_metric(request: web.Request, id) -> web.Response:
    """Get a patient health metric

    Get the plan summary for a patient.

    :param id: Patient health metric identifier
    :type id: str

    """
    return web.Response(status=200)


async def fetch_patient_health_metrics(request: web.Request, filter_patient=None, filter_groups=None, filter_organization=None, page_number=None, page_size=None, page_limit=None, page_cursor=None) -> web.Response:
    """List patient health metrics

    Get a list of patient health metrics.

    :param filter_patient: Filter the patient health metrics for a specified patient. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_patient: str
    :param filter_groups: Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_organization: str
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
