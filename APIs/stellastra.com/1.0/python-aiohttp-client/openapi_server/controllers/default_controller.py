from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_review_post200_response import PostReviewPost200Response
from openapi_server.models.post_review_post400_response import PostReviewPost400Response
from openapi_server.models.post_review_post401_response import PostReviewPost401Response
from openapi_server.models.post_review_post403_response import PostReviewPost403Response
from openapi_server.models.post_review_post_request import PostReviewPostRequest
from openapi_server import util


async def post_review_post(request: web.Request, user_email, rating, body, user_name=None) -> web.Response:
    """Posts the user&#39;s review to Stellastra

    

    :param user_email: User&#39;s email to which the review verification will be sent. 
    :type user_email: str
    :param rating: The user&#39;s star rating, must be a single integer from [1, 2, 3, 4, 5]
    :type rating: int
    :param body: The request body requires the user_email and rating. The parameter use_name is optional. 
    :type body: dict | bytes
    :param user_name: The user&#39;s name, defaults to empty string \&quot;\&quot;.  Thus, if this is omitted, the email to the user will not use the user&#39;s name. 
    :type user_name: str

    """
    body = PostReviewPostRequest.from_dict(body)
    return web.Response(status=200)
