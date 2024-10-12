from typing import List, Dict
from aiohttp import web

from openapi_server.models.send_ssh_public_key_request import SendSSHPublicKeyRequest
from openapi_server.models.send_ssh_public_key_response import SendSSHPublicKeyResponse
from openapi_server.models.send_serial_console_ssh_public_key_request import SendSerialConsoleSSHPublicKeyRequest
from openapi_server.models.send_serial_console_ssh_public_key_response import SendSerialConsoleSSHPublicKeyResponse
from openapi_server import util


async def send_serial_console_ssh_public_key(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_serial_console_ssh_public_key

    Pushes an SSH public key to the specified EC2 instance. The key remains for 60 seconds, which gives you 60 seconds to establish a serial console connection to the instance using SSH. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html\&quot;&gt;EC2 Serial Console&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.

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
    body = SendSerialConsoleSSHPublicKeyRequest.from_dict(body)
    return web.Response(status=200)


async def send_ssh_public_key(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """send_ssh_public_key

    Pushes an SSH public key to the specified EC2 instance for use by the specified user. The key remains for 60 seconds. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html\&quot;&gt;Connect to your Linux instance using EC2 Instance Connect&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.

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
    body = SendSSHPublicKeyRequest.from_dict(body)
    return web.Response(status=200)
