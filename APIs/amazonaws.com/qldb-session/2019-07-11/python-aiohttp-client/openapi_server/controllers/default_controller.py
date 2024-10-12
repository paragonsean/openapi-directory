from typing import List, Dict
from aiohttp import web

from openapi_server.models.send_command_request import SendCommandRequest
from openapi_server.models.send_command_result import SendCommandResult
from openapi_server import util


async def send_command(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_command

    &lt;p&gt;Sends a command to an Amazon QLDB ledger.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Instead of interacting directly with this API, we recommend using the QLDB driver or the QLDB shell to execute data transactions on a ledger.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are working with an AWS SDK, use the QLDB driver. The driver provides a high-level abstraction layer above this &lt;i&gt;QLDB Session&lt;/i&gt; data plane and manages &lt;code&gt;SendCommand&lt;/code&gt; API calls for you. For information and a list of supported programming languages, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-driver.html\&quot;&gt;Getting started with the driver&lt;/a&gt; in the &lt;i&gt;Amazon QLDB Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are working with the AWS Command Line Interface (AWS CLI), use the QLDB shell. The shell is a command line interface that uses the QLDB driver to interact with a ledger. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/qldb/latest/developerguide/data-shell.html\&quot;&gt;Accessing Amazon QLDB using the QLDB shell&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    body = SendCommandRequest.from_dict(body)
    return web.Response(status=200)
