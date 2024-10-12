from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_clients200_response import GetNetworkClients200Response
from openapi_server.models.provision_network_clients_request import ProvisionNetworkClientsRequest
from openapi_server.models.update_network_client_policy_request import UpdateNetworkClientPolicyRequest
from openapi_server.models.update_network_client_splash_authorization_status_request import UpdateNetworkClientSplashAuthorizationStatusRequest
from openapi_server import util


async def get_device_clients(request: web.Request, serial, t0=None, timespan=None) -> web.Response:
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


async def get_network_client(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client associated with the given identifier

    Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_client_events(request: web.Request, network_id, client_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the events associated with this client

    Return the events associated with this client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_network_client_latency_history(request: web.Request, network_id, client_id, t0=None, t1=None, timespan=None, resolution=None) -> web.Response:
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


async def get_network_client_usage_history(request: web.Request, network_id, client_id) -> web.Response:
    """Return the client&#39;s daily usage history

    Return the client&#39;s daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

    :param network_id: 
    :type network_id: str
    :param client_id: 
    :type client_id: str

    """
    return web.Response(status=200)


async def get_network_clients(request: web.Request, network_id, t0=None, timespan=None, per_page=None, starting_after=None, ending_before=None) -> web.Response:
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
