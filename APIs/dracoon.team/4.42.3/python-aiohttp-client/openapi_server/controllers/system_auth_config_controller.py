from typing import List, Dict
from aiohttp import web

from openapi_server.models.active_directory_config import ActiveDirectoryConfig
from openapi_server.models.active_directory_config_list import ActiveDirectoryConfigList
from openapi_server.models.create_active_directory_config_request import CreateActiveDirectoryConfigRequest
from openapi_server.models.create_o_auth_client_request import CreateOAuthClientRequest
from openapi_server.models.create_open_id_idp_config_request import CreateOpenIdIdpConfigRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.o_auth_client import OAuthClient
from openapi_server.models.open_id_idp_config import OpenIdIdpConfig
from openapi_server.models.radius_config import RadiusConfig
from openapi_server.models.radius_config_create_request import RadiusConfigCreateRequest
from openapi_server.models.radius_config_update_request import RadiusConfigUpdateRequest
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.test_active_directory_config_request import TestActiveDirectoryConfigRequest
from openapi_server.models.test_active_directory_config_response import TestActiveDirectoryConfigResponse
from openapi_server.models.update_active_directory_config_request import UpdateActiveDirectoryConfigRequest
from openapi_server.models.update_o_auth_client_request import UpdateOAuthClientRequest
from openapi_server.models.update_open_id_idp_config_request import UpdateOpenIdIdpConfigRequest
from openapi_server import util


async def create_ad_config(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Create Active Directory configuration

    ### Description: Create a new Active Directory configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New Active Directory configuration created.  ### Further Information: None.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateActiveDirectoryConfigRequest.from_dict(body)
    return web.Response(status=200)


async def create_o_auth_client(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Create OAuth client

    ### Description: Create a new OAuth client.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New OAuth client created.  ### Further Information:   Client secret **MUST** have:   * at least 12 characters, at most 32 characters   * only lower case characters, upper case characters and digits   * at least 1 lower case character, 1 upper case character and 1 digit    The client secret is optional and will be generated if it is left empty.    Valid grant types are:   * &#x60;authorization_code&#x60;   * &#x60;implicit&#x60;   * &#x60;password&#x60;   * &#x60;client_credentials&#x60;   * &#x60;refresh_token&#x60;    Grant type &#x60;client_credentials&#x60; is currently **NOT** permitted!  Allowed characters for client ID are: &#x60;[a-zA-Z0-9_-]&#x60;  If grant types &#x60;authorization_code&#x60; or &#x60;implicit&#x60; are used, a redirect URI **MUST** be provided!  Default access token validity: **8 hours**   Default refresh token validity: **30 days** Default approval validity: **½ year**

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateOAuthClientRequest.from_dict(body)
    return web.Response(status=200)


async def create_open_id_idp_config(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Create OpenID Connect IDP configuration

    ### Description: Create new OpenID Connect IDP configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New OpenID Connect IDP configuration is created.  ### Further Information: None.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateOpenIdIdpConfigRequest.from_dict(body)
    return web.Response(status=200)


async def create_radius_config(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Create RADIUS configuration

    ### Description:   Create new RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: New RADIUS configuration is created.  ### Further Information: None.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = RadiusConfigCreateRequest.from_dict(body)
    return web.Response(status=200)


async def remove_ad_config(request: web.Request, ad_id, x_sds_auth_token=None) -> web.Response:
    """Remove Active Directory configuration

    ### Description: Delete an existing Active Directory configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Active Directory configuration is removed.  ### Further Information: None.

    :param ad_id: Active Directory ID
    :type ad_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_o_auth_client(request: web.Request, client_id, x_sds_auth_token=None) -> web.Response:
    """Remove OAuth client

    ### Description: Delete an existing OAuth client.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OAuth client is removed.  ### Further Information: None.

    :param client_id: OAuth client ID
    :type client_id: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_open_id_idp_config(request: web.Request, idp_id, x_sds_auth_token=None) -> web.Response:
    """Remove OpenID Connect IDP configuration

    ### Description: Delete an existing OpenID Connect IDP configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OpenID Connect IDP configuration is removed.  ### Further Information: None.

    :param idp_id: OpenID Connect IDP configuration ID
    :type idp_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_radius_config(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Remove RADIUS configuration

    ### Description:   Delete existing RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: RADIUS configuration is deleted.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_ad_config(request: web.Request, ad_id, x_sds_auth_token=None) -> web.Response:
    """Request Active Directory configuration

    ### Description:   Retrieve the configuration of an Active Directory.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Active Directory configuration is returned.  ### Further Information: None.

    :param ad_id: Active Directory ID
    :type ad_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_ad_configs(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request list of Active Directory configurations

    ### Description:   Retrieve a list of configured Active Directories.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of Active Directory configurations is returned.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_o_auth_client(request: web.Request, client_id, x_sds_auth_token=None) -> web.Response:
    """Request OAuth client

    ### Description:   Retrieve the configuration of an OAuth client.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OAuth client is returned.  ### Further Information: None.

    :param client_id: OAuth client ID
    :type client_id: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_o_auth_clients(request: web.Request, filter=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """Request list of OAuth clients

    ### Description:   Retrieve a list of configured OAuth clients.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of OAuth clients is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isStandard:eq:true&#x60;   Get standard OAuth clients.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;isStandard&#x60; | Standard client filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;isExternal&#x60; | External client filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;isEnabled&#x60; | Enabled/disabled clients filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort criteria are possible.   Fields are connected via logical conjunction **AND**.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;clientName:desc|isStandard:asc&#x60;   Sort by &#x60;clientName&#x60; descending **AND** &#x60;isStandard&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;clientName&#x60; | Client name | | &#x60;isStandard&#x60; | Is a standard client | | &#x60;isExternal&#x60; | Is a external client | | &#x60;isEnabled&#x60; | Is a enabled client |  &lt;/details&gt;

    :param filter: Filter string
    :type filter: str
    :param sort: Sort string
    :type sort: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_open_id_idp_config(request: web.Request, idp_id, x_sds_auth_token=None) -> web.Response:
    """Request OpenID Connect IDP configuration

    ### Description:   Retrieve an OpenID Connect IDP configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OpenID Connect IDP configuration is returned.  ### Further Information: None.

    :param idp_id: OpenID Connect IDP configuration ID
    :type idp_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_open_id_idp_configs(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request list of OpenID Connect IDP configurations

    ### Description:   Retrieve a list of configured OpenID Connect IDPs.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of OpenID Connect IDP configurations is returned.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_radius_config(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request RADIUS configuration

    ### Description:   Retrieve a RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: RADIUS configuration is returned.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def test_ad_config(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Test Active Directory configuration

    ### Description:   Test Active Directory configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Active Directory configuration is returned if successful.  ### Further Information: DRACOON tries to establish a connection with the provided information.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = TestActiveDirectoryConfigRequest.from_dict(body)
    return web.Response(status=200)


async def test_radius_config(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Test RADIUS server availability

    ### Description:   Test RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: RADIUS configuration is returned if successful.  ### Further Information: DRACOON tries to establish a connection with the provided information.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def update_ad_config(request: web.Request, ad_id, body, x_sds_auth_token=None) -> web.Response:
    """Update Active Directory configuration

    ### Description:   Update an existing Active Directory configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Active Directory configuration updated.  ### Further Information: None.

    :param ad_id: Active Directory ID
    :type ad_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateActiveDirectoryConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_o_auth_client(request: web.Request, client_id, body, x_sds_auth_token=None) -> web.Response:
    """Update OAuth client

    ### Description:   Update an existing OAuth client.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OAuth client updated.  ### Further Information:   Client secret **MUST** have:   * at least 12 characters, at most 32 characters   * only lower case characters, upper case characters and digits   * at least 1 lower case character, 1 upper case character and 1 digit    The client secret is optional and will be generated if it is left empty.    Valid grant types are:   * &#x60;authorization_code&#x60;   * &#x60;implicit&#x60;   * &#x60;password&#x60;   * &#x60;client_credentials&#x60;   * &#x60;refresh_token&#x60;    Grant type &#x60;client_credentials&#x60; is currently **NOT** permitted!  If grant types &#x60;authorization_code&#x60; or &#x60;implicit&#x60; are used, a redirect URI **MUST** be provided! 

    :param client_id: OAuth client ID
    :type client_id: str
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateOAuthClientRequest.from_dict(body)
    return web.Response(status=200)


async def update_open_id_idp_config(request: web.Request, idp_id, body, x_sds_auth_token=None) -> web.Response:
    """Update OpenID Connect IDP configuration

    ### Description:   Update an existing OpenID Connect IDP configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: OpenID Connect IDP configuration is updated.  ### Further Information: None.

    :param idp_id: OpenID Connect IDP configuration ID
    :type idp_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateOpenIdIdpConfigRequest.from_dict(body)
    return web.Response(status=200)


async def update_radius_config(request: web.Request, body, x_sds_auth_token=None) -> web.Response:
    """Update RADIUS configuration

    ### Description:   Update existing RADIUS configuration.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: RADIUS configuration is updated.  ### Further Information: None.

    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = RadiusConfigUpdateRequest.from_dict(body)
    return web.Response(status=200)
