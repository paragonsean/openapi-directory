from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_client200_response import GetNetworkClient200Response
from openapi_server.models.get_network_clients200_response import GetNetworkClients200Response
from openapi_server.models.get_organization_clients_bandwidth_usage_history200_response_inner import GetOrganizationClientsBandwidthUsageHistory200ResponseInner
from openapi_server.models.get_organization_clients_overview200_response import GetOrganizationClientsOverview200Response
from openapi_server.models.get_organization_summary_top_clients_by_usage200_response_inner import GetOrganizationSummaryTopClientsByUsage200ResponseInner
from openapi_server.models.get_organization_summary_top_clients_manufacturers_by_usage200_response_inner import GetOrganizationSummaryTopClientsManufacturersByUsage200ResponseInner
from openapi_server.models.provision_network_clients_request import ProvisionNetworkClientsRequest
from openapi_server.models.update_network_client_policy_request import UpdateNetworkClientPolicyRequest
from openapi_server.models.update_network_client_splash_authorization_status_request import UpdateNetworkClientSplashAuthorizationStatusRequest
from openapi_server import util


async def get_device_clients_1(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
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


async def get_network_appliance_client_security_events_1(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
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


async def get_network_client_1(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client associated with the given identifier

    Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_client_policy_1(request: web.Request, network_id, client_id) -> web.Response:
    """Return the policy assigned to a client on the network

    Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_client_splash_authorization_status_1(request: web.Request, network_id, client_id) -> web.Response:
    """Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash

    Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_client_traffic_history_1(request: web.Request, network_id, client_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_client_usage_history_1(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client&#39;s daily usage history

    Return the client&#39;s daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_clients_1(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None, statuses=None, ip=None, ip6=None, ip6_local=None, mac=None, os=None, description=None, vlan=None, recent_device_connections=None) -> web.Response:
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


async def get_network_clients_application_usage_1(request: web.Request, network_id, clients, ssid_number=None, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None) -> web.Response:
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


async def get_network_clients_bandwidth_usage_history_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_clients_overview_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
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


async def get_network_clients_usage_histories_1(request: web.Request, network_id, clients, ssid_number=None, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None) -> web.Response:
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


async def get_network_wireless_client_connection_stats_1(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
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


async def get_network_wireless_client_connectivity_events_1(request: web.Request, network_id, client_id, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None, types=None, included_severities=None, band=None, ssid_number=None, device_serial=None) -> web.Response:
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


async def get_network_wireless_client_latency_history_1(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
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


async def get_network_wireless_client_latency_stats_1(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
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


async def get_network_wireless_clients_connection_stats_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
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


async def get_network_wireless_clients_latency_stats_1(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
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


async def get_organization_clients_bandwidth_usage_history_1(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
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


async def get_organization_clients_overview_1(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
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


async def get_organization_clients_search_1(request: web.Request, organization_id, mac, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the client details in an organization

    Return the client details in an organization

    :param organization_id: 
    :type organization_id: str
    :param mac: The MAC address of the client. Required.
    :type mac: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 5. Default is 5.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_summary_top_clients_by_usage_3(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
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


async def get_organization_summary_top_clients_manufacturers_by_usage_3(request: web.Request, organization_id, t0=None, t1=None, timespan=None) -> web.Response:
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


async def provision_network_clients_1(request: web.Request, network_id, body) -> web.Response:
    """Provisions a client with a name and policy

    Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProvisionNetworkClientsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_client_policy_1(request: web.Request, network_id, client_id, body) -> web.Response:
    """Update the policy assigned to a client on the network

    Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkClientPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_client_splash_authorization_status_1(request: web.Request, network_id, client_id, body) -> web.Response:
    """Update a client&#39;s splash authorization

    Update a client&#39;s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkClientSplashAuthorizationStatusRequest.from_dict(body)
    return web.Response(status=200)
