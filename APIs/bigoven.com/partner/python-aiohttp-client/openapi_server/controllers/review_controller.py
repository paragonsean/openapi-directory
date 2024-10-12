from typing import List, Dict
from aiohttp import web

from openapi_server.models.api2_controllers_web_api_review_controller_post_reply_req import API2ControllersWebAPIReviewControllerPostReplyReq
from openapi_server.models.api2_controllers_web_api_review_controller_review_request import API2ControllersWebAPIReviewControllerReviewRequest
from openapi_server.models.api2_controllers_web_api_review_controller_review_request_legacy import API2ControllersWebAPIReviewControllerReviewRequestLegacy
from openapi_server.models.big_oven_model_api_reply import BigOvenModelAPIReply
from openapi_server.models.big_oven_model_api_review import BigOvenModelAPIReview
from openapi_server import util


async def recipe_recipe_id_review_get(request: web.Request, recipe_id) -> web.Response:
    """Get *my* review for the recipe {recipeId}, where \&quot;me\&quot; is determined by standard authentication headers

    

    :param recipe_id: 
    :type recipe_id: int

    """
    return web.Response(status=200)


async def recipe_review_review_id_get(request: web.Request, review_id) -> web.Response:
    """Get a given review by string-style ID. This will return a payload with FeaturedReply, ReplyCount.              Recommended display is to list top-level reviews with one featured reply underneath.               Currently, the FeaturedReply is the most recent one for that rating.

    

    :param review_id: 
    :type review_id: str

    """
    return web.Response(status=200)


async def review_delete(request: web.Request, recipe_id, review_id) -> web.Response:
    """DEPRECATED! - Deletes a review by recipeId and reviewId. Please use recipe/review/{reviewId} instead.

    

    :param recipe_id: 
    :type recipe_id: int
    :param review_id: 
    :type review_id: int

    """
    return web.Response(status=200)


async def review_delete_reply(request: web.Request, reply_id) -> web.Response:
    """DELETE a reply to a given review. Authenticated user must be the one who originally posted the reply.

    

    :param reply_id: 
    :type reply_id: str

    """
    return web.Response(status=200)


async def review_get(request: web.Request, review_id, recipe_id) -> web.Response:
    """Get a given review - DEPRECATED. See recipe/review/{reviewId} for the current usage.              Beginning in January 2017, BigOven moded from an integer-based ID system to a GUID-style string-based ID system for reviews and replies.              We are also supporting more of a \&quot;Google Play\&quot; style model for Reviews and Replies. That is, there are top-level Reviews and then              an unlimited list of replies (which do not carry star ratings) underneath existing reviews. Also, a given user can only have one review               per recipe. Existing legacy endpoints will continue to work, but we strongly recommend you migrate to using the newer endpoints listed              which do NOT carry the \&quot;DEPRECATED\&quot; flag.

    

    :param review_id: int
    :type review_id: int
    :param recipe_id: int
    :type recipe_id: int

    """
    return web.Response(status=200)


async def review_get_replies(request: web.Request, review_id, pg=None, rpp=None) -> web.Response:
    """Get a paged list of replies for a given review.

    

    :param review_id: 
    :type review_id: str
    :param pg: the page (int), starting with 1
    :type pg: int
    :param rpp: results per page (int)
    :type rpp: int

    """
    return web.Response(status=200)


async def review_get_reviews(request: web.Request, recipe_id, pg=None, rpp=None) -> web.Response:
    """Get paged list of reviews for a recipe. Each review will have at most one FeaturedReply, as well as a ReplyCount.

    

    :param recipe_id: recipe id (int)
    :type recipe_id: int
    :param pg: the page (int), starting with 1
    :type pg: int
    :param rpp: results per page (int)
    :type rpp: int

    """
    return web.Response(status=200)


async def review_post(request: web.Request, recipe_id, body) -> web.Response:
    """Add a new review. Only one review can be provided per {userId, recipeId} pair. Otherwise your review will be updated.

    

    :param recipe_id: 
    :type recipe_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIReviewControllerReviewRequest.from_dict(body)
    return web.Response(status=200)


async def review_post_reply(request: web.Request, review_id, body) -> web.Response:
    """POST a reply to a given review. The date will be set by server. Note that replies no longer have star ratings, only top-level reviews do.

    

    :param review_id: 
    :type review_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIReviewControllerPostReplyReq.from_dict(body)
    return web.Response(status=200)


async def review_put(request: web.Request, review_id, body) -> web.Response:
    """Update a given top-level review.

    

    :param review_id: 
    :type review_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIReviewControllerReviewRequest.from_dict(body)
    return web.Response(status=200)


async def review_put_legacy(request: web.Request, review_id, recipe_id, body) -> web.Response:
    """HTTP PUT (update) a recipe review. DEPRECATED. Please see recipe/review/{reviewId} PUT for the new endpoint.              We are moving to a string-based primary key system, no longer integers, for reviews and replies.

    

    :param review_id: reviewId (int)
    :type review_id: int
    :param recipe_id: recipeId (int)
    :type recipe_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIReviewControllerReviewRequestLegacy.from_dict(body)
    return web.Response(status=200)


async def review_put_reply(request: web.Request, reply_id, body) -> web.Response:
    """Update (PUT) a reply to a given review. Authenticated user must be the original one that posted the reply.

    

    :param reply_id: 
    :type reply_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIReviewControllerPostReplyReq.from_dict(body)
    return web.Response(status=200)
