from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_acknowledge_alarm_request import BatchAcknowledgeAlarmRequest
from openapi_server.models.batch_acknowledge_alarm_response import BatchAcknowledgeAlarmResponse
from openapi_server.models.batch_delete_detector_request import BatchDeleteDetectorRequest
from openapi_server.models.batch_delete_detector_response import BatchDeleteDetectorResponse
from openapi_server.models.batch_disable_alarm_request import BatchDisableAlarmRequest
from openapi_server.models.batch_disable_alarm_response import BatchDisableAlarmResponse
from openapi_server.models.batch_enable_alarm_request import BatchEnableAlarmRequest
from openapi_server.models.batch_enable_alarm_response import BatchEnableAlarmResponse
from openapi_server.models.batch_put_message_request import BatchPutMessageRequest
from openapi_server.models.batch_put_message_response import BatchPutMessageResponse
from openapi_server.models.batch_reset_alarm_request import BatchResetAlarmRequest
from openapi_server.models.batch_reset_alarm_response import BatchResetAlarmResponse
from openapi_server.models.batch_snooze_alarm_request import BatchSnoozeAlarmRequest
from openapi_server.models.batch_snooze_alarm_response import BatchSnoozeAlarmResponse
from openapi_server.models.batch_update_detector_request import BatchUpdateDetectorRequest
from openapi_server.models.batch_update_detector_response import BatchUpdateDetectorResponse
from openapi_server.models.describe_alarm_response import DescribeAlarmResponse
from openapi_server.models.describe_detector_response import DescribeDetectorResponse
from openapi_server.models.list_alarms_response import ListAlarmsResponse
from openapi_server.models.list_detectors_response import ListDetectorsResponse
from openapi_server import util


async def batch_acknowledge_alarm(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_acknowledge_alarm

    Acknowledges one or more alarms. The alarms change to the &lt;code&gt;ACKNOWLEDGED&lt;/code&gt; state after you acknowledge them.

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
    body = BatchAcknowledgeAlarmRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_detector(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_detector

    Deletes one or more detectors that were created. When a detector is deleted, its state will be cleared and the detector will be removed from the list of detectors. The deleted detector will no longer appear if referenced in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ListDetectors.html\&quot;&gt;ListDetectors&lt;/a&gt; API call.

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
    body = BatchDeleteDetectorRequest.from_dict(body)
    return web.Response(status=200)


async def batch_disable_alarm(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_disable_alarm

    Disables one or more alarms. The alarms change to the &lt;code&gt;DISABLED&lt;/code&gt; state after you disable them.

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
    body = BatchDisableAlarmRequest.from_dict(body)
    return web.Response(status=200)


async def batch_enable_alarm(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_enable_alarm

    Enables one or more alarms. The alarms change to the &lt;code&gt;NORMAL&lt;/code&gt; state after you enable them.

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
    body = BatchEnableAlarmRequest.from_dict(body)
    return web.Response(status=200)


async def batch_put_message(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_put_message

    Sends a set of messages to the IoT Events system. Each message payload is transformed into the input you specify (&lt;code&gt;\&quot;inputName\&quot;&lt;/code&gt;) and ingested into any detectors that monitor that input. If multiple messages are sent, the order in which the messages are processed isn&#39;t guaranteed. To guarantee ordering, you must send messages one at a time and wait for a successful response.

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
    body = BatchPutMessageRequest.from_dict(body)
    return web.Response(status=200)


async def batch_reset_alarm(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_reset_alarm

    Resets one or more alarms. The alarms return to the &lt;code&gt;NORMAL&lt;/code&gt; state after you reset them.

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
    body = BatchResetAlarmRequest.from_dict(body)
    return web.Response(status=200)


async def batch_snooze_alarm(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_snooze_alarm

    Changes one or more alarms to the snooze mode. The alarms change to the &lt;code&gt;SNOOZE_DISABLED&lt;/code&gt; state after you set them to the snooze mode.

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
    body = BatchSnoozeAlarmRequest.from_dict(body)
    return web.Response(status=200)


async def batch_update_detector(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_update_detector

    Updates the state, variable values, and timer settings of one or more detectors (instances) of a specified detector model.

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
    body = BatchUpdateDetectorRequest.from_dict(body)
    return web.Response(status=200)


async def describe_alarm(request: web.Request, alarm_model_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key_value=None) -> web.Response:
    """describe_alarm

    Retrieves information about an alarm.

    :param alarm_model_name: The name of the alarm model.
    :type alarm_model_name: str
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
    :param key_value: The value of the key used as a filter to select only the alarms associated with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key\&quot;&gt;key&lt;/a&gt;.
    :type key_value: str

    """
    return web.Response(status=200)


async def describe_detector(request: web.Request, detector_model_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, key_value=None) -> web.Response:
    """describe_detector

    Returns information about the specified detector (instance).

    :param detector_model_name: The name of the detector model whose detectors (instances) you want information about.
    :type detector_model_name: str
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
    :param key_value: A filter used to limit results to detectors (instances) created because of the given key ID.
    :type key_value: str

    """
    return web.Response(status=200)


async def list_alarms(request: web.Request, alarm_model_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_alarms

    Lists one or more alarms. The operation returns only the metadata associated with each alarm.

    :param alarm_model_name: The name of the alarm model.
    :type alarm_model_name: str
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
    :param next_token: The token that you can use to return the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to be returned per request.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_detectors(request: web.Request, detector_model_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, state_name=None, next_token=None, max_results=None) -> web.Response:
    """list_detectors

    Lists detectors (the instances of a detector model).

    :param detector_model_name: The name of the detector model whose detectors (instances) are listed.
    :type detector_model_name: str
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
    :param state_name: A filter that limits results to those detectors (instances) in the given state.
    :type state_name: str
    :param next_token: The token that you can use to return the next set of results.
    :type next_token: str
    :param max_results: The maximum number of results to be returned per request.
    :type max_results: int

    """
    return web.Response(status=200)
