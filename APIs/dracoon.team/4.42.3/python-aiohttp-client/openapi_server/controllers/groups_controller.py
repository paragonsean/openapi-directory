from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_group_members_request import ChangeGroupMembersRequest
from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.group import Group
from openapi_server.models.group_list import GroupList
from openapi_server.models.group_user_list import GroupUserList
from openapi_server.models.last_admin_group_room_list import LastAdminGroupRoomList
from openapi_server.models.role_list import RoleList
from openapi_server.models.room_tree_data_list import RoomTreeDataList
from openapi_server.models.update_group_request import UpdateGroupRequest
from openapi_server import util


async def add_group_members(request: web.Request, group_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Add group members

    ### Description: Add members to a group.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change groups&lt;/span&gt; required.  ### Postcondition:  New members are added to the group.  ### Further Information: Batch function.   The newly provided members will be added to the existing ones.

    :param group_id: Group ID
    :type group_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = ChangeGroupMembersRequest.from_dict(body)
    return web.Response(status=200)


async def create_group(request: web.Request, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Create new user group

    ### Description: Create a new user group.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change groups&lt;/span&gt; required.  ### Postcondition:  A new user group is created.  ### Further Information: * If a group should **NOT** expire, leave &#x60;expireAt&#x60; empty. * Group names are limited to **150** characters * Forbidden characters in group name: [&#x60;&lt;&#x60;, &#x60;&gt;&#x60;] 

    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = CreateGroupRequest.from_dict(body)
    return web.Response(status=200)


async def remove_group(request: web.Request, group_id, x_sds_auth_token=None) -> web.Response:
    """Remove user group

    ### Description: Delete a user group.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; delete groups&lt;/span&gt; required.  ### Postcondition:  User group is deleted.  ### Further Information: None.

    :param group_id: Group ID
    :type group_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def remove_group_members(request: web.Request, group_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Remove group members

    ### Description:   Remove group members.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change groups&lt;/span&gt; required.  ### Postcondition:  Provided users are removed from the user group.  ### Further Information: Batch function.   The provided users are removed from the user group. Maximum number of users to remove in one request is 200.

    :param group_id: Group ID
    :type group_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = ChangeGroupMembersRequest.from_dict(body)
    return web.Response(status=200)


async def request_group(request: web.Request, group_id, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Request user group

    ### Description:   Retrieve detailed information about a user group.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read groups&lt;/span&gt; required.  ### Postcondition:  User group is returned.  ### Further Information: None.

    :param group_id: Group ID
    :type group_id: int
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_group_members(request: web.Request, group_id, offset=None, limit=None, filter=None, x_sds_auth_token=None) -> web.Response:
    """Request group member users or / and users who can become a member

    ### Description:   Retrieve a list of group member users or / and users who can become a member.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read groups&lt;/span&gt; required.  ### Postcondition:  List of users is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isMember:eq:false|user:cn:searchString&#x60;   Get all users that are **NOT** in this group **AND** whose (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;) is like &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;user&#x60; | User filter | &#x60;cn&#x60; | User contains value (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60; **OR** &#x60;username&#x60;). | &#x60;search String&#x60; | | &#x60;isMember&#x60; | Filter group members | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;true&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;displayName&#x60;&lt;/del&gt; | User display name filter (use &#x60;user&#x60; filter) | &#x60;cn&#x60; | User display name contains value (&#x60;firstName&#x60; **OR** &#x60;lastName&#x60; **OR** &#x60;email&#x60;). | &#x60;search String&#x60; |  &lt;/details&gt;

    :param group_id: Group ID
    :type group_id: int
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


async def request_group_roles(request: web.Request, group_id, x_sds_auth_token=None) -> web.Response:
    """Request list of roles assigned to the group

    ### Description:   Retrieve a list of all roles granted to a group.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read groups&lt;/span&gt; required.  ### Postcondition:  List of granted roles is returned.  ### Further Information: None.

    :param group_id: Group ID
    :type group_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_group_rooms(request: web.Request, group_id, x_sds_date_format=None, offset=None, limit=None, filter=None, x_sds_auth_token=None) -> web.Response:
    """Request rooms granted to the group or / and rooms that can be granted

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.10.0&lt;/h3&gt;  ### Description:   Retrieves a list of rooms granted to the group and / or that can be granted.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read groups&lt;/span&gt; required.  ### Postcondition:  List of rooms is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;isGranted:eq:false|name:cn:searchString&#x60;   Get all rooms where the group is **NOT** granted **AND** whose name is like &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Room name filter | &#x60;cn&#x60; | Room name contains value. | &#x60;search String&#x60; | | &#x60;isGranted&#x60; | Filter rooms which the group is (not) granted | &#x60;eq&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;true&#x60;&lt;/li&gt;&lt;li&gt;&#x60;false&#x60;&lt;/li&gt;&lt;li&gt;&#x60;any&#x60;&lt;/li&gt;&lt;/ul&gt;default: &#x60;true&#x60; | | &#x60;effectivePerm&#x60; | Filter rooms with DIRECT or DIRECT **AND** EFFECTIVE permissions&lt;ul&gt;&lt;li&gt;&#x60;false&#x60;: DIRECT permissions&lt;/li&gt;&lt;li&gt;&#x60;true&#x60;:  DIRECT **AND** EFFECTIVE permissions&lt;/li&gt;&lt;/ul&gt;DIRECT means: e.g. room administrator grants &#x60;read&#x60; permissions to group of users **directly** on desired room.&lt;br&gt;EFFECTIVE means: e.g. group of users gets &#x60;read&#x60; permissions on desired room through **inheritance**. | &#x60;eq&#x60; |  | &#x60;true or false&#x60;&lt;br&gt;default: &#x60;true&#x60; |  &lt;/details&gt;

    :param group_id: Group ID
    :type group_id: int
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


async def request_groups(request: web.Request, x_sds_date_format=None, offset=None, limit=None, filter=None, sort=None, x_sds_auth_token=None) -> web.Response:
    """Request list of user groups

    ### Description:   Returns a list of user groups.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read groups&lt;/span&gt; required.  ### Postcondition:  List of user groups is returned.  ### Further Information:  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE&#x60;    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:cn:searchString&#x60;   Filter by group name containing &#x60;searchString&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;name&#x60; | Group name filter | &#x60;cn&#x60; | Group name contains value. | &#x60;search String&#x60; | | &#x60;hasRole&#x60; | (**&#x60;NEW&#x60;**) Group role filter&lt;br&gt;For more information about roles check **&#x60;GET /roles&#x60;** API | &#x60;eq&#x60; | Group role equals value. | &lt;ul&gt;&lt;li&gt;&#x60;CONFIG_MANAGER&#x60; - Manages global configuration&lt;/li&gt;&lt;li&gt;&#x60;USER_MANAGER&#x60; - Manages users&lt;/li&gt;&lt;li&gt;&#x60;GROUP_MANAGER&#x60; - Manages user groups&lt;/li&gt;&lt;li&gt;&#x60;ROOM_MANAGER&#x60; - Manages top level rooms&lt;/li&gt;&lt;li&gt;&#x60;LOG_AUDITOR&#x60; - Reads audit logs&lt;/li&gt;&lt;li&gt;&#x60;NONMEMBER_VIEWER&#x60; - Views users and groups when having room _\&quot;manage\&quot;_ permission&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;name:asc|expireAt:desc&#x60;   Sort by &#x60;name&#x60; ascending **AND** by &#x60;expireAt&#x60; descending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;name&#x60; | Group name | | &#x60;createdAt&#x60; | Creation date | | &#x60;expireAt&#x60; | Expiration date | | &#x60;cntUsers&#x60; | Amount of users |  &lt;/details&gt;

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
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def request_last_admin_rooms_groups(request: web.Request, group_id, x_sds_auth_token=None) -> web.Response:
    """Request rooms where the group is defined as last admin group

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.10.0&lt;/h3&gt;  ### Description:   Retrieve a list of all rooms where the group is defined as last admin group.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change groups&lt;/span&gt; required.  ### Postcondition:  List of rooms is returned.   ### Further Information: An empty list is returned if no rooms were found where the group is defined as last admin group.

    :param group_id: Group ID
    :type group_id: int
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    return web.Response(status=200)


async def update_group(request: web.Request, group_id, body, x_sds_date_format=None, x_sds_auth_token=None) -> web.Response:
    """Update user group&#39;s metadata

    ### Description:   Update user group&#39;s metadata .  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change groups&lt;/span&gt; required.  ### Postcondition:  User group&#39;s metadata is changed.  ### Further Information: * If a group should **NOT** expire, leave &#x60;expireAt&#x60; empty. * Group names are limited to **150** characters * **All** characters are allowed.

    :param group_id: Group ID
    :type group_id: int
    :param body: 
    :type body: dict | bytes
    :param x_sds_date_format: Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/))
    :type x_sds_date_format: str
    :param x_sds_auth_token: Authentication token
    :type x_sds_auth_token: str

    """
    body = UpdateGroupRequest.from_dict(body)
    return web.Response(status=200)
