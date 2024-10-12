from typing import List, Dict
from aiohttp import web

from openapi_server.models.bind_network_request import BindNetworkRequest
from openapi_server.models.claim_network_devices_request import ClaimNetworkDevicesRequest
from openapi_server.models.combine_organization_networks200_response import CombineOrganizationNetworks200Response
from openapi_server.models.combine_organization_networks_request import CombineOrganizationNetworksRequest
from openapi_server.models.create_network_firmware_upgrades_rollback200_response import CreateNetworkFirmwareUpgradesRollback200Response
from openapi_server.models.create_network_firmware_upgrades_rollback_request import CreateNetworkFirmwareUpgradesRollbackRequest
from openapi_server.models.create_network_firmware_upgrades_staged_event_request import CreateNetworkFirmwareUpgradesStagedEventRequest
from openapi_server.models.create_network_firmware_upgrades_staged_group_request import CreateNetworkFirmwareUpgradesStagedGroupRequest
from openapi_server.models.create_network_floor_plan_request import CreateNetworkFloorPlanRequest
from openapi_server.models.create_network_group_policy_request import CreateNetworkGroupPolicyRequest
from openapi_server.models.create_network_meraki_auth_user_request import CreateNetworkMerakiAuthUserRequest
from openapi_server.models.create_network_mqtt_broker_request import CreateNetworkMqttBrokerRequest
from openapi_server.models.create_network_pii_request_request import CreateNetworkPiiRequestRequest
from openapi_server.models.create_network_webhooks_http_server_request import CreateNetworkWebhooksHttpServerRequest
from openapi_server.models.create_network_webhooks_payload_template_request import CreateNetworkWebhooksPayloadTemplateRequest
from openapi_server.models.create_network_webhooks_webhook_test201_response import CreateNetworkWebhooksWebhookTest201Response
from openapi_server.models.create_network_webhooks_webhook_test_request import CreateNetworkWebhooksWebhookTestRequest
from openapi_server.models.create_organization_network_request import CreateOrganizationNetworkRequest
from openapi_server.models.get_network200_response import GetNetwork200Response
from openapi_server.models.get_network_alerts_history200_response_inner import GetNetworkAlertsHistory200ResponseInner
from openapi_server.models.get_network_client200_response import GetNetworkClient200Response
from openapi_server.models.get_network_clients200_response import GetNetworkClients200Response
from openapi_server.models.get_network_events200_response import GetNetworkEvents200Response
from openapi_server.models.get_network_events_event_types200_response_inner import GetNetworkEventsEventTypes200ResponseInner
from openapi_server.models.get_network_firmware_upgrades200_response import GetNetworkFirmwareUpgrades200Response
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response import GetNetworkFirmwareUpgradesStagedEvents200Response
from openapi_server.models.get_network_firmware_upgrades_staged_groups200_response_inner import GetNetworkFirmwareUpgradesStagedGroups200ResponseInner
from openapi_server.models.get_network_firmware_upgrades_staged_stages200_response_inner import GetNetworkFirmwareUpgradesStagedStages200ResponseInner
from openapi_server.models.get_network_health_alerts200_response_inner import GetNetworkHealthAlerts200ResponseInner
from openapi_server.models.get_network_meraki_auth_users200_response_inner import GetNetworkMerakiAuthUsers200ResponseInner
from openapi_server.models.get_network_policies_by_client200_response_inner import GetNetworkPoliciesByClient200ResponseInner
from openapi_server.models.get_network_settings200_response import GetNetworkSettings200Response
from openapi_server.models.get_network_syslog_servers200_response import GetNetworkSyslogServers200Response
from openapi_server.models.get_network_webhooks_http_servers200_response_inner import GetNetworkWebhooksHttpServers200ResponseInner
from openapi_server.models.get_network_webhooks_payload_templates200_response_inner import GetNetworkWebhooksPayloadTemplates200ResponseInner
from openapi_server.models.provision_network_clients_request import ProvisionNetworkClientsRequest
from openapi_server.models.remove_network_devices_request import RemoveNetworkDevicesRequest
from openapi_server.models.rollbacks_network_firmware_upgrades_staged_events_request import RollbacksNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.split_network200_response import SplitNetwork200Response
from openapi_server.models.unbind_network_request import UnbindNetworkRequest
from openapi_server.models.update_network_alerts_settings_request import UpdateNetworkAlertsSettingsRequest
from openapi_server.models.update_network_client_policy_request import UpdateNetworkClientPolicyRequest
from openapi_server.models.update_network_client_splash_authorization_status_request import UpdateNetworkClientSplashAuthorizationStatusRequest
from openapi_server.models.update_network_firmware_upgrades_request import UpdateNetworkFirmwareUpgradesRequest
from openapi_server.models.update_network_firmware_upgrades_staged_events_request import UpdateNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.update_network_firmware_upgrades_staged_stages_request import UpdateNetworkFirmwareUpgradesStagedStagesRequest
from openapi_server.models.update_network_floor_plan_request import UpdateNetworkFloorPlanRequest
from openapi_server.models.update_network_group_policy_request import UpdateNetworkGroupPolicyRequest
from openapi_server.models.update_network_meraki_auth_user_request import UpdateNetworkMerakiAuthUserRequest
from openapi_server.models.update_network_mqtt_broker_request import UpdateNetworkMqttBrokerRequest
from openapi_server.models.update_network_netflow_request import UpdateNetworkNetflowRequest
from openapi_server.models.update_network_request import UpdateNetworkRequest
from openapi_server.models.update_network_settings_request import UpdateNetworkSettingsRequest
from openapi_server.models.update_network_snmp_request import UpdateNetworkSnmpRequest
from openapi_server.models.update_network_syslog_servers_request import UpdateNetworkSyslogServersRequest
from openapi_server.models.update_network_traffic_analysis_request import UpdateNetworkTrafficAnalysisRequest
from openapi_server.models.update_network_webhooks_http_server_request import UpdateNetworkWebhooksHttpServerRequest
from openapi_server.models.update_network_webhooks_payload_template_request import UpdateNetworkWebhooksPayloadTemplateRequest
from openapi_server.models.vmx_network_devices_claim_request import VmxNetworkDevicesClaimRequest
from openapi_server import util


async def bind_network(request: web.Request, network_id, body) -> web.Response:
    """Bind a network to a template.

    Bind a network to a template.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BindNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def claim_network_devices(request: web.Request, network_id, body) -> web.Response:
    """Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

    Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClaimNetworkDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def combine_organization_networks_1(request: web.Request, organization_id, body) -> web.Response:
    """Combine multiple networks into a single network

    Combine multiple networks into a single network

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CombineOrganizationNetworksRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_firmware_upgrades_rollback(request: web.Request, network_id, body) -> web.Response:
    """Rollback a Firmware Upgrade For A Network

    Rollback a Firmware Upgrade For A Network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesRollbackRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_firmware_upgrades_staged_event(request: web.Request, network_id, body) -> web.Response:
    """Create a Staged Upgrade Event for a network

    Create a Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedEventRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_firmware_upgrades_staged_group(request: web.Request, network_id, body) -> web.Response:
    """Create a Staged Upgrade Group for a network

    Create a Staged Upgrade Group for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_floor_plan(request: web.Request, network_id, body) -> web.Response:
    """Upload a floor plan

    Upload a floor plan

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFloorPlanRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_group_policy(request: web.Request, network_id, body) -> web.Response:
    """Create a group policy

    Create a group policy

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkGroupPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_meraki_auth_user(request: web.Request, network_id, body) -> web.Response:
    """Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)

    Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkMerakiAuthUserRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_mqtt_broker(request: web.Request, network_id, body) -> web.Response:
    """Add an MQTT broker

    Add an MQTT broker

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkMqttBrokerRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_pii_request(request: web.Request, network_id, body=None) -> web.Response:
    """Submit a new delete or restrict processing PII request

    Submit a new delete or restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkPiiRequestRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_webhooks_http_server(request: web.Request, network_id, body) -> web.Response:
    """Add an HTTP server to a network

    Add an HTTP server to a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksHttpServerRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_webhooks_payload_template(request: web.Request, network_id, body) -> web.Response:
    """Create a webhook payload template for a network

    Create a webhook payload template for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksPayloadTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_webhooks_webhook_test(request: web.Request, network_id, body) -> web.Response:
    """Send a test webhook for a network

    Send a test webhook for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksWebhookTestRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_network_1(request: web.Request, organization_id, body) -> web.Response:
    """Create a network

    Create a network

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def defer_network_firmware_upgrades_staged_events(request: web.Request, network_id) -> web.Response:
    """Postpone by 1 week all pending staged upgrade stages for a network

    Postpone by 1 week all pending staged upgrade stages for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def delete_network(request: web.Request, network_id) -> web.Response:
    """Delete a network

    Delete a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def delete_network_firmware_upgrades_staged_group(request: web.Request, network_id, group_id) -> web.Response:
    """Delete a Staged Upgrade Group

    Delete a Staged Upgrade Group

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def delete_network_floor_plan(request: web.Request, network_id, floor_plan_id) -> web.Response:
    """Destroy a floor plan

    Destroy a floor plan

    :param network_id: 
    :type network_id: str
    :param floor_plan_id: 
    :type floor_plan_id: str

    """
    return web.Response(status=200)


async def delete_network_group_policy(request: web.Request, network_id, group_policy_id) -> web.Response:
    """Delete a group policy

    Delete a group policy

    :param network_id: 
    :type network_id: str
    :param group_policy_id: 
    :type group_policy_id: str

    """
    return web.Response(status=200)


async def delete_network_meraki_auth_user(request: web.Request, network_id, meraki_auth_user_id) -> web.Response:
    """Deauthorize a user

    Deauthorize a user. To reauthorize a user after deauthorizing them, POST to this endpoint. (Currently, 802.1X RADIUS, splash guest, and client VPN users can be deauthorized.)

    :param network_id: 
    :type network_id: str
    :param meraki_auth_user_id: 
    :type meraki_auth_user_id: str

    """
    return web.Response(status=200)


async def delete_network_mqtt_broker(request: web.Request, network_id, mqtt_broker_id) -> web.Response:
    """Delete an MQTT broker

    Delete an MQTT broker

    :param network_id: 
    :type network_id: str
    :param mqtt_broker_id: 
    :type mqtt_broker_id: str

    """
    return web.Response(status=200)


async def delete_network_pii_request(request: web.Request, network_id, request_id) -> web.Response:
    """Delete a restrict processing PII request

    Delete a restrict processing PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param request_id: 
    :type request_id: str

    """
    return web.Response(status=200)


async def delete_network_webhooks_http_server(request: web.Request, network_id, http_server_id) -> web.Response:
    """Delete an HTTP server from a network

    Delete an HTTP server from a network

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str

    """
    return web.Response(status=200)


async def delete_network_webhooks_payload_template(request: web.Request, network_id, payload_template_id) -> web.Response:
    """Destroy a webhook payload template for a network

    Destroy a webhook payload template for a network. Does not work for included templates (&#39;wpt_00001&#39;, &#39;wpt_00002&#39;, &#39;wpt_00003&#39;, &#39;wpt_00004&#39;, &#39;wpt_00005&#39; or &#39;wpt_00006&#39;)

    :param network_id: 
    :type network_id: str
    :param payload_template_id: 
    :type payload_template_id: str

    """
    return web.Response(status=200)


async def get_network(request: web.Request, network_id) -> web.Response:
    """Return a network

    Return a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_alerts_history(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_alerts_settings(request: web.Request, network_id) -> web.Response:
    """Return the alert configuration for this network

    Return the alert configuration for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_bluetooth_client(request: web.Request, network_id, bluetooth_client_id, include_connectivity_history=None, connectivity_history_timespan=None) -> web.Response:
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


async def get_network_bluetooth_clients(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None, include_connectivity_history=None) -> web.Response:
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


async def get_network_client(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client associated with the given identifier

    Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_client_policy(request: web.Request, network_id, client_id) -> web.Response:
    """Return the policy assigned to a client on the network

    Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_client_splash_authorization_status(request: web.Request, network_id, client_id) -> web.Response:
    """Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash

    Return the splash authorization for a client, for each SSID they&#39;ve associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_client_traffic_history(request: web.Request, network_id, client_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_client_usage_history(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client&#39;s daily usage history

    Return the client&#39;s daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_clients(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None, statuses=None, ip=None, ip6=None, ip6_local=None, mac=None, os=None, description=None, vlan=None, recent_device_connections=None) -> web.Response:
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


async def get_network_clients_application_usage(request: web.Request, network_id, clients, ssid_number=None, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None) -> web.Response:
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


async def get_network_clients_bandwidth_usage_history(request: web.Request, network_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_clients_overview(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
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


async def get_network_clients_usage_histories(request: web.Request, network_id, clients, ssid_number=None, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None) -> web.Response:
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


async def get_network_devices(request: web.Request, network_id) -> web.Response:
    """List the devices in a network

    List the devices in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_events(request: web.Request, network_id, product_type=None, included_event_types=None, excluded_event_types=None, device_mac=None, device_serial=None, device_name=None, client_ip=None, client_mac=None, client_name=None, sm_device_mac=None, sm_device_name=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_events_event_types(request: web.Request, network_id) -> web.Response:
    """List the event type to human-readable description

    List the event type to human-readable description

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades(request: web.Request, network_id) -> web.Response:
    """Get firmware upgrade information for a network

    Get firmware upgrade information for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_events(request: web.Request, network_id) -> web.Response:
    """Get the Staged Upgrade Event from a network

    Get the Staged Upgrade Event from a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_group(request: web.Request, network_id, group_id) -> web.Response:
    """Get a Staged Upgrade Group from a network

    Get a Staged Upgrade Group from a network

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_groups(request: web.Request, network_id) -> web.Response:
    """List of Staged Upgrade Groups in a network

    List of Staged Upgrade Groups in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_stages(request: web.Request, network_id) -> web.Response:
    """Order of Staged Upgrade Groups in a network

    Order of Staged Upgrade Groups in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_floor_plan(request: web.Request, network_id, floor_plan_id) -> web.Response:
    """Find a floor plan by ID

    Find a floor plan by ID

    :param network_id: 
    :type network_id: str
    :param floor_plan_id: 
    :type floor_plan_id: str

    """
    return web.Response(status=200)


async def get_network_floor_plans(request: web.Request, network_id) -> web.Response:
    """List the floor plans that belong to your network

    List the floor plans that belong to your network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_group_policies(request: web.Request, network_id) -> web.Response:
    """List the group policies in a network

    List the group policies in a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_group_policy(request: web.Request, network_id, group_policy_id) -> web.Response:
    """Display a group policy

    Display a group policy

    :param network_id: 
    :type network_id: str
    :param group_policy_id: 
    :type group_policy_id: str

    """
    return web.Response(status=200)


async def get_network_health_alerts(request: web.Request, network_id) -> web.Response:
    """Return all global alerts on this network

    Return all global alerts on this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_meraki_auth_user(request: web.Request, network_id, meraki_auth_user_id) -> web.Response:
    """Return the Meraki Auth splash guest, RADIUS, or client VPN user

    Return the Meraki Auth splash guest, RADIUS, or client VPN user

    :param network_id: 
    :type network_id: str
    :param meraki_auth_user_id: 
    :type meraki_auth_user_id: str

    """
    return web.Response(status=200)


async def get_network_meraki_auth_users(request: web.Request, network_id) -> web.Response:
    """List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)

    List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_mqtt_broker(request: web.Request, network_id, mqtt_broker_id) -> web.Response:
    """Return an MQTT broker

    Return an MQTT broker

    :param network_id: 
    :type network_id: str
    :param mqtt_broker_id: 
    :type mqtt_broker_id: str

    """
    return web.Response(status=200)


async def get_network_mqtt_brokers(request: web.Request, network_id) -> web.Response:
    """List the MQTT brokers for this network

    List the MQTT brokers for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_netflow(request: web.Request, network_id) -> web.Response:
    """Return the NetFlow traffic reporting settings for a network

    Return the NetFlow traffic reporting settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_network_health_channel_utilization(request: web.Request, network_id, t0=None, t1=None, timespan=None, resolution=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_pii_pii_keys(request: web.Request, network_id, username=None, email=None, mac=None, serial=None, imei=None, bluetooth_mac=None) -> web.Response:
    """List the keys required to access Personally Identifiable Information (PII) for a given identifier

    List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key \&quot;0\&quot; containing the applicable keys.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/piiKeys &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param username: The username of a Systems Manager user
    :type username: str
    :param email: The email of a network user account or a Systems Manager device
    :type email: str
    :param mac: The MAC of a network client device or a Systems Manager device
    :type mac: str
    :param serial: The serial of a Systems Manager device
    :type serial: str
    :param imei: The IMEI of a Systems Manager device
    :type imei: str
    :param bluetooth_mac: The MAC of a Bluetooth client
    :type bluetooth_mac: str

    """
    return web.Response(status=200)


async def get_network_pii_request(request: web.Request, network_id, request_id) -> web.Response:
    """Return a PII request

    Return a PII request  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests/{requestId} &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param request_id: 
    :type request_id: str

    """
    return web.Response(status=200)


async def get_network_pii_requests(request: web.Request, network_id) -> web.Response:
    """List the PII requests for this network or organization

    List the PII requests for this network or organization  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/requests &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_pii_sm_devices_for_key(request: web.Request, network_id, username=None, email=None, mac=None, serial=None, imei=None, bluetooth_mac=None) -> web.Response:
    """Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smDevicesForKey &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param username: The username of a Systems Manager user
    :type username: str
    :param email: The email of a network user account or a Systems Manager device
    :type email: str
    :param mac: The MAC of a network client device or a Systems Manager device
    :type mac: str
    :param serial: The serial of a Systems Manager device
    :type serial: str
    :param imei: The IMEI of a Systems Manager device
    :type imei: str
    :param bluetooth_mac: The MAC of a Bluetooth client
    :type bluetooth_mac: str

    """
    return web.Response(status=200)


async def get_network_pii_sm_owners_for_key(request: web.Request, network_id, username=None, email=None, mac=None, serial=None, imei=None, bluetooth_mac=None) -> web.Response:
    """Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  &#x60;&#x60;&#x60; /organizations/{organizationId}/pii/smOwnersForKey &#x60;&#x60;&#x60;

    :param network_id: 
    :type network_id: str
    :param username: The username of a Systems Manager user
    :type username: str
    :param email: The email of a network user account or a Systems Manager device
    :type email: str
    :param mac: The MAC of a network client device or a Systems Manager device
    :type mac: str
    :param serial: The serial of a Systems Manager device
    :type serial: str
    :param imei: The IMEI of a Systems Manager device
    :type imei: str
    :param bluetooth_mac: The MAC of a Bluetooth client
    :type bluetooth_mac: str

    """
    return web.Response(status=200)


async def get_network_policies_by_client(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None, t0=None, timespan=None) -> web.Response:
    """Get policies for all clients with policies

    Get policies for all clients with policies

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_network_settings(request: web.Request, network_id) -> web.Response:
    """Return the settings for a network

    Return the settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_snmp(request: web.Request, network_id) -> web.Response:
    """Return the SNMP settings for a network

    Return the SNMP settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_splash_login_attempts(request: web.Request, network_id, ssid_number=None, login_identifier=None, timespan=None) -> web.Response:
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


async def get_network_syslog_servers(request: web.Request, network_id) -> web.Response:
    """List the syslog servers for a network

    List the syslog servers for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_topology_link_layer(request: web.Request, network_id) -> web.Response:
    """List the LLDP and CDP information for all discovered devices and connections in a network.

    List the LLDP and CDP information for all discovered devices and connections in a network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_traffic(request: web.Request, network_id, t0=None, timespan=None, device_type=None) -> web.Response:
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


async def get_network_traffic_analysis(request: web.Request, network_id) -> web.Response:
    """Return the traffic analysis settings for a network

    Return the traffic analysis settings for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_traffic_shaping_application_categories(request: web.Request, network_id) -> web.Response:
    """Returns the application categories for traffic shaping rules.

    Returns the application categories for traffic shaping rules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_traffic_shaping_dscp_tagging_options(request: web.Request, network_id) -> web.Response:
    """Returns the available DSCP tagging options for your traffic shaping rules.

    Returns the available DSCP tagging options for your traffic shaping rules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_http_server(request: web.Request, network_id, http_server_id) -> web.Response:
    """Return an HTTP server for a network

    Return an HTTP server for a network

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_http_servers(request: web.Request, network_id) -> web.Response:
    """List the HTTP servers for a network

    List the HTTP servers for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_payload_template(request: web.Request, network_id, payload_template_id) -> web.Response:
    """Get the webhook payload template for a network

    Get the webhook payload template for a network

    :param network_id: 
    :type network_id: str
    :param payload_template_id: 
    :type payload_template_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_payload_templates(request: web.Request, network_id) -> web.Response:
    """List the webhook payload templates for a network

    List the webhook payload templates for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_webhook_test(request: web.Request, network_id, webhook_test_id) -> web.Response:
    """Return the status of a webhook test for a network

    Return the status of a webhook test for a network

    :param network_id: 
    :type network_id: str
    :param webhook_test_id: 
    :type webhook_test_id: str

    """
    return web.Response(status=200)


async def get_organization_inventory_onboarding_cloud_monitoring_networks_4(request: web.Request, organization_id, device_type, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Returns list of networks eligible for adding cloud monitored device

    Returns list of networks eligible for adding cloud monitored device

    :param organization_id: 
    :type organization_id: str
    :param device_type: Device Type switch or wireless controller
    :type device_type: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_networks_1(request: web.Request, organization_id, config_template_id=None, is_bound_to_config_template=None, tags=None, tags_filter_type=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List the networks that the user has privileges on in an organization

    List the networks that the user has privileges on in an organization

    :param organization_id: 
    :type organization_id: str
    :param config_template_id: An optional parameter that is the ID of a config template. Will return all networks bound to that template.
    :type config_template_id: str
    :param is_bound_to_config_template: An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false.
    :type is_bound_to_config_template: bool
    :param tags: An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below).
    :type tags: List[str]
    :param tags_filter_type: An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected.
    :type tags_filter_type: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def provision_network_clients(request: web.Request, network_id, body) -> web.Response:
    """Provisions a client with a name and policy

    Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProvisionNetworkClientsRequest.from_dict(body)
    return web.Response(status=200)


async def remove_network_devices(request: web.Request, network_id, body) -> web.Response:
    """Remove a single device

    Remove a single device

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveNetworkDevicesRequest.from_dict(body)
    return web.Response(status=200)


async def rollbacks_network_firmware_upgrades_staged_events(request: web.Request, network_id, body) -> web.Response:
    """Rollback a Staged Upgrade Event for a network

    Rollback a Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RollbacksNetworkFirmwareUpgradesStagedEventsRequest.from_dict(body)
    return web.Response(status=200)


async def split_network(request: web.Request, network_id) -> web.Response:
    """Split a combined network into individual networks for each type of device

    Split a combined network into individual networks for each type of device

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def unbind_network(request: web.Request, network_id, body=None) -> web.Response:
    """Unbind a network from a template.

    Unbind a network from a template.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UnbindNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def update_network(request: web.Request, network_id, body=None) -> web.Response:
    """Update a network

    Update a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_alerts_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update the alert configuration for this network

    Update the alert configuration for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAlertsSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_client_policy(request: web.Request, network_id, client_id, body) -> web.Response:
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


async def update_network_client_splash_authorization_status(request: web.Request, network_id, client_id, body) -> web.Response:
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


async def update_network_firmware_upgrades(request: web.Request, network_id, body=None) -> web.Response:
    """Update firmware upgrade information for a network

    Update firmware upgrade information for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFirmwareUpgradesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_firmware_upgrades_staged_events(request: web.Request, network_id, body) -> web.Response:
    """Update the Staged Upgrade Event for a network

    Update the Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFirmwareUpgradesStagedEventsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_firmware_upgrades_staged_group(request: web.Request, network_id, group_id, body) -> web.Response:
    """Update a Staged Upgrade Group for a network

    Update a Staged Upgrade Group for a network

    :param network_id: 
    :type network_id: str
    :param group_id: 
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_firmware_upgrades_staged_stages(request: web.Request, network_id, body=None) -> web.Response:
    """Assign Staged Upgrade Group order in the sequence.

    Assign Staged Upgrade Group order in the sequence.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFirmwareUpgradesStagedStagesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_floor_plan(request: web.Request, network_id, floor_plan_id, body=None) -> web.Response:
    """Update a floor plan&#39;s geolocation and other meta data

    Update a floor plan&#39;s geolocation and other meta data

    :param network_id: 
    :type network_id: str
    :param floor_plan_id: 
    :type floor_plan_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFloorPlanRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_group_policy(request: web.Request, network_id, group_policy_id, body=None) -> web.Response:
    """Update a group policy

    Update a group policy

    :param network_id: 
    :type network_id: str
    :param group_policy_id: 
    :type group_policy_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkGroupPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_meraki_auth_user(request: web.Request, network_id, meraki_auth_user_id, body=None) -> web.Response:
    """Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)

    Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)

    :param network_id: 
    :type network_id: str
    :param meraki_auth_user_id: 
    :type meraki_auth_user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkMerakiAuthUserRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_mqtt_broker(request: web.Request, network_id, mqtt_broker_id, body=None) -> web.Response:
    """Update an MQTT broker

    Update an MQTT broker

    :param network_id: 
    :type network_id: str
    :param mqtt_broker_id: 
    :type mqtt_broker_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkMqttBrokerRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_netflow(request: web.Request, network_id, body=None) -> web.Response:
    """Update the NetFlow traffic reporting settings for a network

    Update the NetFlow traffic reporting settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkNetflowRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update the settings for a network

    Update the settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_snmp(request: web.Request, network_id, body=None) -> web.Response:
    """Update the SNMP settings for a network

    Update the SNMP settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSnmpRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_syslog_servers(request: web.Request, network_id, body) -> web.Response:
    """Update the syslog servers for a network

    Update the syslog servers for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSyslogServersRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_traffic_analysis(request: web.Request, network_id, body=None) -> web.Response:
    """Update the traffic analysis settings for a network

    Update the traffic analysis settings for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkTrafficAnalysisRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_webhooks_http_server(request: web.Request, network_id, http_server_id, body=None) -> web.Response:
    """Update an HTTP server

    Update an HTTP server. To change a URL, create a new HTTP server.

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWebhooksHttpServerRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_webhooks_payload_template(request: web.Request, network_id, payload_template_id, body=None) -> web.Response:
    """Update a webhook payload template for a network

    Update a webhook payload template for a network

    :param network_id: 
    :type network_id: str
    :param payload_template_id: 
    :type payload_template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWebhooksPayloadTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def vmx_network_devices_claim(request: web.Request, network_id, body) -> web.Response:
    """Claim a vMX into a network

    Claim a vMX into a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = VmxNetworkDevicesClaimRequest.from_dict(body)
    return web.Response(status=200)
