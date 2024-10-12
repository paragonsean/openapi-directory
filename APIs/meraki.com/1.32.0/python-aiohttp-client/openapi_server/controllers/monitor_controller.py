from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_device_camera_snapshot_request import GenerateDeviceCameraSnapshotRequest
from openapi_server.models.get_administered_identities_me200_response import GetAdministeredIdentitiesMe200Response
from openapi_server.models.get_device_switch_ports_statuses200_response_inner import GetDeviceSwitchPortsStatuses200ResponseInner
from openapi_server.models.get_device_wireless_connection_stats200_response import GetDeviceWirelessConnectionStats200Response
from openapi_server.models.get_network_alerts_history200_response_inner import GetNetworkAlertsHistory200ResponseInner
from openapi_server.models.get_network_client200_response import GetNetworkClient200Response
from openapi_server.models.get_network_clients200_response import GetNetworkClients200Response
from openapi_server.models.get_network_events200_response import GetNetworkEvents200Response
from openapi_server.models.get_network_events_event_types200_response_inner import GetNetworkEventsEventTypes200ResponseInner
from openapi_server.models.get_network_insight_application_health_by_time200_response_inner import GetNetworkInsightApplicationHealthByTime200ResponseInner
from openapi_server.models.get_network_sensor_alerts_current_overview_by_metric200_response import GetNetworkSensorAlertsCurrentOverviewByMetric200Response
from openapi_server.models.get_network_sensor_alerts_overview_by_metric200_response_inner import GetNetworkSensorAlertsOverviewByMetric200ResponseInner
from openapi_server.models.get_network_sm_device_cellular_usage_history200_response_inner import GetNetworkSmDeviceCellularUsageHistory200ResponseInner
from openapi_server.models.get_network_sm_device_connectivity200_response_inner import GetNetworkSmDeviceConnectivity200ResponseInner
from openapi_server.models.get_network_sm_device_desktop_logs200_response_inner import GetNetworkSmDeviceDesktopLogs200ResponseInner
from openapi_server.models.get_network_sm_device_device_command_logs200_response_inner import GetNetworkSmDeviceDeviceCommandLogs200ResponseInner
from openapi_server.models.get_network_sm_device_performance_history200_response_inner import GetNetworkSmDevicePerformanceHistory200ResponseInner
from openapi_server.models.get_network_wireless_channel_utilization_history200_response_inner import GetNetworkWirelessChannelUtilizationHistory200ResponseInner
from openapi_server.models.get_network_wireless_client_count_history200_response_inner import GetNetworkWirelessClientCountHistory200ResponseInner
from openapi_server.models.get_network_wireless_connection_stats200_response import GetNetworkWirelessConnectionStats200Response
from openapi_server.models.get_network_wireless_data_rate_history200_response_inner import GetNetworkWirelessDataRateHistory200ResponseInner
from openapi_server.models.get_network_wireless_failed_connections200_response_inner import GetNetworkWirelessFailedConnections200ResponseInner
from openapi_server.models.get_network_wireless_latency_history200_response_inner import GetNetworkWirelessLatencyHistory200ResponseInner
from openapi_server.models.get_network_wireless_signal_quality_history200_response_inner import GetNetworkWirelessSignalQualityHistory200ResponseInner
from openapi_server.models.get_network_wireless_usage_history200_response_inner import GetNetworkWirelessUsageHistory200ResponseInner
from openapi_server.models.get_organization_adaptive_policy_overview200_response import GetOrganizationAdaptivePolicyOverview200Response
from openapi_server.models.get_organization_api_requests200_response_inner import GetOrganizationApiRequests200ResponseInner
from openapi_server.models.get_organization_api_requests_overview_response_codes_by_interval200_response_inner import GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner
from openapi_server.models.get_organization_cellular_gateway_uplink_statuses200_response_inner import GetOrganizationCellularGatewayUplinkStatuses200ResponseInner
from openapi_server.models.get_organization_clients_bandwidth_usage_history200_response_inner import GetOrganizationClientsBandwidthUsageHistory200ResponseInner
from openapi_server.models.get_organization_clients_overview200_response import GetOrganizationClientsOverview200Response
from openapi_server.models.get_organization_devices_availabilities200_response_inner import GetOrganizationDevicesAvailabilities200ResponseInner
from openapi_server.models.get_organization_devices_power_modules_statuses_by_device200_response_inner import GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_statuses200_response import GetOrganizationDevicesStatuses200Response
from openapi_server.models.get_organization_devices_statuses_overview200_response import GetOrganizationDevicesStatusesOverview200Response
from openapi_server.models.get_organization_devices_uplinks_addresses_by_device200_response_inner import GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner
from openapi_server.models.get_organization_devices_uplinks_loss_and_latency200_response_inner import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner
from openapi_server.models.get_organization_sensor_readings_history200_response_inner import GetOrganizationSensorReadingsHistory200ResponseInner
from openapi_server.models.get_organization_sensor_readings_latest200_response_inner import GetOrganizationSensorReadingsLatest200ResponseInner
from openapi_server.models.get_organization_summary_top_appliances_by_utilization200_response_inner import GetOrganizationSummaryTopAppliancesByUtilization200ResponseInner
from openapi_server.models.get_organization_summary_top_clients_by_usage200_response_inner import GetOrganizationSummaryTopClientsByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_clients_manufacturers_by_usage200_response_inner import GetOrganizationSummaryTopClientsManufacturersByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_devices_by_usage200_response_inner import GetOrganizationSummaryTopDevicesByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_devices_models_by_usage200_response_inner import GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_ssids_by_usage200_response_inner import GetOrganizationSummaryTopSsidsByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_switches_by_energy_usage200_response_inner import GetOrganizationSummaryTopSwitchesByEnergyUsage200ResponseInner
from openapi_server.models.get_organization_uplinks_statuses200_response_inner import GetOrganizationUplinksStatuses200ResponseInner
from openapi_server.models.get_organization_webhooks_logs200_response_inner import GetOrganizationWebhooksLogs200ResponseInner
from openapi_server import util


async def generate_device_camera_snapshot_0(request: web.Request, serial, body=None) -> web.Response:
    """Generate a snapshot of what the camera sees at the specified time and return a link to that image.

    Generate a snapshot of what the camera sees at the specified time and return a link to that image.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = GenerateDeviceCameraSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def get_administered_identities_me_0(request: web.Request, ) -> web.Response:
    """Returns the identity of the current user.

    Returns the identity of the current user.


    """
    return web.Response(status=200)


async def get_device_appliance_dhcp_subnets_0(request: web.Request, serial) -> web.Response:
    """Return the DHCP subnet information for an appliance

    Return the DHCP subnet information for an appliance

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_appliance_performance_0(request: web.Request, serial) -> web.Response:
    """Return the performance score for a single MX

    Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_appliance_prefixes_delegated_0(request: web.Request, serial) -> web.Response:
    """Return current delegated IPv6 prefixes on an appliance.

    Return current delegated IPv6 prefixes on an appliance.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_appliance_prefixes_delegated_vlan_assignments_0(request: web.Request, serial) -> web.Response:
    """Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

    Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_live_0(request: web.Request, serial) -> web.Response:
    """Returns live state from camera of analytics zones

    Returns live state from camera of analytics zones

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_overview_0(request: web.Request, serial, t0=None, t1=None, timespan=None, object_type=None) -> web.Response:
    """Returns an overview of aggregate analytics data for a timespan

    Returns an overview of aggregate analytics data for a timespan

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
    :type timespan: float
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_recent_0(request: web.Request, serial, object_type=None) -> web.Response:
    """Returns most recent record for analytics zones

    Returns most recent record for analytics zones

    :param serial: 
    :type serial: str
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_zone_history_0(request: web.Request, serial, zone_id, t0=None, t1=None, timespan=None, resolution=None, object_type=None) -> web.Response:
    """Return historical records for analytic zones

    Return historical records for analytic zones

    :param serial: 
    :type serial: str
    :param zone_id: 
    :type zone_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60.
    :type resolution: int
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_zones_0(request: web.Request, serial) -> web.Response:
    """Returns all configured analytic zones for this camera

    Returns all configured analytic zones for this camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_clients_0(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """List the clients of a device, up to a maximum of a month ago

    List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_device_lldp_cdp_0(request: web.Request, serial) -> web.Response:
    """List LLDP and CDP information for a device

    List LLDP and CDP information for a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_loss_and_latency_history_0(request: web.Request, serial, ip, t0=None, t1=None, timespan=None, resolution=None, uplink=None) -> web.Response:
    """Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

    Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

    :param serial: 
    :type serial: str
    :param ip: The destination IP used to obtain the requested stats. This is required.
    :type ip: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
    :type resolution: int
    :param uplink: The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
    :type uplink: str

    """
    return web.Response(status=200)


async def get_device_switch_ports_statuses_0(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the status for all the ports of a switch

    Return the status for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_device_switch_ports_statuses_packets_0(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
    """Return the packet counters for all the ports of a switch

    Return the packet counters for all the ports of a switch

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_device_wireless_connection_stats_0(request: web.Request, serial, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for a given AP on this network

    Aggregated connectivity info for a given AP on this network

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str

    """
    return web.Response(status=200)


async def get_device_wireless_latency_stats_0(request: web.Request, serial, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
    """Aggregated latency info for a given AP on this network

    Aggregated latency info for a given AP on this network

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str
    :param fields: Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    :type fields: str

    """
    return web.Response(status=200)


async def get_device_wireless_status_0(request: web.Request, serial) -> web.Response:
    """Return the SSID statuses of an access point

    Return the SSID statuses of an access point

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_alerts_history_0(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the alert history for this network

    Return the alert history for this network

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_appliance_client_security_events_0(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
    """List the security events for a client

    List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param t0: The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param sort_order: Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order.
    :type sort_order: str

    """
    return web.Response(status=200)


async def get_network_appliance_security_events_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
    """List the security events for a network

    List the security events for a network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param sort_order: Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order.
    :type sort_order: str

    """
    return web.Response(status=200)


async def get_network_appliance_uplinks_usage_history_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Get the sent and received bytes for each uplink of a network.

    Get the sent and received bytes for each uplink of a network.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_network_bluetooth_client_0(request: web.Request, network_id, bluetooth_client_id, include_connectivity_history=None, connectivity_history_timespan=None) -> web.Response:
    """Return a Bluetooth client

    Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.

    :param network_id: 
    :type network_id: str
    :param bluetooth_client_id: 
    :type bluetooth_client_id: str
    :param include_connectivity_history: Include the connectivity history for this client
    :type include_connectivity_history: bool
    :param connectivity_history_timespan: The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.
    :type connectivity_history_timespan: int

    """
    return web.Response(status=200)


async def get_network_bluetooth_clients_0(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None, include_connectivity_history=None) -> web.Response:
    """List the Bluetooth clients seen by APs in this network

    List the Bluetooth clients seen by APs in this network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param include_connectivity_history: Include the connectivity history for this client
    :type include_connectivity_history: bool

    """
    return web.Response(status=200)


async def get_network_client_0(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client associated with the given identifier

    Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_client_traffic_history_0(request: web.Request, network_id, client_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the client&#39;s network traffic data over time

    Return the client&#39;s network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide &gt; General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_client_usage_history_0(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client&#39;s daily usage history

    Return the client&#39;s daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_clients_0(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None, statuses=None, ip=None, ip6=None, ip6_local=None, mac=None, os=None, description=None, vlan=None, recent_device_connections=None) -> web.Response:
    """List the clients that have used this network in the timespan

    List the clients that have used this network in the timespan

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param statuses: Filters clients based on status. Can be one of &#39;Online&#39; or &#39;Offline&#39;.
    :type statuses: List[str]
    :param ip: Filters clients based on a partial or full match for the ip address field.
    :type ip: str
    :param ip6: Filters clients based on a partial or full match for the ip6 address field.
    :type ip6: str
    :param ip6_local: Filters clients based on a partial or full match for the ip6Local address field.
    :type ip6_local: str
    :param mac: Filters clients based on a partial or full match for the mac address field.
    :type mac: str
    :param os: Filters clients based on a partial or full match for the os (operating system) field.
    :type os: str
    :param description: Filters clients based on a partial or full match for the description field.
    :type description: str
    :param vlan: Filters clients based on the full match for the VLAN field.
    :type vlan: str
    :param recent_device_connections: Filters clients based on recent connection type. Can be one of &#39;Wired&#39; or &#39;Wireless&#39;.
    :type recent_device_connections: List[str]

    """
    return web.Response(status=200)


async def get_network_clients_application_usage_0(request: web.Request, network_id, clients, ssid_number=None, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None) -> web.Response:
    """Return the application usage data for clients

    Return the application usage data for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param clients: A list of client keys, MACs or IPs separated by comma.
    :type clients: str
    :param ssid_number: An SSID number to include. If not specified, eveusage histories application usagents for all SSIDs will be returned.
    :type ssid_number: int
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_network_clients_bandwidth_usage_history_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

    Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_clients_overview_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Return overview statistics for network clients

    Return overview statistics for network clients

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_network_clients_usage_histories_0(request: web.Request, network_id, clients, ssid_number=None, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None) -> web.Response:
    """Return the usage histories for clients

    Return the usage histories for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param clients: A list of client keys, MACs or IPs separated by comma.
    :type clients: str
    :param ssid_number: An SSID number to include. If not specified, events for all SSIDs will be returned.
    :type ssid_number: int
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_network_events_0(request: web.Request, network_id, product_type=None, included_event_types=None, excluded_event_types=None, device_mac=None, device_serial=None, device_name=None, client_ip=None, client_mac=None, client_name=None, sm_device_mac=None, sm_device_name=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List the events for the network

    List the events for the network

    :param network_id: 
    :type network_id: str
    :param product_type: The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway
    :type product_type: str
    :param included_event_types: A list of event types. The returned events will be filtered to only include events with these types.
    :type included_event_types: List[str]
    :param excluded_event_types: A list of event types. The returned events will be filtered to exclude events with these types.
    :type excluded_event_types: List[str]
    :param device_mac: The MAC address of the Meraki device which the list of events will be filtered with
    :type device_mac: str
    :param device_serial: The serial of the Meraki device which the list of events will be filtered with
    :type device_serial: str
    :param device_name: The name of the Meraki device which the list of events will be filtered with
    :type device_name: str
    :param client_ip: The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks.
    :type client_ip: str
    :param client_mac: The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks.
    :type client_mac: str
    :param client_name: The name, or partial name, of the client which the list of events will be filtered with
    :type client_name: str
    :param sm_device_mac: The MAC address of the Systems Manager device which the list of events will be filtered with
    :type sm_device_mac: str
    :param sm_device_name: The name of the Systems Manager device which the list of events will be filtered with
    :type sm_device_name: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_events_event_types_0(request: web.Request, network_id) -> web.Response:
    """List the event type to human-readable description

    List the event type to human-readable description

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_insight_application_health_by_time_0(request: web.Request, network_id, application_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Get application health by time

    Get application health by time

    :param network_id: 
    :type network_id: str
    :param application_id: 
    :type application_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_network_network_health_channel_utilization_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Get the channel utilization over each radio for all APs in a network.

    Get the channel utilization over each radio for all APs in a network.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600.
    :type resolution: int
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_current_overview_by_metric_0(request: web.Request, network_id) -> web.Response:
    """Return an overview of currently alerting sensors by metric

    Return an overview of currently alerting sensors by metric

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_sensor_alerts_overview_by_metric_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, interval=None) -> web.Response:
    """Return an overview of alert occurrences over a timespan, by metric

    Return an overview of alert occurrences over a timespan, by metric

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param interval: The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.
    :type interval: int

    """
    return web.Response(status=200)


async def get_network_sm_device_cellular_usage_history_0(request: web.Request, network_id, device_id) -> web.Response:
    """Return the client&#39;s daily cellular data usage history

    Return the client&#39;s daily cellular data usage history. Usage data is in kilobytes.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_device_connectivity_0(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

    Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_desktop_logs_0(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of various Systems Manager network connection details for desktop devices.

    Return historical records of various Systems Manager network connection details for desktop devices.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_device_command_logs_0(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of commands sent to Systems Manager devices

    Return historical records of commands sent to Systems Manager devices. Note that this will include the name of the Dashboard user who initiated the command if it was generated by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out of any reports.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_sm_device_performance_history_0(request: web.Request, network_id, device_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return historical records of various Systems Manager client metrics for desktop devices.

    Return historical records of various Systems Manager client metrics for desktop devices.

    :param network_id: 
    :type network_id: str
    :param device_id: 
    :type device_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_splash_login_attempts_0(request: web.Request, network_id, ssid_number=None, login_identifier=None, timespan=None) -> web.Response:
    """List the splash login attempts for a network

    List the splash login attempts for a network

    :param network_id: 
    :type network_id: str
    :param ssid_number: Only return the login attempts for the specified SSID
    :type ssid_number: int
    :param login_identifier: The username, email, or phone number used during login
    :type login_identifier: str
    :param timespan: The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months
    :type timespan: int

    """
    return web.Response(status=200)


async def get_network_topology_link_layer_0(request: web.Request, network_id) -> web.Response:
    """List the LLDP and CDP information for all discovered devices and connections in a network.

    List the LLDP and CDP information for all discovered devices and connections in a network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_traffic_0(request: web.Request, network_id, t0=None, timespan=None, device_type=None) -> web.Response:
    """Return the traffic analysis data for this network

    Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
    :type timespan: float
    :param device_type: Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage.
    :type device_type: str

    """
    return web.Response(status=200)


async def get_network_wireless_air_marshal_0(request: web.Request, network_id, t0=None, timespan=None) -> web.Response:
    """List Air Marshal scan results from a network

    List Air Marshal scan results from a network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_network_wireless_channel_utilization_history_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None) -> web.Response:
    """Return AP channel utilization over time for a device or network client

    Return AP channel utilization over time for a device or network client

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
    :type resolution: int
    :param auto_resolution: Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false.
    :type auto_resolution: bool
    :param client_id: Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client&#39;s connection history.
    :type client_id: str
    :param device_serial: Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
    :type device_serial: str
    :param ap_tag: Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
    :type ap_tag: str
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;).
    :type band: str

    """
    return web.Response(status=200)


async def get_network_wireless_client_connection_stats_0(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for a given client on this network

    Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str

    """
    return web.Response(status=200)


async def get_network_wireless_client_connectivity_events_0(request: web.Request, network_id, client_id, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None, types=None, included_severities=None, band=None, ssid_number=None, device_serial=None) -> web.Response:
    """List the wireless connectivity events for a client within a network in the timespan.

    List the wireless connectivity events for a client within a network in the timespan.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param types: A list of event types to include. If not specified, events of all types will be returned. Valid types are &#39;assoc&#39;, &#39;disassoc&#39;, &#39;auth&#39;, &#39;deauth&#39;, &#39;dns&#39;, &#39;dhcp&#39;, &#39;roam&#39;, &#39;connection&#39; and/or &#39;sticky&#39;.
    :type types: List[str]
    :param included_severities: A list of severities to include. If not specified, events of all severities will be returned. Valid severities are &#39;good&#39;, &#39;info&#39;, &#39;warn&#39; and/or &#39;bad&#39;.
    :type included_severities: List[str]
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39;, &#39;6&#39;).
    :type band: str
    :param ssid_number: An SSID number to include. If not specified, events for all SSIDs will be returned.
    :type ssid_number: int
    :param device_serial: Filter results by an AP&#39;s serial number.
    :type device_serial: str

    """
    return web.Response(status=200)


async def get_network_wireless_client_count_history_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
    """Return wireless client counts over time for a network, device, or network client

    Return wireless client counts over time for a network, device, or network client

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    :type resolution: int
    :param auto_resolution: Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false.
    :type auto_resolution: bool
    :param client_id: Filter results by network client to return per-device client counts over time inner joined by the queried client&#39;s connection history.
    :type client_id: str
    :param device_serial: Filter results by device.
    :type device_serial: str
    :param ap_tag: Filter results by AP tag.
    :type ap_tag: str
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;).
    :type band: str
    :param ssid: Filter results by SSID number.
    :type ssid: int

    """
    return web.Response(status=200)


async def get_network_wireless_client_latency_history_0(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
    """Return the latency history for a client

    Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.
    :type resolution: int

    """
    return web.Response(status=200)


async def get_network_wireless_client_latency_stats_0(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
    """Aggregated latency info for a given client on this network

    Aggregated latency info for a given client on this network. Clients are identified by their MAC.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str
    :param fields: Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    :type fields: str

    """
    return web.Response(status=200)


async def get_network_wireless_clients_connection_stats_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for this network, grouped by clients

    Aggregated connectivity info for this network, grouped by clients

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str

    """
    return web.Response(status=200)


async def get_network_wireless_clients_latency_stats_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
    """Aggregated latency info for this network, grouped by clients

    Aggregated latency info for this network, grouped by clients

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str
    :param fields: Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    :type fields: str

    """
    return web.Response(status=200)


async def get_network_wireless_connection_stats_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for this network

    Aggregated connectivity info for this network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str

    """
    return web.Response(status=200)


async def get_network_wireless_data_rate_history_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
    """Return PHY data rates over time for a network, device, or network client

    Return PHY data rates over time for a network, device, or network client

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    :type resolution: int
    :param auto_resolution: Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false.
    :type auto_resolution: bool
    :param client_id: Filter results by network client.
    :type client_id: str
    :param device_serial: Filter results by device.
    :type device_serial: str
    :param ap_tag: Filter results by AP tag.
    :type ap_tag: str
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;).
    :type band: str
    :param ssid: Filter results by SSID number.
    :type ssid: int

    """
    return web.Response(status=200)


async def get_network_wireless_devices_connection_stats_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
    """Aggregated connectivity info for this network, grouped by node

    Aggregated connectivity info for this network, grouped by node

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str

    """
    return web.Response(status=200)


async def get_network_wireless_devices_latency_stats_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
    """Aggregated latency info for this network, grouped by node

    Aggregated latency info for this network, grouped by node

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str
    :param fields: Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    :type fields: str

    """
    return web.Response(status=200)


async def get_network_wireless_failed_connections_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, serial=None, client_id=None) -> web.Response:
    """List of all failed client connection events on this network in a given time range

    List of all failed client connection events on this network in a given time range

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str
    :param serial: Filter by AP
    :type serial: str
    :param client_id: Filter by client MAC
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_latency_history_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None, access_category=None) -> web.Response:
    """Return average wireless latency over time for a network, device, or network client

    Return average wireless latency over time for a network, device, or network client

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    :type resolution: int
    :param auto_resolution: Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false.
    :type auto_resolution: bool
    :param client_id: Filter results by network client.
    :type client_id: str
    :param device_serial: Filter results by device.
    :type device_serial: str
    :param ap_tag: Filter results by AP tag.
    :type ap_tag: str
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;).
    :type band: str
    :param ssid: Filter results by SSID number.
    :type ssid: int
    :param access_category: Filter by access category.
    :type access_category: str

    """
    return web.Response(status=200)


async def get_network_wireless_latency_stats_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
    """Aggregated latency info for this network

    Aggregated latency info for this network

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    :type timespan: float
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information.
    :type band: str
    :param ssid: Filter results by SSID
    :type ssid: int
    :param vlan: Filter results by VLAN
    :type vlan: int
    :param ap_tag: Filter results by AP Tag
    :type ap_tag: str
    :param fields: Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    :type fields: str

    """
    return web.Response(status=200)


async def get_network_wireless_mesh_statuses_0(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List wireless mesh statuses for repeaters

    List wireless mesh statuses for repeaters

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 500. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_wireless_signal_quality_history_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
    """Return signal quality (SNR/RSSI) over time for a device or network client

    Return signal quality (SNR/RSSI) over time for a device or network client

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    :type resolution: int
    :param auto_resolution: Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false.
    :type auto_resolution: bool
    :param client_id: Filter results by network client.
    :type client_id: str
    :param device_serial: Filter results by device.
    :type device_serial: str
    :param ap_tag: Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
    :type ap_tag: str
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;).
    :type band: str
    :param ssid: Filter results by SSID number.
    :type ssid: int

    """
    return web.Response(status=200)


async def get_network_wireless_usage_history_0(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
    """Return AP usage over time for a device or network client

    Return AP usage over time for a device or network client

    :param network_id: 
    :type network_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
    :type resolution: int
    :param auto_resolution: Automatically select a data resolution based on the given timespan; this overrides the value specified by the &#39;resolution&#39; parameter. The default setting is false.
    :type auto_resolution: bool
    :param client_id: Filter results by network client to return per-device AP usage over time inner joined by the queried client&#39;s connection history.
    :type client_id: str
    :param device_serial: Filter results by device. Requires :band.
    :type device_serial: str
    :param ap_tag: Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
    :type ap_tag: str
    :param band: Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;).
    :type band: str
    :param ssid: Filter results by SSID number.
    :type ssid: int

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_overview_0(request: web.Request, organization_id) -> web.Response:
    """Returns adaptive policy aggregate statistics for an organization

    Returns adaptive policy aggregate statistics for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_api_requests_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, admin_id=None, path=None, method=None, response_code=None, source_ip=None, user_agent=None, version=None, operation_ids=None) -> web.Response:
    """List the API requests made by an organization

    List the API requests made by an organization

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param admin_id: Filter the results by the ID of the admin who made the API requests
    :type admin_id: str
    :param path: Filter the results by the path of the API requests
    :type path: str
    :param method: Filter the results by the method of the API requests (must be &#39;GET&#39;, &#39;PUT&#39;, &#39;POST&#39; or &#39;DELETE&#39;)
    :type method: str
    :param response_code: Filter the results by the response code of the API requests
    :type response_code: int
    :param source_ip: Filter the results by the IP address of the originating API request
    :type source_ip: str
    :param user_agent: Filter the results by the user agent string of the API request
    :type user_agent: str
    :param version: Filter the results by the API version of the API request
    :type version: int
    :param operation_ids: Filter the results by one or more operation IDs for the API request
    :type operation_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_api_requests_overview_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return an aggregated overview of API requests data

    Return an aggregated overview of API requests data

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_api_requests_overview_response_codes_by_interval_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None, interval=None, version=None, operation_ids=None, source_ips=None, admin_ids=None, user_agent=None) -> web.Response:
    """Tracks organizations&#39; API requests by response code across a given time period

    Tracks organizations&#39; API requests by response code across a given time period

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
    :type timespan: float
    :param interval: The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
    :type interval: int
    :param version: Filter by API version of the endpoint. Allowable values are: [0, 1]
    :type version: int
    :param operation_ids: Filter by operation ID of the endpoint
    :type operation_ids: List[str]
    :param source_ips: Filter by source IP that made the API request
    :type source_ips: List[str]
    :param admin_ids: Filter by admin ID of user that made the API request
    :type admin_ids: List[str]
    :param user_agent: Filter by user agent string for API request. This will filter by a complete or partial match.
    :type user_agent: str

    """
    return web.Response(status=200)


async def get_organization_appliance_security_events_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
    """List the security events for an organization

    List the security events for an organization

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param sort_order: Sorted order of security events based on event detection time. Order options are &#39;ascending&#39; or &#39;descending&#39;. Default is ascending order.
    :type sort_order: str

    """
    return web.Response(status=200)


async def get_organization_appliance_uplink_statuses_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MX and Z series appliances in the organization

    List the uplink status of every Meraki MX and Z series appliances in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def get_organization_appliance_vpn_stats_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, t0=None, t1=None, timespan=None) -> web.Response:
    """Show VPN history stat for networks in an organization

    Show VPN history stat for networks in an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456
    :type network_ids: List[str]
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_appliance_vpn_statuses_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None) -> web.Response:
    """Show VPN status for networks in an organization

    Show VPN status for networks in an organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_cellular_gateway_uplink_statuses_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MG cellular gateway in the organization

    List the uplink status of every Meraki MG cellular gateway in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def get_organization_clients_bandwidth_usage_history_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.

    Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_clients_overview_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return summary information around client data usage (in mb) across the given organization.

    Return summary information around client data usage (in mb) across the given organization.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_configuration_changes_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, network_id=None, admin_id=None) -> web.Response:
    """View the Change Log for your organization

    View the Change Log for your organization

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 5000. Default is 5000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_id: Filters on the given network
    :type network_id: str
    :param admin_id: Filters on the given Admin
    :type admin_id: str

    """
    return web.Response(status=200)


async def get_organization_devices_availabilities_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the availability information for devices in an organization

    List the availability information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_power_modules_statuses_by_device_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the power status information for devices in an organization

    List the power status information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_statuses_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, statuses=None, product_types=None, models=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the status of every Meraki device in the organization

    List the status of every Meraki device in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter devices by network ids.
    :type network_ids: List[str]
    :param serials: Optional parameter to filter devices by serials.
    :type serials: List[str]
    :param statuses: Optional parameter to filter devices by statuses. Valid statuses are [\&quot;online\&quot;, \&quot;alerting\&quot;, \&quot;offline\&quot;, \&quot;dormant\&quot;].
    :type statuses: List[str]
    :param product_types: An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param models: Optional parameter to filter devices by models.
    :type models: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below).
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_statuses_overview_0(request: web.Request, organization_id, product_types=None, network_ids=None) -> web.Response:
    """Return an overview of current device statuses

    Return an overview of current device statuses

    :param organization_id: 
    :type organization_id: str
    :param product_types: An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    :type product_types: List[str]
    :param network_ids: An optional parameter to filter device statuses by network.
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def get_organization_devices_uplinks_addresses_by_device_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, product_types=None, serials=None, tags=None, tags_filter_type=None) -> web.Response:
    """List the current uplink addresses for devices in an organization.

    List the current uplink addresses for devices in an organization.

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
    :type network_ids: List[str]
    :param product_types: Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
    :type product_types: List[str]
    :param serials: Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    :type serials: List[str]
    :param tags: An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches.
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str

    """
    return web.Response(status=200)


async def get_organization_devices_uplinks_loss_and_latency_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None, uplink=None, ip=None) -> web.Response:
    """Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
    :type timespan: float
    :param uplink: Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
    :type uplink: str
    :param ip: Optional filter for a specific destination IP. Default will return all destination IPs.
    :type ip: str

    """
    return web.Response(status=200)


async def get_organization_licenses_overview_0(request: web.Request, organization_id) -> web.Response:
    """Return an overview of the license state for an organization

    Return an overview of the license state for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_openapi_spec_0(request: web.Request, organization_id) -> web.Response:
    """Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON

    Return the OpenAPI 2.0 Specification of the organization&#39;s API documentation in JSON

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_sensor_readings_history_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None, network_ids=None, serials=None, metrics=None) -> web.Response:
    """Return all reported readings from sensors in a given timespan, sorted by timestamp

    Return all reported readings from sensors in a given timespan, sorted by timestamp

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
    :type timespan: float
    :param network_ids: Optional parameter to filter readings by network.
    :type network_ids: List[str]
    :param serials: Optional parameter to filter readings by sensor.
    :type serials: List[str]
    :param metrics: Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
    :type metrics: List[str]

    """
    return web.Response(status=200)


async def get_organization_sensor_readings_latest_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, metrics=None) -> web.Response:
    """Return the latest available reading for each metric from each sensor, sorted by sensor serial

    Return the latest available reading for each metric from each sensor, sorted by sensor serial

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter readings by network.
    :type network_ids: List[str]
    :param serials: Optional parameter to filter readings by sensor.
    :type serials: List[str]
    :param metrics: Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
    :type metrics: List[str]

    """
    return web.Response(status=200)


async def get_organization_summary_top_appliances_by_utilization_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return the top 10 appliances sorted by utilization over given time range.

    Return the top 10 appliances sorted by utilization over given time range.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_clients_by_usage_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 clients by data usage (in mb) over given time range.

    Return metrics for organization&#39;s top 10 clients by data usage (in mb) over given time range.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_clients_manufacturers_by_usage_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top clients by data usage (in mb) over given time range, grouped by manufacturer.

    Return metrics for organization&#39;s top clients by data usage (in mb) over given time range, grouped by manufacturer.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_devices_by_usage_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range

    Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_devices_models_by_usage_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range

    Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_ssids_by_usage_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 ssids by data usage over given time range

    Return metrics for organization&#39;s top 10 ssids by data usage over given time range. Default unit is megabytes.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_summary_top_switches_by_energy_usage_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
    """Return metrics for organization&#39;s top 10 switches by energy usage over given time range

    Return metrics for organization&#39;s top 10 switches by energy usage over given time range. Default unit is joules.

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_uplinks_statuses_0(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MX, MG and Z series devices in the organization

    List the uplink status of every Meraki MX, MG and Z series devices in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def get_organization_webhooks_alert_types_0(request: web.Request, organization_id, product_type=None) -> web.Response:
    """Return a list of alert types to be used with managing webhook alerts

    Return a list of alert types to be used with managing webhook alerts

    :param organization_id: 
    :type organization_id: str
    :param product_type: Filter sample alerts to a specific product type
    :type product_type: str

    """
    return web.Response(status=200)


async def get_organization_webhooks_logs_0(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, url=None) -> web.Response:
    """Return the log of webhook POSTs sent

    Return the log of webhook POSTs sent

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param url: The URL the webhook was sent to
    :type url: str

    """
    return web.Response(status=200)
