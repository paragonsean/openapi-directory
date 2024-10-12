from typing import List, Dict
from aiohttp import web

from openapi_server.models.claim_devices_by_claim_code_response import ClaimDevicesByClaimCodeResponse
from openapi_server.models.describe_device_response import DescribeDeviceResponse
from openapi_server.models.finalize_device_claim_request import FinalizeDeviceClaimRequest
from openapi_server.models.finalize_device_claim_response import FinalizeDeviceClaimResponse
from openapi_server.models.get_device_methods_response import GetDeviceMethodsResponse
from openapi_server.models.initiate_device_claim_response import InitiateDeviceClaimResponse
from openapi_server.models.invoke_device_method_request import InvokeDeviceMethodRequest
from openapi_server.models.invoke_device_method_response import InvokeDeviceMethodResponse
from openapi_server.models.list_device_events_response import ListDeviceEventsResponse
from openapi_server.models.list_devices_response import ListDevicesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.unclaim_device_response import UnclaimDeviceResponse
from openapi_server.models.update_device_state_request import UpdateDeviceStateRequest
from openapi_server import util


async def claim_devices_by_claim_code(request: web.Request, claim_code, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """claim_devices_by_claim_code

    Adds device(s) to your account (i.e., claim one or more devices) if and only if you  received a claim code with the device(s).

    :param claim_code: The claim code, starting with \&quot;C-\&quot;, as provided by the device manufacturer.
    :type claim_code: str
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


async def describe_device(request: web.Request, device_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_device

    Given a device ID, returns a DescribeDeviceResponse object describing the  details of the device.

    :param device_id: The unique identifier of the device.
    :type device_id: str
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


async def finalize_device_claim(request: web.Request, device_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """finalize_device_claim

    &lt;p&gt;Given a device ID, finalizes the claim request for the associated device.&lt;/p&gt;&lt;note&gt;  &lt;p&gt;Claiming a device consists of initiating a claim, then publishing a device event,  and finalizing the claim. For a device of type button, a device event can  be published by simply clicking the device.&lt;/p&gt;  &lt;/note&gt;

    :param device_id: The unique identifier of the device.
    :type device_id: str
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
    body = FinalizeDeviceClaimRequest.from_dict(body)
    return web.Response(status=200)


async def get_device_methods(request: web.Request, device_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_device_methods

    Given a device ID, returns the invokable methods associated with the device.

    :param device_id: The unique identifier of the device.
    :type device_id: str
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


async def initiate_device_claim(request: web.Request, device_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """initiate_device_claim

    &lt;p&gt;Given a device ID, initiates a claim request for the associated device.&lt;/p&gt;&lt;note&gt;  &lt;p&gt;Claiming a device consists of initiating a claim, then publishing a device event,  and finalizing the claim. For a device of type button, a device event can  be published by simply clicking the device.&lt;/p&gt;  &lt;/note&gt;

    :param device_id: The unique identifier of the device.
    :type device_id: str
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


async def invoke_device_method(request: web.Request, device_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """invoke_device_method

    Given a device ID, issues a request to invoke a named device method (with possible  parameters). See the \&quot;Example POST\&quot; code snippet below.

    :param device_id: The unique identifier of the device.
    :type device_id: str
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
    body = InvokeDeviceMethodRequest.from_dict(body)
    return web.Response(status=200)


async def list_device_events(request: web.Request, device_id, from_time_stamp, to_time_stamp, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_device_events

    Using a device ID, returns a DeviceEventsResponse object containing an  array of events for the device.

    :param device_id: The unique identifier of the device.
    :type device_id: str
    :param from_time_stamp: The start date for the device event query, in ISO8061 format. For example,  2018-03-28T15:45:12.880Z  
    :type from_time_stamp: str
    :param to_time_stamp: The end date for the device event query, in ISO8061 format. For example,  2018-03-28T15:45:12.880Z  
    :type to_time_stamp: str
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
    :param max_results: The maximum number of results to return per request. If not set, a default value of  100 is used.
    :type max_results: int
    :param next_token: The token to retrieve the next set of results.
    :type next_token: str

    """
    from_time_stamp = util.deserialize_datetime(from_time_stamp)
    to_time_stamp = util.deserialize_datetime(to_time_stamp)
    return web.Response(status=200)


async def list_devices(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, device_type=None, max_results=None, next_token=None) -> web.Response:
    """list_devices

    Lists the 1-Click compatible devices associated with your AWS account.

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
    :param device_type: The type of the device, such as \&quot;button\&quot;.
    :type device_type: str
    :param max_results: The maximum number of results to return per request. If not set, a default value of  100 is used.
    :type max_results: int
    :param next_token: The token to retrieve the next set of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags associated with the specified resource ARN.

    :param resource_arn: The ARN of the resource.
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

    Adds or updates the tags associated with the resource ARN. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-1-click/latest/developerguide/1click-appendix.html#1click-limits\&quot;&gt;AWS IoT 1-Click Service Limits&lt;/a&gt; for the maximum number of tags allowed per  resource.

    :param resource_arn: The ARN of the resource.
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


async def unclaim_device(request: web.Request, device_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """unclaim_device

    Disassociates a device from your AWS account using its device ID.

    :param device_id: The unique identifier of the device.
    :type device_id: str
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


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Using tag keys, deletes the tags (key/value pairs) associated with the specified  resource ARN.

    :param resource_arn: The ARN of the resource.
    :type resource_arn: str
    :param tag_keys: A collections of tag keys. For example, {\&quot;key1\&quot;,\&quot;key2\&quot;}
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


async def update_device_state(request: web.Request, device_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_device_state

    Using a Boolean value (true or false), this operation  enables or disables the device given a device ID.

    :param device_id: The unique identifier of the device.
    :type device_id: str
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
    body = UpdateDeviceStateRequest.from_dict(body)
    return web.Response(status=200)
