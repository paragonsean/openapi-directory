from typing import List, Dict
from aiohttp import web

from openapi_server.models.join_storage_session_request import JoinStorageSessionRequest
from openapi_server import util


async def join_storage_session(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """join_storage_session

    &lt;p&gt; Join the ongoing one way-video and/or multi-way audio WebRTC session as a video producing device for an input channel. If there’s no existing session for the channel, a new streaming session needs to be created, and the Amazon Resource Name (ARN) of the signaling channel must be provided. &lt;/p&gt; &lt;p&gt;Currently for the &lt;code&gt;SINGLE_MASTER&lt;/code&gt; type, a video producing device is able to ingest both audio and video media into a stream, while viewers can only ingest audio. Both a video producing device and viewers can join the session first, and wait for other participants.&lt;/p&gt; &lt;p&gt;While participants are having peer to peer conversations through webRTC, the ingested media session will be stored into the Kinesis Video Stream. Multiple viewers are able to playback real-time media.&lt;/p&gt; &lt;p&gt;Customers can also use existing Kinesis Video Streams features like &lt;code&gt;HLS&lt;/code&gt; or &lt;code&gt;DASH&lt;/code&gt; playback, Image generation, and more with ingested WebRTC media.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Assume that only one video producing device client can be associated with a session for the channel. If more than one client joins the session of a specific channel as a video producing device, the most recent client request takes precedence. &lt;/p&gt; &lt;/note&gt;

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
    body = JoinStorageSessionRequest.from_dict(body)
    return web.Response(status=200)
