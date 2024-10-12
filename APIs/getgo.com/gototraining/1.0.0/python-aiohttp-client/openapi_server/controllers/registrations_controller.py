from typing import List, Dict
from aiohttp import web

from openapi_server.models.registrant import Registrant
from openapi_server.models.registrant_created import RegistrantCreated
from openapi_server.models.registrant_req_create import RegistrantReqCreate
from openapi_server import util


async def cancel_registration(request: web.Request, authorization, organizer_key, training_key, registrant_key) -> web.Response:
    """Cancel Registration

    This call cancels a registration in a scheduled training for a specific registrant. If the registrant has paid for the training, a cancellation cannot be completed with this method; it must be completed on the external admin site. No notification is sent to the registrant or the organizer by default. The registrant can re-register if needed.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int
    :param registrant_key: The key of the registrant
    :type registrant_key: int

    """
    return web.Response(status=200)


async def get_registrant(request: web.Request, authorization, organizer_key, training_key, registrant_key) -> web.Response:
    """Get Registrant

    Retrieves details for specific registrant in a specific training. Registrants can be:&lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval)&lt;br&gt;APPROVED - registrant registered and is approved&lt;br&gt;DENIED - registrant registered and was not approved.&lt;br&gt;&lt;br&gt;IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int
    :param registrant_key: The key of the registrant
    :type registrant_key: int

    """
    return web.Response(status=200)


async def get_registrants(request: web.Request, authorization, organizer_key, training_key) -> web.Response:
    """Get Training Registrants

    Retrieves details on all registrants for a specific training. Registrants can be:&lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval)&lt;br&gt;APPROVED - registrant registered and is approved&lt;br&gt;DENIED - registrant registered and was not approved.&lt;br&gt;&lt;br&gt;IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int

    """
    return web.Response(status=200)


async def register_for_training(request: web.Request, authorization, organizer_key, training_key, body) -> web.Response:
    """Register for Training

    Registers one person, identified by a unique email address, for a training. Approval is automatic unless payment or approval is required. The response contains the Confirmation page URL and Join URL for the registrant. NOTE: If some registrants do not receive a confirmation email, the emails could be getting blocked by their email server due to spam filtering or a grey-listing setting.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the training organizer
    :type organizer_key: int
    :param training_key: The key of the training
    :type training_key: int
    :param body: The details of the registrant to create
    :type body: dict | bytes

    """
    body = RegistrantReqCreate.from_dict(body)
    return web.Response(status=200)
