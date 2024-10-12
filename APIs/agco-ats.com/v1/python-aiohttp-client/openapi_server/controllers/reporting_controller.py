from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_bundle import APIPagedResponseUpdateSystemModelsBundle
from openapi_server.models.api_paged_response_update_system_models_client_status_update_system_models_paged_client_status_metadata import APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata
from openapi_server.models.api_paged_response_update_system_models_package_status_summary import APIPagedResponseUpdateSystemModelsPackageStatusSummary
from openapi_server.models.api_paged_response_update_system_models_update_group import APIPagedResponseUpdateSystemModelsUpdateGroup
from openapi_server.models.api_paged_response_update_system_models_update_group_client_relationship import APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship
from openapi_server.models.update_system_models_client import UpdateSystemModelsClient
from openapi_server.models.update_system_models_client_info import UpdateSystemModelsClientInfo
from openapi_server.models.update_system_models_package import UpdateSystemModelsPackage
from openapi_server.models.update_system_models_package_status_summary import UpdateSystemModelsPackageStatusSummary
from openapi_server.models.update_system_models_update_metrics_data import UpdateSystemModelsUpdateMetricsData
from openapi_server import util


async def reporting_bundle_status_summary(request: web.Request, bundle_id, limit=None, offset=None) -> web.Response:
    """Get a summary of all Packages in a Bundle

    No Documentation Found.

    :param bundle_id: The BundleID
    :type bundle_id: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def reporting_bundles_in_update_group(request: web.Request, id, include_inactive, limit=None, offset=None) -> web.Response:
    """Get a list of bundles for UpdateGroup.

    No Documentation Found.

    :param id: The UpdateGroupID
    :type id: str
    :param include_inactive: Include Inactive Bundles (true|false)
    :type include_inactive: bool
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def reporting_client_info(request: web.Request, client_id) -> web.Response:
    """Get Client Information

    No Documentation Found.

    :param client_id: The Client ID
    :type client_id: str

    """
    return web.Response(status=200)


async def reporting_current_packages_in_update_group(request: web.Request, id, subscription_type_filter=None) -> web.Response:
    """Get the current packages for an update group.

    No Documentation Found.

    :param id: The UpdateGroupID
    :type id: str
    :param subscription_type_filter: Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned.
    :type subscription_type_filter: str

    """
    return web.Response(status=200)


async def reporting_get_client(request: web.Request, id) -> web.Response:
    """Get a Client in the Update System.

    No Documentation Found.

    :param id: The Client ID
    :type id: str

    """
    return web.Response(status=200)


async def reporting_get_subscriptions(request: web.Request, client_id=None, update_group_id=None, limit=None, offset=None) -> web.Response:
    """Get a list of current Client Subscriptions.

    No Documentation Found.

    :param client_id: Optional. Filter by Client ID
    :type client_id: str
    :param update_group_id: Optional. Filter by Update Group ID
    :type update_group_id: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def reporting_package_status_summary(request: web.Request, package_id) -> web.Response:
    """Get a summary report for a Specific Package

    No Documentation Found.

    :param package_id: The Package ID
    :type package_id: str

    """
    return web.Response(status=200)


async def reporting_registered_clients(request: web.Request, update_group_id=None, client_id=None, tag=None, report_result=None, report_result_is_valid=None, report_value=None, last_check_in_before=None, last_check_in_after=None, order_by=None, limit=None, offset=None) -> web.Response:
    """Get a list of subscribed clients

    No Documentation Found.

    :param update_group_id: Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned.
    :type update_group_id: str
    :param client_id: Optional. Filter where ClientID matches a value. Wildcards are supported (*).
    :type client_id: str
    :param tag: Optional. Filter where Tag matches a value. Wildcards are supported (*).
    :type tag: str
    :param report_result: Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*).
    :type report_result: str
    :param report_result_is_valid: Optional and UpdateGroupID must be included. When &#39;true&#39; filters results where ReportResult equals ReportResultExpected.  When &#39;false&#39; filters results where ValueToValidate does not equal ReportResults.
    :type report_result_is_valid: bool
    :param report_value: Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*).
    :type report_value: str
    :param last_check_in_before: Optional. Filter where LastCheckIn occured before the provided date.
    :type last_check_in_before: str
    :param last_check_in_after: Optional. Filter where LastCheckIn occured after the provided date.
    :type last_check_in_after: str
    :param order_by: Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...                 If sort direction is not provided for a field, it will be sorted ascending.
    :type order_by: str
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    last_check_in_before = util.deserialize_datetime(last_check_in_before)
    last_check_in_after = util.deserialize_datetime(last_check_in_after)
    return web.Response(status=200)


async def reporting_update_groups(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def reporting_update_metrics(request: web.Request, update_group_id, bundle_number=None) -> web.Response:
    """Get data for pie charts in UpdateMetrics.

    No Documentation Found.

    :param update_group_id: The UpdateType in which clients must be for the report to include them.
    :type update_group_id: str
    :param bundle_number: Optional. Tells us which chart to show based upon filter.
    :type bundle_number: int

    """
    return web.Response(status=200)
