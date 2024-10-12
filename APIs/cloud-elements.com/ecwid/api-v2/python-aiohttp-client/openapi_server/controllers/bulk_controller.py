from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_download_request import BulkDownloadRequest
from openapi_server.models.bulk_job_list import BulkJobList
from openapi_server.models.bulk_query import BulkQuery
from openapi_server.models.bulk_status import BulkStatus
from openapi_server.models.bulk_upload_response import BulkUploadResponse
from openapi_server import util


async def create_bulk_by_object_name(request: web.Request, authorization, object_name, elements_async_callback_url=None, meta_data=None, file=None) -> web.Response:
    """Upload a file of objects to be bulk uploaded to the provider.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object for which data needs to be uploaded.
    :type object_name: str
    :param elements_async_callback_url: The Url to send the notification to when the Job is completed
    :type elements_async_callback_url: str
    :param meta_data: Optional JSON MetaData that contains callback-payload, path or format, ex: {\\\&quot;path\\\&quot; :&amp;lt;path for the sub resource&amp;gt;, \\\&quot;format\\\&quot;: &amp;lt;json/csv&amp;gt;, \\\&quot;callback-payload\\\&quot;:&amp;lt;json&amp;gt;}. path - is passed to the endpoint for bulk loading the data into a nested object. Optional JSON Metadata that contains identifierFieldName, action, listId or campaignId. The identifierField name is used for upserts and the optional fields like listId or campaignId. Example: {\\\&quot;listId\\\&quot;:\\\&quot;1014\\\&quot;,\\\&quot;action\\\&quot;:\\\&quot;upsert\\\&quot;}. If the Upload format is JSON pass metadata as {\\\&quot;format\\\&quot;:\\\&quot;json\\\&quot;}. callback-payload - is passed back in bulk job notification 
    :type meta_data: str
    :param file: The file of objects to bulk load. If the JSON file upload, each JSON record should be in a single line
    :type file: str

    """
    return web.Response(status=200)


async def create_bulk_download(request: web.Request, authorization, body) -> web.Response:
    """Create a new bulk download job (asynchronous)

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param body: The object body
    :type body: dict | bytes

    """
    body = BulkDownloadRequest.from_dict(body)
    return web.Response(status=200)


async def create_bulk_query(request: web.Request, authorization, elements_async_callback_url=None, q=None, last_run_date=None, _from=None, to=None, meta_data=None) -> web.Response:
    """Create an asynchronous bulk query job.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param elements_async_callback_url: The Url to send the notification to when the Job is completed
    :type elements_async_callback_url: str
    :param q: The CEQL query. When this parameter is omitted, all objects of the given type are returned via the bulk job. Endpoint limiters may still apply.
    :type q: str
    :param last_run_date: The last time this query was run. This is optional. You can also have this parameter in the query and leave this blank - optional eg. &#39;2014-10-06T13:22:17-08:00&#39;
    :type last_run_date: str
    :param _from: The created/updated date of the object to filter on - optional eg. &#39;2014-10-06T13:22:17-08:00&#39;
    :type _from: str
    :param to: The created/updated date of the object to filter on - optional eg. &#39;2014-10-06T13:22:17-08:00&#39;
    :type to: str
    :param meta_data: Optional JSON MetaData that contains callback-payload and fileName, ex: {\\\&quot;callback-payload\\\&quot; : &lt;Json&gt; , \\\&quot;fileName\\\&quot; : \\\&quot;{Date format}_Name of the file\\\&quot;}. If the fileName is MyFile then pass metadata as {\\\&quot;fileName\\\&quot; : \\\&quot;{yyyy-MM-dd HH:mm:ss}_MyFile\\\&quot;}. The valid date formats are \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ssXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ\\\&quot;, \\\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;\\\&quot;, \\\&quot;yyyy-MM-dd HH:mm:ss\\\&quot;, \\\&quot;yyyy.MM.dd G &#39;at&#39; HH:mm:ss z\\\&quot;, \\\&quot;h:mm a\\\&quot;, \\\&quot;yyyyy.MMMMM.dd GGG hh:mm aaa\\\&quot; and \\\&quot;yyMMddHHmmssZ\\\&quot;. callback-payload - is passed back in bulk job notification 
    :type meta_data: str

    """
    return web.Response(status=200)


async def get_bulk_by_object_name(request: web.Request, authorization, id, object_name) -> web.Response:
    """Retrieve the results of an asynchronous bulk query.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the bulk job
    :type id: str
    :param object_name: The name of the object
    :type object_name: str

    """
    return web.Response(status=200)


async def get_bulk_errors(request: web.Request, authorization, id, page_size=None, next_page=None, fields=None) -> web.Response:
    """Retrieve the errors of a bulk job.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the bulk job to retrieve its errors.
    :type id: str
    :param page_size: The page size for pagination, which defaults to 200 if not supplied
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def get_bulk_jobs(request: web.Request, authorization, where=None, next_page=None, page_size=None, fields=None) -> web.Response:
    """Fetch all the bulk jobs for an instance

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param where: The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query. For example to get all upload jobs the expression would be where&#x3D;job_direction&#x3D;&#39;UPLOAD&#39;. The following fields are valid search fields &#39;object_name&#39;, &#39;job_status&#39;, &#39;job_direction&#39;, &#39;record_count&#39;
    :type where: str
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param page_size: The page size for pagination, which defaults to 200 if not supplied
    :type page_size: int
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def get_bulk_status(request: web.Request, authorization, id) -> web.Response:
    """Retrieve the status of a bulk job.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the bulk job to retrieve its status.
    :type id: str

    """
    return web.Response(status=200)


async def replace_bulk_cancel(request: web.Request, authorization, id) -> web.Response:
    """Cancel an asynchronous bulk query job.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param id: The ID of the bulk job to cancel.
    :type id: str

    """
    return web.Response(status=200)
