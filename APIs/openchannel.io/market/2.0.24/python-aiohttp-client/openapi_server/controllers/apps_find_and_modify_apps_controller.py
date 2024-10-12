from typing import List, Dict
from aiohttp import web

from openapi_server.models.app import App
from openapi_server.models.app_pages import AppPages
from openapi_server.models.app_version import AppVersion
from openapi_server.models.search_pages import SearchPages
from openapi_server.models.version_pages import VersionPages
from openapi_server import util


async def apps_app_id_delete(request: web.Request, app_id, developer_id) -> web.Response:
    """Removes app and all versions

    - This method is called on behalf of a developer. 

    :param app_id: The id of the App to be removed
    :type app_id: str
    :param developer_id: The unique id of the developer that is removing this app
    :type developer_id: str

    """
    return web.Response(status=200)


async def apps_app_id_get(request: web.Request, app_id, user_id=None, track_views=None) -> web.Response:
    """Returns a single APPROVED or SUSPENDED app

    - A &#39;view&#39; event is recorded when trackViews is set to true 

    :param app_id: The id of the App to be located
    :type app_id: str
    :param user_id: The unique id of the user that is requesting this resource
    :type user_id: str
    :param track_views: Whether this call should be tracked as a &#39;view&#39; for this app. Default is false.
    :type track_views: bool

    """
    return web.Response(status=200)


async def apps_app_id_live_post(request: web.Request, app_id, developer_id, version) -> web.Response:
    """Change the live app to another, previously approved version

    - This method is called on behalf of a developer. 

    :param app_id: The id of the App to be changed
    :type app_id: str
    :param developer_id: The unique id of the developer that is changing this AppVersion
    :type developer_id: str
    :param version: The new version of the live App
    :type version: str

    """
    return web.Response(status=200)


async def apps_app_id_publish_post(request: web.Request, app_id, developer_id, version, auto_approve=None) -> web.Response:
    """Publishes the current working version of the app to the marketplace

    - This method is called on behalf of a developer.  - Only effects the current working version of the app. 

    :param app_id: The id of the app to be published
    :type app_id: str
    :param developer_id: The unique id of the developer that is modifying this app
    :type developer_id: str
    :param version: The version of the app to be published
    :type version: int
    :param auto_approve: If true, this AppVersion is automatically approved and becomes immediately available to end users
    :type auto_approve: bool

    """
    return web.Response(status=200)


async def apps_app_id_versions_version_delete(request: web.Request, app_id, version, developer_id) -> web.Response:
    """Removes AppVersion

    - This method is called on behalf of a developer. 

    :param app_id: The id of the App to be removed
    :type app_id: str
    :param version: The version of the App to be removed
    :type version: str
    :param developer_id: The unique id of the developer that is removing this app
    :type developer_id: str

    """
    return web.Response(status=200)


async def apps_app_id_versions_version_get(request: web.Request, app_id, version, developer_id=None) -> web.Response:
    """Returns a single AppVersion

    - Only returns AppVersions owned by this developer 

    :param app_id: The id of the App to be located
    :type app_id: str
    :param version: The version number of the app
    :type version: int
    :param developer_id: The unique id of the developer that is requesting this resource
    :type developer_id: str

    """
    return web.Response(status=200)


async def apps_app_id_versions_version_patch(request: web.Request, app_id, version, developer_id, name=None, type=None, model=None, custom_data=None, attributes=None, restrict=None, allow=None, access=None, approval_required=None) -> web.Response:
    """Updates the app fields or creates a new version

    - This method is called on behalf of a developer. - Price and is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly updated app - This endpoint updates only the fields provided in the request (relative update). In contrast, the POST version of this method replaces the entire object to match the request (absolute update).  

    :param app_id: The id of the App to be updated
    :type app_id: str
    :param version: The version of the App to be updated
    :type version: str
    :param developer_id: The unique id of the developer that is updating this app
    :type developer_id: str
    :param name: The name of the app
    :type name: str
    :param type: The type for this app
    :type type: str
    :param model: A JSON object representing the pricing model type for this app
    :type model: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str
    :param attributes: A custom set of app attributes defined by the administrator and attached to this app
    :type attributes: str
    :param restrict: JSON object to restrict users from purchasing or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or purchasing this app
    :type restrict: str
    :param allow: JSON object to allow users to purchase or view this app. Example: {&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} allows only users from canada and mexico to purchase this app
    :type allow: str
    :param access: JSON array of data access requirements
    :type access: str
    :param approval_required: False if updates should skip the approval process and be available immediately. Default is True
    :type approval_required: str

    """
    return web.Response(status=200)


async def apps_app_id_versions_version_post(request: web.Request, app_id, version, developer_id, name=None, type=None, model=None, custom_data=None, attributes=None, restrict=None, allow=None, access=None, approval_required=None) -> web.Response:
    """Updates the app or creates a new version

    - This method is called on behalf of a developer. - Price and is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly updated app - This endpoint replaces the entire object to match the request (absolute update). In contrast, the PATCH version of this endpoint updates only the fields provided in the request (relative update). 

    :param app_id: The id of the App to be updated
    :type app_id: str
    :param version: The version of the App to be updated
    :type version: str
    :param developer_id: The unique id of the developer that is updating this app
    :type developer_id: str
    :param name: The name of the app
    :type name: str
    :param type: The type for this app
    :type type: str
    :param model: A JSON object representing the pricing model type for this app
    :type model: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str
    :param attributes: A custom set of app attributes defined by the administrator and attached to this app
    :type attributes: str
    :param restrict: JSON object to restrict users from purchasing or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or purchasing this app
    :type restrict: str
    :param allow: JSON object to allow users to purchase or view this app. Example: {&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} allows only users from canada and mexico to purchase this app
    :type allow: str
    :param access: JSON array of data access requirements
    :type access: str
    :param approval_required: False if updates should skip the approval process and be available immediately. Default is True
    :type approval_required: str

    """
    return web.Response(status=200)


async def apps_app_id_versions_version_status_post(request: web.Request, app_id, version, developer_id=None, status=None, modified_by=None, reason=None) -> web.Response:
    """Allows a developer or administrator to change the status of apps

    Only certain status changes are allowed. For instance, a developer is only able to suspend and unsuspend their app (which must already be approved). See here for a state change diagram of allowed status changes for administrators: https://support.openchannel.io/documentation/api/#415-apps-status-change 

    :param app_id: The id of the App to be updated
    :type app_id: str
    :param version: The version of the App to be updated
    :type version: int
    :param developer_id: The unique id of the developer that is modifying this app
    :type developer_id: str
    :param status: The new status for this app. Can be either &#39;inReview&#39;, &#39;approved&#39;, &#39;suspended&#39; or &#39;rejected&#39;
    :type status: str
    :param modified_by: The role initiating this status change. Can be either &#39;developer&#39; or &#39;administrator&#39; (default)
    :type modified_by: str
    :param reason: The reason for this status change
    :type reason: str

    """
    return web.Response(status=200)


async def apps_by_safe_name_safe_name_get(request: web.Request, safe_name, user_id=None, track_views=None) -> web.Response:
    """Returns a single APPROVED or SUSPENDED app

    - A &#39;view&#39; event is recorded when trackViews is set to true 

    :param safe_name: The safeName of the App to be located
    :type safe_name: str
    :param user_id: The unique id of the user that is requesting this resource
    :type user_id: str
    :param track_views: Whether this call should be tracked as a &#39;view&#39; for this app. Default is false.
    :type track_views: bool

    """
    return web.Response(status=200)


async def apps_get(request: web.Request, query=None, sort=None, page_number=None, limit=None, user_id=None, is_owner=None) -> web.Response:
    """Returns a paginated list of APPROVED or SUSPENDED apps

    - Results are paginated and the default is value is 1000 if no limit is provided - If no query is specified, returns all APPROVED or SUSPENDED apps within the marketplace 

    :param query: A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the apps that have the name &#39;MyApp&#39;
    :type query: str
    :param sort: A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int
    :param user_id: The unique id of the user requesting this resource
    :type user_id: str
    :param is_owner: Whether this result should only contain apps that are owned by this user
    :type is_owner: bool

    """
    return web.Response(status=200)


async def apps_post(request: web.Request, developer_id, name, type=None, model=None, custom_data=None, attributes=None, restrict=None, allow=None, access=None) -> web.Response:
    """Adds a new app for this developer

    - This method is called on behalf of a developer. - Price is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly created app 

    :param developer_id: The unique id of the developer that is adding this app
    :type developer_id: str
    :param name: The name of the app
    :type name: str
    :param type: The type for this app
    :type type: str
    :param model: A JSON object representing the pricing model type for this app
    :type model: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str
    :param attributes: A custom set of app attributes defined by the administrator and attached to this app
    :type attributes: str
    :param restrict: JSON object to restrict users from owning or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;own&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or owning this app
    :type restrict: str
    :param allow: JSON object to restrict users from owning or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;own&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or owning this app
    :type allow: str
    :param access: JSON array of data access requirements
    :type access: str

    """
    return web.Response(status=200)


async def apps_text_search_get(request: web.Request, text, fields, query=None, page_number=None, limit=None, user_id=None, is_owned=None) -> web.Response:
    """Searches through the text of fields to find APPROVED or SUSPENDED apps

    - Results are returned for the market provided within the basic authentication credentials 

    :param text: The text to search for.
    :type text: str
    :param fields: A JSON array containing all the fields to be searched through. Example: [&#39;name&#39;, &#39;customData.description&#39;]
    :type fields: str
    :param query: A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the documents that have the name &#39;MyApp&#39;
    :type query: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int
    :param user_id: The unique id of the user requesting this resource
    :type user_id: str
    :param is_owned: Whether this result should only contain apps that are owned by this user
    :type is_owned: bool

    """
    return web.Response(status=200)


async def apps_versions_get(request: web.Request, query=None, sort=None, page_number=None, limit=None, developer_id=None) -> web.Response:
    """Returns a paginated list of AppVersions

    - Results are paginated when limit is set, otherwise all results are returned - If no query is specified, returns all AppVersions within the marketplace - Only returns AppVersions owned by this developer 

    :param query: A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the apps that have the name &#39;MyApp&#39;
    :type query: str
    :param sort: A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int
    :param developer_id: The unique id of the developer requesting this resource
    :type developer_id: str

    """
    return web.Response(status=200)
