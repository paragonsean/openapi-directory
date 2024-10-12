from typing import List, Dict
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.group_data import GroupData
from openapi_server.models.group_error import GroupError
from openapi_server.models.group_user import GroupUser
from openapi_server.models.group_user_error import GroupUserError
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_item import InvoiceItem
from openapi_server.models.not_found import NotFound
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_data import SubscriptionData
from openapi_server.models.subscription_error import SubscriptionError
from openapi_server.models.team import Team
from openapi_server.models.team_data import TeamData
from openapi_server.models.team_error import TeamError
from openapi_server import util


async def teams_billing_invoice_items_list(request: web.Request, team, invoice_id, limit=None, offset=None, ordering=None) -> web.Response:
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


async def teams_billing_invoice_items_read(request: web.Request, team, invoice_id, id) -> web.Response:
    """Get a specific team InvoiceItem.

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param invoice_id: Invoice id, expressed as UUID.
    :type invoice_id: str
    :param id: InvoiceItem id, expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def teams_billing_invoices_list(request: web.Request, team, limit=None, offset=None) -> web.Response:
    """Get team invoices

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param limit: Limit when getting items.
    :type limit: str
    :param offset: Offset when getting items.
    :type offset: str

    """
    return web.Response(status=200)


async def teams_billing_invoices_read(request: web.Request, team, id) -> web.Response:
    """Get an invoice

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param id: Invoice unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def teams_billing_subscriptions_create(request: web.Request, team, subscription_data=None) -> web.Response:
    """Create a new team subscription

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param subscription_data: 
    :type subscription_data: dict | bytes

    """
    subscription_data = SubscriptionData.from_dict(subscription_data)
    return web.Response(status=200)


async def teams_billing_subscriptions_delete(request: web.Request, team, id) -> web.Response:
    """Delete a subscription

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param id: Subscription unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def teams_billing_subscriptions_list(request: web.Request, team, limit=None, offset=None, ordering=None) -> web.Response:
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


async def teams_billing_subscriptions_read(request: web.Request, team, id) -> web.Response:
    """Get team subscriptions

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param id: Unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def teams_create(request: web.Request, team_data=None) -> web.Response:
    """Create a new team

    

    :param team_data: 
    :type team_data: dict | bytes

    """
    team_data = TeamData.from_dict(team_data)
    return web.Response(status=200)


async def teams_delete(request: web.Request, team) -> web.Response:
    """Delete a team

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str

    """
    return web.Response(status=200)


async def teams_groups_add_to_group(request: web.Request, team, group) -> web.Response:
    """Add user to group

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param group: Group unique identifier expressed as UUID or name.
    :type group: str

    """
    return web.Response(status=200)


async def teams_groups_delete(request: web.Request, team, group) -> web.Response:
    """Delete team group

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param group: Group unique identifier expressed as UUID or name.
    :type group: str

    """
    return web.Response(status=200)


async def teams_groups_list(request: web.Request, team, limit=None, offset=None) -> web.Response:
    """Get team groups

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param limit: Limit when getting data.
    :type limit: str
    :param offset: Offset when getting data.
    :type offset: str

    """
    return web.Response(status=200)


async def teams_groups_read(request: web.Request, team, group) -> web.Response:
    """Get team group

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param group: Group unique identifier expressed as UUID or name.
    :type group: str

    """
    return web.Response(status=200)


async def teams_groups_remove_from_group(request: web.Request, team, group) -> web.Response:
    """User removed from group

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param group: Group unique identifier expressed as UUID or name.
    :type group: str

    """
    return web.Response(status=200)


async def teams_groups_replace(request: web.Request, team, group, group_data=None) -> web.Response:
    """Patch team group

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param group: Group unique identifier expressed as UUID or name.
    :type group: str
    :param group_data: 
    :type group_data: dict | bytes

    """
    group_data = GroupData.from_dict(group_data)
    return web.Response(status=200)


async def teams_groups_update(request: web.Request, team, group, group_data=None) -> web.Response:
    """Patch team group

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param group: Group unique identifier expressed as UUID or name.
    :type group: str
    :param group_data: 
    :type group_data: dict | bytes

    """
    group_data = GroupData.from_dict(group_data)
    return web.Response(status=200)


async def teams_list(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get teams

    

    :param limit: Limit when getting data.
    :type limit: str
    :param offset: Offset when getting data.
    :type offset: str

    """
    return web.Response(status=200)


async def teams_read(request: web.Request, team) -> web.Response:
    """Get a team

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str

    """
    return web.Response(status=200)


async def teams_replace(request: web.Request, team, team_data=None) -> web.Response:
    """Replace a team

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param team_data: 
    :type team_data: dict | bytes

    """
    team_data = TeamData.from_dict(team_data)
    return web.Response(status=200)


async def teams_update(request: web.Request, team, team_data=None) -> web.Response:
    """Update a team

    

    :param team: Team unique identifier expressed as UUID or name.
    :type team: str
    :param team_data: 
    :type team_data: dict | bytes

    """
    team_data = TeamData.from_dict(team_data)
    return web.Response(status=200)
