from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def flat_rates_delete_flat_rate(request: web.Request, guid) -> web.Response:
    """Delete a flat rate of a phase.

    Returns: No Content (204) if succeeded.

    :param guid: ID of flat rate.
    :type guid: str

    """
    return web.Response(status=200)


async def project_fees_delete_project_free(request: web.Request, guid) -> web.Response:
    """Deletes a project fee.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the project fee.
    :type guid: str

    """
    return web.Response(status=200)


async def project_recurring_fee_rules_delete_project_recurring_fee_rule(request: web.Request, guid) -> web.Response:
    """Deletes a projectRecurringFeeRule.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the project recurring fee rule.
    :type guid: str

    """
    return web.Response(status=200)
