from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def change_password(request: web.Request, account, body, x_request_id=None) -> web.Response:
    """Changes a user’s password.

    You must provide the login name and current password or API key of the user whose password is to be updated in an HTTP Basic Authentication header. Also replaces the user’s API key with a new securely generated random value. You can fetch the new API key using the Login method.  The Basic authentication-compliant header is formed by: 1. Concatenating the role&#39;s name, a literal colon character &#39;:&#39;,    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: &#x60;Basic &#x60;    (note the required space). 4. Providing the result as the value of the &#x60;Authorization&#x60; HTTP header:    &#x60;Authorization: Basic &lt;authentication string&gt;&#x60;.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, &#x60;curl&#x60; and all of the Conjur client libraries provide this.  Note that machine roles (Hosts) do not have passwords. They authenticate using their API keys, while passwords are only used by human users. 

    :param account: Organization account name
    :type account: str
    :param body: New password
    :type body: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def enable_authenticator(request: web.Request, authenticator, account, x_request_id=None, enabled=None) -> web.Response:
    """Enables or disables authenticator defined without service_id.

    Allows you to either enable or disable a given authenticator that does not have service_id (For example: authn-gcp).  When you enable or disable an authenticator via this endpoint, the status of the authenticator is stored in the Conjur database. The enablement status of the authenticator service may be overridden by setting the &#x60;CONJUR_AUTHENTICATORS&#x60; environment variable on the Conjur server; in the case where this environment variable is set, the database record of whether the authenticator service is enabled will be ignored.  **This endpoint is part of an early implementation of support for enabling Conjur authenticators via the API, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future.** 

    :param authenticator: The authenticator to update
    :type authenticator: str
    :param account: Organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param enabled: 
    :type enabled: bool

    """
    return web.Response(status=200)


async def enable_authenticator_instance(request: web.Request, authenticator, service_id, account, x_request_id=None) -> web.Response:
    """Enables or disables authenticator service instances.

    Allows you to either enable or disable a given authenticator service instance.  When you enable or disable an authenticator service instance via this endpoint, the status of the authenticator service instance is stored in the Conjur database. The enablement status of the authenticator service instance may be overridden by setting the &#x60;CONJUR_AUTHENTICATORS&#x60; environment variable on the Conjur server; in the case where this environment variable is set, the database record of whether the authenticator service instance is enabled will be ignored.  **This endpoint is part of an early implementation of support for enabling Conjur authenticators via the API, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future.** 

    :param authenticator: The authenticator to update
    :type authenticator: dict | bytes
    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param account: Organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    authenticator = .from_dict(authenticator)
    return web.Response(status=200)


async def get_access_token(request: web.Request, account, login, body, x_request_id=None, accept_encoding=None) -> web.Response:
    """Gets a short-lived access token, which is required in the header of most subsequent API requests. 

    A client can obtain an access token by presenting a valid login name and API key.  The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  The &#x60;login&#x60; must be URL encoded. For example, &#x60;alice@devops&#x60; must be encoded as &#x60;alice%40devops&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  For host authentication, the &#x60;login&#x60; is the host ID with the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  This is the default authentication endpoint only. See other endpoints for details on authenticating to Conjur using another method, e.g. for applications running in Azure or Kubernetes. 

    :param account: Organization account name
    :type account: str
    :param login: URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60;
    :type login: str
    :param body: API Key
    :type body: 
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param accept_encoding: Setting the Accept-Encoding header to base64 will return a pre-encoded access token
    :type accept_encoding: str

    """
    return web.Response(status=200)


async def get_access_token_via_aws(request: web.Request, service_id, account, login, body, x_request_id=None, accept_encoding=None) -> web.Response:
    """Get a short-lived access token for applications running in AWS.

    The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  The &#x60;login&#x60; must be URL encoded and the host ID must have the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  For detailed instructions on authenticating to Conjur using this endpoint, reference the documentation: [AWS IAM Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/AWS_IAM_Authenticator.htm) (&#x60;authn-iam&#x60;). 

    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param account: Organization account name
    :type account: str
    :param login: URL-encoded login name. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60;
    :type login: dict | bytes
    :param body: AWS Signature header
    :type body: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param accept_encoding: Setting the Accept-Encoding header to base64 will return a pre-encoded access token
    :type accept_encoding: str

    """
    login = .from_dict(login)
    return web.Response(status=200)


async def get_access_token_via_azure(request: web.Request, service_id, account, login, x_request_id=None, accept_encoding=None, jwt=None) -> web.Response:
    """Gets a short-lived access token for applications running in Azure.

    The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  The &#x60;login&#x60; must be URL encoded and the host ID must have the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  To authenticate to Conjur using this endpoint, reference the detailed documentation: [Azure Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/azure_authn.htm) (&#x60;authn-azure&#x60;). 

    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param account: Organization account name
    :type account: str
    :param login: URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60;
    :type login: dict | bytes
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param accept_encoding: Setting the Accept-Encoding header to base64 will return a pre-encoded access token
    :type accept_encoding: str
    :param jwt: 
    :type jwt: str

    """
    login = .from_dict(login)
    return web.Response(status=200)


async def get_access_token_via_gcp(request: web.Request, account, x_request_id=None, accept_encoding=None, jwt=None) -> web.Response:
    """Gets a short-lived access token for applications running in Google Cloud Platform. 

    Use the GCP Authenticator API to send an authentication request from a Google Cloud service to Conjur.  For more information, see [the documentation](https://docs.conjur.org/Latest/en/Content/Operations/Services/cjr-gcp-authn.htm). 

    :param account: Organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param accept_encoding: Setting the Accept-Encoding header to base64 will return a pre-encoded access token
    :type accept_encoding: str
    :param jwt: 
    :type jwt: str

    """
    return web.Response(status=200)


async def get_access_token_via_jwt(request: web.Request, account, service_id, x_request_id=None, jwt=None) -> web.Response:
    """Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. 

    Use the JWT Authenticator to leverage the identity layer provided by JWT to authenticate with Conjur. 

    :param account: Organization account name
    :type account: str
    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param jwt: 
    :type jwt: str

    """
    return web.Response(status=200)


async def get_access_token_via_jwt_with_id(request: web.Request, account, id, service_id, x_request_id=None) -> web.Response:
    """Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. Covers the case of use of optional URL parameter \&quot;ID\&quot; 

    Use the JWT Authenticator to leverage the identity layer provided by JWT to authenticate with Conjur. 

    :param account: Organization account name
    :type account: str
    :param id: Organization user id
    :type id: str
    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def get_access_token_via_kubernetes(request: web.Request, service_id, account, login, x_request_id=None, accept_encoding=None) -> web.Response:
    """Gets a short-lived access token for applications running in Kubernetes.

    The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  The &#x60;login&#x60; must be URL encoded and the host ID must have the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  To authenticate to Conjur using this endpoint, reference the detailed documentation: [Kubernetes Authenticator](https://docs.conjur.org/Latest/en/Content/Operations/Services/k8s_auth.htm) (&#x60;authn-k8s&#x60;). 

    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param account: Organization account name
    :type account: str
    :param login: URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60;
    :type login: dict | bytes
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param accept_encoding: Setting the Accept-Encoding header to base64 will return a pre-encoded access token
    :type accept_encoding: str

    """
    login = .from_dict(login)
    return web.Response(status=200)


async def get_access_token_via_ldap(request: web.Request, service_id, account, login, x_request_id=None, accept_encoding=None, body=None) -> web.Response:
    """Gets a short-lived access token for users and hosts using their LDAP identity to access the Conjur API. 

    The access token is used to communicate to the REST API that the bearer of the token has been authorized to access the API and perform specific actions specified by the scope that was granted during authorization.  For API usage, the base64-encoded access token is ordinarily passed as an HTTP Authorization header as &#x60;Authorization: Token token&#x3D;&lt;base64-encoded token&gt;&#x60;.  The &#x60;login&#x60; must be URL encoded. For example, &#x60;alice@devops&#x60; must be encoded as &#x60;alice%40devops&#x60;.  The &#x60;service_id&#x60;, if given, must be URL encoded. For example, &#x60;prod/gke&#x60; must be encoded as &#x60;prod%2Fgke&#x60;.  For host authentication, the &#x60;login&#x60; is the host ID with the prefix &#x60;host/&#x60;. For example, the host webserver would login as &#x60;host/webserver&#x60;, and would be encoded as &#x60;host%2Fwebserver&#x60;.  To authenticate to Conjur using a LDAP, reference the detailed documentation: [LDAP Authenticator](https://docs.conjur.org/Latest/en/Content/Integrations/ldap/ldap_authenticator.html) (&#x60;authn-ldap&#x60;). 

    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param account: Organization account name
    :type account: str
    :param login: URL-encoded login name. For users, it’s the user ID. For hosts, the login name is &#x60;host/&lt;host-id&gt;&#x60;
    :type login: dict | bytes
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param accept_encoding: Setting the Accept-Encoding header to base64 will return a pre-encoded access token
    :type accept_encoding: str
    :param body: API key
    :type body: 

    """
    login = .from_dict(login)
    return web.Response(status=200)


async def get_access_token_via_oidc(request: web.Request, service_id, account, x_request_id=None, id_token=None) -> web.Response:
    """Gets a short-lived access token for applications using OpenID Connect (OIDC) to access the Conjur API. 

    Use the OIDC Authenticator to leverage the identity layer provided by OIDC to authenticate with Conjur.  For more information see [the documentation](https://docs.conjur.org/Latest/en/Content/OIDC/OIDC.htm). 

    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param account: Organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param id_token: 
    :type id_token: str

    """
    return web.Response(status=200)


async def get_api_key(request: web.Request, account, x_request_id=None) -> web.Response:
    """Gets the API key of a user given the username and password via HTTP Basic Authentication. 

    Passwords are stored in the Conjur database using &#x60;bcrypt&#x60; with a work factor of 12. Therefore, login is a fairly expensive operation. However, once the API key is obtained, it may be used to inexpensively obtain access tokens by calling the Authenticate method. An access token is required to use most other parts of the Conjur API.  The Basic authentication-compliant header is formed by: 1. Concatenating the role&#39;s name, a literal colon character &#39;:&#39;,    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: &#x60;Basic &#x60;    (note the required space). 4. Providing the result as the value of the &#x60;Authorization&#x60; HTTP header:    &#x60;Authorization: Basic &lt;authentication string&gt;&#x60;.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, &#x60;curl&#x60; and all of the Conjur client libraries provide this.  Note that machine roles (Hosts) do not have passwords and do not need to use this endpoint. 

    :param account: Organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def get_api_key_via_ldap(request: web.Request, service_id, account, x_request_id=None) -> web.Response:
    """Gets the Conjur API key of a user given the LDAP username and password via HTTP Basic Authentication. 

    Exchange your LDAP credentials for a Conjur API key. Once the API key is obtained, it may be used to inexpensively obtain access tokens by calling the Authenticate method. An access token is required to use most other parts of the Conjur API.  The Basic authentication-compliant header is formed by: 1. Concatenating the LDAP username, a literal colon character &#39;:&#39;,    and the password to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: &#x60;Basic &#x60;    (note the required space). 4. Providing the result as the value of the &#x60;Authorization&#x60; HTTP header:    &#x60;Authorization: Basic &lt;authentication string&gt;&#x60;.  Your HTTP/REST client probably provides HTTP basic authentication support. 

    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param account: Organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def k8s_inject_client_cert(request: web.Request, service_id, body, x_request_id=None, host_id_prefix=None) -> web.Response:
    """For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application&#39;s Kubernetes pod. 

    This request sends a Certificate Signing Request to Conjur, which uses the Kubernetes API to inject a client certificate into the application pod.  This endpoint requires a properly configured Conjur Certificate Authority service alongside a properly configured and enabled Kubernetes authenticator. For detailed instructions, see [the documentation](https://docs.conjur.org/Latest/en/Content/Integrations/kubernetes.htm). 

    :param service_id: URL-Encoded authenticator service ID
    :type service_id: str
    :param body: Valid certificate signing request that includes the host identity suffix as the CSR common name 
    :type body: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param host_id_prefix: Dot-separated policy tree, prefixed by &#x60;host.&#x60;, where the application identity is defined
    :type host_id_prefix: str

    """
    return web.Response(status=200)


async def rotate_api_key(request: web.Request, account, x_request_id=None, role=None) -> web.Response:
    """Rotates a role&#39;s API key.

    Any role can rotate its own API key. The name and password (for users) or current API key (for hosts and users) of the role must be provided via HTTP Basic Authorization.  To rotate another role&#39;s API key, you may provide your name and password (for users) or current API key (for hosts and users) via HTTP Basic Authorization with the request. Alternatively, you may provide your Conjur access token via the standard Conjur &#x60;Authorization&#x60; header.  The Basic authentication-compliant header is formed by: 1. Concatenating the role&#39;s name, a literal colon character &#39;:&#39;,    and the password or API key to create the authentication string. 2. Base64-encoding the authentication string. 3. Prefixing the authentication string with the scheme: &#x60;Basic &#x60;    (note the required space). 4. Providing the result as the value of the &#x60;Authorization&#x60; HTTP header:    &#x60;Authorization: Basic &lt;authentication string&gt;&#x60;.  Your HTTP/REST client probably provides HTTP basic authentication support. For example, &#x60;curl&#x60; and all of the Conjur client libraries provide this.  If using the Conjur &#x60;Authorization&#x60; header, its value should be set to &#x60;Token token&#x3D;&lt;base64-encoded access token&gt;&#x60;.  Note that the body of the request must be the empty string. 

    :param account: Organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param role: (**Optional**) role specifier in &#x60;{kind}:{identifier}&#x60; format  ##### Permissions required  &#x60;update&#x60; privilege on the role whose API key is being rotated. 
    :type role: str

    """
    return web.Response(status=200)
