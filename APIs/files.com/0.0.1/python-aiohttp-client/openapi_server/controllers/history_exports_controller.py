from typing import List, Dict
from aiohttp import web

from openapi_server.models.history_export_entity import HistoryExportEntity
from openapi_server import util


async def get_history_exports_id(request: web.Request, id) -> web.Response:
    """Show History Export

    Show History Export

    :param id: History Export ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_history_exports(request: web.Request, end_at=None, query_action=None, query_destination=None, query_failure_type=None, query_file_id=None, query_folder=None, query_interface=None, query_ip=None, query_parent_id=None, query_path=None, query_src=None, query_target_id=None, query_target_name=None, query_target_permission=None, query_target_permission_set=None, query_target_platform=None, query_target_user_id=None, query_target_username=None, query_user_id=None, query_username=None, start_at=None, user_id=None) -> web.Response:
    """Create History Export

    Create History Export

    :param end_at: End date/time of export range.
    :type end_at: str
    :param query_action: Filter results by this this action type. Valid values: &#x60;create&#x60;, &#x60;read&#x60;, &#x60;update&#x60;, &#x60;destroy&#x60;, &#x60;move&#x60;, &#x60;login&#x60;, &#x60;failedlogin&#x60;, &#x60;copy&#x60;, &#x60;user_create&#x60;, &#x60;user_update&#x60;, &#x60;user_destroy&#x60;, &#x60;group_create&#x60;, &#x60;group_update&#x60;, &#x60;group_destroy&#x60;, &#x60;permission_create&#x60;, &#x60;permission_destroy&#x60;, &#x60;api_key_create&#x60;, &#x60;api_key_update&#x60;, &#x60;api_key_destroy&#x60;
    :type query_action: str
    :param query_destination: Return results that are file moves with this path as destination.
    :type query_destination: str
    :param query_failure_type: If searching for Histories about login failures, this parameter restricts results to failures of this specific type.  Valid values: &#x60;expired_trial&#x60;, &#x60;account_overdue&#x60;, &#x60;locked_out&#x60;, &#x60;ip_mismatch&#x60;, &#x60;password_mismatch&#x60;, &#x60;site_mismatch&#x60;, &#x60;username_not_found&#x60;, &#x60;none&#x60;, &#x60;no_ftp_permission&#x60;, &#x60;no_web_permission&#x60;, &#x60;no_directory&#x60;, &#x60;errno_enoent&#x60;, &#x60;no_sftp_permission&#x60;, &#x60;no_dav_permission&#x60;, &#x60;no_restapi_permission&#x60;, &#x60;key_mismatch&#x60;, &#x60;region_mismatch&#x60;, &#x60;expired_access&#x60;, &#x60;desktop_ip_mismatch&#x60;, &#x60;desktop_api_key_not_used_quickly_enough&#x60;, &#x60;disabled&#x60;, &#x60;country_mismatch&#x60;
    :type query_failure_type: str
    :param query_file_id: Return results that are file actions related to the file indicated by this File ID
    :type query_file_id: str
    :param query_folder: Return results that are file actions related to files or folders inside this folder path.
    :type query_folder: str
    :param query_interface: Filter results by this this interface type. Valid values: &#x60;web&#x60;, &#x60;ftp&#x60;, &#x60;robot&#x60;, &#x60;jsapi&#x60;, &#x60;webdesktopapi&#x60;, &#x60;sftp&#x60;, &#x60;dav&#x60;, &#x60;desktop&#x60;, &#x60;restapi&#x60;, &#x60;scim&#x60;, &#x60;office&#x60;, &#x60;mobile&#x60;, &#x60;as2&#x60;, &#x60;inbound_email&#x60;, &#x60;remote&#x60;
    :type query_interface: str
    :param query_ip: Filter results by this IP address.
    :type query_ip: str
    :param query_parent_id: Return results that are file actions inside the parent folder specified by this folder ID
    :type query_parent_id: str
    :param query_path: Return results that are file actions related to this path.
    :type query_path: str
    :param query_src: Return results that are file moves originating from this path.
    :type query_src: str
    :param query_target_id: If searching for Histories about specific objects (such as Users, or API Keys), this paremeter restricts results to objects that match this ID.
    :type query_target_id: str
    :param query_target_name: If searching for Histories about Users, Groups or other objects with names, this parameter restricts results to objects with this name/username.
    :type query_target_name: str
    :param query_target_permission: If searching for Histories about Permisisons, this parameter restricts results to permissions of this level.
    :type query_target_permission: str
    :param query_target_permission_set: If searching for Histories about API keys, this parameter restricts results to API keys with this permission set.
    :type query_target_permission_set: str
    :param query_target_platform: If searching for Histories about API keys, this parameter restricts results to API keys associated with this platform.
    :type query_target_platform: str
    :param query_target_user_id: If searching for Histories about API keys, this parameter restricts results to API keys created by/for this user ID.
    :type query_target_user_id: str
    :param query_target_username: If searching for Histories about API keys, this parameter restricts results to API keys created by/for this username.
    :type query_target_username: str
    :param query_user_id: Return results that are actions performed by the user indiciated by this User ID
    :type query_user_id: str
    :param query_username: Filter results by this username.
    :type query_username: str
    :param start_at: Start date/time of export range.
    :type start_at: str
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    end_at = util.deserialize_datetime(end_at)
    start_at = util.deserialize_datetime(start_at)
    return web.Response(status=200)
