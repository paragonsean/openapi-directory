from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_thing_shadow_response import DeleteThingShadowResponse
from openapi_server.models.get_retained_message_response import GetRetainedMessageResponse
from openapi_server.models.get_thing_shadow_response import GetThingShadowResponse
from openapi_server.models.list_named_shadows_for_thing_response import ListNamedShadowsForThingResponse
from openapi_server.models.list_retained_messages_response import ListRetainedMessagesResponse
from openapi_server.models.publish_request import PublishRequest
from openapi_server.models.update_thing_shadow_request import UpdateThingShadowRequest
from openapi_server.models.update_thing_shadow_response import UpdateThingShadowResponse
from openapi_server import util


async def delete_thing_shadow(request: web.Request, thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, name=None) -> web.Response:
    """delete_thing_shadow

    &lt;p&gt;Deletes the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;DeleteThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html\&quot;&gt;DeleteThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

    :param thing_name: The name of the thing.
    :type thing_name: str
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
    :param name: The name of the shadow.
    :type name: str

    """
    return web.Response(status=200)


async def get_retained_message(request: web.Request, topic, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_retained_message

    &lt;p&gt;Gets the details of a single retained message for the specified topic.&lt;/p&gt; &lt;p&gt;This action returns the message payload of the retained message, which can incur messaging costs. To list only the topic names of the retained messages, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListRetainedMessages.html\&quot;&gt;ListRetainedMessages&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleethubfordevicemanagement.html#awsiotfleethubfordevicemanagement-actions-as-permissions\&quot;&gt;GetRetainedMessage&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

    :param topic: The topic name of the retained message to retrieve.
    :type topic: str
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


async def get_thing_shadow(request: web.Request, thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, name=None) -> web.Response:
    """get_thing_shadow

    &lt;p&gt;Gets the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_GetThingShadow.html\&quot;&gt;GetThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

    :param thing_name: The name of the thing.
    :type thing_name: str
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
    :param name: The name of the shadow.
    :type name: str

    """
    return web.Response(status=200)


async def list_named_shadows_for_thing(request: web.Request, thing_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, page_size=None) -> web.Response:
    """list_named_shadows_for_thing

    &lt;p&gt;Lists the shadows for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListNamedShadowsForThing&lt;/a&gt; action.&lt;/p&gt;

    :param thing_name: The name of the thing.
    :type thing_name: str
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
    :param next_token: The token to retrieve the next set of results.
    :type next_token: str
    :param page_size: The result page size.
    :type page_size: int

    """
    return web.Response(status=200)


async def list_retained_messages(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_retained_messages

    &lt;p&gt;Lists summary information about the retained messages stored for the account.&lt;/p&gt; &lt;p&gt;This action returns only the topic names of the retained messages. It doesn&#39;t return any message payloads. Although this action doesn&#39;t return a message payload, it can still incur messaging costs.&lt;/p&gt; &lt;p&gt;To get the message payload of a retained message, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetRetainedMessage.html\&quot;&gt;GetRetainedMessage&lt;/a&gt; with the topic name of the retained message.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleethubfordevicemanagement.html#awsiotfleethubfordevicemanagement-actions-as-permissions\&quot;&gt;ListRetainedMessages&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

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
    :param next_token: To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results.
    :type next_token: str
    :param max_results: The maximum number of results to return at one time.
    :type max_results: int

    """
    return web.Response(status=200)


async def publish(request: web.Request, topic, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, qos=None, retain=None, x_amz_mqtt5_user_properties=None, x_amz_mqtt5_payload_format_indicator=None, content_type=None, response_topic=None, x_amz_mqtt5_correlation_data=None, message_expiry=None) -> web.Response:
    """publish

    &lt;p&gt;Publishes an MQTT message.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;Publish&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about MQTT messages, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html\&quot;&gt;MQTT Protocol&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

    :param topic: The name of the MQTT topic.
    :type topic: str
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
    :param qos: The Quality of Service (QoS) level. The default QoS level is 0.
    :type qos: int
    :param retain: &lt;p&gt;A Boolean value that determines whether to set the RETAIN flag when the message is published.&lt;/p&gt; &lt;p&gt;Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;true&lt;/code&gt; | &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt;
    :type retain: bool
    :param x_amz_mqtt5_user_properties: &lt;p&gt;A JSON string that contains an array of JSON objects. If you don’t use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. &lt;code&gt;userProperties&lt;/code&gt; is an HTTP header value in the API.&lt;/p&gt; &lt;p&gt;The following example &lt;code&gt;userProperties&lt;/code&gt; parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:&lt;/p&gt; &lt;p&gt; &lt;code&gt;[{\&quot;deviceName\&quot;: \&quot;alpha\&quot;}, {\&quot;deviceCnt\&quot;: \&quot;45\&quot;}]&lt;/code&gt; &lt;/p&gt;
    :type x_amz_mqtt5_user_properties: str
    :param x_amz_mqtt5_payload_format_indicator: An &lt;code&gt;Enum&lt;/code&gt; string value that indicates whether the payload is formatted as UTF-8. &lt;code&gt;payloadFormatIndicator&lt;/code&gt; is an HTTP header value in the API.
    :type x_amz_mqtt5_payload_format_indicator: str
    :param content_type: A UTF-8 encoded string that describes the content of the publishing message.
    :type content_type: str
    :param response_topic: A UTF-8 encoded string that&#39;s used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.
    :type response_topic: str
    :param x_amz_mqtt5_correlation_data: The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it&#39;s received. &lt;code&gt;correlationData&lt;/code&gt; is an HTTP header value in the API.
    :type x_amz_mqtt5_correlation_data: str
    :param message_expiry: A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesn&#39;t expire. For more information about the limits of &lt;code&gt;messageExpiry&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits\&quot;&gt;Amazon Web Services IoT Core message broker and protocol limits and quotas &lt;/a&gt; from the Amazon Web Services Reference Guide.
    :type message_expiry: int

    """
    body = PublishRequest.from_dict(body)
    return web.Response(status=200)


async def update_thing_shadow(request: web.Request, thing_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, name=None) -> web.Response:
    """update_thing_shadow

    &lt;p&gt;Updates the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;UpdateThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html\&quot;&gt;UpdateThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

    :param thing_name: The name of the thing.
    :type thing_name: str
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
    :param name: The name of the shadow.
    :type name: str

    """
    body = UpdateThingShadowRequest.from_dict(body)
    return web.Response(status=200)
