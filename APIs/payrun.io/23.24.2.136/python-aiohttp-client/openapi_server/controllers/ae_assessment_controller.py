from typing import List, Dict
from aiohttp import web

from openapi_server.models.ae_assessment import AEAssessment
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server import util


async def delete_ae_assessment(request: web.Request, employer_id, employee_id, ae_assessment_id, authorization, api_version) -> web.Response:
    """Delete auto enrolment assessment

    Deletes an existing auto enrolment assessment for the employee. Used to remove historical assessments

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param ae_assessment_id: The auto enrolment assessment unique identifier. E.g. AE001
    :type ae_assessment_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_ae_assessment_from_employee(request: web.Request, employer_id, employee_id, ae_assessment_id, authorization, api_version) -> web.Response:
    """Get the auto enrolment assessment

    Gets the auto enrolment assessment from the specified employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param ae_assessment_id: The auto enrolment assessment unique identifier. E.g. AE001
    :type ae_assessment_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_ae_assessments_from_employee(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get the auto enrolment assessments

    Gets all auto enrolment assessments from the specified employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_ae_assessments_from_pay_run(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Get the auto enrolment assessments

    Gets all auto enrolment assessments from the specified pay run

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_new_ae_assessment(request: web.Request, employer_id, employee_id, authorization, api_version, body) -> web.Response:
    """Insert new auto enrolment assessment

    Creates a new auto enrolment assessment for the employee. Used to insert historical assessments

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The auto enrolment assessment object.
    :type body: dict | bytes

    """
    body = AEAssessment.from_dict(body)
    return web.Response(status=200)


async def put_new_ae_assessment(request: web.Request, employer_id, employee_id, ae_assessment_id, authorization, api_version, body) -> web.Response:
    """Insert new auto enrolment assessment

    Creates a new auto enrolment assessment for the employee. Used to insert historical assessments

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param ae_assessment_id: The auto enrolment assessment unique identifier. E.g. AE001
    :type ae_assessment_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The auto enrolment assessment object.
    :type body: dict | bytes

    """
    body = AEAssessment.from_dict(body)
    return web.Response(status=200)
