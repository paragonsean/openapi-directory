from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.cancellation_policy import CancellationPolicy
from openapi_server.models.cancellation_request import CancellationRequest
from openapi_server.models.network_service_config import NetworkServiceConfig
from openapi_server.models.network_service_config_request import NetworkServiceConfigRequest
from openapi_server.models.network_service_config_update import NetworkServiceConfigUpdate
from openapi_server.models.network_service_config_update_partial import NetworkServiceConfigUpdatePartial
from openapi_server.models.network_service_configs_destroy400_response import NetworkServiceConfigsDestroy400Response
from openapi_server import util


async def network_service_config_cancellation_policy_read(request: web.Request, id, decommission_at=None) -> web.Response:
    """network_service_config_cancellation_policy_read

    The cancellation-policy can be queried to answer the questions:  If I cancel my subscription, *when will it be technically decommissioned*? If I cancel my subscription, *until what date will I be charged*?  When the query parameter &#x60;decommision_at&#x60; is not provided it will provide the first possible cancellation date and charge period if cancelled at above date.  The granularity of the date field is a day, the start and end of which are to be interpreted by the IXP (some may use UTC, some may use their local time zone).

    :param id: Get by id
    :type id: str
    :param decommission_at: By providing a date in the format &#x60;YYYY-MM-DD&#x60; you can query the policy what would happen if you request a decommissioning on this date.
    :type decommission_at: str

    """
    return web.Response(status=200)


async def network_service_configs_create(request: web.Request, body=None) -> web.Response:
    """network_service_configs_create

    Create a &#x60;network-service-config&#x60;.

    :param body: Polymorhic Network Service Config Request
    :type body: dict | bytes

    """
    body = NetworkServiceConfigRequest.from_dict(body)
    return web.Response(status=200)


async def network_service_configs_destroy(request: web.Request, id, body=None) -> web.Response:
    """network_service_configs_destroy

    Request decommissioning the network service configuration.  The network service config will assume the state &#x60;decommission_requested&#x60;. This will cascade to related resources like &#x60;network-feature-configs&#x60;.

    :param id: Get by id
    :type id: str
    :param body: Service Cancellation Request
    :type body: dict | bytes

    """
    body = CancellationRequest.from_dict(body)
    return web.Response(status=200)


async def network_service_configs_list(request: web.Request, id=None, state=None, state__is_not=None, managing_account=None, consuming_account=None, external_ref=None, type=None, inner_vlan=None, outer_vlan=None, capacity=None, network_service=None, connection=None, product_offering=None) -> web.Response:
    """network_service_configs_list

    Get all &#x60;network-service-config&#x60;s.

    :param id: Filter by id
    :type id: List[str]
    :param state: Filter by state
    :type state: str
    :param state__is_not: Filter by state__is_not
    :type state__is_not: str
    :param managing_account: Filter by managing_account
    :type managing_account: str
    :param consuming_account: Filter by consuming_account
    :type consuming_account: str
    :param external_ref: Filter by external_ref
    :type external_ref: str
    :param type: Filter by type
    :type type: str
    :param inner_vlan: Filter by inner_vlan
    :type inner_vlan: int
    :param outer_vlan: Filter by outer_vlan
    :type outer_vlan: int
    :param capacity: Filter by capacity
    :type capacity: int
    :param network_service: Filter by network_service
    :type network_service: str
    :param connection: Filter by connection
    :type connection: str
    :param product_offering: Filter by product_offering
    :type product_offering: str

    """
    return web.Response(status=200)


async def network_service_configs_partial_update(request: web.Request, id, body=None) -> web.Response:
    """network_service_configs_partial_update

    Update parts of an exisiting &#x60;network-service-config&#x60;.

    :param id: Get by id
    :type id: str
    :param body: Polymorphic Network Service Config
    :type body: dict | bytes

    """
    body = NetworkServiceConfigUpdatePartial.from_dict(body)
    return web.Response(status=200)


async def network_service_configs_read(request: web.Request, id) -> web.Response:
    """network_service_configs_read

    Get a &#x60;network-service-config&#x60;

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def network_service_configs_update(request: web.Request, id, body=None) -> web.Response:
    """network_service_configs_update

    Update an exisiting &#x60;network-service-config&#x60;

    :param id: Get by id
    :type id: str
    :param body: Polymorphic Network Service Config
    :type body: dict | bytes

    """
    body = NetworkServiceConfigUpdate.from_dict(body)
    return web.Response(status=200)
