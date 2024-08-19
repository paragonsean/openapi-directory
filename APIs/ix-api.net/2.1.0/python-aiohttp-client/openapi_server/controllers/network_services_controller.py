from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.cancellation_policy import CancellationPolicy
from openapi_server.models.cancellation_request import CancellationRequest
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.network_service import NetworkService
from openapi_server.models.network_service_change_request import NetworkServiceChangeRequest
from openapi_server.models.network_service_configs_destroy400_response import NetworkServiceConfigsDestroy400Response
from openapi_server.models.network_service_request import NetworkServiceRequest
from openapi_server.models.network_service_request_partial import NetworkServiceRequestPartial
from openapi_server import util


async def network_service_cancellation_policy_read(request: web.Request, id, decommission_at=None) -> web.Response:
    """network_service_cancellation_policy_read

    The cancellation-policy can be queried to answer the questions:  If I cancel my service, *when will it be technically decommissioned*? If I cancel my service, *until what date will I be charged*?  When the query parameter &#x60;decommision_at&#x60; is not provided it will provide the first possible cancellation date and charge period if cancelled at above date.  The granularity of the date field is a day, the start and end of which are to be interpreted by the IXP (some may use UTC, some may use their local time zone).

    :param id: Get by id
    :type id: str
    :param decommission_at: By providing a date in the format &#x60;YYYY-MM-DD&#x60; you can query the policy what would happen if you request a decommissioning on this date.
    :type decommission_at: str

    """
    return web.Response(status=200)


async def network_service_change_request_create(request: web.Request, id, body=None) -> web.Response:
    """network_service_change_request_create

    Request a change to the network service.  A participant in a network service of type &#x60;p2p_vc&#x60; can issue a change request, expressing a desired change in the capacity. The change is accepted when all sides have configured the network service configs with the new bandwidth. These changes can sometimes require a change of the product offering. The product offering may only differ in regards to bandwidth.  The network service will change it&#39;s state from &#x60;production&#x60; into &#x60;production_change_pending&#x60;.  Only one change request may be issued at a time.

    :param id: Get by id
    :type id: str
    :param body: NetworkServiceChangeRequest
    :type body: dict | bytes

    """
    body = NetworkServiceChangeRequest.from_dict(body)
    return web.Response(status=200)


async def network_service_change_request_destroy(request: web.Request, id) -> web.Response:
    """network_service_change_request_destroy

    Retract or reject a change to the network service.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def network_service_change_request_read(request: web.Request, id) -> web.Response:
    """network_service_change_request_read

    Get the change request.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def network_services_create(request: web.Request, body=None) -> web.Response:
    """network_services_create

    Create a new network service

    :param body: Polymorphic Network Service Request
    :type body: dict | bytes

    """
    body = NetworkServiceRequest.from_dict(body)
    return web.Response(status=200)


async def network_services_destroy(request: web.Request, id, body=None) -> web.Response:
    """network_services_destroy

    Request decomissioning of the network service.  The network service will enter the state of &#x60;decommission_requested&#x60;. The request will cascade to related network service and feature configs.  An *optional request body* can be provided to request a specific service termination date.  If no date is given in the request body, it is assumed to be the earliest possible date.  Possible values for &#x60;decommission_at&#x60; can be queried through the &#x60;network_service_cancellation_policy_read&#x60; operation.  The response will contain the dates on which the changes will be effected.

    :param id: Get by id
    :type id: str
    :param body: Service Cancellation Request
    :type body: dict | bytes

    """
    body = CancellationRequest.from_dict(body)
    return web.Response(status=200)


async def network_services_list(request: web.Request, id=None, state=None, state__is_not=None, managing_account=None, consuming_account=None, external_ref=None, type=None, pop=None, product_offering=None) -> web.Response:
    """network_services_list

    List available &#x60;NetworkService&#x60;s.

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
    :param pop: Filter by pop
    :type pop: str
    :param product_offering: Filter by product_offering
    :type product_offering: str

    """
    return web.Response(status=200)


async def network_services_partial_update(request: web.Request, id, body=None) -> web.Response:
    """network_services_partial_update

    Partially update a network service

    :param id: Get by id
    :type id: str
    :param body: Polymorphic Network Service Request
    :type body: dict | bytes

    """
    body = NetworkServiceRequestPartial.from_dict(body)
    return web.Response(status=200)


async def network_services_read(request: web.Request, id) -> web.Response:
    """network_services_read

    Get a specific &#x60;network-service&#x60; by id.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def network_services_update(request: web.Request, id, body=None) -> web.Response:
    """network_services_update

    Update a network service

    :param id: Get by id
    :type id: str
    :param body: Polymorphic Network Service Request
    :type body: dict | bytes

    """
    body = NetworkServiceRequest.from_dict(body)
    return web.Response(status=200)
