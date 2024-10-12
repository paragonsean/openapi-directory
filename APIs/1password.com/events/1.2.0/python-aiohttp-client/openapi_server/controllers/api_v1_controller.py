from typing import List, Dict
from aiohttp import web

from openapi_server.models.audit_event_items import AuditEventItems
from openapi_server.models.error import Error
from openapi_server.models.item_usage_items import ItemUsageItems
from openapi_server.models.sign_in_attempt_items import SignInAttemptItems
from openapi_server import util


async def get_audit_events(request: web.Request, ) -> web.Response:
    """Retrieves audit events for actions performed by team members within a 1Password account

    This endpoint requires your JSON Web Token to have the *auditevents* feature.


    """
    return web.Response(status=200)


async def get_item_usages(request: web.Request, ) -> web.Response:
    """Retrieves events for each usage of an item stored in a shared vault within a 1Password account

    This endpoint requires your JSON Web Token to have the *itemusages* feature.


    """
    return web.Response(status=200)


async def get_sign_in_attempts(request: web.Request, ) -> web.Response:
    """Retrieves events for both successful and failed attempts to sign into a 1Password account

    This endpoint requires your JSON Web Token to have the *signinattempts* feature.


    """
    return web.Response(status=200)
