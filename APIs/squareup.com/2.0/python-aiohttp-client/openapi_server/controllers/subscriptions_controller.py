from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_subscription_response import CancelSubscriptionResponse
from openapi_server.models.create_subscription_request import CreateSubscriptionRequest
from openapi_server.models.create_subscription_response import CreateSubscriptionResponse
from openapi_server.models.list_subscription_events_response import ListSubscriptionEventsResponse
from openapi_server.models.resume_subscription_response import ResumeSubscriptionResponse
from openapi_server.models.retrieve_subscription_response import RetrieveSubscriptionResponse
from openapi_server.models.search_subscriptions_request import SearchSubscriptionsRequest
from openapi_server.models.search_subscriptions_response import SearchSubscriptionsResponse
from openapi_server.models.update_subscription_request import UpdateSubscriptionRequest
from openapi_server.models.update_subscription_response import UpdateSubscriptionResponse
from openapi_server import util


async def cancel_subscription(request: web.Request, subscription_id) -> web.Response:
    """CancelSubscription

    Sets the &#x60;canceled_date&#x60; field to the end of the active billing period. After this date, the status changes from ACTIVE to CANCELED.

    :param subscription_id: The ID of the subscription to cancel.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def create_subscription(request: web.Request, body) -> web.Response:
    """CreateSubscription

    Creates a subscription for a customer to a subscription plan.  If you provide a card on file in the request, Square charges the card for the subscription. Otherwise, Square bills an invoice to the customer&#39;s email address. The subscription starts immediately, unless the request includes the optional &#x60;start_date&#x60;. Each individual subscription is associated with a particular location.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def list_subscription_events(request: web.Request, subscription_id, cursor=None, limit=None) -> web.Response:
    """ListSubscriptionEvents

    Lists all events for a specific subscription. In the current implementation, only &#x60;START_SUBSCRIPTION&#x60; and &#x60;STOP_SUBSCRIPTION&#x60; (when the subscription was canceled) events are returned.

    :param subscription_id: The ID of the subscription to retrieve the events for.
    :type subscription_id: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    :type cursor: str
    :param limit: The upper limit on the number of subscription events to return in the response.  Default: &#x60;200&#x60;
    :type limit: int

    """
    return web.Response(status=200)


async def resume_subscription(request: web.Request, subscription_id) -> web.Response:
    """ResumeSubscription

    Resumes a deactivated subscription.

    :param subscription_id: The ID of the subscription to resume.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def retrieve_subscription(request: web.Request, subscription_id) -> web.Response:
    """RetrieveSubscription

    Retrieves a subscription.

    :param subscription_id: The ID of the subscription to retrieve.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def search_subscriptions(request: web.Request, body) -> web.Response:
    """SearchSubscriptions

    Searches for subscriptions. Results are ordered chronologically by subscription creation date. If the request specifies more than one location ID, the endpoint orders the result by location ID, and then by creation date within each location. If no locations are given in the query, all locations are searched.  You can also optionally specify &#x60;customer_ids&#x60; to search by customer. If left unset, all customers associated with the specified locations are returned. If the request specifies customer IDs, the endpoint orders results first by location, within location by customer ID, and within customer by subscription creation date.  For more information, see [Retrieve subscriptions](https://developer.squareup.com/docs/subscriptions-api/overview#retrieve-subscriptions).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchSubscriptionsRequest.from_dict(body)
    return web.Response(status=200)


async def update_subscription(request: web.Request, subscription_id, body) -> web.Response:
    """UpdateSubscription

    Updates a subscription. You can set, modify, and clear the &#x60;subscription&#x60; field values.

    :param subscription_id: The ID for the subscription to update.
    :type subscription_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateSubscriptionRequest.from_dict(body)
    return web.Response(status=200)
