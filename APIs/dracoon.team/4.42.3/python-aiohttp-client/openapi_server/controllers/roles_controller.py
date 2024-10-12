from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.group_ids import GroupIds
from openapi_server.models.role_group_list import RoleGroupList
from openapi_server.models.role_list import RoleList
from openapi_server.models.role_user_list import RoleUserList
from openapi_server.models.user_ids import UserIds
from openapi_server import util


async def add_role_groups(request: web.Request, role_id, body, x_sds_auth_token=None) -> web.Response:
    """Assign group(s) to the role

    ### Description: Assign group(s) to a role.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; grant permission on desired role&lt;/span&gt; required.  ### Postcondition: One or more groups will be added to a role.  ### Further Information: None.

    :param role_id: Role ID
    :type role_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = GroupIds.from_dict(body)
    return web.Response(status=200)


async def add_role_users(request: web.Request, role_id, body, x_sds_auth_token=None) -> web.Response:
    """Assign user(s) to the role

    ### Description: Assign user(s) to a role.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; grant permission on desired role&lt;/span&gt; required.  ### Postcondition: One or more users will be added to a role.  ### Further Information: None.

    :param role_id: Role ID
    :type role_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UserIds.from_dict(body)
    return web.Response(status=200)


async def request_role_groups(request: web.Request, role_id, offset=None, limit=None, filter=None, x_sds_auth_token=None) -> web.Response:
    """Request groups with specific role

    ### Description:   Get all groups with a specific role.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read groups&lt;/span&gt; required.  ### Postcondition: List of to the role assigned groups is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isMember:eq:false|name:cn:searchString&#x60;   Get all groups that are **NOT** a member of that role **AND** whose name contains &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;isMember&#x60; | Filter the groups which are (not) member of that role | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;true&#x60; | | &#x60;name&#x60; | Group name filter | &#x60;cn&#x60; | Group name contains value. | &#x60;search String&#x60; |  &lt;/details&gt;

    :param role_id: Role ID
    :type role_id: int
    :param offset: Range offset
    :type offset: int
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param filter: Filter string
    :type filter: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_role_users(request: web.Request, role_id, offset=None, limit=None, filter=None, x_sds_auth_token=None) -> web.Response:
    """Request users with specific role

    ### Description:   Get all users with a specific role.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read users&lt;/span&gt; required.  ### Postcondition: List of users is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isMember:eq:false|user:cn:searchString&#x60;   Get all users that are **NOT** member of that role **AND** whose (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) is like &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;user&#x60; | User filter | &#x60;cn&#x60; | User contains value (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;). | &#x60;search String&#x60; | | &#x60;isMember&#x60; | Filter the users which are (not) member of that role | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;true&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;displayName&#x60;&lt;/del&gt; | User display name filter (use &#x60;user&#x60; filter) | &#x60;cn&#x60; | User display name contains value (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60;). | &#x60;search String&#x60; |  &lt;/details&gt;

    :param role_id: Role ID
    :type role_id: int
    :param offset: Range offset
    :type offset: int
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param filter: Filter string
    :type filter: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_roles(request: web.Request, x_sds_auth_token=None) -> web.Response:
    """Request all roles with assigned rights

    ### Description:   Retrieve a list of all roles with assigned rights.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read users&lt;/span&gt; required.  ### Postcondition: List of roles with assigned rights is returned.  ### Further Information: None.

    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def revoke_role_groups(request: web.Request, role_id, body, x_sds_auth_token=None) -> web.Response:
    """Revoke granted role from group(s)

    ### Description:   Revoke granted group(s) from a role.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; grant permission on desired role&lt;/span&gt; required.   For each role, at least one non-expiring user **MUST** remain who may grant the role.  ### Postcondition: One or more groups will be removed from a role.  ### Further Information: None.

    :param role_id: Role ID
    :type role_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = GroupIds.from_dict(body)
    return web.Response(status=200)


async def revoke_role_users(request: web.Request, role_id, body, x_sds_auth_token=None) -> web.Response:
    """Revoke granted role from user(s)

    ### Description:   Revoke granted user(s) from a role.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; grant permission on desired role&lt;/span&gt; required.   For each role, at least one non-expiring user **MUST** remain who may grant the role.  ### Postcondition: One or more users will be removed from a role.  ### Further Information: None.

    :param role_id: Role ID
    :type role_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UserIds.from_dict(body)
    return web.Response(status=200)
