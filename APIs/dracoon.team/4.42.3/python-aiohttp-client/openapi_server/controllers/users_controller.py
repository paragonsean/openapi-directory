from typing import List, Dict
from aiohttp import web

from openapi_server.models.attributes_response import AttributesResponse
from openapi_server.models.create_user_request import CreateUserRequest
from openapi_server.models.emergency_mfa_code_response import EmergencyMfaCodeResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.last_admin_user_room_list import LastAdminUserRoomList
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.role_list import RoleList
from openapi_server.models.room_tree_data_list import RoomTreeDataList
from openapi_server.models.update_user_request import UpdateUserRequest
from openapi_server.models.user_attributes import UserAttributes
from openapi_server.models.user_data import UserData
from openapi_server.models.user_group_list import UserGroupList
from openapi_server.models.user_list import UserList
from openapi_server import util


async def create_user(request: web.Request, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Create new user

    ### Description: Create a new user.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change users&lt;/span&gt; required.  ### Postcondition: New user is created.  ### Further Information: * If a user should **NOT** expire, leave &#x60;expireAt&#x60; empty. * All input fields are limited to **150** characters * Forbidden characters in first or last name: [&#x60;&lt;&#x60;, &#x60;&gt;&#x60;] * Forbidden characters in passwords: [&#x60;&amp;&#x60;, &#x60;&#39;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;]  ### Authentication Method Options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Option Key | Option Value | | :--- | :--- | :--- | | &#x60;basic&#x60; / &#x60;sql&#x60; | &#x60;username&#x60; | Unique user identifier | | &#x60;active_directory&#x60; | &#x60;ad_config_id&#x60; (optional) | Active Directory configuration ID | |  | &#x60;username&#x60; | Active Directory username according to authentication setting &#x60;userFilter&#x60; | | &#x60;radius&#x60; | &#x60;username&#x60; | RADIUS username | | &#x60;openid&#x60; | &#x60;openid_config_id&#x60; (optional) | OpenID Connect configuration ID | |  | &#x60;username&#x60; | OpenID Connect username according to authentication setting &#x60;mappingClaim&#x60; |  &lt;/details&gt;

    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateUserRequest.from_dict(body)
    return web.Response(status=200)


async def remove_user(request: web.Request, user_id, x_sds_auth_token=None) -> web.Response:
    """Remove user

    ### Description: Delete a user.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; delete users&lt;/span&gt; required.  ### Postcondition: User is deleted.  ### Further Information: User **CANNOT** be deleted if he is a last room administrator of any room.

    :param user_id: User ID
    :type user_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_user_attribute(request: web.Request, user_id, key, x_sds_auth_token=None) -> web.Response:
    """Remove custom user attribute

    ### Description: Delete custom user attribute.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change users&lt;/span&gt; required.  ### Postcondition: Custom user attribute is deleted.  ### Further Information: * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**.

    :param user_id: User ID
    :type user_id: int
    :param key: Key
    :type key: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_emergency_mfa_code(request: web.Request, user_id, x_sds_auth_token=None) -> web.Response:
    """Request emergency MFA code

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description:   Request emergency MFA code for a specific user.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change users&lt;/span&gt; required.  ### Postcondition: Emergency MFA code is returned.  ### Further Information: Emergency code can be used instead of standard MFA authentication to disable all MFA setups.

    :param user_id: 
    :type user_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_last_admin_rooms_users(request: web.Request, user_id, x_sds_auth_token=None) -> web.Response:
    """Request rooms where the user is last admin

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.10.0&lt;/h3&gt;  ### Description:   Retrieve a list of all rooms where the user is last admin (except homeroom and its subordinary rooms).  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change users&lt;/span&gt; required.  ### Postcondition: List of rooms is returned.   ### Further Information: An empty list is returned if no rooms were found where the user is last admin.

    :param user_id: User ID
    :type user_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_user(request: web.Request, user_id, x_sds_date_format=None, effective_roles=None, x_sds_auth_token=None) -> web.Response:
    """Request user

    ### Description:   Retrieve detailed information about a single user.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read users&lt;/span&gt; required.  ### Postcondition: User information is returned.  ### Further Information: None.  ### Authentication Method Options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Option Key | Option Value | | :--- | :--- | :--- | | &#x60;basic&#x60; / &#x60;sql&#x60; | &#x60;username&#x60; | Unique user identifier | | &#x60;active_directory&#x60; | &#x60;ad_config_id&#x60; (optional) | Active Directory configuration ID | |  | &#x60;username&#x60; | Active Directory username according to authentication setting &#x60;userFilter&#x60; | | &#x60;radius&#x60; | &#x60;username&#x60; | RADIUS username | | &#x60;openid&#x60; | &#x60;openid_config_id&#x60; (optional) | OpenID Connect configuration ID | |  | &#x60;username&#x60; | OpenID Connect username according to authentication setting &#x60;mappingClaim&#x60; |  &lt;/details&gt;

    :param user_id: User ID
    :type user_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param effective_roles: Filter users with DIRECT or DIRECT **AND** EFFECTIVE roles.  * &#x60;false&#x60;: DIRECT roles  * &#x60;true&#x60;: DIRECT **AND** EFFECTIVE roles  DIRECT means: e.g. user gets role **directly** granted from someone with _grant permission_ right.  EFFECTIVE means: e.g. user gets role through **group membership**.
    :type effective_roles: bool
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_user_attributes(request: web.Request, user_id, offset=None, limit=None, filter=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """Request custom user attributes

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.12.0&lt;/h3&gt;  ### Description:   Retrieve a list of user attributes.  ### Precondition: None.  ### Postcondition: List of attributes is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;key:cn:searchString_1|value:cn:searchString_2&#x60;   Filter by attribute key contains &#x60;searchString_1&#x60; **AND** attribute value contains &#x60;searchString_2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;key&#x60; | User attribute key filter | &#x60;cn, eq, sw&#x60; | Attribute key contains / equals / starts with value. | &#x60;search String&#x60; | | &#x60;value&#x60; | User attribute value filter | &#x60;cn, eq, sw&#x60; | Attribute value contains / equals / starts with value. | &#x60;search String&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;key:asc|value:desc&#x60;   Sort by &#x60;key&#x60; ascending **AND** by &#x60;value&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;key&#x60; | User attribute key | | &#x60;value&#x60; | User attribute value |  &lt;/details&gt;

    :param user_id: User ID
    :type user_id: int
    :param offset: Range offset
    :type offset: int
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param filter: Filter string
    :type filter: str
    :param sort: Sort string
    :type sort: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_user_groups(request: web.Request, user_id, offset=None, limit=None, filter=None, x_sds_auth_token=None) -> web.Response:
    """Request groups that user is a member of or / and can become a member

    ### Description:   Retrieves a list of groups a user is member of and / or can become a member.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read users&lt;/span&gt; required.  ### Postcondition: List of groups is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isMember:eq:false|name:cn:searchString&#x60;   Get all groups that the user is **NOT** member of **AND** whose name is like &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Group name filter | &#x60;cn&#x60; | Group name contains value. | &#x60;search String&#x60; | | &#x60;isMember&#x60; | Filter the groups which the user is (not) member of | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;true&#x60; |  &lt;/details&gt;

    :param user_id: User ID
    :type user_id: int
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


async def request_user_roles(request: web.Request, user_id, x_sds_auth_token=None) -> web.Response:
    """Request user&#39;s granted roles

    ### Description:   Retrieve a list of all roles granted to a user.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read users&lt;/span&gt; required.  ### Postcondition: List of granted roles is returned.  ### Further Information: None.

    :param user_id: User ID
    :type user_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_users(request: web.Request, x_sds_date_format=None, offset=None, limit=None, filter=None, sort=None, include_attributes=None, include_roles=None, include_manageable_rooms=None, x_sds_auth_token=None) -> web.Response:
    """Request users

    ### Description:   Returns a list of DRACOON users.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read users&lt;/span&gt; required.  ### Postcondition: List of users is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Except for &#x60;login&#x60;, &#x60;firstName&#x60; and  &#x60;lastName&#x60; - these are connected via logical disjunction (**OR**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;login:cn:searchString_1|firstName:cn:searchString_2|lockStatus:eq:2&#x60;   Filter users by login contains &#x60;searchString_1&#x60; **OR** firstName contains &#x60;searchString_2&#x60; **AND** those who are **NOT** locked.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60;  | Operator Description | &#x60;VALUE&#x60;                                                                                                                                                                                                                                                                                                                                                                                              | | :--- | :--- |:------------| :--- |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | &#x60;email&#x60; | Email filter | &#x60;eq&#x60;, &#x60;cn&#x60;  | Email contains value. | &#x60;search String&#x60;                                                                                                                                                                                                                                                                                                                                                                                      | | &#x60;userName&#x60; | User name filter | &#x60;eq&#x60;, &#x60;cn&#x60;  | UserName contains value. | &#x60;search String&#x60;                                                                                                                                                                                                                                                                                                                                                                                      | | &#x60;firstName&#x60; | User first name filter | &#x60;cn&#x60;        | User first name contains value. | &#x60;search String&#x60;                                                                                                                                                                                                                                                                                                                                                                                      | | &#x60;lastName&#x60; | User last name filter | &#x60;cn&#x60;        | User last name contains value. | &#x60;search String&#x60;                                                                                                                                                                                                                                                                                                                                                                                      | | &#x60;isLocked&#x60; | User lock status filter | &#x60;eq&#x60;        |  | &#x60;true or false&#x60;                                                                                                                                                                                                                                                                                                                                                                                      | | &#x60;effectiveRoles&#x60; | Filter users with DIRECT or DIRECT **AND** EFFECTIVE roles&lt;ul&gt;&lt;li&gt;&#x60;false&#x60;: DIRECT roles&lt;/li&gt;&lt;li&gt;&#x60;true&#x60;: DIRECT **AND** EFFECTIVE roles&lt;/li&gt;&lt;/ul&gt;DIRECT means: e.g. user gets role **directly** granted from someone with _grant permission_ right.&lt;br&gt;EFFECTIVE means: e.g. user gets role through **group membership**. | &#x60;eq&#x60;        |  | &#x60;true or false&#x60;&lt;br&gt;default: &#x60;false&#x60;                                                                                                                                                                                                                                                                                                                                                                  | | &#x60;createdAt&#x60; | Creation date filter | &#x60;ge, le&#x60;    | Creation date is greater / less equals than value.&lt;br&gt;Multiple operator values are allowed and will be connected via logical conjunction (**AND**).&lt;br&gt;e.g. &#x60;createdAt:ge:2016-12-31&#x60;&amp;#124;&#x60;createdAt:le:2018-01-01&#x60; | &#x60;Date (yyyy-MM-dd)&#x60;                                                                                                                                                                                                                                                                                                                                                                                  | | &#x60;phone&#x60; | Phone filter | &#x60;eq&#x60;        | Phone equals value. | &#x60;search String&#x60;                                                                                                                                                                                                                                                                                                                                                                                      | | &#x60;isEncryptionEnabled&#x60; | Encryption status filter&lt;ul&gt;&lt;li&gt;client-side encryption&lt;/li&gt;&lt;li&gt;private key possession&lt;/li&gt;&lt;/ul&gt; | &#x60;eq&#x60;        |  | &#x60;true or false&#x60;                                                                                                                                                                                                                                                                                                                                                                                      | | &#x60;hasRole&#x60; | User role filter&lt;br&gt;Depends on **effectiveRoles**.&lt;br&gt;For more Roles information please call &#x60;GET /roles API&#x60; | &#x60;eq&#x60;, &#x60;neq&#x60; | User role  equals value. | &lt;ul&gt;&lt;li&gt;&#x60;CONFIG_MANAGER&#x60; - Manage global configs&lt;/li&gt;&lt;li&gt;&#x60;USER_MANAGER&#x60; - Manage Users&lt;/li&gt;&lt;li&gt;&#x60;GROUP_MANAGER&#x60; - Manage User-Groups&lt;/li&gt;&lt;li&gt;&#x60;ROOM_MANAGER&#x60; - Manage top level Data Rooms&lt;/li&gt;&lt;li&gt;&#x60;LOG_AUDITOR&#x60; - Read logs&lt;/li&gt;&lt;li&gt;&#x60;NONMEMBER_VIEWER&#x60; - View users and groups when having room manage permission&lt;/li&gt;&lt;li&gt;&#x60;USER&#x60; - Regular User role&lt;/li&gt;&lt;li&gt;&#x60;GUEST_USER&#x60; - Guest User role&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;lockStatus&#x60;&lt;/del&gt; | User lock status filter | &#x60;eq&#x60; | User lock status equals value. | &lt;ul&gt;&lt;li&gt;&#x60;0&#x60; - Locked&lt;/li&gt;&lt;li&gt;&#x60;1&#x60; - Web access allowed&lt;/li&gt;&lt;li&gt;&#x60;2&#x60; - Web and mobile access allowed&lt;/li&gt;&lt;/ul&gt; | | &lt;del&gt;&#x60;login&#x60;&lt;/del&gt; | User login filter | &#x60;cn&#x60; | User login contains value. | &#x60;search String&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;firstName:asc|lastLoginSuccessAt:desc&#x60;   Sort by &#x60;firstName&#x60; ascending **AND** by &#x60;lastLoginSuccessAt&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;userName&#x60; | User name | | &#x60;email&#x60; | User email | | &#x60;firstName&#x60; | User first name | | &#x60;lastName&#x60; | User last name | | &#x60;isLocked&#x60; | User lock status | | &#x60;lastLoginSuccessAt&#x60; | Last successful login date | | &#x60;expireAt&#x60; | Expiration date | | &#x60;createdAt&#x60; | Creation date |  &lt;/details&gt;  ### Deprecated sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &lt;del&gt;&#x60;gender&#x60;&lt;/del&gt; | Gender | | &lt;del&gt;&#x60;lockStatus&#x60;&lt;/del&gt; | User lock status | | &lt;del&gt;&#x60;login&#x60;&lt;/del&gt; | User login |  &lt;/details&gt;

    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param offset: Range offset
    :type offset: int
    :param limit: Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;).
    :type limit: int
    :param filter: Filter string
    :type filter: str
    :param sort: Sort string
    :type sort: str
    :param include_attributes: Include custom user attributes.
    :type include_attributes: bool
    :param include_roles: Include roles
    :type include_roles: bool
    :param include_manageable_rooms: Include hasManageableRooms (deprecated)
    :type include_manageable_rooms: bool
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_users_rooms(request: web.Request, user_id, x_sds_date_format=None, offset=None, limit=None, filter=None, x_sds_auth_token=None) -> web.Response:
    """Request rooms granted to the user or / and rooms that can be granted

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.10.0&lt;/h3&gt;  ### Description:   Retrieves a list of rooms granted to the user and / or that can be granted.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read users&lt;/span&gt; required.  ### Postcondition: List of rooms is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isGranted:eq:true|isLastAdmin:eq:true|name:cn:searchString&#x60;   Get all rooms that the user is granted **AND** is last admin **AND** whose name is like &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Room name filter | &#x60;cn&#x60; | Room name contains value. | &#x60;search String&#x60; | | &#x60;isGranted&#x60; | Filter the rooms which the user is (not) granted. | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;true&#x60; | | &#x60;isLastAdmin&#x60; | Filter the rooms which the user is last room administrator.&lt;br&gt;Only in connection with &#x60;isGranted:eq:true&#x60; filter possible. | &#x60;eq&#x60; |  | &#x60;true&#x60; | | &#x60;effectivePerm&#x60; | Filter rooms with DIRECT or DIRECT **AND** EFFECTIVE permissions&lt;ul&gt;&lt;li&gt;&#x60;false&#x60;: DIRECT permissions&lt;/li&gt;&lt;li&gt;&#x60;true&#x60;: DIRECT **AND** EFFECTIVE permissions&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;: DIRECT **AND** EFFECTIVE **AND** OVER GROUP permissions&lt;/li&gt;&lt;/ul&gt;DIRECT means: e.g. room administrator grants &#x60;read&#x60; permissions to group of users **directly** on desired room.&lt;br&gt;EFFECTIVE means: e.g. group of users gets &#x60;read&#x60; permissions on desired room through **inheritance**.&lt;br&gt;OVER GROUP means: e.g. user gets &#x60;read&#x60; permissions on desired room through **group membership**. | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;false&#x60; |  &lt;/details&gt;

    :param user_id: User ID
    :type user_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
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


async def set_user_attributes(request: web.Request, user_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Set custom user attributes

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.28.0&lt;/h3&gt;  ### Description:   Set custom user attributes.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change users&lt;/span&gt; required.  ### Postcondition: Custom user attributes are set.  ### Further Information: Batch function.   All existing user attributes will be deleted.    * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**.

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UserAttributes.from_dict(body)
    return web.Response(status=200)


async def update_user(request: web.Request, user_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Update user&#39;s metadata

    ### Description:   Update user&#39;s metadata.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change users&lt;/span&gt; required.  ### Postcondition: User&#39;s metadata is updated.  ### Further Information: * If a user should **NOT** expire, leave &#x60;expireAt&#x60; empty. * All input fields are limited to **150** characters * **All** characters are allowed.  ### Authentication Method Options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Authentication Method | Option Key | Option Value | | :--- | :--- | :--- | | &#x60;basic&#x60; / &#x60;sql&#x60; | &#x60;username&#x60; | Unique user identifier | | &#x60;active_directory&#x60; | &#x60;ad_config_id&#x60; (optional) | Active Directory configuration ID | |  | &#x60;username&#x60; | Active Directory username according to authentication setting &#x60;userFilter&#x60; | | &#x60;radius&#x60; | &#x60;username&#x60; | RADIUS username | | &#x60;openid&#x60; | &#x60;openid_config_id&#x60; (optional) | OpenID Connect configuration ID | |  | &#x60;username&#x60; | OpenID Connect username according to authentication setting &#x60;mappingClaim&#x60; |  &lt;/details&gt;

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateUserRequest.from_dict(body)
    return web.Response(status=200)


async def update_user_attributes(request: web.Request, user_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Add or edit custom user attributes

    ### Description:   Add or edit custom user attributes. &lt;br/&gt;&lt;br/&gt;&lt;span style&#x3D;\&quot;font-weight: bold; color: red;\&quot;&gt; &amp;#128679; **Warning: Please note that the response with HTTP status code 200 (OK) is deprecated and will be replaced with HTTP status code 204 (No content)!**&lt;/span&gt;&lt;br/&gt;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change users&lt;/span&gt; required.  ### Postcondition: Custom user attributes gets added or edited.  ### Further Information: Batch function.   If an entry exists before, it will be overwritten.    * Allowed characters for keys are: &#x60;[a-zA-Z0-9_-]&#x60;   * Characters are **case-insensitive**.

    :param user_id: User ID
    :type user_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UserAttributes.from_dict(body)
    return web.Response(status=200)
