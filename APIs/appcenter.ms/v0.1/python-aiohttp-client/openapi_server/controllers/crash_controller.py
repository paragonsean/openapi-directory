from typing import List, Dict
from aiohttp import web

from openapi_server.models.branch_configurations_delete200_response import BranchConfigurationsDelete200Response
from openapi_server.models.crash import Crash
from openapi_server.models.crash_groups_list200_response import CrashGroupsList200Response
from openapi_server.models.crash_groups_list200_response_crash_groups_inner import CrashGroupsList200ResponseCrashGroupsInner
from openapi_server.models.crash_groups_update_request import CrashGroupsUpdateRequest
from openapi_server.models.crashes_delete200_response import CrashesDelete200Response
from openapi_server.models.crashes_get_app_crashes_info200_response import CrashesGetAppCrashesInfo200Response
from openapi_server.models.crashes_get_app_versions200_response_inner import CrashesGetAppVersions200ResponseInner
from openapi_server.models.crashes_get_crash_attachment_location200_response import CrashesGetCrashAttachmentLocation200Response
from openapi_server.models.crashes_get_raw_crash_location200_response import CrashesGetRawCrashLocation200Response
from openapi_server.models.crashes_list_attachments200_response_inner import CrashesListAttachments200ResponseInner
from openapi_server.models.missing_symbol_groups_info200_response import MissingSymbolGroupsInfo200Response
from openapi_server.models.missing_symbol_groups_list200_response import MissingSymbolGroupsList200Response
from openapi_server.models.missing_symbol_groups_list_default_response import MissingSymbolGroupsListDefaultResponse
from openapi_server.models.stacktrace import Stacktrace
from openapi_server.models.symbol_uploads_complete_request import SymbolUploadsCompleteRequest
from openapi_server.models.symbol_uploads_create200_response import SymbolUploadsCreate200Response
from openapi_server.models.symbol_uploads_create_request import SymbolUploadsCreateRequest
from openapi_server.models.symbol_uploads_get_location200_response import SymbolUploadsGetLocation200Response
from openapi_server.models.symbol_uploads_list200_response_inner import SymbolUploadsList200ResponseInner
from openapi_server.models.symbols_get_location200_response import SymbolsGetLocation200Response
from openapi_server.models.symbols_get_status200_response import SymbolsGetStatus200Response
from openapi_server.models.symbols_list200_response_inner import SymbolsList200ResponseInner
from openapi_server import util


async def crash_groups_get(request: web.Request, crash_group_id, owner_name, app_name) -> web.Response:
    """crash_groups_get

    Gets a specific group.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crash_groups_get_stacktrace(request: web.Request, crash_group_id, owner_name, app_name, grouping_only=None) -> web.Response:
    """crash_groups_get_stacktrace

    Gets a stacktrace for a specific crash.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param grouping_only: true if the stacktrace should be only the relevant thread / exception. Default is false
    :type grouping_only: bool

    """
    return web.Response(status=200)


async def crash_groups_list(request: web.Request, owner_name, app_name, last_occurrence_from=None, last_occurrence_to=None, app_version=None, group_type=None, group_status=None, group_text_search=None, orderby=None, continuation_token=None) -> web.Response:
    """crash_groups_list

    Gets a list of crash groups and whether the list contains all available groups.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param last_occurrence_from: Earliest date when the last time a crash occured in a crash group
    :type last_occurrence_from: str
    :param last_occurrence_to: Latest date when the last time a crash occured in a crash group
    :type last_occurrence_to: str
    :param app_version: version
    :type app_version: str
    :param group_type: 
    :type group_type: str
    :param group_status: 
    :type group_status: str
    :param group_text_search: A freetext search that matches in crash, crash types, crash stack_traces and crash user
    :type group_text_search: str
    :param orderby: the OData-like $orderby argument
    :type orderby: str
    :param continuation_token: Cassandra request continuation token. The token is used for pagination.
    :type continuation_token: str

    """
    last_occurrence_from = util.deserialize_datetime(last_occurrence_from)
    last_occurrence_to = util.deserialize_datetime(last_occurrence_to)
    return web.Response(status=200)


async def crash_groups_update(request: web.Request, crash_group_id, owner_name, app_name, body) -> web.Response:
    """crash_groups_update

    Updates a group.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: Group change object. All fields are optional and only provided fields will get updated.
    :type body: dict | bytes

    """
    body = CrashGroupsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def crashes_delete(request: web.Request, crash_group_id, crash_id, owner_name, app_name, retention_delete=None) -> web.Response:
    """crashes_delete

    Delete a specific crash and related attachments and blobs for an app.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param crash_id: id of a specific crash
    :type crash_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param retention_delete: true in that case if the method should skip update counts
    :type retention_delete: bool

    """
    return web.Response(status=200)


async def crashes_get(request: web.Request, crash_group_id, crash_id, owner_name, app_name, include_report=None, include_log=None, include_details=None, include_stacktrace=None, grouping_only=None) -> web.Response:
    """crashes_get

    Gets a specific crash for an app.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param crash_id: id of a specific crash
    :type crash_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param include_report: true if the crash should include the raw crash report. Default is false
    :type include_report: bool
    :param include_log: true if the crash should include the custom log report. Default is false
    :type include_log: bool
    :param include_details: true if the crash should include in depth crash details
    :type include_details: bool
    :param include_stacktrace: true if the crash should include the stacktrace information
    :type include_stacktrace: bool
    :param grouping_only: true if the stacktrace should be only the relevant thread / exception. Default is false
    :type grouping_only: bool

    """
    return web.Response(status=200)


async def crashes_get_app_crashes_info(request: web.Request, owner_name, app_name) -> web.Response:
    """crashes_get_app_crashes_info

    Gets whether the application has any crashes.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crashes_get_app_versions(request: web.Request, owner_name, app_name) -> web.Response:
    """crashes_get_app_versions

    Gets a list of application versions.

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crashes_get_crash_attachment_location(request: web.Request, crash_id, attachment_id, owner_name, app_name) -> web.Response:
    """crashes_get_crash_attachment_location

    Gets the URI location to download crash attachment.

    :param crash_id: id of a specific crash
    :type crash_id: str
    :param attachment_id: attachment id
    :type attachment_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crashes_get_crash_text_attachment_content(request: web.Request, crash_id, attachment_id, owner_name, app_name) -> web.Response:
    """crashes_get_crash_text_attachment_content

    Gets content of the text attachment.

    :param crash_id: id of a specific crash
    :type crash_id: str
    :param attachment_id: attachment id
    :type attachment_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crashes_get_native_crash(request: web.Request, crash_group_id, crash_id, owner_name, app_name) -> web.Response:
    """crashes_get_native_crash

    Gets the native log of a specific crash.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param crash_id: id of a specific crash
    :type crash_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crashes_get_native_crash_download(request: web.Request, crash_group_id, crash_id, owner_name, app_name) -> web.Response:
    """crashes_get_native_crash_download

    Gets the native log of a specific crash as a text attachment.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param crash_id: id of a specific crash
    :type crash_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crashes_get_raw_crash_location(request: web.Request, crash_group_id, crash_id, owner_name, app_name) -> web.Response:
    """crashes_get_raw_crash_location

    Gets the URI location to download json of a specific crash.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param crash_id: id of a specific crash
    :type crash_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def crashes_get_stacktrace(request: web.Request, crash_group_id, crash_id, owner_name, app_name, grouping_only=None) -> web.Response:
    """crashes_get_stacktrace

    Gets a stacktrace for a specific crash.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param crash_id: id of a specific crash
    :type crash_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param grouping_only: true if the stacktrace should be only the relevant thread / exception. Default is false
    :type grouping_only: bool

    """
    return web.Response(status=200)


async def crashes_list(request: web.Request, crash_group_id, owner_name, app_name, include_report=None, include_log=None, date_from=None, date_to=None, app_version=None, error_type=None) -> web.Response:
    """crashes_list

    Gets all crashes of a group.

    :param crash_group_id: id of a specific group
    :type crash_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param include_report: true if the crash should include the raw crash report. Default is false
    :type include_report: bool
    :param include_log: true if the crash should include the custom log report. Default is false
    :type include_log: bool
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str
    :param app_version: version
    :type app_version: str
    :param error_type: 
    :type error_type: str

    """
    date_from = util.deserialize_datetime(date_from)
    date_to = util.deserialize_datetime(date_to)
    return web.Response(status=200)


async def crashes_list_attachments(request: web.Request, crash_id, owner_name, app_name) -> web.Response:
    """crashes_list_attachments

    Gets all attachments for a specific crash.

    :param crash_id: id of a specific crash
    :type crash_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def missing_symbol_groups_get(request: web.Request, symbol_group_id, owner_name, app_name) -> web.Response:
    """Gets missing symbol crash group by its id

    Gets missing symbol crash group by its id

    :param symbol_group_id: missing symbol crash group id
    :type symbol_group_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def missing_symbol_groups_info(request: web.Request, owner_name, app_name) -> web.Response:
    """Gets application level statistics for all missing symbol groups

    Gets application level statistics for all missing symbol groups

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def missing_symbol_groups_list(request: web.Request, top, owner_name, app_name) -> web.Response:
    """Gets top N (ordered by crash count) of crash groups by missing symbol

    Gets top N (ordered by crash count) of crash groups by missing symbol

    :param top: top N elements
    :type top: int
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def symbol_uploads_complete(request: web.Request, symbol_upload_id, owner_name, app_name, body) -> web.Response:
    """symbol_uploads_complete

    Commits or aborts the symbol upload process for a new set of symbols for the specified application

    :param symbol_upload_id: The ID of the symbol upload
    :type symbol_upload_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The symbol information
    :type body: dict | bytes

    """
    body = SymbolUploadsCompleteRequest.from_dict(body)
    return web.Response(status=200)


async def symbol_uploads_create(request: web.Request, owner_name, app_name, body) -> web.Response:
    """symbol_uploads_create

    Begins the symbol upload process for a new set of symbols for the specified application

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param body: The symbol information
    :type body: dict | bytes

    """
    body = SymbolUploadsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def symbol_uploads_delete(request: web.Request, symbol_upload_id, owner_name, app_name) -> web.Response:
    """symbol_uploads_delete

    Deletes a symbol upload by id for the specified application

    :param symbol_upload_id: The ID of the symbol upload
    :type symbol_upload_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def symbol_uploads_get(request: web.Request, symbol_upload_id, owner_name, app_name) -> web.Response:
    """symbol_uploads_get

    Gets a symbol upload by id for the specified application

    :param symbol_upload_id: The ID of the symbol upload
    :type symbol_upload_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def symbol_uploads_get_location(request: web.Request, symbol_upload_id, owner_name, app_name) -> web.Response:
    """symbol_uploads_get_location

    Gets the URL to download the symbol upload

    :param symbol_upload_id: The ID of the symbol upload
    :type symbol_upload_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def symbol_uploads_list(request: web.Request, owner_name, app_name, top=None, status=None, symbol_type=None) -> web.Response:
    """symbol_uploads_list

    Gets a list of all uploads for the specified application

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str
    :param top: The maximum number of results to return.
    :type top: int
    :param status: Filter results by the current status of a symbol upload: * all: all states in the symbol upload process. Includes created, aborted, committed, processing, indexed and failed states * uploaded: all states after package is uploaded. Includes committed, processing, indexed and failed states * processed: symbol upload processing is completed. Includes indexed and failed states. 
    :type status: str
    :param symbol_type: The type of symbols
    :type symbol_type: str

    """
    return web.Response(status=200)


async def symbols_get(request: web.Request, symbol_id, owner_name, app_name) -> web.Response:
    """symbols_get

    Returns a particular symbol by id (uuid) for the provided application

    :param symbol_id: The ID of the symbol (uuid of the symbol)
    :type symbol_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def symbols_get_location(request: web.Request, symbol_id, owner_name, app_name) -> web.Response:
    """symbols_get_location

    Gets the URL to download the symbol

    :param symbol_id: The ID of the symbol (uuid of the symbol)
    :type symbol_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def symbols_get_status(request: web.Request, symbol_id, owner_name, app_name) -> web.Response:
    """symbols_get_status

    Returns a particular symbol by id (uuid) for the provided application

    :param symbol_id: The ID of the symbol (uuid of the symbol)
    :type symbol_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def symbols_ignore(request: web.Request, symbol_id, owner_name, app_name) -> web.Response:
    """symbols_ignore

    Marks a symbol by id (uuid) as ignored

    :param symbol_id: The ID of the symbol (uuid of the symbol)
    :type symbol_id: str
    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)


async def symbols_list(request: web.Request, owner_name, app_name) -> web.Response:
    """symbols_list

    Returns the list of all symbols for the provided application

    :param owner_name: The name of the owner
    :type owner_name: str
    :param app_name: The name of the application
    :type app_name: str

    """
    return web.Response(status=200)
