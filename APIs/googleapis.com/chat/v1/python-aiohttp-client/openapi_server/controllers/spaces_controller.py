from typing import List, Dict
from aiohttp import web

from openapi_server.models.attachment import Attachment
from openapi_server.models.complete_import_space_response import CompleteImportSpaceResponse
from openapi_server.models.list_memberships_response import ListMembershipsResponse
from openapi_server.models.list_messages_response import ListMessagesResponse
from openapi_server.models.list_reactions_response import ListReactionsResponse
from openapi_server.models.list_spaces_response import ListSpacesResponse
from openapi_server.models.membership import Membership
from openapi_server.models.message import Message
from openapi_server.models.reaction import Reaction
from openapi_server.models.set_up_space_request import SetUpSpaceRequest
from openapi_server.models.space import Space
from openapi_server import util


async def chat_spaces_complete_import(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chat_spaces_complete_import

    Completes the [import process](https://developers.google.com/chat/api/guides/import-data) for the specified space and makes it visible to users. Requires app authentication and domain-wide delegation. For more information, see [Authorize Google Chat apps to import data](https://developers.google.com/chat/api/guides/authorize-import).

    :param name: Required. Resource name of the import mode space. Format: &#x60;spaces/{space}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def chat_spaces_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, request_id=None, body=None) -> web.Response:
    """chat_spaces_create

    Creates a named space. Spaces grouped by topics aren&#39;t supported. For an example, see [Create a space](https://developers.google.com/chat/api/guides/v1/spaces/create). If you receive the error message &#x60;ALREADY_EXISTS&#x60; when creating a space, try a different &#x60;displayName&#x60;. An existing space within the Google Workspace organization might already use this display name. Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param request_id: Optional. A unique identifier for this request. A random UUID is recommended. Specifying an existing request ID returns the space created with that ID instead of creating a new space. Specifying an existing request ID from the same Chat app with a different authenticated user returns an error.
    :type request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Space.from_dict(body)
    return web.Response(status=200)


async def chat_spaces_find_direct_message(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, name=None) -> web.Response:
    """chat_spaces_find_direct_message

    Returns the existing direct message with the specified user. If no direct message space is found, returns a &#x60;404 NOT_FOUND&#x60; error. For an example, see [Find a direct message](/chat/api/guides/v1/spaces/find-direct-message). With [user authentication](https://developers.google.com/chat/api/guides/auth/users), returns the direct message space between the specified user and the authenticated user. With [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts), returns the direct message space between the specified user and the calling Chat app. Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users) or [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts).

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param name: Required. Resource name of the user to find direct message with. Format: &#x60;users/{user}&#x60;, where &#x60;{user}&#x60; is either the &#x60;id&#x60; for the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the &#x60;id&#x60; for the [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) in the Directory API. For example, if the People API profile ID is &#x60;123456789&#x60;, you can find a direct message with that person by using &#x60;users/123456789&#x60; as the &#x60;name&#x60;. When [authenticated as a user](https://developers.google.com/chat/api/guides/auth/users), you can use the email as an alias for &#x60;{user}&#x60;. For example, &#x60;users/example@gmail.com&#x60; where &#x60;example@gmail.com&#x60; is the email of the Google Chat user.
    :type name: str

    """
    return web.Response(status=200)


async def chat_spaces_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """chat_spaces_list

    Lists spaces the caller is a member of. Group chats and DMs aren&#39;t listed until the first message is sent. For an example, see [List spaces](https://developers.google.com/chat/api/guides/v1/spaces/list). Requires [authentication](https://developers.google.com/chat/api/guides/auth). Supports [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) and [user authentication](https://developers.google.com/chat/api/guides/auth/users). Lists spaces visible to the caller or authenticated user. Group chats and DMs aren&#39;t listed until the first message is sent.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. A query filter. You can filter spaces by the space type ([&#x60;space_type&#x60;](https://developers.google.com/chat/api/reference/rest/v1/spaces#spacetype)). To filter by space type, you must specify valid enum value, such as &#x60;SPACE&#x60; or &#x60;GROUP_CHAT&#x60; (the &#x60;space_type&#x60; can&#39;t be &#x60;SPACE_TYPE_UNSPECIFIED&#x60;). To query for multiple space types, use the &#x60;OR&#x60; operator. For example, the following queries are valid: &#x60;&#x60;&#x60; space_type &#x3D; \&quot;SPACE\&quot; spaceType &#x3D; \&quot;GROUP_CHAT\&quot; OR spaceType &#x3D; \&quot;DIRECT_MESSAGE\&quot; &#x60;&#x60;&#x60; Invalid queries are rejected by the server with an &#x60;INVALID_ARGUMENT&#x60; error.
    :type filter: str
    :param page_size: Optional. The maximum number of spaces to return. The service might return fewer than this value. If unspecified, at most 100 spaces are returned. The maximum value is 1,000. If you use a value more than 1,000, it&#39;s automatically changed to 1,000. Negative values return an &#x60;INVALID_ARGUMENT&#x60; error.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous list spaces call. Provide this parameter to retrieve the subsequent page. When paginating, the filter value should match the call that provided the page token. Passing a different value may lead to unexpected results.
    :type page_token: str

    """
    return web.Response(status=200)


async def chat_spaces_members_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chat_spaces_members_create

    Creates a human membership or app membership for the calling app. Creating memberships for other apps isn&#39;t supported. For an example, see [ Create a membership](https://developers.google.com/chat/api/guides/v1/members/create). When creating a membership, if the specified member has their auto-accept policy turned off, then they&#39;re invited, and must accept the space invitation before joining. Otherwise, creating a membership adds the member directly to the specified space. Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users). To specify the member to add, set the &#x60;membership.member.name&#x60; in the &#x60;CreateMembershipRequest&#x60;: - To add the calling app to a space or a direct message between two human users, use &#x60;users/app&#x60;. Unable to add other apps to the space. - To add a human user, use &#x60;users/{user}&#x60;, where &#x60;{user}&#x60; can be the email address for the user. For users in the same Workspace organization &#x60;{user}&#x60; can also be the &#x60;id&#x60; for the person from the People API, or the &#x60;id&#x60; for the user in the Directory API. For example, if the People API Person profile ID for &#x60;user@example.com&#x60; is &#x60;123456789&#x60;, you can add the user to the space by setting the &#x60;membership.member.name&#x60; to &#x60;users/user@example.com&#x60; or &#x60;users/123456789&#x60;.

    :param parent: Required. The resource name of the space for which to create the membership. Format: spaces/{space}
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Membership.from_dict(body)
    return web.Response(status=200)


async def chat_spaces_members_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None, show_groups=None, show_invited=None) -> web.Response:
    """chat_spaces_members_list

    Lists memberships in a space. For an example, see [List memberships](https://developers.google.com/chat/api/guides/v1/members/list). Listing memberships with [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/chat/api/guides/auth/users) lists memberships in spaces that the authenticated user has access to. Requires [authentication](https://developers.google.com/chat/api/guides/auth). Supports [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) and [user authentication](https://developers.google.com/chat/api/guides/auth/users).

    :param parent: Required. The resource name of the space for which to fetch a membership list. Format: spaces/{space}
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. A query filter. You can filter memberships by a member&#39;s role ([&#x60;role&#x60;](https://developers.google.com/chat/api/reference/rest/v1/spaces.members#membershiprole)) and type ([&#x60;member.type&#x60;](https://developers.google.com/chat/api/reference/rest/v1/User#type)). To filter by role, set &#x60;role&#x60; to &#x60;ROLE_MEMBER&#x60; or &#x60;ROLE_MANAGER&#x60;. To filter by type, set &#x60;member.type&#x60; to &#x60;HUMAN&#x60; or &#x60;BOT&#x60;. To filter by both role and type, use the &#x60;AND&#x60; operator. To filter by either role or type, use the &#x60;OR&#x60; operator. For example, the following queries are valid: &#x60;&#x60;&#x60; role &#x3D; \&quot;ROLE_MANAGER\&quot; OR role &#x3D; \&quot;ROLE_MEMBER\&quot; member.type &#x3D; \&quot;HUMAN\&quot; AND role &#x3D; \&quot;ROLE_MANAGER\&quot; &#x60;&#x60;&#x60; The following queries are invalid: &#x60;&#x60;&#x60; member.type &#x3D; \&quot;HUMAN\&quot; AND member.type &#x3D; \&quot;BOT\&quot; role &#x3D; \&quot;ROLE_MANAGER\&quot; AND role &#x3D; \&quot;ROLE_MEMBER\&quot; &#x60;&#x60;&#x60; Invalid queries are rejected by the server with an &#x60;INVALID_ARGUMENT&#x60; error.
    :type filter: str
    :param page_size: Optional. The maximum number of memberships to return. The service might return fewer than this value. If unspecified, at most 100 memberships are returned. The maximum value is 1,000. If you use a value more than 1,000, it&#39;s automatically changed to 1,000. Negative values return an &#x60;INVALID_ARGUMENT&#x60; error.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous call to list memberships. Provide this parameter to retrieve the subsequent page. When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.
    :type page_token: str
    :param show_groups: Optional. When &#x60;true&#x60;, also returns memberships associated with a Google Group, in addition to other types of memberships. If a filter is set, Google Group memberships that don&#39;t match the filter criteria aren&#39;t returned.
    :type show_groups: bool
    :param show_invited: Optional. When &#x60;true&#x60;, also returns memberships associated with invited members, in addition to other types of memberships. If a filter is set, invited memberships that don&#39;t match the filter criteria aren&#39;t returned. Currently requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).
    :type show_invited: bool

    """
    return web.Response(status=200)


async def chat_spaces_messages_attachments_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """chat_spaces_messages_attachments_get

    Gets the metadata of a message attachment. The attachment data is fetched using the [media API](https://developers.google.com/chat/api/reference/rest/v1/media/download). For an example, see [Get a message attachment](https://developers.google.com/chat/api/guides/v1/media-and-attachments/get). Requires [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts).

    :param name: Required. Resource name of the attachment, in the form &#x60;spaces/*/messages/*/attachments/*&#x60;.
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def chat_spaces_messages_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, message_id=None, message_reply_option=None, request_id=None, thread_key=None, body=None) -> web.Response:
    """chat_spaces_messages_create

    Creates a message in a Google Chat space. For an example, see [Create a message](https://developers.google.com/chat/api/guides/v1/messages/create). Calling this method requires [authentication](https://developers.google.com/chat/api/guides/auth) and supports the following authentication types: - For text messages, user authentication or app authentication are supported. - For card messages, only app authentication is supported. (Only Chat apps can create card messages.)

    :param parent: Required. The resource name of the space in which to create a message. Format: &#x60;spaces/{space}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param message_id: Optional. A custom ID for a message. Lets Chat apps get, update, or delete a message without needing to store the system-assigned ID in the message&#39;s resource name (represented in the message &#x60;name&#x60; field). The value for this field must meet the following requirements: * Begins with &#x60;client-&#x60;. For example, &#x60;client-custom-name&#x60; is a valid custom ID, but &#x60;custom-name&#x60; is not. * Contains up to 63 characters and only lowercase letters, numbers, and hyphens. * Is unique within a space. A Chat app can&#39;t use the same custom ID for different messages. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message).
    :type message_id: str
    :param message_reply_option: Optional. Specifies whether a message starts a thread or replies to one. Only supported in named spaces.
    :type message_reply_option: str
    :param request_id: Optional. A unique request ID for this message. Specifying an existing request ID returns the message created with that ID instead of creating a new message.
    :type request_id: str
    :param thread_key: Optional. Deprecated: Use thread.thread_key instead. ID for the thread. Supports up to 4000 characters. To start or add to a thread, create a message and specify a &#x60;threadKey&#x60; or the thread.name. For example usage, see [Start or reply to a message thread](https://developers.google.com/chat/api/guides/v1/messages/create#create-message-thread).
    :type thread_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = Message.from_dict(body)
    return web.Response(status=200)


async def chat_spaces_messages_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, order_by=None, page_size=None, page_token=None, show_deleted=None) -> web.Response:
    """chat_spaces_messages_list

    Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. For an example, see [List messages](/chat/api/guides/v1/messages/list). Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

    :param parent: Required. The resource name of the space to list messages from. Format: &#x60;spaces/{space}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: A query filter. You can filter messages by date (&#x60;create_time&#x60;) and thread (&#x60;thread.name&#x60;). To filter messages by the date they were created, specify the &#x60;create_time&#x60; with a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and double quotation marks. For example, &#x60;\&quot;2023-04-21T11:30:00-04:00\&quot;&#x60;. You can use the greater than operator &#x60;&gt;&#x60; to list messages that were created after a timestamp, or the less than operator &#x60;&lt;&#x60; to list messages that were created before a timestamp. To filter messages within a time interval, use the &#x60;AND&#x60; operator between two timestamps. To filter by thread, specify the &#x60;thread.name&#x60;, formatted as &#x60;spaces/{space}/threads/{thread}&#x60;. You can only specify one &#x60;thread.name&#x60; per query. To filter by both thread and date, use the &#x60;AND&#x60; operator in your query. For example, the following queries are valid: &#x60;&#x60;&#x60; create_time &gt; \&quot;2012-04-21T11:30:00-04:00\&quot; create_time &gt; \&quot;2012-04-21T11:30:00-04:00\&quot; AND thread.name &#x3D; spaces/AAAAAAAAAAA/threads/123 create_time &gt; \&quot;2012-04-21T11:30:00+00:00\&quot; AND create_time &lt; \&quot;2013-01-01T00:00:00+00:00\&quot; AND thread.name &#x3D; spaces/AAAAAAAAAAA/threads/123 thread.name &#x3D; spaces/AAAAAAAAAAA/threads/123 &#x60;&#x60;&#x60; Invalid queries are rejected by the server with an &#x60;INVALID_ARGUMENT&#x60; error.
    :type filter: str
    :param order_by: Optional, if resuming from a previous query. How the list of messages is ordered. Specify a value to order by an ordering operation. Valid ordering operation values are as follows: - &#x60;ASC&#x60; for ascending. - &#x60;DESC&#x60; for descending. The default ordering is &#x60;create_time ASC&#x60;.
    :type order_by: str
    :param page_size: The maximum number of messages returned. The service might return fewer messages than this value. If unspecified, at most 25 are returned. The maximum value is 1,000. If you use a value more than 1,000, it&#39;s automatically changed to 1,000. Negative values return an &#x60;INVALID_ARGUMENT&#x60; error.
    :type page_size: int
    :param page_token: Optional, if resuming from a previous query. A page token received from a previous list messages call. Provide this parameter to retrieve the subsequent page. When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.
    :type page_token: str
    :param show_deleted: Whether to include deleted messages. Deleted messages include deleted time and metadata about their deletion, but message content is unavailable.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def chat_spaces_messages_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, allow_missing=None, update_mask=None, body=None) -> web.Response:
    """chat_spaces_messages_patch

    Updates a message. There&#39;s a difference between the &#x60;patch&#x60; and &#x60;update&#x60; methods. The &#x60;patch&#x60; method uses a &#x60;patch&#x60; request while the &#x60;update&#x60; method uses a &#x60;put&#x60; request. We recommend using the &#x60;patch&#x60; method. For an example, see [Update a message](https://developers.google.com/chat/api/guides/v1/messages/update). Requires [authentication](https://developers.google.com/chat/api/guides/auth). Supports [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) and [user authentication](https://developers.google.com/chat/api/guides/auth/users). When using app authentication, requests can only update messages created by the calling Chat app.

    :param name: Resource name of the message. Format: &#x60;spaces/{space}/messages/{message}&#x60; Where &#x60;{space}&#x60; is the ID of the space where the message is posted and &#x60;{message}&#x60; is a system-assigned ID for the message. For example, &#x60;spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB&#x60;. If you set a custom ID when you create a message, you can use this ID to specify the message in a request by replacing &#x60;{message}&#x60; with the value from the &#x60;clientAssignedMessageId&#x60; field. For example, &#x60;spaces/AAAAAAAAAAA/messages/client-custom-name&#x60;. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message).
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param allow_missing: Optional. If &#x60;true&#x60; and the message isn&#39;t found, a new message is created and &#x60;updateMask&#x60; is ignored. The specified message ID must be [client-assigned](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message) or the request fails.
    :type allow_missing: bool
    :param update_mask: Required. The field paths to update. Separate multiple values with commas or use &#x60;*&#x60; to update all field paths. Currently supported field paths: - &#x60;text&#x60; - &#x60;attachment&#x60; - &#x60;cards&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - &#x60;cards_v2&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - Developer Preview: &#x60;accessory_widgets&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).)
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Message.from_dict(body)
    return web.Response(status=200)


async def chat_spaces_messages_reactions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chat_spaces_messages_reactions_create

    Creates a reaction and adds it to a message. For an example, see [Create a reaction](https://developers.google.com/chat/api/guides/v1/reactions/create). Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users). Only unicode emoji are supported.

    :param parent: Required. The message where the reaction is created. Format: &#x60;spaces/{space}/messages/{message}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Reaction.from_dict(body)
    return web.Response(status=200)


async def chat_spaces_messages_reactions_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, force=None) -> web.Response:
    """chat_spaces_messages_reactions_delete

    Deletes a reaction to a message. For an example, see [Delete a reaction](https://developers.google.com/chat/api/guides/v1/reactions/delete). Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

    :param name: Required. Name of the reaction to delete. Format: &#x60;spaces/{space}/messages/{message}/reactions/{reaction}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param force: When &#x60;true&#x60;, deleting a message also deletes its threaded replies. When &#x60;false&#x60;, if a message has threaded replies, deletion fails. Only applies when [authenticating as a user](https://developers.google.com/chat/api/guides/auth/users). Has no effect when [authenticating as a Chat app] (https://developers.google.com/chat/api/guides/auth/service-accounts).
    :type force: bool

    """
    return web.Response(status=200)


async def chat_spaces_messages_reactions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """chat_spaces_messages_reactions_list

    Lists reactions to a message. For an example, see [List reactions](https://developers.google.com/chat/api/guides/v1/reactions/list). Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

    :param parent: Required. The message users reacted to. Format: &#x60;spaces/{space}/messages/{message}&#x60;
    :type parent: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: Optional. A query filter. You can filter reactions by [emoji](https://developers.google.com/chat/api/reference/rest/v1/Emoji) (either &#x60;emoji.unicode&#x60; or &#x60;emoji.custom_emoji.uid&#x60;) and [user](https://developers.google.com/chat/api/reference/rest/v1/User) (&#x60;user.name&#x60;). To filter reactions for multiple emojis or users, join similar fields with the &#x60;OR&#x60; operator, such as &#x60;emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.unicode &#x3D; \&quot;👍\&quot;&#x60; and &#x60;user.name &#x3D; \&quot;users/AAAAAA\&quot; OR user.name &#x3D; \&quot;users/BBBBBB\&quot;&#x60;. To filter reactions by emoji and user, use the &#x60;AND&#x60; operator, such as &#x60;emoji.unicode &#x3D; \&quot;🙂\&quot; AND user.name &#x3D; \&quot;users/AAAAAA\&quot;&#x60;. If your query uses both &#x60;AND&#x60; and &#x60;OR&#x60;, group them with parentheses. For example, the following queries are valid: &#x60;&#x60;&#x60; user.name &#x3D; \&quot;users/{user}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.unicode &#x3D; \&quot;👍\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; AND user.name &#x3D; \&quot;users/{user}\&quot; (emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot;) AND user.name &#x3D; \&quot;users/{user}\&quot; &#x60;&#x60;&#x60; The following queries are invalid: &#x60;&#x60;&#x60; emoji.unicode &#x3D; \&quot;🙂\&quot; AND emoji.unicode &#x3D; \&quot;👍\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; AND emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR user.name &#x3D; \&quot;users/{user}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; OR user.name &#x3D; \&quot;users/{user}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; AND user.name &#x3D; \&quot;users/{user}\&quot; &#x60;&#x60;&#x60; Invalid queries are rejected by the server with an &#x60;INVALID_ARGUMENT&#x60; error.
    :type filter: str
    :param page_size: Optional. The maximum number of reactions returned. The service can return fewer reactions than this value. If unspecified, the default value is 25. The maximum value is 200; values above 200 are changed to 200.
    :type page_size: int
    :param page_token: Optional. (If resuming from a previous query.) A page token received from a previous list reactions call. Provide this to retrieve the subsequent page. When paginating, the filter value should match the call that provided the page token. Passing a different value might lead to unexpected results.
    :type page_token: str

    """
    return web.Response(status=200)


async def chat_spaces_messages_update(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, allow_missing=None, update_mask=None, body=None) -> web.Response:
    """chat_spaces_messages_update

    Updates a message. There&#39;s a difference between the &#x60;patch&#x60; and &#x60;update&#x60; methods. The &#x60;patch&#x60; method uses a &#x60;patch&#x60; request while the &#x60;update&#x60; method uses a &#x60;put&#x60; request. We recommend using the &#x60;patch&#x60; method. For an example, see [Update a message](https://developers.google.com/chat/api/guides/v1/messages/update). Requires [authentication](https://developers.google.com/chat/api/guides/auth). Supports [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) and [user authentication](https://developers.google.com/chat/api/guides/auth/users). When using app authentication, requests can only update messages created by the calling Chat app.

    :param name: Resource name of the message. Format: &#x60;spaces/{space}/messages/{message}&#x60; Where &#x60;{space}&#x60; is the ID of the space where the message is posted and &#x60;{message}&#x60; is a system-assigned ID for the message. For example, &#x60;spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB&#x60;. If you set a custom ID when you create a message, you can use this ID to specify the message in a request by replacing &#x60;{message}&#x60; with the value from the &#x60;clientAssignedMessageId&#x60; field. For example, &#x60;spaces/AAAAAAAAAAA/messages/client-custom-name&#x60;. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message).
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param allow_missing: Optional. If &#x60;true&#x60; and the message isn&#39;t found, a new message is created and &#x60;updateMask&#x60; is ignored. The specified message ID must be [client-assigned](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message) or the request fails.
    :type allow_missing: bool
    :param update_mask: Required. The field paths to update. Separate multiple values with commas or use &#x60;*&#x60; to update all field paths. Currently supported field paths: - &#x60;text&#x60; - &#x60;attachment&#x60; - &#x60;cards&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - &#x60;cards_v2&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - Developer Preview: &#x60;accessory_widgets&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).)
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Message.from_dict(body)
    return web.Response(status=200)


async def chat_spaces_setup(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """chat_spaces_setup

    Creates a space and adds specified users to it. The calling user is automatically added to the space, and shouldn&#39;t be specified as a membership in the request. For an example, see [Set up a space](https://developers.google.com/chat/api/guides/v1/spaces/set-up). To specify the human members to add, add memberships with the appropriate &#x60;member.name&#x60; in the &#x60;SetUpSpaceRequest&#x60;. To add a human user, use &#x60;users/{user}&#x60;, where &#x60;{user}&#x60; can be the email address for the user. For users in the same Workspace organization &#x60;{user}&#x60; can also be the &#x60;id&#x60; for the person from the People API, or the &#x60;id&#x60; for the user in the Directory API. For example, if the People API Person profile ID for &#x60;user@example.com&#x60; is &#x60;123456789&#x60;, you can add the user to the space by setting the &#x60;membership.member.name&#x60; to &#x60;users/user@example.com&#x60; or &#x60;users/123456789&#x60;. For a space or group chat, if the caller blocks or is blocked by some members, then those members aren&#39;t added to the created space. To create a direct message (DM) between the calling user and another human user, specify exactly one membership to represent the human user. If one user blocks the other, the request fails and the DM isn&#39;t created. To create a DM between the calling user and the calling app, set &#x60;Space.singleUserBotDm&#x60; to &#x60;true&#x60; and don&#39;t specify any memberships. You can only use this method to set up a DM with the calling app. To add the calling app as a member of a space or an existing DM between two human users, see [create a membership](https://developers.google.com/chat/api/guides/v1/members/create). If a DM already exists between two users, even when one user blocks the other at the time a request is made, then the existing DM is returned. Spaces with threaded replies aren&#39;t supported. If you receive the error message &#x60;ALREADY_EXISTS&#x60; when setting up a space, try a different &#x60;displayName&#x60;. An existing space within the Google Workspace organization might already use this display name. Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetUpSpaceRequest.from_dict(body)
    return web.Response(status=200)
