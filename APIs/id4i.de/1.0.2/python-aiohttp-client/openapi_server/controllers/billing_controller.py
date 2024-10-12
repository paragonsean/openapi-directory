from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.billing_position import BillingPosition
from openapi_server.models.service_costs import ServiceCosts
from openapi_server import util


async def get_positions_for_organization(request: web.Request, organization_id, from_date=None, to_date=None) -> web.Response:
    """Get billing positions for a given organization

    

    :param organization_id: The organization to compute the billing information for
    :type organization_id: str
    :param from_date: Billing start date
    :type from_date: str
    :param to_date: Billing end date
    :type to_date: str

    """
    from_date = util.deserialize_datetime(from_date)
    to_date = util.deserialize_datetime(to_date)
    return web.Response(status=200)


async def get_sum_for_organization(request: web.Request, organization_id, from_date=None, to_date=None) -> web.Response:
    """Get billing amount of services for a given organization

    

    :param organization_id: The organization to compute the billing information for
    :type organization_id: str
    :param from_date: Billing start date
    :type from_date: str
    :param to_date: Billing end date
    :type to_date: str

    """
    from_date = util.deserialize_datetime(from_date)
    to_date = util.deserialize_datetime(to_date)
    return web.Response(status=200)
