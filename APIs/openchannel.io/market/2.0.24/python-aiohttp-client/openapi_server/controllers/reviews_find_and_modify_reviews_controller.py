from typing import List, Dict
from aiohttp import web

from openapi_server.models.review import Review
from openapi_server.models.review_pages import ReviewPages
from openapi_server import util


async def reviews_get(request: web.Request, query=None, sort=None, page_number=None, limit=None) -> web.Response:
    """Find reviews for a particular App and marketplace. Results are automatically paginated when limit is set

    - Results are paginated and the default is value is 100 if no limit is provided 

    :param query: A query document. Example: {&#39;rating&#39;: 500} matches all the reviews that have a rating of 500. 
    :type query: str
    :param sort: A sort document. Example: {&#39;rating&#39;:1} sorts the results by rating in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int

    """
    return web.Response(status=200)


async def reviews_post(request: web.Request, app_id, user_id, headline, rating, description, user_account_id=None, type=None, must_own_app=None, auto_approve=None, custom_data=None) -> web.Response:
    """Post a review from a User and returns the new post

    - Only authenticated users are able to post reviews - Returns the newly created review 

    :param app_id: The id of the App that will own this review
    :type app_id: str
    :param user_id: The id of the User that is posting this review
    :type user_id: str
    :param headline: The review&#39;s headline. Limited to 50 characters.
    :type headline: str
    :param rating: The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
    :type rating: int
    :param description: The review&#39;s description. Limited to 2000 characters.
    :type description: str
    :param user_account_id: The id of the User account that is posting this review
    :type user_account_id: str
    :param type: The type for this review
    :type type: str
    :param must_own_app: True if a review can be created only by a user that has owned the app. The default is True.
    :type must_own_app: bool
    :param auto_approve: True if the review should be automatically approved. The default is False.
    :type auto_approve: bool
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)


async def reviews_review_id_delete(request: web.Request, review_id, user_id, user_account_id=None) -> web.Response:
    """Remove a review

    - Only the review author is able to remove their review 

    :param review_id: The id of the Review to be updated
    :type review_id: str
    :param user_id: The id of the User that is removing this review
    :type user_id: str
    :param user_account_id: The id of the User account that is emoving this review
    :type user_account_id: str

    """
    return web.Response(status=200)


async def reviews_review_id_get(request: web.Request, review_id) -> web.Response:
    """Find a Review within a particular App and marketplace

    

    :param review_id: The id of the review to be located
    :type review_id: str

    """
    return web.Response(status=200)


async def reviews_review_id_patch(request: web.Request, review_id, user_id, user_account_id=None, headline=None, rating=None, description=None, custom_data=None) -> web.Response:
    """Update a review fields

    - Only the review author is able to update their review - Returns the newly updated review 

    :param review_id: The id of the Review to be updated
    :type review_id: str
    :param user_id: The id of the User that is updating this review
    :type user_id: str
    :param user_account_id: The id of the User account that is posting this review
    :type user_account_id: str
    :param headline: The review&#39;s headline. Limited to 50 characters.
    :type headline: str
    :param rating: The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
    :type rating: int
    :param description: The review&#39;s description. Limited to 2000 characters.
    :type description: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)


async def reviews_review_id_post(request: web.Request, review_id, user_id, user_account_id, headline, rating, description, custom_data=None) -> web.Response:
    """Update a review from a User and returns the new post

    - Only the review author is able to update their review - Returns the newly updated review 

    :param review_id: The id of the Review to be updated
    :type review_id: str
    :param user_id: The id of the User that is updating this review
    :type user_id: str
    :param user_account_id: The id of the User account that is posting this review
    :type user_account_id: str
    :param headline: The review&#39;s headline. Limited to 50 characters.
    :type headline: str
    :param rating: The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
    :type rating: int
    :param description: The review&#39;s description. Limited to 2000 characters.
    :type description: str
    :param custom_data: A custom JSON object that you can create and attach to this record
    :type custom_data: str

    """
    return web.Response(status=200)
