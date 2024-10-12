from typing import List, Dict
from aiohttp import web

from openapi_server.models.adds_configuration import AddsConfiguration
from openapi_server.models.adds_service_members import AddsServiceMembers
from openapi_server.models.alerts import Alerts
from openapi_server.models.credentials import Credentials
from openapi_server.models.dimensions import Dimensions
from openapi_server.models.forest_summary import ForestSummary
from openapi_server.models.metric_metadata import MetricMetadata
from openapi_server.models.metric_metadata_list import MetricMetadataList
from openapi_server.models.metric_sets import MetricSets
from openapi_server.models.metrics import Metrics
from openapi_server.models.replication_details_list import ReplicationDetailsList
from openapi_server.models.replication_status import ReplicationStatus
from openapi_server.models.replication_summary_list import ReplicationSummaryList
from openapi_server.models.service_member import ServiceMember
from openapi_server.models.service_members import ServiceMembers
from openapi_server.models.service_properties import ServiceProperties
from openapi_server.models.services import Services
from openapi_server.models.user_preference import UserPreference
from openapi_server import util


async def ad_domain_service_members_list(request: web.Request, service_name, is_groupby_site, next_partition_key, next_row_key, api_version, filter=None, query=None, take_count=None) -> web.Response:
    """ad_domain_service_members_list

    Gets the details of the servers, for a given Active Directory Domain Service, that are onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service.
    :type service_name: str
    :param is_groupby_site: Indicates if the result should be grouped by site or not.
    :type is_groupby_site: bool
    :param next_partition_key: The next partition key to query for.
    :type next_partition_key: str
    :param next_row_key: The next row key to query for.
    :type next_row_key: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The server property filter to apply.
    :type filter: str
    :param query: The custom query.
    :type query: str
    :param take_count: The take count , which specifies the number of elements that can be returned from a sequence.
    :type take_count: int

    """
    return web.Response(status=200)


async def adds_service_get_metrics(request: web.Request, service_name, metric_name, group_name, api_version, group_key=None, from_date=None, to_date=None) -> web.Response:
    """adds_service_get_metrics

    Gets the server related metrics for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param group_key: The group key
    :type group_key: str
    :param from_date: The start date.
    :type from_date: str
    :param to_date: The end date.
    :type to_date: str

    """
    from_date = util.deserialize_datetime(from_date)
    to_date = util.deserialize_datetime(to_date)
    return web.Response(status=200)


async def adds_service_members_delete(request: web.Request, service_name, service_member_id, api_version, confirm=None) -> web.Response:
    """adds_service_members_delete

    Deletes a Active Directory Domain Controller server that has been onboarded to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param confirm: Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered.
    :type confirm: bool

    """
    return web.Response(status=200)


async def adds_service_members_get(request: web.Request, service_name, service_member_id, api_version) -> web.Response:
    """adds_service_members_get

    Gets the details of a server, for a given Active Directory Domain Controller service, that are onboarded to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def adds_service_members_list(request: web.Request, service_name, api_version, filter=None) -> web.Response:
    """adds_service_members_list

    Gets the details of the Active Directory Domain servers, for a given Active Directory Domain Service, that are onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The server property filter to apply.
    :type filter: str

    """
    return web.Response(status=200)


async def adds_service_members_list_credentials(request: web.Request, service_name, service_member_id, api_version, filter=None) -> web.Response:
    """adds_service_members_list_credentials

    Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param service_member_id: The server Id.
    :type service_member_id: str
    :type service_member_id: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The property filter to apply.
    :type filter: str

    """
    return web.Response(status=200)


async def adds_services_add(request: web.Request, api_version, service) -> web.Response:
    """adds_services_add

    Onboards a service for a given tenant in Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param service: The service object.
    :type service: dict | bytes

    """
    service = ServiceProperties.from_dict(service)
    return web.Response(status=200)


async def adds_services_get_forest_summary(request: web.Request, service_name, api_version) -> web.Response:
    """adds_services_get_forest_summary

    Gets the forest summary for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def adds_services_get_metric_metadata(request: web.Request, service_name, metric_name, api_version) -> web.Response:
    """adds_services_get_metric_metadata

    Gets the service related metric information.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def adds_services_get_metric_metadata_for_group(request: web.Request, service_name, metric_name, group_name, api_version, group_key=None, from_date=None, to_date=None) -> web.Response:
    """adds_services_get_metric_metadata_for_group

    Gets the service related metrics for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param group_key: The group key
    :type group_key: str
    :param from_date: The start date.
    :type from_date: str
    :param to_date: The end date.
    :type to_date: str

    """
    from_date = util.deserialize_datetime(from_date)
    to_date = util.deserialize_datetime(to_date)
    return web.Response(status=200)


async def adds_services_list(request: web.Request, api_version, filter=None, service_type=None, skip_count=None, take_count=None) -> web.Response:
    """adds_services_list

    Gets the details of Active Directory Domain Service, for a tenant, that are onboarded to Azure Active Directory Connect Health.

    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The service property filter to apply.
    :type filter: str
    :param service_type: The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
    :type service_type: str
    :param skip_count: The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
    :type skip_count: int
    :param take_count: The take count , which specifies the number of elements that can be returned from a sequence.
    :type take_count: int

    """
    return web.Response(status=200)


async def adds_services_list_metric_metadata(request: web.Request, service_name, api_version, filter=None, perf_counter=None) -> web.Response:
    """adds_services_list_metric_metadata

    Gets the service related metrics information.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The metric metadata property filter to apply.
    :type filter: str
    :param perf_counter: Indicates if only performance counter metrics are requested.
    :type perf_counter: bool

    """
    return web.Response(status=200)


async def adds_services_list_metrics_average(request: web.Request, service_name, metric_name, group_name, api_version) -> web.Response:
    """adds_services_list_metrics_average

    Gets the average of the metric values for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def adds_services_list_metrics_sum(request: web.Request, service_name, metric_name, group_name, api_version) -> web.Response:
    """adds_services_list_metrics_sum

    Gets the sum of the metric values for a given metric and group combination.

    :param service_name: The name of the service.
    :type service_name: str
    :param metric_name: The metric name
    :type metric_name: str
    :param group_name: The group name
    :type group_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def adds_services_list_replication_details(request: web.Request, service_name, api_version, filter=None, with_details=None) -> web.Response:
    """adds_services_list_replication_details

    Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The server property filter to apply.
    :type filter: str
    :param with_details: Indicates if InboundReplicationNeighbor details are required or not.
    :type with_details: bool

    """
    return web.Response(status=200)


async def adds_services_list_replication_summary(request: web.Request, service_name, is_groupby_site, query, next_partition_key, next_row_key, api_version, filter=None, take_count=None) -> web.Response:
    """adds_services_list_replication_summary

    Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service.
    :type service_name: str
    :param is_groupby_site: Indicates if the result should be grouped by site or not.
    :type is_groupby_site: bool
    :param query: The custom query.
    :type query: str
    :param next_partition_key: The next partition key to query for.
    :type next_partition_key: str
    :param next_row_key: The next row key to query for.
    :type next_row_key: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The server property filter to apply.
    :type filter: str
    :param take_count: The take count , which specifies the number of elements that can be returned from a sequence.
    :type take_count: int

    """
    return web.Response(status=200)


async def adds_services_list_server_alerts(request: web.Request, service_member_id, service_name, api_version, filter=None, state=None, _from=None, to=None) -> web.Response:
    """adds_services_list_server_alerts

    Gets the details of an alert for a given Active Directory Domain Controller service and server combination.

    :param service_member_id: The server Id for which the alert details needs to be queried.
    :type service_member_id: str
    :type service_member_id: str
    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The alert property filter to apply.
    :type filter: str
    :param state: The alert state to query for.
    :type state: str
    :param _from: The start date to query for.
    :type _from: str
    :param to: The end date till when to query for.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def adds_services_replication_status_get(request: web.Request, service_name, api_version) -> web.Response:
    """adds_services_replication_status_get

    Gets Replication status for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def adds_services_service_members_add(request: web.Request, service_name, api_version, service_member) -> web.Response:
    """adds_services_service_members_add

    Onboards  a server, for a given Active Directory Domain Controller service, to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service under which the server is to be onboarded.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param service_member: The server object.
    :type service_member: dict | bytes

    """
    service_member = ServiceMember.from_dict(service_member)
    return web.Response(status=200)


async def adds_services_service_members_list(request: web.Request, service_name, api_version, filter=None, dimension_type=None, dimension_signature=None) -> web.Response:
    """adds_services_service_members_list

    Gets the details of the servers, for a given Active Directory Domain Controller service, that are onboarded to Azure Active Directory Connect Health Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The server property filter to apply.
    :type filter: str
    :param dimension_type: The server specific dimension.
    :type dimension_type: str
    :param dimension_signature: The value of the dimension.
    :type dimension_signature: str

    """
    return web.Response(status=200)


async def adds_services_user_preference_add(request: web.Request, service_name, feature_name, api_version, setting) -> web.Response:
    """adds_services_user_preference_add

    Adds the user preferences for a given feature.

    :param service_name: The name of the service.
    :type service_name: str
    :param feature_name: The name of the feature.
    :type feature_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param setting: The user preference setting.
    :type setting: dict | bytes

    """
    setting = UserPreference.from_dict(setting)
    return web.Response(status=200)


async def adds_services_user_preference_delete(request: web.Request, service_name, feature_name, api_version) -> web.Response:
    """adds_services_user_preference_delete

    Deletes the user preferences for a given feature.

    :param service_name: The name of the service.
    :type service_name: str
    :param feature_name: The name of the feature.
    :type feature_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def adds_services_user_preference_get(request: web.Request, service_name, feature_name, api_version) -> web.Response:
    """adds_services_user_preference_get

    Gets the user preferences for a given feature.

    :param service_name: The name of the service.
    :type service_name: str
    :param feature_name: The name of the feature.
    :type feature_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def alerts_list_adds_alerts(request: web.Request, service_name, api_version, filter=None, state=None, _from=None, to=None) -> web.Response:
    """alerts_list_adds_alerts

    Gets the alerts for a given Active Directory Domain Service.

    :param service_name: The name of the service.
    :type service_name: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str
    :param filter: The alert property filter to apply.
    :type filter: str
    :param state: The alert state to query for.
    :type state: str
    :param _from: The start date to query for.
    :type _from: str
    :param to: The end date till when to query for.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def configuration_list_adds_configurations(request: web.Request, service_name, grouping=None) -> web.Response:
    """configuration_list_adds_configurations

    Gets the service configurations.

    :param service_name: The name of the service.
    :type service_name: str
    :param grouping: The grouping for configurations.
    :type grouping: str

    """
    return web.Response(status=200)


async def dimensions_list_adds_dimensions(request: web.Request, service_name, dimension, api_version) -> web.Response:
    """dimensions_list_adds_dimensions

    Gets the dimensions for a given dimension type in a server.

    :param service_name: The name of the service.
    :type service_name: str
    :param dimension: The dimension type.
    :type dimension: str
    :param api_version: The version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
