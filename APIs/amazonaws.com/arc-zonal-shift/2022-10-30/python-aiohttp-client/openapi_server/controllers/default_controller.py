from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_managed_resource_response import GetManagedResourceResponse
from openapi_server.models.list_managed_resources_response import ListManagedResourcesResponse
from openapi_server.models.list_zonal_shifts_response import ListZonalShiftsResponse
from openapi_server.models.start_zonal_shift_request import StartZonalShiftRequest
from openapi_server.models.update_zonal_shift_request import UpdateZonalShiftRequest
from openapi_server.models.zonal_shift import ZonalShift
from openapi_server import util


async def cancel_zonal_shift(request: web.Request, zonal_shift_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_zonal_shift

    Cancel a zonal shift in Amazon Route 53 Application Recovery Controller that you&#39;ve started for a resource in your AWS account in an AWS Region. 

    :param zonal_shift_id: The internally-generated identifier of a zonal shift.
    :type zonal_shift_id: str
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


async def get_managed_resource(request: web.Request, resource_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_managed_resource

    &lt;p&gt;Get information about a resource that&#39;s been registered for zonal shifts with Amazon Route 53 Application Recovery Controller in this AWS Region. Resources that are registered for zonal shifts are managed resources in Route 53 ARC.&lt;/p&gt; &lt;p&gt;At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.&lt;/p&gt;

    :param resource_identifier: &lt;p&gt;The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.&lt;/p&gt; &lt;p&gt;At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.&lt;/p&gt;
    :type resource_identifier: str
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


async def list_managed_resources(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_managed_resources

    Lists all the resources in your AWS account in this AWS Region that are managed for zonal shifts in Amazon Route 53 Application Recovery Controller, and information about them. The information includes their Amazon Resource Names (ARNs), the Availability Zones the resources are deployed in, and the resource name.

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
    :param max_results: The number of objects that you want to return with this call.
    :type max_results: int
    :param next_token: Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_zonal_shifts(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, status=None) -> web.Response:
    """list_zonal_shifts

    Lists all the active zonal shifts in Amazon Route 53 Application Recovery Controller in your AWS account in this AWS Region.

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
    :param max_results: The number of objects that you want to return with this call.
    :type max_results: int
    :param next_token: Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results.
    :type next_token: str
    :param status: &lt;p&gt;A status for a zonal shift.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; for a zonal shift can have one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;ACTIVE&lt;/b&gt;: The zonal shift is started and active.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;EXPIRED&lt;/b&gt;: The zonal shift has expired (the expiry time was exceeded).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;CANCELED&lt;/b&gt;: The zonal shift was canceled.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type status: str

    """
    return web.Response(status=200)


async def start_zonal_shift(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_zonal_shift

    &lt;p&gt;You start a zonal shift to temporarily move load balancer traffic away from an Availability Zone in a AWS Region, to help your application recover immediately, for example, from a developer&#39;s bad code deployment or from an AWS infrastructure failure in a single Availability Zone. You can start a zonal shift in Route 53 ARC only for managed resources in your account in an AWS Region. Resources are automatically registered with Route 53 ARC by AWS services.&lt;/p&gt; &lt;p&gt;At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.&lt;/p&gt; &lt;p&gt;When you start a zonal shift, traffic for the resource is no longer routed to the Availability Zone. The zonal shift is created immediately in Route 53 ARC. However, it can take a short time, typically up to a few minutes, for existing, in-progress connections in the Availability Zone to complete.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html\&quot;&gt;Zonal shift&lt;/a&gt; in the Amazon Route 53 Application Recovery Controller Developer Guide.&lt;/p&gt;

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
    body = StartZonalShiftRequest.from_dict(body)
    return web.Response(status=200)


async def update_zonal_shift(request: web.Request, zonal_shift_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_zonal_shift

    Update an active zonal shift in Amazon Route 53 Application Recovery Controller in your AWS account. You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift. 

    :param zonal_shift_id: The identifier of a zonal shift.
    :type zonal_shift_id: str
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
    body = UpdateZonalShiftRequest.from_dict(body)
    return web.Response(status=200)
