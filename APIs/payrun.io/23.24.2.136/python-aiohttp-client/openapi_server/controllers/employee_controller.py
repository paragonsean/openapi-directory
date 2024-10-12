from typing import List, Dict
from aiohttp import web

from openapi_server.models.ae_assessment import AEAssessment
from openapi_server.models.commentary import Commentary
from openapi_server.models.employee import Employee
from openapi_server.models.employee_secret import EmployeeSecret
from openapi_server.models.employee_summary import EmployeeSummary
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server import util


async def delete_employee(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Delete an Employee

    Delete the specified employee

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


async def delete_employee_revision(request: web.Request, employer_id, employee_id, effective_date, authorization, api_version) -> web.Response:
    """Delete an Employee revision matching the specified revision date.

    Deletes the specified employee revision for the matching revision date

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def delete_employee_revision_by_number(request: web.Request, employer_id, employee_id, revision_number, authorization, api_version) -> web.Response:
    """Delete an Employee revision matching the specified revision number.

    Deletes the specified employee revision for the matching revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_employee_secret(request: web.Request, employer_id, employee_id, secret_id, authorization, api_version) -> web.Response:
    """Deletes employee secret

    Deletes an employee secret from the given resource location

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_ae_assessment_from_employee_0(request: web.Request, employer_id, employee_id, ae_assessment_id, authorization, api_version) -> web.Response:
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


async def get_ae_assessments_from_employee_0(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
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


async def get_all_employee_tags_0(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all employee tags

    Gets all the employee tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_commentaries_from_employee(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get links to all commentaries for the specified employee

    Get links to all commentaries for the specified employee.

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


async def get_commentary_from_employee(request: web.Request, employer_id, employee_id, commentary_id, authorization, api_version) -> web.Response:
    """Get commentary from employee

    Gets the specified commentary report from the employee

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param commentary_id: The commentary unique identifier. E.g. C001
    :type commentary_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_commentary_from_pay_run_by_employee(request: web.Request, employer_id, pay_schedule_id, pay_run_id, employee_id, authorization, api_version) -> web.Response:
    """Get commentary from payrun by specified employee.

    Get commentary from payrun by specified employee.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param pay_run_id: The pay runs&#39; unique identifier. E.g. PR001
    :type pay_run_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employee_by_effective_date(request: web.Request, employer_id, employee_id, effective_date, authorization, api_version) -> web.Response:
    """Get employee by effective date.

    Returns the employee&#39;s state at the specified effective date.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_employee_from_employer(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get employee from employer

    Gets the specified employee from employer by employee code.

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


async def get_employee_revision_by_number(request: web.Request, employer_id, employee_id, revision_number, authorization, api_version) -> web.Response:
    """Gets the employee by revision number

    Get the employee revision matching the specified revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employee_revision_summaries(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get all employee revision summaries

    Gets links to all employee revision summaries

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


async def get_employee_revision_summary_by_number(request: web.Request, employer_id, employee_id, revision_number, authorization, api_version) -> web.Response:
    """Gets the employee summary by revision number

    Get the employee revision summary matching the specified revision number

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param revision_number: The revision number. E.g. 1
    :type revision_number: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employee_revisions(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get all employee revisions

    Gets links to all employee revisions

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


async def get_employee_secret(request: web.Request, employer_id, employee_id, secret_id, authorization, api_version) -> web.Response:
    """Get employee secret

    Get the public visible employee secret object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employee_secrets(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get all employee secret links

    Get all the employee secret links

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


async def get_employee_summaries_by_effective_date(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Get employee summaries from employer at a given effective date.

    Get links to all employee summaries for the employer on specified effective date.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_employee_summaries_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get employee summaries from employer.

    Get links to all employee summaries for the specified employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employee_summary_by_effective_date(request: web.Request, employer_id, employee_id, effective_date, authorization, api_version) -> web.Response:
    """Get employee summary by effective date.

    Gets the employee summary for the specified effective date.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_employee_summary_from_employer(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Get employee summary from employer

    Gets the specified employee summary data from employer by employee code.

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


async def get_employees_by_effective_date(request: web.Request, employer_id, effective_date, authorization, api_version) -> web.Response:
    """Get employees from employer at a given effective date.

    Get links to all employees for the employer on specified effective date.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_employees_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get employees from employer.

    Get links to all employees for the specified employer.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employees_from_pay_run(request: web.Request, employer_id, pay_schedule_id, pay_run_id, authorization, api_version) -> web.Response:
    """Get employees from the pay run

    Gets links to all employees included in the specified pay run.

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


async def get_employees_from_pay_schedule(request: web.Request, employer_id, pay_schedule_id, authorization, api_version) -> web.Response:
    """Get all employees revisions from a pay schedule.

    Gets links to all employee revisions that have ever existed in the specified pay schedule.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_employees_from_pay_schedule_on_effective_date(request: web.Request, employer_id, pay_schedule_id, effective_date, authorization, api_version) -> web.Response:
    """Get employees from a pay schedule on effective date.

    Gets links to all employee revisions in the specified pay schedule for the given effective date.

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param pay_schedule_id: The pay schedules&#39; unique identifier. E.g SCH001
    :type pay_schedule_id: str
    :param effective_date: The effective date to be applied. E.g 2016-04-06
    :type effective_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    effective_date = util.deserialize_date(effective_date)
    return web.Response(status=200)


async def get_employees_with_tag_0(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get employees with tag

    Gets the employees with the tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_pay_runs_from_employee_0(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Gets the pay runs from the employee

    Get links to all pay runs for the specified employee.

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


async def patch_employee(request: web.Request, employer_id, employee_id, authorization, api_version, body) -> web.Response:
    """Patches the employee

    Patches the specified employee with the supplied values

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The employee object.
    :type body: dict | bytes

    """
    body = Employee.from_dict(body)
    return web.Response(status=200)


async def post_employee_into_employer(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Create a new Employee

    Create a new employee object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The employee object.
    :type body: dict | bytes

    """
    body = Employee.from_dict(body)
    return web.Response(status=200)


async def post_employee_secret(request: web.Request, employer_id, employee_id, authorization, api_version) -> web.Response:
    """Create a new employee secret

    Create new employee secret using auto generated resource location key

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


async def put_employee_into_employer(request: web.Request, employer_id, employee_id, authorization, api_version, body) -> web.Response:
    """Updates the Employee

    Updates the existing specified employee object

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The employee object.
    :type body: dict | bytes

    """
    body = Employee.from_dict(body)
    return web.Response(status=200)


async def put_employee_secret(request: web.Request, employer_id, employee_id, secret_id, authorization, api_version) -> web.Response:
    """Create a new employee secret

    Create / update an employee secret at the given resource location

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param employee_id: The employees&#39; unique identifier. E.g EE001
    :type employee_id: str
    :param secret_id: The secret unique identifier. E.g ERSEC001
    :type secret_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
