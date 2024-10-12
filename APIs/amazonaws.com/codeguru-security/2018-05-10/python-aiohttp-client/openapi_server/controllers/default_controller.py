from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_get_findings_request import BatchGetFindingsRequest
from openapi_server.models.batch_get_findings_response import BatchGetFindingsResponse
from openapi_server.models.create_scan_request import CreateScanRequest
from openapi_server.models.create_scan_response import CreateScanResponse
from openapi_server.models.create_upload_url_request import CreateUploadUrlRequest
from openapi_server.models.create_upload_url_response import CreateUploadUrlResponse
from openapi_server.models.get_account_configuration_response import GetAccountConfigurationResponse
from openapi_server.models.get_findings_response import GetFindingsResponse
from openapi_server.models.get_metrics_summary_response import GetMetricsSummaryResponse
from openapi_server.models.get_scan_response import GetScanResponse
from openapi_server.models.list_findings_metrics_response import ListFindingsMetricsResponse
from openapi_server.models.list_scans_response import ListScansResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_account_configuration_request import UpdateAccountConfigurationRequest
from openapi_server.models.update_account_configuration_response import UpdateAccountConfigurationResponse
from openapi_server import util


async def batch_get_findings(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_get_findings

    Returns a list of all requested findings.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = BatchGetFindingsRequest.from_dict(body)
    return web.Response(status=200)


async def create_scan(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_scan

    Use to create a scan using code uploaded to an S3 bucket.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateScanRequest.from_dict(body)
    return web.Response(status=200)


async def create_upload_url(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_upload_url

    &lt;p&gt;Generates a pre-signed URL and request headers used to upload a code resource.&lt;/p&gt; &lt;p&gt;You can upload your code resource to the URL and add the request headers using any HTTP client.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateUploadUrlRequest.from_dict(body)
    return web.Response(status=200)


async def get_account_configuration(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_configuration

    Use to get account level configuration.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_findings(request: web.Request, scan_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, status=None) -> web.Response:
    """get_findings

    Returns a list of all findings generated by a particular scan.

    :param scan_name: The name of the scan you want to retrieve findings from.
    :type scan_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the &lt;code&gt;nextToken&lt;/code&gt; element is returned in the response. Use &lt;code&gt;nextToken&lt;/code&gt; in a subsequent request to retrieve additional results.
    :type max_results: int
    :param next_token: A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the &lt;code&gt;nextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page.
    :type next_token: str
    :param status: The status of the findings you want to get. Pass either &lt;code&gt;Open&lt;/code&gt;, &lt;code&gt;Closed&lt;/code&gt;, or &lt;code&gt;All&lt;/code&gt;.
    :type status: str

    """
    return web.Response(status=200)


async def get_metrics_summary(request: web.Request, _date, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_metrics_summary

    Returns top level metrics about an account from a specified date, including number of open findings, the categories with most findings, the scans with most open findings, and scans with most open critical findings. 

    :param _date: The date you want to retrieve summary metrics from, rounded to the nearest day. The date must be within the past two years since metrics data is only stored for two years. If a date outside of this range is passed, the response will be empty.
    :type _date: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)


async def get_scan(request: web.Request, scan_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, run_id=None) -> web.Response:
    """get_scan

    Returns details about a scan, including whether or not a scan has completed.

    :param scan_name: The name of the scan you want to view details about.
    :type scan_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param run_id: UUID that identifies the individual scan run you want to view details about. You retrieve this when you call the &lt;code&gt;CreateScan&lt;/code&gt; operation. Defaults to the latest scan run if missing.
    :type run_id: str

    """
    return web.Response(status=200)


async def list_findings_metrics(request: web.Request, end_date, start_date, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_findings_metrics

    Returns metrics about all findings in an account within a specified time range.

    :param end_date: The end date of the interval which you want to retrieve metrics from.
    :type end_date: str
    :param start_date: The start date of the interval which you want to retrieve metrics from.
    :type start_date: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the &lt;code&gt;nextToken&lt;/code&gt; element is returned in the response. Use &lt;code&gt;nextToken&lt;/code&gt; in a subsequent request to retrieve additional results.
    :type max_results: int
    :param next_token: A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the &lt;code&gt;nextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page.
    :type next_token: str

    """
    end_date = util.deserialize_datetime(end_date)
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)


async def list_scans(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_scans

    Returns a list of all the standard scans in an account. Does not return express scans.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: The maximum number of results to return in the response. Use this parameter when paginating results. If additional results exist beyond the number you specify, the &lt;code&gt;nextToken&lt;/code&gt; element is returned in the response. Use &lt;code&gt;nextToken&lt;/code&gt; in a subsequent request to retrieve additional results.
    :type max_results: int
    :param next_token: A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the &lt;code&gt;nextToken&lt;/code&gt; value returned from the previous request to continue listing results after the first page.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Returns a list of all tags associated with a scan.

    :param resource_arn: The ARN of the &lt;code&gt;ScanName&lt;/code&gt; object. You can retrieve this ARN by calling &lt;code&gt;ListScans&lt;/code&gt; or &lt;code&gt;GetScan&lt;/code&gt;.
    :type resource_arn: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Use to add one or more tags to an existing scan.

    :param resource_arn: The ARN of the &lt;code&gt;ScanName&lt;/code&gt; object. You can retrieve this ARN by calling &lt;code&gt;ListScans&lt;/code&gt; or &lt;code&gt;GetScan&lt;/code&gt;.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Use to remove one or more tags from an existing scan.

    :param resource_arn: The ARN of the &lt;code&gt;ScanName&lt;/code&gt; object. You can retrieve this ARN by calling &lt;code&gt;ListScans&lt;/code&gt; or &lt;code&gt;GetScan&lt;/code&gt;.
    :type resource_arn: str
    :param tag_keys: A list of keys for each tag you want to remove from a scan.
    :type tag_keys: List[str]
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def update_account_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_account_configuration

    Use to update account-level configuration with an encryption key.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateAccountConfigurationRequest.from_dict(body)
    return web.Response(status=200)
