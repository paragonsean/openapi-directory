from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_review_request import EditReviewRequest
from openapi_server.models.get_reviewby_review_id200_response import GetReviewbyReviewId200Response
from openapi_server.models.getalistof_reviews200_response import GetalistofReviews200Response
from openapi_server.models.save_multiple_reviews_request import SaveMultipleReviewsRequest
from openapi_server.models.save_review200_response import SaveReview200Response
from openapi_server.models.save_review_request import SaveReviewRequest
from openapi_server import util


async def delete_multiple_reviews(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Delete Multiple Reviews

    Deletes multiple reviews at once.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)


async def delete_review(request: web.Request, review_id, content_type, accept) -> web.Response:
    """Delete Review

    Deletes an existing review.

    :param review_id: Review ID.
    :type review_id: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def edit_review(request: web.Request, review_id, content_type, accept, body) -> web.Response:
    """Update a Review

    Updates the information of a review.

    :param review_id: Review ID.
    :type review_id: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditReviewRequest.from_dict(body)
    return web.Response(status=200)


async def get_reviewby_review_id(request: web.Request, review_id, content_type, accept) -> web.Response:
    """Get Review by Review ID

    Retrieves information of a product review by its ID.

    :param review_id: Review ID.
    :type review_id: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def getalistof_reviews(request: web.Request, search_term, _from, to, order_by, status, product_id, content_type, accept) -> web.Response:
    """Get a list of Reviews

    Retrieves a list of reviews.

    :param search_term: Returns Reviews that contain the search term in &#x60;productId&#x60;, &#x60;sku&#x60;, &#x60;shopperId&#x60;, or &#x60;reviewerName&#x60;.
    :type search_term: str
    :param _from: Zero base starting record number, &#x60;0&#x60; is the default value.
    :type _from: str
    :param to: Zero base ending record number, &#x60;3&#x60; is the default value.
    :type to: str
    :param order_by: Case-sensitive fieldName to order records (optionally add &#x60;:asc&#x60; or &#x60;:desc&#x60;).
    :type order_by: str
    :param status: Status of the review, approved (&#x60;true&#x60;) or not (&#x60;false&#x60;).
    :type status: bool
    :param product_id: Filter the reviews by product ID.
    :type product_id: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def save_multiple_reviews(request: web.Request, content_type, accept, body) -> web.Response:
    """Create Multiple Reviews

    Creates multiple reviews.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: list | bytes

    """
    body = [SaveMultipleReviewsRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def save_review(request: web.Request, content_type, accept, body) -> web.Response:
    """Create a Review

    Creates a single review

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveReviewRequest.from_dict(body)
    return web.Response(status=200)
