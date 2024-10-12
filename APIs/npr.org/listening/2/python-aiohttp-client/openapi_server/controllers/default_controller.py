from typing import List, Dict
from aiohttp import web

from openapi_server.models.aggregation_audio_item_list_document import AggregationAudioItemListDocument
from openapi_server.models.audio_item_list_document import AudioItemListDocument
from openapi_server.models.channels_document import ChannelsDocument
from openapi_server.models.error_document import ErrorDocument
from openapi_server.models.organization_category_audio_list_document import OrganizationCategoryAudioListDocument
from openapi_server.models.organization_overview_document import OrganizationOverviewDocument
from openapi_server.models.rating_data import RatingData
from openapi_server.models.search_list_document import SearchListDocument
from openapi_server import util


async def get_agg_recommendations(request: web.Request, agg_id, authorization, start_num=None) -> web.Response:
    """Get a set of recommendations for an aggregation independent of the user&#39;s listening history

    This endpoint provides a list of recent audio items associated with the aggregation along with metadata about the aggregation.

    :param agg_id: ID of an aggregation such as a program or podcast. If the specified ID is a program that publishes rundowns, the latest rundown will be returned.
    :type agg_id: int
    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param start_num: The result to start with. Allows paging through the episodes of a podcast or program, with the default, &#x60;startNum&#x3D;0&#x60;, being the most recent episode. Ignored for programs that publish a rundown.
    :type start_num: int

    """
    return web.Response(status=200)


async def get_channels(request: web.Request, authorization, explore_only=None) -> web.Response:
    """Get the list of available channels

    These channels allow the user to specify a focus for the content returned in the recommendations endpoint.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param explore_only: If set to &#x60;true&#x60;, this call will return only channels that should be shown in the client&#39;s &#x60;Explore&#x60; view
    :type explore_only: bool

    """
    return web.Response(status=200)


async def get_history(request: web.Request, authorization) -> web.Response:
    """Get recent ratings the logged-in user has submitted

    This endpoint provides the list of recently-rated audio recommendations that the logged-in user has consumed. Some rated recommendations are filtered, such as sponsorship and donation.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str

    """
    return web.Response(status=200)


async def get_organization_category(request: web.Request, org_id, category, authorization) -> web.Response:
    """Get a list of recommendations from a category of content from an organization

    This endpoint provides a list of recommendations from a category of content from  an organization.

    :param org_id: ID of an organization, such as an NPR One station
    :type org_id: int
    :param category: One of the three categories of content - newscast, story, or podcast
    :type category: str
    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str

    """
    return web.Response(status=200)


async def get_organization_overview(request: web.Request, org_id, authorization) -> web.Response:
    """Get a variety of details about an organization including various lists of recent audio items

    This endpoint provides a variety of details about an organization including various lists of recent audio items.

    :param org_id: ID of an organization, such as an NPR One station
    :type org_id: int
    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str

    """
    return web.Response(status=200)


async def get_promo(request: web.Request, authorization) -> web.Response:
    """Retrieve the most recent promo audio heard by the logged-in user

    Gets the most recently played promo for which the user has neither tapped through the promo or listened to the target story.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str

    """
    return web.Response(status=200)


async def get_recommendations(request: web.Request, authorization, x_advertising_id=None, channel=None, shared_media_id=None, notified_media_id=None) -> web.Response:
    """Get a list of media for the logged-in user from NPR&#39;s recommendation engine

    This endpoint returns a list of audio recommendations. It is designed to be used for an initial list of recommendations, and then &#x60;POST /v2/ratings?recommend&#x3D;true&#x60; should be used for subsequent requests for recommendations.  A fully-populated link to the ratings endpoint is returned with each individual recommendation and is located in the AudioItemDocument under the &#x60;links[&#39;recommendations&#39;]&#x60; object. The query parameters in this link should not be modified. Be sure to copy and send back the entire ratings object (RatingData), as new fields may be added to it in the future.  A 500 will be returned if there are no eligible remaining recommendations.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param x_advertising_id: A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example.
    :type x_advertising_id: str
    :param channel: Determines the focus of the recommendations returned. Channel &#x60;npr&#x60; is recommended for most use cases.
    :type channel: str
    :param shared_media_id: This media was shared directly with the user; if provided, the service will add this recommendation to the top of the list
    :type shared_media_id: str
    :param notified_media_id: The user received a push notification about this media; if provided, the service will add this recommendation to the top of the list
    :type notified_media_id: str

    """
    return web.Response(status=200)


async def get_search_recommendations(request: web.Request, authorization, search_terms) -> web.Response:
    """Get a list of recent audio and aggregation items associated with search terms

    In the schema shown below, SearchItemDocument is not an actual type of returned object; the object returned by a search will be either an AggregationAudioItemListDocument or an AudioItemDocument.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param search_terms: Search terms to search on; can include URL-encoded punctuation
    :type search_terms: str

    """
    return web.Response(status=200)


async def post_rating(request: web.Request, authorization, body, x_advertising_id=None, channel=None, recommend=None) -> web.Response:
    """Collect new ratings for media previously recommended to the logged-in user

    This endpoint is the main mechanism for providing feedback from the user to NPR about the recommendations that are obtained from &#x60;GET /listening/v2/recommendations&#x60;.  A fully-populated link to this endpoint is returned with each individual recommendation and is located in the AudioItemDocument under the &#x60;links[&#39;recommendations&#39;]&#x60; object. The query parameters in this link should not be modified. Be sure to copy and send back the entire ratings object (RatingData), as new fields may be added to it in the future.  This endpoint can return a blank JSON.doc or AudioItemDocument depending on the &#x60;recommend&#x3D;true|false&#x60; parameter. The &#x60;recommend&#x3D;true&#x60; flag allows this endpoint to both receive ratings and send back recommendations in the same call.

    :param authorization: Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token.
    :type authorization: str
    :param body: A list of RatingData objects which contains data about ratings such as the id of the content, the rating value, elapsed time and more.
    :type body: list | bytes
    :param x_advertising_id: A device-specific advertising identifier, if possible. Apple&#39;s IDFA is an example.
    :type x_advertising_id: str
    :param channel: Determines the focus of the recommendations returned. Channel &#x60;npr&#x60; is recommended for most use cases.
    :type channel: str
    :param recommend: If set to &#x60;false&#x60;, this call will return a blank document; otherwise it will return a new recommendation object
    :type recommend: bool

    """
    body = [RatingData.from_dict(d) for d in body]
    return web.Response(status=200)
