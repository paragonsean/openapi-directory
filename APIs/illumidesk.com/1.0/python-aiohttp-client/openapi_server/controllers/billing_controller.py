from typing import List, Dict
from aiohttp import web

from openapi_server.models.card import Card
from openapi_server.models.card_data_post import CardDataPost
from openapi_server.models.card_data_putand_patch import CardDataPutandPatch
from openapi_server.models.card_error import CardError
from openapi_server.models.card_update_error import CardUpdateError
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_item import InvoiceItem
from openapi_server.models.not_found import NotFound
from openapi_server.models.plan import Plan
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_data import SubscriptionData
from openapi_server.models.subscription_error import SubscriptionError
from openapi_server import util


async def billing_cards_create(request: web.Request, namespace, card_data=None) -> web.Response:
    """Create new credit card

    

    :param namespace: User or team name.
    :type namespace: str
    :param card_data: 
    :type card_data: dict | bytes

    """
    card_data = CardDataPost.from_dict(card_data)
    return web.Response(status=200)


async def billing_cards_delete(request: web.Request, namespace, id) -> web.Response:
    """Delete a credit card

    

    :param namespace: User or team name.
    :type namespace: str
    :param id: Card unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def billing_cards_list(request: web.Request, namespace, limit=None, offset=None, ordering=None) -> web.Response:
    """Get credit cards

    

    :param namespace: User or team name.
    :type namespace: str
    :param limit: Set limit when retrieving credit or debit cards.
    :type limit: str
    :param offset: Set offset when retriving cards.
    :type offset: str
    :param ordering: Order when retrieving cards.
    :type ordering: str

    """
    return web.Response(status=200)


async def billing_cards_read(request: web.Request, namespace, id) -> web.Response:
    """Get credit card by id

    

    :param namespace: User or team name.
    :type namespace: str
    :param id: User unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def billing_cards_replace(request: web.Request, namespace, id, card_data=None) -> web.Response:
    """Replace a credit card

    

    :param namespace: User or team name.
    :type namespace: str
    :param id: 
    :type id: str
    :param card_data: 
    :type card_data: dict | bytes

    """
    card_data = CardDataPutandPatch.from_dict(card_data)
    return web.Response(status=200)


async def billing_cards_update(request: web.Request, namespace, id, card_data=None) -> web.Response:
    """Update a credit card

    

    :param namespace: User or team name.
    :type namespace: str
    :param id: Card unique identifier.
    :type id: str
    :param card_data: 
    :type card_data: dict | bytes

    """
    card_data = CardDataPutandPatch.from_dict(card_data)
    return web.Response(status=200)


async def billing_invoice_items_list(request: web.Request, namespace, invoice_id, limit=None, offset=None, ordering=None) -> web.Response:
    """Get invoice items for a given invoice.

    

    :param namespace: User or team name.
    :type namespace: str
    :param invoice_id: Invoice id, expressed as UUID.
    :type invoice_id: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str
    :param ordering: Ordering when getting items.
    :type ordering: str

    """
    return web.Response(status=200)


async def billing_invoice_items_read(request: web.Request, namespace, invoice_id, id) -> web.Response:
    """Get a specific InvoiceItem.

    

    :param namespace: User or team name.
    :type namespace: str
    :param invoice_id: Invoice id, expressed as UUID.
    :type invoice_id: str
    :param id: InvoiceItem id, expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def billing_invoices_list(request: web.Request, namespace, limit=None, offset=None, ordering=None) -> web.Response:
    """Get invoices

    

    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str
    :param ordering: Ordering when getting items.
    :type ordering: str

    """
    return web.Response(status=200)


async def billing_invoices_read(request: web.Request, namespace, id) -> web.Response:
    """Get an invoice

    

    :param namespace: User or team name.
    :type namespace: str
    :param id: Invoice unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def billing_plans_list(request: web.Request, namespace, limit=None, offset=None, ordering=None) -> web.Response:
    """Get billing plans

    

    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str
    :param ordering: Ordering when getting items.
    :type ordering: str

    """
    return web.Response(status=200)


async def billing_plans_read(request: web.Request, namespace, id) -> web.Response:
    """Get a billing plan

    

    :param namespace: User or team name.
    :type namespace: str
    :param id: Plan unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def billing_subscriptions_create(request: web.Request, namespace, subscription_data=None) -> web.Response:
    """Create a new subscription

    

    :param namespace: User or team name.
    :type namespace: str
    :param subscription_data: 
    :type subscription_data: dict | bytes

    """
    subscription_data = SubscriptionData.from_dict(subscription_data)
    return web.Response(status=200)


async def billing_subscriptions_delete(request: web.Request, namespace, id) -> web.Response:
    """Delete a subscription

    

    :param namespace: User or team name.
    :type namespace: str
    :param id: Subscription unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def billing_subscriptions_list(request: web.Request, namespace, limit=None, offset=None, ordering=None) -> web.Response:
    """Get active subscriptons

    

    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str
    :param ordering: Ordering when getting items.
    :type ordering: str

    """
    return web.Response(status=200)


async def billing_subscriptions_read(request: web.Request, namespace, id) -> web.Response:
    """Get a subscriptions

    

    :param namespace: User or team name.
    :type namespace: str
    :param id: Unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def teams_billing_invoice_items_list_0(request: web.Request, team, invoice_id, limit=None, offset=None, ordering=None) -> web.Response:
    """Get team invoice items for a given invoice.

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param invoice_id: Invoice id, expressed as UUID.
    :type invoice_id: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str
    :param ordering: Ordering when getting items.
    :type ordering: str

    """
    return web.Response(status=200)


async def teams_billing_invoice_items_read_0(request: web.Request, team, invoice_id, id) -> web.Response:
    """Get a specific team InvoiceItem.

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param invoice_id: Invoice id, expressed as UUID.
    :type invoice_id: str
    :param id: InvoiceItem id, expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def teams_billing_invoices_list_0(request: web.Request, team, limit=None, offset=None) -> web.Response:
    """Get team invoices

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str

    """
    return web.Response(status=200)


async def teams_billing_invoices_read_0(request: web.Request, team, id) -> web.Response:
    """Get an invoice

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param id: Invoice unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def teams_billing_subscriptions_create_0(request: web.Request, team, subscription_data=None) -> web.Response:
    """Create a new team subscription

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param subscription_data: 
    :type subscription_data: dict | bytes

    """
    subscription_data = SubscriptionData.from_dict(subscription_data)
    return web.Response(status=200)


async def teams_billing_subscriptions_delete_0(request: web.Request, team, id) -> web.Response:
    """Delete a subscription

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param id: Subscription unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def teams_billing_subscriptions_list_0(request: web.Request, team, limit=None, offset=None, ordering=None) -> web.Response:
    """Get active team subscriptons

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str
    :param ordering: Ordering when getting items.
    :type ordering: str

    """
    return web.Response(status=200)


async def teams_billing_subscriptions_read_0(request: web.Request, team, id) -> web.Response:
    """Get team subscriptions

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param id: Unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)
