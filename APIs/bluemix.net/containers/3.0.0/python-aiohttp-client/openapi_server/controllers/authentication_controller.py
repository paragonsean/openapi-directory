from typing import List, Dict
from aiohttp import web

from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_refresh import CertificateRefresh
from openapi_server import util


async def tlskey_get(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """Retrieve the TLS Certificate

    This endpoint returns the TLS (Transport Layer Security) certificate to the user (corresponding IBM Containers command: &#x60;cf ic login&#x60;). The TLS certificate is a SSL certificate that is used to authenticate the user&#39;s CLI with the IBM Containers service and to establish a secure communication between the user&#39;s local machine and the container in Bluemix.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def tlskey_refresh_put(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """Refresh the TLS Certificate

    This endpoint requests to generate a new TLS (Transport Layer Security) certificate on the server and to update the existing user TLS certificate (corresponding IBM Containers command: &#x60;cf ic init&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. 
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)
