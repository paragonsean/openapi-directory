from typing import List, Dict
from aiohttp import web

from openapi_server.models.complete_attachment_upload_request import CompleteAttachmentUploadRequest
from openapi_server.models.create_participant_connection_request import CreateParticipantConnectionRequest
from openapi_server.models.create_participant_connection_response import CreateParticipantConnectionResponse
from openapi_server.models.disconnect_participant_request import DisconnectParticipantRequest
from openapi_server.models.get_attachment_request import GetAttachmentRequest
from openapi_server.models.get_attachment_response import GetAttachmentResponse
from openapi_server.models.get_transcript_request import GetTranscriptRequest
from openapi_server.models.get_transcript_response import GetTranscriptResponse
from openapi_server.models.send_event_request import SendEventRequest
from openapi_server.models.send_event_response import SendEventResponse
from openapi_server.models.send_message_request import SendMessageRequest
from openapi_server.models.send_message_response import SendMessageResponse
from openapi_server.models.start_attachment_upload_request import StartAttachmentUploadRequest
from openapi_server.models.start_attachment_upload_response import StartAttachmentUploadResponse
from openapi_server import util


async def complete_attachment_upload(request: web.Request, x_amz_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """complete_attachment_upload

    &lt;p&gt;Allows you to confirm that the attachment has been uploaded using the pre-signed URL provided in StartAttachmentUpload API. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_bearer: The authentication token associated with the participant&#39;s connection.
    :type x_amz_bearer: str
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
    body = CompleteAttachmentUploadRequest.from_dict(body)
    return web.Response(status=200)


async def create_participant_connection(request: web.Request, x_amz_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_participant_connection

    &lt;p&gt;Creates the participant&#39;s connection. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ParticipantToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ConnectionToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The participant token is valid for the lifetime of the participant – until they are part of a contact.&lt;/p&gt; &lt;p&gt;The response URL for &lt;code&gt;WEBSOCKET&lt;/code&gt; Type has a connect expiry timeout of 100s. Clients must manually connect to the returned websocket URL and subscribe to the desired topic. &lt;/p&gt; &lt;p&gt;For chat, you need to publish the following on the established websocket connection:&lt;/p&gt; &lt;p&gt; &lt;code&gt;{\&quot;topic\&quot;:\&quot;aws/subscribe\&quot;,\&quot;content\&quot;:{\&quot;topics\&quot;:[\&quot;aws/chat\&quot;]}}&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Upon websocket URL expiry, as specified in the response ConnectionExpiry parameter, clients need to call this API again to obtain a new websocket URL and perform the same steps as before.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Message streaming support&lt;/b&gt;: This API can also be used together with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_StartContactStreaming.html\&quot;&gt;StartContactStreaming&lt;/a&gt; API to create a participant connection for chat contacts that are not using a websocket. For more information about message streaming, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-message-streaming.html\&quot;&gt;Enable real-time chat message streaming&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Feature specifications&lt;/b&gt;: For information about feature specifications, such as the allowed number of open websocket connections per participant, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#feature-limits\&quot;&gt;Feature specifications&lt;/a&gt; in the &lt;i&gt;Amazon Connect Administrator Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_bearer: &lt;p&gt;This is a header parameter.&lt;/p&gt; &lt;p&gt;The ParticipantToken as obtained from &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html\&quot;&gt;StartChatContact&lt;/a&gt; API response.&lt;/p&gt;
    :type x_amz_bearer: str
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
    body = CreateParticipantConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def disconnect_participant(request: web.Request, x_amz_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disconnect_participant

    &lt;p&gt;Disconnects a participant. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_bearer: The authentication token associated with the participant&#39;s connection.
    :type x_amz_bearer: str
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
    body = DisconnectParticipantRequest.from_dict(body)
    return web.Response(status=200)


async def get_attachment(request: web.Request, x_amz_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_attachment

    &lt;p&gt;Provides a pre-signed URL for download of a completed attachment. This is an asynchronous API for use with active contacts.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_bearer: The authentication token associated with the participant&#39;s connection.
    :type x_amz_bearer: str
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
    body = GetAttachmentRequest.from_dict(body)
    return web.Response(status=200)


async def get_transcript(request: web.Request, x_amz_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_transcript

    &lt;p&gt;Retrieves a transcript of the session, including details about any attachments. For information about accessing past chat contact transcripts for a persistent chat, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html\&quot;&gt;Enable persistent chat&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_bearer: The authentication token associated with the participant&#39;s connection.
    :type x_amz_bearer: str
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = GetTranscriptRequest.from_dict(body)
    return web.Response(status=200)


async def send_event(request: web.Request, x_amz_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_event

    &lt;p&gt;Sends an event. &lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_bearer: The authentication token associated with the participant&#39;s connection.
    :type x_amz_bearer: str
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
    body = SendEventRequest.from_dict(body)
    return web.Response(status=200)


async def send_message(request: web.Request, x_amz_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_message

    &lt;p&gt;Sends a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_bearer: The authentication token associated with the connection.
    :type x_amz_bearer: str
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
    body = SendMessageRequest.from_dict(body)
    return web.Response(status=200)


async def start_attachment_upload(request: web.Request, x_amz_bearer, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_attachment_upload

    &lt;p&gt;Provides a pre-signed Amazon S3 URL in response for uploading the file directly to S3.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;ConnectionToken&lt;/code&gt; is used for invoking this API instead of &lt;code&gt;ParticipantToken&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon Connect Participant Service APIs do not use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 authentication&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_bearer: The authentication token associated with the participant&#39;s connection.
    :type x_amz_bearer: str
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
    body = StartAttachmentUploadRequest.from_dict(body)
    return web.Response(status=200)
