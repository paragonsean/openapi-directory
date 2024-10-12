from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_transactions200_response import GetTransactions200Response
from openapi_server import util


async def get_transaction(request: web.Request, id, include_chargestation=None, include_evse=None, include_connector=None, include_driver=None, include_token=None, include_reservation=None, include_organization=None, include_rate=None) -> web.Response:
    """get_transaction

    Get a specific transaction

    :param id: The transaction id that needs to be fetched
    :type id: str
    :param include_chargestation: Populate chargestation
    :type include_chargestation: bool
    :param include_evse: Populate evse
    :type include_evse: bool
    :param include_connector: Populate connector
    :type include_connector: bool
    :param include_driver: Populate driver
    :type include_driver: bool
    :param include_token: Populate token
    :type include_token: bool
    :param include_reservation: Populate reservation
    :type include_reservation: bool
    :param include_organization: Populate organization
    :type include_organization: bool
    :param include_rate: Populate rate
    :type include_rate: bool

    """
    return web.Response(status=200)


async def get_transaction_cost(request: web.Request, id) -> web.Response:
    """get_transaction_cost

    Get a specific transaction&#39;s cost

    :param id: The transaction id that needs to be fetched
    :type id: str

    """
    return web.Response(status=200)


async def get_transactions(request: web.Request, status=None, paginate_limit=None, paginate_page=None, paginate_enabled=None, sort_by=None, sort_order=None, created_at_gte=None, created_at_lte=None, updated_at_gte=None, updated_at_lte=None, include_chargestation=None, include_evse=None, include_connector=None, include_driver=None, include_token=None, include_reservation=None, include_organization=None, include_rate=None) -> web.Response:
    """get_transactions

    Get a list of transactions

    :param status: Started to get only active transactions
    :type status: str
    :param paginate_limit: Number of results per page
    :type paginate_limit: int
    :param paginate_page: The queried page index
    :type paginate_page: str
    :param paginate_enabled: Enable pagination
    :type paginate_enabled: bool
    :param sort_by: Sort data by this key
    :type sort_by: str
    :param sort_order: asc to sort ascending (default is desc - descending)
    :type sort_order: str
    :param created_at_gte: Date as ISO String
    :type created_at_gte: str
    :param created_at_lte: Date as ISO String
    :type created_at_lte: str
    :param updated_at_gte: Date as ISO String
    :type updated_at_gte: str
    :param updated_at_lte: Date as ISO String
    :type updated_at_lte: str
    :param include_chargestation: Populate chargestation
    :type include_chargestation: bool
    :param include_evse: Populate evse
    :type include_evse: bool
    :param include_connector: Populate connector
    :type include_connector: bool
    :param include_driver: Populate driver
    :type include_driver: bool
    :param include_token: Populate token
    :type include_token: bool
    :param include_reservation: Populate reservation
    :type include_reservation: bool
    :param include_organization: Populate organization
    :type include_organization: bool
    :param include_rate: Populate rate
    :type include_rate: bool

    """
    created_at_gte = util.deserialize_datetime(created_at_gte)
    created_at_lte = util.deserialize_datetime(created_at_lte)
    updated_at_gte = util.deserialize_datetime(updated_at_gte)
    updated_at_lte = util.deserialize_datetime(updated_at_lte)
    return web.Response(status=200)
