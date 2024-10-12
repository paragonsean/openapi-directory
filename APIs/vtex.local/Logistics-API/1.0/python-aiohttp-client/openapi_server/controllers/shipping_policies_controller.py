from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_body import RequestBody
from openapi_server.models.request_body1 import RequestBody1
from openapi_server import util


async def api_logistics_pvt_shipping_policies_get(request: web.Request, accept, content_type, page, per_page) -> web.Response:
    """List shipping policies

    This endpoint lists existing shipping policies from carriers in your store.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param page: Desired number of pages to retrieve information from your Shipping Policies.
    :type page: str
    :param per_page: Desired number of items per page, to retrieve information from your Shipping Policies.
    :type per_page: str

    """
    return web.Response(status=200)


async def api_logistics_pvt_shipping_policies_id_delete(request: web.Request, accept, content_type, id) -> web.Response:
    """Delete shipping policies by ID

    This endpoint deletes existing shipping policies from carriers in your store, searching by their IDs.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param id: ID of the shipping policy.
    :type id: str

    """
    return web.Response(status=200)


async def api_logistics_pvt_shipping_policies_id_get(request: web.Request, accept, content_type, id) -> web.Response:
    """Retrieve shipping policy by ID

    This endpoint lists existing [shipping policies](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140) from carriers in your store, searching by their IDs.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param id: ID of the shipping policy.
    :type id: str

    """
    return web.Response(status=200)


async def api_logistics_pvt_shipping_policies_id_put(request: web.Request, accept, content_type, id, body=None) -> web.Response:
    """Update shipping policy

    This endpoint updates information on existing Shipping Policies from carriers.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param id: Shipping policy&#39;s ID
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody1.from_dict(body)
    return web.Response(status=200)


async def api_logistics_pvt_shipping_policies_post(request: web.Request, accept, content_type, body=None) -> web.Response:
    """Create shipping policy

    This endpoint creates new shipping policies from carriers in your store.    &gt; Note that, while most of our API endpoints return time fields in UTC, this endpoint returns **Scheduled Delivery** related time fields adjusted to the configured time zone of the account.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody.from_dict(body)
    return web.Response(status=200)
