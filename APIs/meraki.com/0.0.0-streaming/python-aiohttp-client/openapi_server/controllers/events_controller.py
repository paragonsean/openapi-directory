from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_events(request: web.Request, network_id, product_type=None, included_event_types=None, excluded_event_types=None, device_mac=None, device_serial=None, device_name=None, client_ip=None, client_mac=None, client_name=None, sm_device_mac=None, sm_device_name=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List the events for the network

    List the events for the network

    :param network_id: 
    :type network_id: str
    :param product_type: The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and environmental
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
