from typing import List, Dict
from aiohttp import web

from openapi_server.models.floating_ip import FloatingIP
from openapi_server import util


async def containers_floating_ips_get(request: web.Request, x_auth_token, x_auth_project_id, all=None) -> web.Response:
    """List available public IP addresses in a space

    This endpoint returns a list of all public IP addresses that are allocated to a space and not bound to a container. If you want to list all public IP addresses that are allocated to a space, even those that are already bound to a container, use the &#x60;all&#x60; query parameter (corrsponding IBM Containers command: &#x60;cf ic ip list&#x60;).

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param all: If this option is set to &#x60;all&#x3D;1&#x60;, &#x60;all&#x3D;True&#x60;, or &#x60;all&#x3D;true&#x60;, all public IP addresses that are allocated to a space are returned. If this option is set to &#x60;all&#x3D;0&#x60;, &#x60;all&#x3D;False&#x60;, or &#x60;all&#x3D;false&#x60;, only available public IP addresses that are allocated but not bound to a container are returned. By default, only available public IP addresses are returned.
    :type all: bool

    """
    return web.Response(status=200)


async def containers_floating_ips_ip_release_post(request: web.Request, x_auth_token, x_auth_project_id, ip) -> web.Response:
    """Release public IP address

    This endpoint releases a public IP address from a space (corresponding IBM Containers command: &#x60;cf ic ip release &lt;ip_adress&gt;&#x60;). The public IP address is no longer allocated to the space. If a container was bound to the IP address, it is automatically unbound.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param ip: The public IP address that you want to release. Run &#x60;cf ic ip list&#x60; or call the &#x60;GET /containers/floating-ips?all&#x3D;true&#x60; endpoint to review all public IP address that are allocated to your space. After a public IP address is released, it will no longer be allocated to your space.
    :type ip: str

    """
    return web.Response(status=200)


async def containers_floating_ips_request_post(request: web.Request, x_auth_token, x_auth_project_id) -> web.Response:
    """Request a public IP address for a space

    This endpoint requests a new public IP address for a space (corresponding IBM Containers command: &#x60;cf ic ip request&#x60;). The number of public IP addresses depends on the quota that is assigned to the space. If there is not enough quota left to request a new public IP address, you can either contact your organization manager to increase the quota, or unbind an existing IP address from a container by running &#x60;cf ic ip unbind &lt;ip_adress&gt; &lt;container&gt;&#x60; command, or  calling the &#x60;POST /container/{name_or_id}/floating-ips/{ip}/unbind&#x60; endpoint.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str

    """
    return web.Response(status=200)


async def containers_name_or_id_floating_ips_ip_bind_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, ip) -> web.Response:
    """Bind a public IP address to a single container

    This endpoint binds an available public IP address to a single container (corresponding IBM Containers command: &#x60;cf ic ip bind &lt;ip_adress&gt; &lt;container&gt;&#x60;). After a container is bound to a public IP address, it can be accessed at &#x60;https://&lt;public_ip_adress&gt;:&lt;public_port&gt;&#x60;.

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The name or ID of the container that you want to bind to the public IP address. Run the &#x60;cf ic ps&#x60; command or call the &#x60;GET /containers/json&#x60; endpoint to retrieve a list of containers in your space.
    :type name_or_id: str
    :param ip: The public IP address that you want to bind to your container.   Note: The public IP address must be available in the space and not bound to a container. Run &#x60;cf ic ip list&#x60; or call the &#x60;GET /containers/floating-ips&#x60; endpoint.
    :type ip: str

    """
    return web.Response(status=200)


async def containers_name_or_id_floating_ips_ip_unbind_post(request: web.Request, x_auth_token, x_auth_project_id, name_or_id, ip) -> web.Response:
    """Unbind a public IP address from a container

    This endpoint unbinds a public IP address from a container (corresponding IBM Containers command: &#x60;cf ic ip unbind &lt;ip_adress&gt; &lt;container&gt;&#x60;). The container that is unbound from the IP address will not be accessible from the internet anymore. The public IP address will be further allocated to the space and can be used to be bound to other containers. 

    :param x_auth_token: The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token.
    :type x_auth_token: str
    :param x_auth_project_id: The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID.
    :type x_auth_project_id: str
    :param name_or_id: The name or ID of the container that you want to bind to the public IP address. Run the &#x60;cf ic ps&#x60; command or call the &#x60;GET /containers/json&#x60; endpoint to retrieve a list of containers in your space. 
    :type name_or_id: str
    :param ip: The public IP address that you want to unbind from your container.    Note: After unbinding a public IP address, this IP address will still be allocated to the space and can be used to be bound to other containers.
    :type ip: str

    """
    return web.Response(status=200)
