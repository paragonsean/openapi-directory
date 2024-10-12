from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_report409_response import CancelReport409Response
from openapi_server.models.create_async_report200_response import CreateAsyncReport200Response
from openapi_server.models.create_async_report400_response import CreateAsyncReport400Response
from openapi_server.models.create_async_report403_response import CreateAsyncReport403Response
from openapi_server.models.create_async_report422_response import CreateAsyncReport422Response
from openapi_server.models.create_async_report_request import CreateAsyncReportRequest
from openapi_server.models.download_report200_response import DownloadReport200Response
from openapi_server.models.get_records200_response import GetRecords200Response
from openapi_server.models.get_records403_response import GetRecords403Response
from openapi_server.models.get_records422_response import GetRecords422Response
from openapi_server.models.get_report200_response import GetReport200Response
from openapi_server.models.get_report404_response import GetReport404Response
from openapi_server.models.list_reports200_response import ListReports200Response
from openapi_server.models.list_reports400_response import ListReports400Response
from openapi_server.models.list_reports401_response import ListReports401Response
from openapi_server import util


async def cancel_report(request: web.Request, report_id) -> web.Response:
    """Cancel the execution of a report

    Cancel the execution of a pending or processing report.

    :param report_id: UUID of the report
    :type report_id: str

    """
    return web.Response(status=200)


async def create_async_report(request: web.Request, body=None) -> web.Response:
    """Create an asynchronous report

    Request a report on your account activity

    :param body: The parameters of the JSON body will be used to create and filter the report.&lt;br&gt; The value of the &#x60;product&#x60; field will define which product the report will be created for and which parameters are accepted. 
    :type body: dict | bytes

    """
    body = CreateAsyncReportRequest.from_dict(body)
    return web.Response(status=200)


async def download_report(request: web.Request, file_id) -> web.Response:
    """Get report data

    Download a zipped archive of the rendered report. The file is available for download for 72 hours.&lt;br&gt; The zip file will be named &#x60;&lt;PRODUCT&gt;_&lt;REPORT_ID&gt;.zip&#x60;&lt;br&gt; The csv file in the zip archive will be named as &#x60;report_&lt;PRODUCT&gt;_&lt;ACCOUNT_ID&gt;_&lt;DATE&gt;.csv&#x60; the date will be formatted as &#x60;yyyyMMdd&#x60;. 

    :param file_id: UUID of the file.
    :type file_id: str

    """
    return web.Response(status=200)


async def get_records(request: web.Request, account_id, product, direction=None, id=None, date_start=None, date_end=None, include_message=None, show_concatenated=None, status=None) -> web.Response:
    """Load records synchronously

    Fetch usage data synchronously

    :param account_id: The account for which the list of reports will be queried.
    :type account_id: str
    :param product: The product to return records for
    :type product: str
    :param direction: Direction of the communication, either &#x60;inbound&#x60; (received by our services), or &#x60;outbound&#x60; (originated from our services). Required for products &#x60;SMS&#x60; and &#x60;MESSAGES&#x60;. Optional for &#x60;VOICE-CALL&#x60;. Invalid for &#x60;IN-APP-VOICE&#x60;, &#x60;CONVERSATIONS&#x60;, &#x60;NUMBER-INSIGHT&#x60;, &#x60;VERIFY-API&#x60;.
    :type direction: str
    :param id: The UUID of the message or call to be searched for. You can specify a comma-separated list of UUIDs. If UUIDs are not found they are listed in the response in the &#x60;ids_not_found&#x60; field.  If you specify &#x60;id&#x60;, you must not specify &#x60;status&#x60;, &#x60;date_start&#x60; or &#x60;date_end&#x60;. 
    :type id: str
    :param date_start: ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;) for when reports should begin.   It filters on the time the API call was received by Vonage and corresponds to the field &#x60;date_received&#x60; (&#x60;date_start&#x60; for Voice) in the report file. It is inclusive, i.e. the provided value is less than or equal to the value in the field &#x60;date_received&#x60; (&#x60;date_start&#x60; for Voice) in the CDR.  If you provide this, you must provide &#x60;date_end&#x60; and must not provide &#x60;id&#x60;. 
    :type date_start: str
    :param date_end: **Must be no more than 24 hours later than &#x60;date_start&#x60;**  ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;) for when report should end.  It is exclusive, i.e. the provided value is strictly greater than the value in the field &#x60;date_received&#x60; in the CDR.  If you provide this, you must provide &#x60;date_start&#x60; and must not provide &#x60;id&#x60;. 
    :type date_end: str
    :param include_message: Include the message contents in the records. Only applicable for use with products &#x60;SMS&#x60; and &#x60;MESSAGES&#x60;, where it is optional.
    :type include_message: bool
    :param show_concatenated: Indicates whether the SMS was split up into multiple parts (due to its length).
    :type show_concatenated: bool
    :param status: The SMS status to search for. Optional where product is &#x60;SMS&#x60;.
    :type status: str

    """
    date_start = util.deserialize_date(date_start)
    date_end = util.deserialize_date(date_end)
    return web.Response(status=200)


async def get_report(request: web.Request, report_id) -> web.Response:
    """Get status of report

    Retrieve status and metadata about a requested report.

    :param report_id: UUID of the report request (&#x60;request_id&#x60; in response).
    :type report_id: str

    """
    return web.Response(status=200)


async def list_reports(request: web.Request, account_id, status, date_from=None, date_to=None) -> web.Response:
    """List reports

    List reports created by the specified account based on filtered provided.

    :param account_id: The account for which the list of reports will be queried.
    :type account_id: str
    :param status: A comma-separated list of report status values. Reports with any of the statuses specified are returned. The values in the comma-seperated list specified for &#x60;status&#x60; can be any of &#x60;PENDING&#x60;, &#x60;PROCESSING&#x60;, &#x60;SUCCESS&#x60;, &#x60;ABORTED&#x60;, &#x60;FAILED&#x60;, &#x60;TRUNCATED&#x60;.
    :type status: str
    :param date_from: ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date from which the list of reports will be queried. Format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;.
    :type date_from: str
    :param date_to: ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date until which the list of reports will be queried. Format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;.
    :type date_to: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)
