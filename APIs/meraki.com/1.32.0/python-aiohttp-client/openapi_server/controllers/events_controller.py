from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_firmware_upgrades_staged_event_request import CreateNetworkFirmwareUpgradesStagedEventRequest
from openapi_server.models.get_network_events200_response import GetNetworkEvents200Response
from openapi_server.models.get_network_events_event_types200_response_inner import GetNetworkEventsEventTypes200ResponseInner
from openapi_server.models.get_network_firmware_upgrades_staged_events200_response import GetNetworkFirmwareUpgradesStagedEvents200Response
from openapi_server.models.rollbacks_network_firmware_upgrades_staged_events_request import RollbacksNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server.models.update_network_firmware_upgrades_staged_events_request import UpdateNetworkFirmwareUpgradesStagedEventsRequest
from openapi_server import util


async def create_network_firmware_upgrades_staged_event_3(request: web.Request, network_id, body) -> web.Response:
    """Create a Staged Upgrade Event for a network

    Create a Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkFirmwareUpgradesStagedEventRequest.from_dict(body)
    return web.Response(status=200)


async def defer_network_firmware_upgrades_staged_events_3(request: web.Request, network_id) -> web.Response:
    """Postpone by 1 week all pending staged upgrade stages for a network

    Postpone by 1 week all pending staged upgrade stages for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_client_security_events_3(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
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


async def get_network_appliance_security_events_2(request: web.Request, network_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
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


async def get_network_events_1(request: web.Request, network_id, product_type=None, included_event_types=None, excluded_event_types=None, device_mac=None, device_serial=None, device_name=None, client_ip=None, client_mac=None, client_name=None, sm_device_mac=None, sm_device_name=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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


async def get_network_events_event_types_1(request: web.Request, network_id) -> web.Response:
    """List the event type to human-readable description

    List the event type to human-readable description

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_firmware_upgrades_staged_events_3(request: web.Request, network_id) -> web.Response:
    """Get the Staged Upgrade Event from a network

    Get the Staged Upgrade Event from a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_appliance_security_events_2(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, sort_order=None) -> web.Response:
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


async def rollbacks_network_firmware_upgrades_staged_events_3(request: web.Request, network_id, body) -> web.Response:
    """Rollback a Staged Upgrade Event for a network

    Rollback a Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RollbacksNetworkFirmwareUpgradesStagedEventsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_firmware_upgrades_staged_events_3(request: web.Request, network_id, body) -> web.Response:
    """Update the Staged Upgrade Event for a network

    Update the Staged Upgrade Event for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkFirmwareUpgradesStagedEventsRequest.from_dict(body)
    return web.Response(status=200)
