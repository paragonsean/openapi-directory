from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_feedback_response import UserFeedbackResponse
from openapi_server import util


async def userfeedback_post(request: web.Request, fid, user_token, offer_id, feedback) -> web.Response:
    """Provide User Feedback on Offer

    This resource allows a user to provide a thumbs-up or a thumbs-down rating of the specified offer. Offer matches that are disliked will be supressed from the results of future calls to Matched Offers. 

    :param fid: Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    :type fid: str
    :param user_token: Session identifier as returned by the UserToken resource.
    :type user_token: str
    :param offer_id: System-wide identifier for the campaign, not intended for end-user display.
    :type offer_id: str
    :param feedback: User response to the offer. 0- Dislike offer. 1- Like offer.
    :type feedback: int

    """
    return web.Response(status=200)
