from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_patient_plan_summaries_response import FetchPatientPlanSummariesResponse
from openapi_server.models.fetch_patient_plan_summary_response import FetchPatientPlanSummaryResponse
from openapi_server.models.update_patient_plan_summary_request import UpdatePatientPlanSummaryRequest
from openapi_server.models.update_patient_plan_summary_response import UpdatePatientPlanSummaryResponse
from openapi_server import util


async def fetch_patient_plan_summaries(request: web.Request, filter_patient=None, filter_groups=None, filter_organization=None, include=None) -> web.Response:
    """List patient plan summaries

    Get a list of patient plan summaries

    :param filter_patient: Patient id to fetch plan summary for. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_patient: str
    :param filter_groups: Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_groups: str
    :param filter_organization: Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;. 
    :type filter_organization: str
    :param include: List of related resources to include in the response
    :type include: str

    """
    return web.Response(status=200)


async def fetch_patient_plan_summary(request: web.Request, id, include=None) -> web.Response:
    """Get the plan summary for a patient

    Get the plan summary for a patient.

    :param id: Plan summary identifier
    :type id: str
    :param include: List of related resources to include in the response
    :type include: str

    """
    return web.Response(status=200)


async def update_patient_plan_summary(request: web.Request, id, body) -> web.Response:
    """Update a plan summary

    Update a plan summary record for a patient.

    :param id: Plan summary identifier
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePatientPlanSummaryRequest.from_dict(body)
    return web.Response(status=200)
