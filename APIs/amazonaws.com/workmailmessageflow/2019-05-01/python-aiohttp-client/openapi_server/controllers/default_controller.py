from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_raw_message_content_response import GetRawMessageContentResponse
from openapi_server.models.put_raw_message_content_request import PutRawMessageContentRequest
from openapi_server import util


async def get_raw_message_content(request: web.Request, message_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_raw_message_content

    Retrieves the raw content of an in-transit email message, in MIME format.

    :param message_id: The identifier of the email message to retrieve.
    :type message_id: str
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


async def put_raw_message_content(request: web.Request, message_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_raw_message_content

    &lt;p&gt;Updates the raw content of an in-transit email message, in MIME format.&lt;/p&gt; &lt;p&gt;This example describes how to update in-transit email message. For more information and examples for using this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html\&quot;&gt; Updating message content with AWS Lambda&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Updates to an in-transit message only appear when you call &lt;code&gt;PutRawMessageContent&lt;/code&gt; from an AWS Lambda function configured with a synchronous &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html#synchronous-rules\&quot;&gt; Run Lambda&lt;/a&gt; rule. If you call &lt;code&gt;PutRawMessageContent&lt;/code&gt; on a delivered or sent message, the message remains unchanged, even though &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_GetRawMessageContent.html\&quot;&gt;GetRawMessageContent&lt;/a&gt; returns an updated message. &lt;/p&gt; &lt;/note&gt;

    :param message_id: The identifier of the email message being updated.
    :type message_id: str
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
    body = PutRawMessageContentRequest.from_dict(body)
    return web.Response(status=200)
