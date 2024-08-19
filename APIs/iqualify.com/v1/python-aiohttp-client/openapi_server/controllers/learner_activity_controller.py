from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.learner_progress_response import LearnerProgressResponse
from openapi_server.models.learner_response import LearnerResponse
from openapi_server.models.social_notes_response import SocialNotesResponse
from openapi_server.models.unit_reactions_analytics_response import UnitReactionsAnalyticsResponse
from openapi_server.models.users_all_progress_get200_response import UsersAllProgressGet200Response
from openapi_server.models.users_user_email_offerings_offering_id_progress_get200_response import UsersUserEmailOfferingsOfferingIdProgressGet200Response
from openapi_server import util


async def offerings_offering_id_analytics_learners_progress_get(request: web.Request, offering_id) -> web.Response:
    """Find learner progress in a specified offering

    Responds with all learner progress in the offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_social_notes_get(request: web.Request, offering_id) -> web.Response:
    """Find shared social notes in an offering

    Responds with all shared social notes in a specified offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def offerings_offering_id_analytics_unit_reactions_get(request: web.Request, offering_id) -> web.Response:
    """Find unit reactions

    Responds with user reactions to units in a specified offering.

    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def users_all_progress_get(request: web.Request, top=None, orderby=None, filter=None) -> web.Response:
    """Find learner progress in all offerings

    Responds with all learners&#39; progress in all offerings.

    :param top: Returns only the first n results.
    :type top: str
    :param orderby: Sorts the results.
    :type orderby: str
    :param filter: Filters the results, based on a Boolean condition.
    :type filter: str

    """
    return web.Response(status=200)


async def users_user_email_offerings_offering_id_progress_get(request: web.Request, user_email, offering_id) -> web.Response:
    """Find learner&#39;s progress in a specified offering

    Responds with the learner&#39;s progress in a specified offering.

    :param user_email: user&#39;s email
    :type user_email: str
    :param offering_id: offering&#39;s id
    :type offering_id: str

    """
    return web.Response(status=200)


async def users_user_email_progress_get(request: web.Request, user_email) -> web.Response:
    """Find learner&#39;s progress in offerings

    Responds with the specified learner&#39;s progress in all offerings.

    :param user_email: user&#39;s email
    :type user_email: str

    """
    return web.Response(status=200)
