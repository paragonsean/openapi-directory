from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_script_processes_response import ListScriptProcessesResponse
from openapi_server.models.list_user_processes_response import ListUserProcessesResponse
from openapi_server import util


async def script_processes_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, user_process_filter_deployment_id=None, user_process_filter_end_time=None, user_process_filter_function_name=None, user_process_filter_project_name=None, user_process_filter_script_id=None, user_process_filter_start_time=None, user_process_filter_statuses=None, user_process_filter_types=None, user_process_filter_user_access_levels=None) -> web.Response:
    """script_processes_list

    List information about processes made by or on behalf of a user, such as process type and current status.

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
    :param page_size: The maximum number of returned processes per page of results. Defaults to 50.
    :type page_size: int
    :param page_token: The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from a previous response.
    :type page_token: str
    :param user_process_filter_deployment_id: Optional field used to limit returned processes to those originating from projects with a specific deployment ID.
    :type user_process_filter_deployment_id: str
    :param user_process_filter_end_time: Optional field used to limit returned processes to those that completed on or before the given timestamp.
    :type user_process_filter_end_time: str
    :param user_process_filter_function_name: Optional field used to limit returned processes to those originating from a script function with the given function name.
    :type user_process_filter_function_name: str
    :param user_process_filter_project_name: Optional field used to limit returned processes to those originating from projects with project names containing a specific string.
    :type user_process_filter_project_name: str
    :param user_process_filter_script_id: Optional field used to limit returned processes to those originating from projects with a specific script ID.
    :type user_process_filter_script_id: str
    :param user_process_filter_start_time: Optional field used to limit returned processes to those that were started on or after the given timestamp.
    :type user_process_filter_start_time: str
    :param user_process_filter_statuses: Optional field used to limit returned processes to those having one of the specified process statuses.
    :type user_process_filter_statuses: List[str]
    :param user_process_filter_types: Optional field used to limit returned processes to those having one of the specified process types.
    :type user_process_filter_types: List[str]
    :param user_process_filter_user_access_levels: Optional field used to limit returned processes to those having one of the specified user access levels.
    :type user_process_filter_user_access_levels: List[str]

    """
    return web.Response(status=200)


async def script_processes_list_script_processes(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, script_id=None, script_process_filter_deployment_id=None, script_process_filter_end_time=None, script_process_filter_function_name=None, script_process_filter_start_time=None, script_process_filter_statuses=None, script_process_filter_types=None, script_process_filter_user_access_levels=None) -> web.Response:
    """script_processes_list_script_processes

    List information about a script&#39;s executed processes, such as process type and current status.

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
    :param page_size: The maximum number of returned processes per page of results. Defaults to 50.
    :type page_size: int
    :param page_token: The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from a previous response.
    :type page_token: str
    :param script_id: The script ID of the project whose processes are listed.
    :type script_id: str
    :param script_process_filter_deployment_id: Optional field used to limit returned processes to those originating from projects with a specific deployment ID.
    :type script_process_filter_deployment_id: str
    :param script_process_filter_end_time: Optional field used to limit returned processes to those that completed on or before the given timestamp.
    :type script_process_filter_end_time: str
    :param script_process_filter_function_name: Optional field used to limit returned processes to those originating from a script function with the given function name.
    :type script_process_filter_function_name: str
    :param script_process_filter_start_time: Optional field used to limit returned processes to those that were started on or after the given timestamp.
    :type script_process_filter_start_time: str
    :param script_process_filter_statuses: Optional field used to limit returned processes to those having one of the specified process statuses.
    :type script_process_filter_statuses: List[str]
    :param script_process_filter_types: Optional field used to limit returned processes to those having one of the specified process types.
    :type script_process_filter_types: List[str]
    :param script_process_filter_user_access_levels: Optional field used to limit returned processes to those having one of the specified user access levels.
    :type script_process_filter_user_access_levels: List[str]

    """
    return web.Response(status=200)
