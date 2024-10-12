from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_authenticators200_response import GetAuthenticators200Response
from openapi_server.models.get_service_authenticator_status200_response import GetServiceAuthenticatorStatus200Response
from openapi_server.models.info200_response import Info200Response
from openapi_server.models.who_am_i200_response import WhoAmI200Response
from openapi_server import util


async def get_authenticators(request: web.Request, x_request_id=None) -> web.Response:
    """Details about which authenticators are on the Conjur Server

    Response contains three members: installed, configured, and enabled.  installed: The authenticator is implemented in Conjur and is available for configuration configured: The authenticator has a webservice in the DB that was loaded by policy enabled: The authenticator is enabled (in the DB or in the ENV) and is ready for authentication 

    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def get_gcp_authenticator_status(request: web.Request, account, x_request_id=None) -> web.Response:
    """Details whether an authentication service has been configured properly

    Once the status webservice has been properly configured and the relevant user groups have been given permissions to access the status webservice, the users in those groups can check the status of the authenticator.  This operation only supports the GCP authenticator  See [Conjur Documentation](https://docs.conjur.org/Latest/en/Content/Integrations/Authn-status.htm) for details on setting up the authenticator status webservice. 

    :param account: The organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def get_service_authenticator_status(request: web.Request, authenticator, service_id, account, x_request_id=None) -> web.Response:
    """Details whether an authentication service has been configured properly

    Once the status webservice has been properly configured and the relevant user groups have been given permissions to access the status webservice, the users in those groups can check the status of the authenticator.  Supported Authenticators:   - Azure   - OIDC  Not Supported:   - AWS IAM   - Kubernetes   - LDAP  See [Conjur Documentation](https://docs.conjur.org/Latest/en/Content/Integrations/Authn-status.htm) for details on setting up the authenticator status webservice. 

    :param authenticator: The type of authenticator
    :type authenticator: str
    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param account: The organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def health(request: web.Request, ) -> web.Response:
    """Health info about conjur

    You can request health checks against any cluster node using the Conjur API. These routes do not require authentication.  The health check attempts an internal HTTP or TCP connection to each Conjur Enterprise service. It also attempts a simple transaction against all internal databases. 


    """
    return web.Response(status=200)


async def info(request: web.Request, ) -> web.Response:
    """Basic information about the Conjur Enterprise server

    Information about the Conjur Enterprise node which was queried against.  Includes authenticator info, release/version info, configuration details, internal services, and role information. 


    """
    return web.Response(status=200)


async def remote_health(request: web.Request, remote) -> web.Response:
    """Health info about a given Conjur Enterprise server

    Use the remote_health route to check the health of any Conjur Enterprise Server from any other Conjur Enterprise Server. With this route, you can check master health relative to a follower, or follower health relative to a standby, and so on. 

    :param remote: The hostname of the remote to check
    :type remote: str

    """
    return web.Response(status=200)


async def who_am_i(request: web.Request, x_request_id=None) -> web.Response:
    """Provides information about the client making an API request.

    WhoAmI provides information about the client making an API request. It can be used to help troubleshoot configuration by verifying authentication and the client IP address for audit and network access restrictions. For more information, see Host Attributes. 

    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)
