from typing import List, Dict
from aiohttp import web

from openapi_server.models.disable_request import DisableRequest
from openapi_server.models.disable_result import DisableResult
from openapi_server.models.notify_shopper_request import NotifyShopperRequest
from openapi_server.models.notify_shopper_result import NotifyShopperResult
from openapi_server.models.recurring_details_request import RecurringDetailsRequest
from openapi_server.models.recurring_details_result import RecurringDetailsResult
from openapi_server.models.schedule_account_updater_request import ScheduleAccountUpdaterRequest
from openapi_server.models.schedule_account_updater_result import ScheduleAccountUpdaterResult
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def post_disable(request: web.Request, body=None) -> web.Response:
    """Disable stored payment details

    Disables stored payment details to stop charging a shopper with this particular recurring detail ID.  For more information, refer to [Disable stored details](https://docs.adyen.com/classic-integration/recurring-payments/disable-stored-details/).

    :param body: 
    :type body: dict | bytes

    """
    body = DisableRequest.from_dict(body)
    return web.Response(status=200)


async def post_list_recurring_details(request: web.Request, body=None) -> web.Response:
    """Get stored payment details

    Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for presentation to the shopper.  For more information, refer to [Retrieve stored details](https://docs.adyen.com/classic-integration/recurring-payments/retrieve-stored-details/).

    :param body: 
    :type body: dict | bytes

    """
    body = RecurringDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def post_notify_shopper(request: web.Request, body=None) -> web.Response:
    """Ask issuer to notify the shopper

    Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This endpoint is used only for local acquiring in India. For more information, refer to [Recurring card payments in India](https://docs.adyen.com/payment-methods/cards/cards-recurring-india).

    :param body: 
    :type body: dict | bytes

    """
    body = NotifyShopperRequest.from_dict(body)
    return web.Response(status=200)


async def post_schedule_account_updater(request: web.Request, body=None) -> web.Response:
    """Schedule running the Account Updater

    When making the API call, you can submit either the credit card information, or the recurring detail reference and the shopper reference: * If the card information is provided, all the sub-fields for &#x60;card&#x60; are mandatory. * If the recurring detail reference is provided, the fields for &#x60;shopperReference&#x60; and &#x60;selectedRecurringDetailReference&#x60; are mandatory.

    :param body: 
    :type body: dict | bytes

    """
    body = ScheduleAccountUpdaterRequest.from_dict(body)
    return web.Response(status=200)
