from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_gift_card_activity_request import CreateGiftCardActivityRequest
from openapi_server.models.create_gift_card_activity_response import CreateGiftCardActivityResponse
from openapi_server.models.list_gift_card_activities_response import ListGiftCardActivitiesResponse
from openapi_server import util


async def create_gift_card_activity(request: web.Request, body) -> web.Response:
    """CreateGiftCardActivity

    Creates a gift card activity. For more information, see  [GiftCardActivity](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#giftcardactivity) and  [Using activated gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#using-activated-gift-cards).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateGiftCardActivityRequest.from_dict(body)
    return web.Response(status=200)


async def list_gift_card_activities(request: web.Request, gift_card_id=None, type=None, location_id=None, begin_time=None, end_time=None, limit=None, cursor=None, sort_order=None) -> web.Response:
    """ListGiftCardActivities

    Lists gift card activities. By default, you get gift card activities for all gift cards in the seller&#39;s account. You can optionally specify query parameters to filter the list. For example, you can get a list of gift card activities for a gift card, for all gift cards in a specific region, or for activities within a time window.

    :param gift_card_id: If you provide a gift card ID, the endpoint returns activities that belong  to the specified gift card. Otherwise, the endpoint returns all gift card activities for  the seller.
    :type gift_card_id: str
    :param type: If you provide a type, the endpoint returns gift card activities of this type.  Otherwise, the endpoint returns all types of gift card activities.
    :type type: str
    :param location_id: If you provide a location ID, the endpoint returns gift card activities for that location.  Otherwise, the endpoint returns gift card activities for all locations.
    :type location_id: str
    :param begin_time: The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year.
    :type begin_time: str
    :param end_time: The timestamp for the end of the reporting period, in RFC 3339 format. Inclusive. Default: The current time.
    :type end_time: str
    :param limit: If you provide a limit value, the endpoint returns the specified number  of results (or less) per page. A maximum value is 100. The default value is 50.
    :type limit: int
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If you do not provide the cursor, the call returns the first page of the results.
    :type cursor: str
    :param sort_order: The order in which the endpoint returns the activities, based on &#x60;created_at&#x60;. - &#x60;ASC&#x60; - Oldest to newest. - &#x60;DESC&#x60; - Newest to oldest (default).
    :type sort_order: str

    """
    return web.Response(status=200)
