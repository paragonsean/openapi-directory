from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.report_definition import ReportDefinition
from openapi_server.models.transform_definition import TransformDefinition
from openapi_server import util


async def delete_report_definition(request: web.Request, report_definition_id, authorization, api_version) -> web.Response:
    """Deletes a report definition

    Delete the specified report definition

    :param report_definition_id: The report definition unique identifier.
    :type report_definition_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def delete_transform_definition(request: web.Request, transform_definition_id, authorization, api_version) -> web.Response:
    """Deletes a transform definition

    Delete the specified transform definition

    :param transform_definition_id: The transform definition unique identifier.
    :type transform_definition_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_active_pay_instructions_report_output(request: web.Request, employer_key, employee_key, from_date, authorization, api_version, active_on=None, to_date=None, type=None) -> web.Response:
    """Runs the active pay instructions report

    Returns the result of the executed active pay instructions report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param employee_key: The employee unique key. E.g. EE001
    :type employee_key: str
    :param from_date: The lower filter date. E.g 2016-04-06
    :type from_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param active_on: The active date to consider. E.g 2017-04-05
    :type active_on: str
    :param to_date: The upper filter date. E.g 2017-04-05
    :type to_date: str
    :param type: the data type to filter on. E.g. TaxPayInstruction
    :type type: str

    """
    from_date = util.deserialize_date(from_date)
    active_on = util.deserialize_date(active_on)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def get_aoe_liability_report_ouput(request: web.Request, employer_key, pay_schedule_key, tax_year, authorization, api_version, tax_period=None, transform_definition_key=None) -> web.Response:
    """Runs the AOE liability report

    Returns the result of the executed AOE liability report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param tax_period: The tax period number.
    :type tax_period: str
    :param transform_definition_key: The transform definition unique key. E.g. P45-Pdf
    :type transform_definition_key: str

    """
    return web.Response(status=200)


async def get_dps_message_report_output(request: web.Request, employer_key, from_date, authorization, api_version, to_date=None, message_types=None, message_statuses=None, start_index=None, max_index=None) -> web.Response:
    """Runs the DPS message report

    Returns the result of the executed DPS message report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param from_date: The lower filter date. E.g 2016-04-06
    :type from_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param to_date: The upper filter date. E.g 2017-04-05
    :type to_date: str
    :param message_types: The DPS message types as a CSV list. E.g. P6,P9,SL1,SL2
    :type message_types: str
    :param message_statuses: The DPS message status as a CSV list. E.g. Retrieved,Processed,Blocked,Ignored
    :type message_statuses: str
    :param start_index: The element index to begin the report. Used to control paging within large data sets. E.g. 1
    :type start_index: str
    :param max_index: The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    :type max_index: str

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def get_employer_summary_report_ouput(request: web.Request, employer_key, context_date, authorization, api_version) -> web.Response:
    """Runs the employer summary report

    Returns the result of the employer summary report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param context_date: The date context for the report. E.g. 2018-04-30
    :type context_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    context_date = util.deserialize_date(context_date)
    return web.Response(status=200)


async def get_gross_to_net_report_output(request: web.Request, employer_key, pay_schedule_key, tax_year, authorization, api_version, tax_period=None, start_index=None, max_index=None) -> web.Response:
    """Runs the gross to net report

    Returns the result of the executed gross to net report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param tax_period: The tax period number.
    :type tax_period: str
    :param start_index: The element index to begin the report. Used to control paging within large data sets. E.g. 1
    :type start_index: str
    :param max_index: The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    :type max_index: str

    """
    return web.Response(status=200)


async def get_holiday_balance_report_output(request: web.Request, employer_key, holiday_year_end, authorization, api_version, employee_codes=None, start_index=None, max_index=None) -> web.Response:
    """Runs the holiday balance report

    Returns the result of the executed holiday balance report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param holiday_year_end: The holiday year end for the report. E.g. 2018-12-31
    :type holiday_year_end: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param employee_codes: A comma separated list of the employee codes. E.g. EMP001,EMP002
    :type employee_codes: str
    :param start_index: The element index to begin the report. Used to control paging within large data sets. E.g. 1
    :type start_index: str
    :param max_index: The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    :type max_index: str

    """
    holiday_year_end = util.deserialize_date(holiday_year_end)
    return web.Response(status=200)


async def get_journal_report_ouput(request: web.Request, employer_key, pay_frequency, tax_year, ledger_target, authorization, api_version, tax_period=None) -> web.Response:
    """Runs the journal report

    Returns the result of the journal report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_frequency: The pay frequency option. E.g. Monthly
    :type pay_frequency: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param ledger_target: Specific to JOURNAL report, a filter used to select the journal lines for the specified ledger target. E.g. [Default]
    :type ledger_target: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param tax_period: The tax period number.
    :type tax_period: str

    """
    return web.Response(status=200)


async def get_last_pay_date_report_ouput(request: web.Request, employer_key, employee_key, authorization, api_version) -> web.Response:
    """Runs the last pay date report

    Returns the result of the executed last pay date report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param employee_key: The employee unique key. E.g. EE001
    :type employee_key: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_net_pay_report_output(request: web.Request, employer_key, pay_schedule_key, tax_year, authorization, api_version, tax_period=None, start_index=None, max_index=None) -> web.Response:
    """Runs the net pay report

    Returns the result of the executed net pay report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param tax_period: The tax period number.
    :type tax_period: str
    :param start_index: The element index to begin the report. Used to control paging within large data sets. E.g. 1
    :type start_index: str
    :param max_index: The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    :type max_index: str

    """
    return web.Response(status=200)


async def get_next_pay_period_dates_report_output(request: web.Request, employer_key, pay_schedule_key, authorization, api_version) -> web.Response:
    """Runs the next pay period report

    Returns the result of the executed next pay period report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_p11_summary_report_output(request: web.Request, employer_key, pay_schedule_key, tax_year, authorization, api_version, start_index=None, max_index=None) -> web.Response:
    """Runs the P11 summary report

    Returns the result of the executed P11 summary report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param start_index: The element index to begin the report. Used to control paging within large data sets. E.g. 1
    :type start_index: str
    :param max_index: The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    :type max_index: str

    """
    return web.Response(status=200)


async def get_p32_net_report_output(request: web.Request, employer_key, tax_year, authorization, api_version) -> web.Response:
    """Runs the P32 report

    Returns the result of the executed P32 report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_p32_summary_net_report_output(request: web.Request, employer_key, tax_year, authorization, api_version) -> web.Response:
    """Runs the P32 summary report

    Returns the result of the executed P32 summary report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_p45_report_output(request: web.Request, employer_key, employee_key, authorization, api_version, transform_definition_key=None) -> web.Response:
    """Runs the P45 report

    Returns the result of the executed P45 report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param employee_key: The employee unique key. E.g. EE001
    :type employee_key: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param transform_definition_key: The transform definition unique key. E.g. P45-Pdf
    :type transform_definition_key: str

    """
    return web.Response(status=200)


async def get_p60_report_output(request: web.Request, employer_key, tax_year, authorization, api_version, employee_codes=None, transform_definition_key=None, start_index=None, max_index=None) -> web.Response:
    """Runs the P60 report

    Returns the result of the executed P60 report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param employee_codes: A comma separated list of the employee codes. E.g. EMP001,EMP002
    :type employee_codes: str
    :param transform_definition_key: The transform definition unique key. E.g. P45-Pdf
    :type transform_definition_key: str
    :param start_index: The element index to begin the report. Used to control paging within large data sets. E.g. 1
    :type start_index: str
    :param max_index: The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    :type max_index: str

    """
    return web.Response(status=200)


async def get_papdis_report_ouput(request: web.Request, employer_key, pay_schedule_key, tax_year, pension_key, message_function_code, authorization, api_version, payment_date=None, transform_definition_key=None) -> web.Response:
    """Runs the PAPDIS report

    Returns the result of the executed PAPDIS report. PAPDIS is a free and open data interface standard designed to allow payroll and middleware software developers to create a file that can be used by pension providers to exchange data. http://www.papdis.org/

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param pension_key: The pension scheme unique key. E.g. PENSCH001
    :type pension_key: str
    :param message_function_code: Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions).
    :type message_function_code: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param payment_date: The payment date context for the report. E.g. 2018-04-30
    :type payment_date: str
    :param transform_definition_key: The transform definition unique key. E.g. P45-Pdf
    :type transform_definition_key: str

    """
    payment_date = util.deserialize_date(payment_date)
    return web.Response(status=200)


async def get_pass_report_ouput(request: web.Request, employer_key, pay_schedule_key, tax_year, pension_key, message_function_code, intermediary_id, document_id, authorization, api_version, payment_date=None) -> web.Response:
    """Runs the PASS report

    Returns the result of the executed PASS report. PASS stands for Payroll and Systemsync. PASS 1.1 is an extension of the PAPDIS V1.1 schema. https://pensionsynckb.systemsyncsolutions.com/display/PKB/PASS+1.1

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param pension_key: The pension scheme unique key. E.g. PENSCH001
    :type pension_key: str
    :param message_function_code: Specific to PAPDIS report, specifies the business function that the sender is requesting. If left BLANK it will be assumed to be 0 (Enrol / Receive Contributions).
    :type message_function_code: str
    :param intermediary_id: Specific to PensionSync PASS report, a unique identifier for the Intermediary who is acting on behalf of the employer.
    :type intermediary_id: str
    :param document_id: Specific to PensionSync PASS report, a document identifier unique for this document within the Intermediary.
    :type document_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param payment_date: The payment date context for the report. E.g. 2018-04-30
    :type payment_date: str

    """
    payment_date = util.deserialize_date(payment_date)
    return web.Response(status=200)


async def get_pay_dashboard_payslip_report_ouput(request: web.Request, employer_key, pay_schedule_key, tax_year, publication_date, authorization, api_version, employee_codes=None, transform_definition_key=None, start_index=None, max_index=None, payment_date=None) -> web.Response:
    """Runs the Pay Dashboard payslips report

    Returns the result of the executed Pay Dashboard payslip report for the given query parameters. See https://api.paydashboard.com for details. For compatability should be returned as JSON with TransformDefinitionKey&#x3D;Json-Clean.

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param publication_date: Specific to the Pay Dashboard report, allows the specification of a future payslip publication date. E.g. 2018-12-31
    :type publication_date: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param employee_codes: A comma separated list of the employee codes. E.g. EMP001,EMP002
    :type employee_codes: str
    :param transform_definition_key: The transform definition unique key. E.g. P45-Pdf
    :type transform_definition_key: str
    :param start_index: The element index to begin the report. Used to control paging within large data sets. E.g. 1
    :type start_index: str
    :param max_index: The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    :type max_index: str
    :param payment_date: The payment date context for the report. E.g. 2018-04-30
    :type payment_date: str

    """
    publication_date = util.deserialize_date(publication_date)
    payment_date = util.deserialize_date(payment_date)
    return web.Response(status=200)


async def get_payslip3_report_output(request: web.Request, employer_key, pay_schedule_key, tax_year, authorization, api_version, employee_codes=None, transform_definition_key=None, start_index=None, max_index=None, payment_date=None) -> web.Response:
    """Runs the verbose payslip report

    Returns the result of the executed verbose payslip report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param pay_schedule_key: The pay schedule unique key. E.g. SCH001
    :type pay_schedule_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param employee_codes: A comma separated list of the employee codes. E.g. EMP001,EMP002
    :type employee_codes: str
    :param transform_definition_key: The transform definition unique key. E.g. P45-Pdf
    :type transform_definition_key: str
    :param start_index: The element index to begin the report. Used to control paging within large data sets. E.g. 1
    :type start_index: str
    :param max_index: The highest element index to return from the report. Used to control paging within large data sets. E.g. 100
    :type max_index: str
    :param payment_date: The payment date context for the report. E.g. 2018-04-30
    :type payment_date: str

    """
    payment_date = util.deserialize_date(payment_date)
    return web.Response(status=200)


async def get_pension_liability_report_output(request: web.Request, employer_key, tax_year, pension_key, authorization, api_version) -> web.Response:
    """Runs the pension liability report

    Returns the result of the executed pension liability report for the given query parameters

    :param employer_key: The employer unique key. E.g. ER001
    :type employer_key: str
    :param tax_year: The tax year. E.g. 2017 &#x3D; 2017/18 year.
    :type tax_year: str
    :param pension_key: The pension scheme unique key. E.g. PENSCH001
    :type pension_key: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_report_definition_from_application(request: web.Request, report_definition_id, authorization, api_version) -> web.Response:
    """Get the report definition

    Returns the specified report definition from the authroised application

    :param report_definition_id: The report definition unique identifier.
    :type report_definition_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_report_definitions_from_application(request: web.Request, authorization, api_version) -> web.Response:
    """Gets all reports

    Get links to all saved report definitions under authorised application

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_report_output(request: web.Request, report_definition_id, authorization, api_version) -> web.Response:
    """Runs the specified report definition

    Returns the result of the executed report definition

    :param report_definition_id: The report definition unique identifier.
    :type report_definition_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_transform_definition_from_application(request: web.Request, transform_definition_id, authorization, api_version) -> web.Response:
    """Get the transform definition

    Returns the specified transform definition from the authroised application

    :param transform_definition_id: The transform definition unique identifier.
    :type transform_definition_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_transform_definitions_from_application(request: web.Request, authorization, api_version) -> web.Response:
    """Gets all transform definitions

    Get links to all saved transform definitions under authorised application

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_report_definition(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create a new report definition

    Creates a new report defintion object

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The report definition object.
    :type body: dict | bytes

    """
    body = ReportDefinition.from_dict(body)
    return web.Response(status=200)


async def post_transform_definition(request: web.Request, authorization, api_version, body) -> web.Response:
    """Create a new transform definition

    Creates a new transform defintion object

    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The transform definition object to be executed against the report data.
    :type body: dict | bytes

    """
    body = TransformDefinition.from_dict(body)
    return web.Response(status=200)


async def put_report_definition(request: web.Request, report_definition_id, authorization, api_version, body) -> web.Response:
    """Updates a report definition

    Updates the existing specified report definition object

    :param report_definition_id: The report definition unique identifier.
    :type report_definition_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The report definition object.
    :type body: dict | bytes

    """
    body = ReportDefinition.from_dict(body)
    return web.Response(status=200)


async def put_transform_definition(request: web.Request, transform_definition_id, authorization, api_version, body) -> web.Response:
    """Updates a transform definition

    Updates the existing specified transform definition object

    :param transform_definition_id: The transform definition unique identifier.
    :type transform_definition_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The transform definition object to be executed against the report data.
    :type body: dict | bytes

    """
    body = TransformDefinition.from_dict(body)
    return web.Response(status=200)
