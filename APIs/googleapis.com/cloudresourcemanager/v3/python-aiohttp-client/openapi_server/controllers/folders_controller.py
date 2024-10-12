from typing import List, Dict
from aiohttp import web

from openapi_server.models.folder import Folder
from openapi_server.models.list_folders_response import ListFoldersResponse
from openapi_server.models.operation import Operation
from openapi_server.models.search_folders_response import SearchFoldersResponse
from openapi_server import util


async def cloudresourcemanager_folders_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudresourcemanager_folders_create

    Creates a folder in the resource hierarchy. Returns an &#x60;Operation&#x60; which can be used to track the progress of the folder creation workflow. Upon success, the &#x60;Operation.response&#x60; field will be populated with the created Folder. In order to succeed, the addition of this new folder must not violate the folder naming, height, or fanout constraints. + The folder&#39;s &#x60;display_name&#x60; must be distinct from all other folders that share its parent. + The addition of the folder must not cause the active folder hierarchy to exceed a height of 10. Note, the full active + deleted folder hierarchy is allowed to reach a height of 20; this provides additional headroom when moving folders that contain deleted folders. + The addition of the folder must not cause the total number of folders under its parent to exceed 300. If the operation fails due to a folder constraint violation, some errors may be returned by the &#x60;CreateFolder&#x60; request, with status code &#x60;FAILED_PRECONDITION&#x60; and an error description. Other folder constraint violations will be communicated in the &#x60;Operation&#x60;, with the specific &#x60;PreconditionFailure&#x60; returned in the details list in the &#x60;Operation.error&#x60; field. The caller must have &#x60;resourcemanager.folders.create&#x60; permission on the identified parent.

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
    body = Folder.from_dict(body)
    return web.Response(status=200)


async def cloudresourcemanager_folders_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, parent=None, show_deleted=None) -> web.Response:
    """cloudresourcemanager_folders_list

    Lists the folders that are direct descendants of supplied parent resource. &#x60;list()&#x60; provides a strongly consistent view of the folders underneath the specified parent resource. &#x60;list()&#x60; returns folders sorted based upon the (ascending) lexical ordering of their display_name. The caller must have &#x60;resourcemanager.folders.list&#x60; permission on the identified parent.

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
    :param page_size: Optional. The maximum number of folders to return in the response. The server can return fewer folders than requested. If unspecified, server picks an appropriate default.
    :type page_size: int
    :param page_token: Optional. A pagination token returned from a previous call to &#x60;ListFolders&#x60; that indicates where this listing should continue from.
    :type page_token: str
    :param parent: Required. The name of the parent resource whose folders are being listed. Only children of this parent resource are listed; descendants are not listed. If the parent is a folder, use the value &#x60;folders/{folder_id}&#x60;. If the parent is an organization, use the value &#x60;organizations/{org_id}&#x60;. Access to this method is controlled by checking the &#x60;resourcemanager.folders.list&#x60; permission on the &#x60;parent&#x60;.
    :type parent: str
    :param show_deleted: Optional. Controls whether folders in the DELETE_REQUESTED state should be returned. Defaults to false.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def cloudresourcemanager_folders_search(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudresourcemanager_folders_search

    Search for folders that match specific filter criteria. &#x60;search()&#x60; provides an eventually consistent view of the folders a user has access to which meet the specified filter criteria. This will only return folders on which the caller has the permission &#x60;resourcemanager.folders.get&#x60;.

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
    :param page_size: Optional. The maximum number of folders to return in the response. The server can return fewer folders than requested. If unspecified, server picks an appropriate default.
    :type page_size: int
    :param page_token: Optional. A pagination token returned from a previous call to &#x60;SearchFolders&#x60; that indicates from where search should continue.
    :type page_token: str
    :param query: Optional. Search criteria used to select the folders to return. If no search criteria is specified then all accessible folders will be returned. Query expressions can be used to restrict results based upon displayName, state and parent, where the operators &#x60;&#x3D;&#x60; (&#x60;:&#x60;) &#x60;NOT&#x60;, &#x60;AND&#x60; and &#x60;OR&#x60; can be used along with the suffix wildcard symbol &#x60;*&#x60;. The &#x60;displayName&#x60; field in a query expression should use escaped quotes for values that include whitespace to prevent unexpected behavior. &#x60;&#x60;&#x60; | Field | Description | |-------------------------|----------------------------------------| | displayName | Filters by displayName. | | parent | Filters by parent (for example: folders/123). | | state, lifecycleState | Filters by state. | &#x60;&#x60;&#x60; Some example queries are: * Query &#x60;displayName&#x3D;Test*&#x60; returns Folder resources whose display name starts with \&quot;Test\&quot;. * Query &#x60;state&#x3D;ACTIVE&#x60; returns Folder resources with &#x60;state&#x60; set to &#x60;ACTIVE&#x60;. * Query &#x60;parent&#x3D;folders/123&#x60; returns Folder resources that have &#x60;folders/123&#x60; as a parent resource. * Query &#x60;parent&#x3D;folders/123 AND state&#x3D;ACTIVE&#x60; returns active Folder resources that have &#x60;folders/123&#x60; as a parent resource. * Query &#x60;displayName&#x3D;\\\\\&quot;Test String\\\\\&quot;&#x60; returns Folder resources with display names that include both \&quot;Test\&quot; and \&quot;String\&quot;.
    :type query: str

    """
    return web.Response(status=200)
