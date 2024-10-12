from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_wireless_rf_profile201_response import CreateNetworkWirelessRfProfile201Response
from openapi_server.models.create_network_wireless_rf_profile_request import CreateNetworkWirelessRfProfileRequest
from openapi_server.models.create_network_wireless_ssid_identity_psk_request import CreateNetworkWirelessSsidIdentityPskRequest
from openapi_server.models.get_device_wireless_bluetooth_settings200_response import GetDeviceWirelessBluetoothSettings200Response
from openapi_server.models.get_device_wireless_connection_stats200_response import GetDeviceWirelessConnectionStats200Response
from openapi_server.models.get_network_wireless_bluetooth_settings200_response import GetNetworkWirelessBluetoothSettings200Response
from openapi_server.models.get_network_wireless_channel_utilization_history200_response_inner import GetNetworkWirelessChannelUtilizationHistory200ResponseInner
from openapi_server.models.get_network_wireless_client_count_history200_response_inner import GetNetworkWirelessClientCountHistory200ResponseInner
from openapi_server.models.get_network_wireless_connection_stats200_response import GetNetworkWirelessConnectionStats200Response
from openapi_server.models.get_network_wireless_data_rate_history200_response_inner import GetNetworkWirelessDataRateHistory200ResponseInner
from openapi_server.models.get_network_wireless_failed_connections200_response_inner import GetNetworkWirelessFailedConnections200ResponseInner
from openapi_server.models.get_network_wireless_latency_history200_response_inner import GetNetworkWirelessLatencyHistory200ResponseInner
from openapi_server.models.get_network_wireless_settings200_response import GetNetworkWirelessSettings200Response
from openapi_server.models.get_network_wireless_signal_quality_history200_response_inner import GetNetworkWirelessSignalQualityHistory200ResponseInner
from openapi_server.models.get_network_wireless_ssid_eap_override200_response import GetNetworkWirelessSsidEapOverride200Response
from openapi_server.models.get_network_wireless_ssid_identity_psks200_response_inner import GetNetworkWirelessSsidIdentityPsks200ResponseInner
from openapi_server.models.get_network_wireless_ssid_splash_settings200_response import GetNetworkWirelessSsidSplashSettings200Response
from openapi_server.models.get_network_wireless_usage_history200_response_inner import GetNetworkWirelessUsageHistory200ResponseInner
from openapi_server.models.get_organization_wireless_devices_ethernet_statuses200_response_inner import GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner
from openapi_server.models.update_device_wireless_bluetooth_settings_request import UpdateDeviceWirelessBluetoothSettingsRequest
from openapi_server.models.update_device_wireless_radio_settings_request import UpdateDeviceWirelessRadioSettingsRequest
from openapi_server.models.update_network_wireless_alternate_management_interface_request import UpdateNetworkWirelessAlternateManagementInterfaceRequest
from openapi_server.models.update_network_wireless_billing_request import UpdateNetworkWirelessBillingRequest
from openapi_server.models.update_network_wireless_bluetooth_settings_request import UpdateNetworkWirelessBluetoothSettingsRequest
from openapi_server.models.update_network_wireless_rf_profile_request import UpdateNetworkWirelessRfProfileRequest
from openapi_server.models.update_network_wireless_settings_request import UpdateNetworkWirelessSettingsRequest
from openapi_server.models.update_network_wireless_ssid_bonjour_forwarding_request import UpdateNetworkWirelessSsidBonjourForwardingRequest
from openapi_server.models.update_network_wireless_ssid_device_type_group_policies_request import UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest
from openapi_server.models.update_network_wireless_ssid_eap_override_request import UpdateNetworkWirelessSsidEapOverrideRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l3_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l7_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_hotspot20_request import UpdateNetworkWirelessSsidHotspot20Request
from openapi_server.models.update_network_wireless_ssid_identity_psk_request import UpdateNetworkWirelessSsidIdentityPskRequest
from openapi_server.models.update_network_wireless_ssid_request import UpdateNetworkWirelessSsidRequest
from openapi_server.models.update_network_wireless_ssid_schedules_request import UpdateNetworkWirelessSsidSchedulesRequest
from openapi_server.models.update_network_wireless_ssid_splash_settings_request import UpdateNetworkWirelessSsidSplashSettingsRequest
from openapi_server.models.update_network_wireless_ssid_traffic_shaping_rules_request import UpdateNetworkWirelessSsidTrafficShapingRulesRequest
from openapi_server.models.update_network_wireless_ssid_vpn_request import UpdateNetworkWirelessSsidVpnRequest
from openapi_server import util


async def create_network_wireless_rf_profile(request: web.Request, network_id, body) -> web.Response:
    """Creates new RF profile for this network

    Creates new RF profile for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWirelessRfProfileRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_wireless_ssid_identity_psk(request: web.Request, network_id, number, body) -> web.Response:
    """Create an Identity PSK

    Create an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWirelessSsidIdentityPskRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_wireless_rf_profile(request: web.Request, network_id, rf_profile_id) -> web.Response:
    """Delete a RF Profile

    Delete a RF Profile

    :param network_id: 
    :type network_id: str
    :param rf_profile_id: 
    :type rf_profile_id: str

    """
    return web.Response(status=200)


async def delete_network_wireless_ssid_identity_psk(request: web.Request, network_id, number, identity_psk_id) -> web.Response:
    """Delete an Identity PSK

    Delete an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str

    """
    return web.Response(status=200)


async def get_device_wireless_bluetooth_settings(request: web.Request, serial) -> web.Response:
    """Return the bluetooth settings for a wireless device

    Return the bluetooth settings for a wireless device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_wireless_connection_stats(request: web.Request, serial, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
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


async def get_device_wireless_latency_stats(request: web.Request, serial, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
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


async def get_device_wireless_radio_settings(request: web.Request, serial) -> web.Response:
    """Return the radio settings of a device

    Return the radio settings of a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_wireless_status(request: web.Request, serial) -> web.Response:
    """Return the SSID statuses of an access point

    Return the SSID statuses of an access point

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_network_wireless_air_marshal(request: web.Request, network_id, t0=None, timespan=None) -> web.Response:
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


async def get_network_wireless_alternate_management_interface(request: web.Request, network_id) -> web.Response:
    """Return alternate management interface and devices with IP assigned

    Return alternate management interface and devices with IP assigned

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_billing(request: web.Request, network_id) -> web.Response:
    """Return the billing settings of this network

    Return the billing settings of this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_bluetooth_settings(request: web.Request, network_id) -> web.Response:
    """Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

    Return the Bluetooth settings for a network. &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt; must be enabled on the network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_channel_utilization_history(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None) -> web.Response:
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


async def get_network_wireless_client_connection_stats(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
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


async def get_network_wireless_client_connectivity_events(request: web.Request, network_id, client_id, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None, types=None, included_severities=None, band=None, ssid_number=None, device_serial=None) -> web.Response:
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


async def get_network_wireless_client_count_history(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
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


async def get_network_wireless_client_latency_history(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
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


async def get_network_wireless_client_latency_stats(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
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


async def get_network_wireless_clients_connection_stats(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
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


async def get_network_wireless_clients_latency_stats(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
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


async def get_network_wireless_connection_stats(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
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


async def get_network_wireless_data_rate_history(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
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


async def get_network_wireless_devices_connection_stats(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None) -> web.Response:
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


async def get_network_wireless_devices_latency_stats(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
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


async def get_network_wireless_failed_connections(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, serial=None, client_id=None) -> web.Response:
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


async def get_network_wireless_latency_history(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None, access_category=None) -> web.Response:
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


async def get_network_wireless_latency_stats(request: web.Request, network_id, t0=None, t1=None, timespan=None, band=None, ssid=None, vlan=None, ap_tag=None, fields=None) -> web.Response:
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


async def get_network_wireless_mesh_statuses(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_wireless_rf_profile(request: web.Request, network_id, rf_profile_id) -> web.Response:
    """Return a RF profile

    Return a RF profile

    :param network_id: 
    :type network_id: str
    :param rf_profile_id: 
    :type rf_profile_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_rf_profiles(request: web.Request, network_id, include_template_profiles=None) -> web.Response:
    """List the non-basic RF profiles for this network

    List the non-basic RF profiles for this network

    :param network_id: 
    :type network_id: str
    :param include_template_profiles: If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
    :type include_template_profiles: bool

    """
    return web.Response(status=200)


async def get_network_wireless_settings(request: web.Request, network_id) -> web.Response:
    """Return the wireless settings for a network

    Return the wireless settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_signal_quality_history(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
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


async def get_network_wireless_ssid(request: web.Request, network_id, number) -> web.Response:
    """Return a single MR SSID

    Return a single MR SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_bonjour_forwarding(request: web.Request, network_id, number) -> web.Response:
    """List the Bonjour forwarding setting and rules for the SSID

    List the Bonjour forwarding setting and rules for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_device_type_group_policies(request: web.Request, network_id, number) -> web.Response:
    """List the device type group policies for the SSID

    List the device type group policies for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_eap_override(request: web.Request, network_id, number) -> web.Response:
    """Return the EAP overridden parameters for an SSID

    Return the EAP overridden parameters for an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_firewall_l3_firewall_rules(request: web.Request, network_id, number) -> web.Response:
    """Return the L3 firewall rules for an SSID on an MR network

    Return the L3 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_firewall_l7_firewall_rules(request: web.Request, network_id, number) -> web.Response:
    """Return the L7 firewall rules for an SSID on an MR network

    Return the L7 firewall rules for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_hotspot20(request: web.Request, network_id, number) -> web.Response:
    """Return the Hotspot 2.0 settings for an SSID

    Return the Hotspot 2.0 settings for an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_identity_psk(request: web.Request, network_id, number, identity_psk_id) -> web.Response:
    """Return an Identity PSK

    Return an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_identity_psks(request: web.Request, network_id, number) -> web.Response:
    """List all Identity PSKs in a wireless network

    List all Identity PSKs in a wireless network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_schedules(request: web.Request, network_id, number) -> web.Response:
    """List the outage schedule for the SSID

    List the outage schedule for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_splash_settings(request: web.Request, network_id, number) -> web.Response:
    """Display the splash page settings for the given SSID

    Display the splash page settings for the given SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_traffic_shaping_rules(request: web.Request, network_id, number) -> web.Response:
    """Display the traffic shaping settings for a SSID on an MR network

    Display the traffic shaping settings for a SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_vpn(request: web.Request, network_id, number) -> web.Response:
    """List the VPN settings for the SSID.

    List the VPN settings for the SSID.

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssids(request: web.Request, network_id) -> web.Response:
    """List the MR SSIDs in a network

    List the MR SSIDs in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_usage_history(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, auto_resolution=None, client_id=None, device_serial=None, ap_tag=None, band=None, ssid=None) -> web.Response:
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


async def get_organization_wireless_devices_ethernet_statuses(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None) -> web.Response:
    """Endpoint to see power status for wireless devices

    Endpoint to see power status for wireless devices

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456
    :type network_ids: List[str]

    """
    return web.Response(status=200)


async def update_device_wireless_bluetooth_settings(request: web.Request, serial, body=None) -> web.Response:
    """Update the bluetooth settings for a wireless device

    Update the bluetooth settings for a wireless device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceWirelessBluetoothSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_device_wireless_radio_settings(request: web.Request, serial, body=None) -> web.Response:
    """Update the radio settings of a device

    Update the radio settings of a device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceWirelessRadioSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_alternate_management_interface(request: web.Request, network_id, body=None) -> web.Response:
    """Update alternate management interface and device static IP

    Update alternate management interface and device static IP

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessAlternateManagementInterfaceRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_billing(request: web.Request, network_id, body=None) -> web.Response:
    """Update the billing settings

    Update the billing settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessBillingRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_bluetooth_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update the Bluetooth settings for a network

    Update the Bluetooth settings for a network. See the docs page for &lt;a href&#x3D;\&quot;https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)\&quot;&gt;Bluetooth settings&lt;/a&gt;.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessBluetoothSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_rf_profile(request: web.Request, network_id, rf_profile_id, body=None) -> web.Response:
    """Updates specified RF profile for this network

    Updates specified RF profile for this network

    :param network_id: 
    :type network_id: str
    :param rf_profile_id: 
    :type rf_profile_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessRfProfileRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update the wireless settings for a network

    Update the wireless settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the attributes of an MR SSID

    Update the attributes of an MR SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_bonjour_forwarding(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the bonjour forwarding setting and rules for the SSID

    Update the bonjour forwarding setting and rules for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidBonjourForwardingRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_device_type_group_policies(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the device type group policies for the SSID

    Update the device type group policies for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_eap_override(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the EAP overridden parameters for an SSID.

    Update the EAP overridden parameters for an SSID.

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidEapOverrideRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_firewall_l3_firewall_rules(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the L3 firewall rules of an SSID on an MR network

    Update the L3 firewall rules of an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_firewall_l7_firewall_rules(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the L7 firewall rules of an SSID on an MR network

    Update the L7 firewall rules of an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_hotspot20(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the Hotspot 2.0 settings of an SSID

    Update the Hotspot 2.0 settings of an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidHotspot20Request.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_identity_psk(request: web.Request, network_id, number, identity_psk_id, body=None) -> web.Response:
    """Update an Identity PSK

    Update an Identity PSK

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param identity_psk_id: 
    :type identity_psk_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidIdentityPskRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_schedules(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the outage schedule for the SSID

    Update the outage schedule for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidSchedulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_splash_settings(request: web.Request, network_id, number, body=None) -> web.Response:
    """Modify the splash page settings for the given SSID

    Modify the splash page settings for the given SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidSplashSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_traffic_shaping_rules(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the traffic shaping settings for an SSID on an MR network

    Update the traffic shaping settings for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidTrafficShapingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_vpn(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the VPN settings for the SSID

    Update the VPN settings for the SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidVpnRequest.from_dict(body)
    return web.Response(status=200)
