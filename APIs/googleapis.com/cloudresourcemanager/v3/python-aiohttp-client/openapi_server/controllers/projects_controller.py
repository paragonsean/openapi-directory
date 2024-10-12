from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_projects_response import ListProjectsResponse
from openapi_server.models.move_project_request import MoveProjectRequest
from openapi_server.models.operation import Operation
from openapi_server.models.project import Project
from openapi_server.models.search_projects_response import SearchProjectsResponse
from openapi_server import util


async def cloudresourcemanager_projects_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudresourcemanager_projects_create

    Request that a new project be created. The result is an &#x60;Operation&#x60; which can be used to track the creation process. This process usually takes a few seconds, but can sometimes take much longer. The tracking &#x60;Operation&#x60; is automatically deleted after a few hours, so there is no need to call &#x60;DeleteOperation&#x60;.

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
    body = Project.from_dict(body)
    return web.Response(status=200)


async def cloudresourcemanager_projects_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, parent=None, show_deleted=None) -> web.Response:
    """cloudresourcemanager_projects_list

    Lists projects that are direct children of the specified folder or organization resource. &#x60;list()&#x60; provides a strongly consistent view of the projects underneath the specified parent resource. &#x60;list()&#x60; returns projects sorted based upon the (ascending) lexical ordering of their &#x60;display_name&#x60;. The caller must have &#x60;resourcemanager.projects.list&#x60; permission on the identified parent.

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
    :param page_size: Optional. The maximum number of projects to return in the response. The server can return fewer projects than requested. If unspecified, server picks an appropriate default.
    :type page_size: int
    :param page_token: Optional. A pagination token returned from a previous call to ListProjects that indicates from where listing should continue.
    :type page_token: str
    :param parent: Required. The name of the parent resource whose projects are being listed. Only children of this parent resource are listed; descendants are not listed. If the parent is a folder, use the value &#x60;folders/{folder_id}&#x60;. If the parent is an organization, use the value &#x60;organizations/{org_id}&#x60;.
    :type parent: str
    :param show_deleted: Optional. Indicate that projects in the &#x60;DELETE_REQUESTED&#x60; state should also be returned. Normally only &#x60;ACTIVE&#x60; projects are returned.
    :type show_deleted: bool

    """
    return web.Response(status=200)


async def cloudresourcemanager_projects_move(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudresourcemanager_projects_move

    Move a project to another place in your resource hierarchy, under a new resource parent. Returns an operation which can be used to track the process of the project move workflow. Upon success, the &#x60;Operation.response&#x60; field will be populated with the moved project. The caller must have &#x60;resourcemanager.projects.move&#x60; permission on the project, on the project&#39;s current and proposed new parent. If project has no current parent, or it currently does not have an associated organization resource, you will also need the &#x60;resourcemanager.projects.setIamPolicy&#x60; permission in the project. 

    :param name: Required. The name of the project to move.
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
    :type body: dict | bytes

    """
    body = MoveProjectRequest.from_dict(body)
    return web.Response(status=200)


async def cloudresourcemanager_projects_search(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, query=None) -> web.Response:
    """cloudresourcemanager_projects_search

    Search for projects that the caller has the &#x60;resourcemanager.projects.get&#x60; permission on, and also satisfy the specified query. This method returns projects in an unspecified order. This method is eventually consistent with project mutations; this means that a newly created project may not appear in the results or recent updates to an existing project may not be reflected in the results. To retrieve the latest state of a project, use the GetProject method.

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
    :param page_size: Optional. The maximum number of projects to return in the response. The server can return fewer projects than requested. If unspecified, server picks an appropriate default.
    :type page_size: int
    :param page_token: Optional. A pagination token returned from a previous call to ListProjects that indicates from where listing should continue.
    :type page_token: str
    :param query: Optional. A query string for searching for projects that the caller has &#x60;resourcemanager.projects.get&#x60; permission to. If multiple fields are included in the query, then it will return results that match any of the fields. Some eligible fields are: &#x60;&#x60;&#x60; | Field | Description | |-------------------------|----------------------------------------------| | displayName, name | Filters by displayName. | | parent | Project&#39;s parent (for example: folders/123, organizations/*). Prefer parent field over parent.type and parent.id.| | parent.type | Parent&#39;s type: &#x60;folder&#x60; or &#x60;organization&#x60;. | | parent.id | Parent&#39;s id number (for example: 123) | | id, projectId | Filters by projectId. | | state, lifecycleState | Filters by state. | | labels | Filters by label name or value. | | labels.\\ (where *key* is the name of a label) | Filters by label name.| &#x60;&#x60;&#x60; Search expressions are case insensitive. Some examples queries: &#x60;&#x60;&#x60; | Query | Description | |------------------|-----------------------------------------------------| | name:how* | The project&#39;s name starts with \&quot;how\&quot;. | | name:Howl | The project&#39;s name is &#x60;Howl&#x60; or &#x60;howl&#x60;. | | name:HOWL | Equivalent to above. | | NAME:howl | Equivalent to above. | | labels.color:* | The project has the label &#x60;color&#x60;. | | labels.color:red | The project&#39;s label &#x60;color&#x60; has the value &#x60;red&#x60;. | | labels.color:red labels.size:big | The project&#39;s label &#x60;color&#x60; has the value &#x60;red&#x60; or its label &#x60;size&#x60; has the value &#x60;big&#x60;. | &#x60;&#x60;&#x60; If no query is specified, the call will return projects for which the user has the &#x60;resourcemanager.projects.get&#x60; permission.
    :type query: str

    """
    return web.Response(status=200)


async def cloudresourcemanager_projects_undelete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudresourcemanager_projects_undelete

    Restores the project identified by the specified &#x60;name&#x60; (for example, &#x60;projects/415104041262&#x60;). You can only use this method for a project that has a lifecycle state of DELETE_REQUESTED. After deletion starts, the project cannot be restored. The caller must have &#x60;resourcemanager.projects.undelete&#x60; permission for this project.

    :param name: Required. The name of the project (for example, &#x60;projects/415104041262&#x60;). Required.
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
