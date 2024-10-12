from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_customer_profile_evaluation_response import ListCustomerProfileEvaluationResponse
from openapi_server.models.trusthub_v1_customer_profile_customer_profile_evaluation import TrusthubV1CustomerProfileCustomerProfileEvaluation
from openapi_server import util


async def create_customer_profile_evaluation(request: web.Request, customer_profile_sid, policy_sid) -> web.Response:
    """create_customer_profile_evaluation

    Create a new Evaluation

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param policy_sid: The unique string of a policy that is associated to the customer_profile resource.
    :type policy_sid: str

    """
    return web.Response(status=200)


async def fetch_customer_profile_evaluation(request: web.Request, customer_profile_sid, sid) -> web.Response:
    """fetch_customer_profile_evaluation

    Fetch specific Evaluation Instance.

    :param customer_profile_sid: The unique string that we created to identify the customer_profile resource.
    :type customer_profile_sid: str
    :param sid: The unique string that identifies the Evaluation resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_customer_profile_evaluation(request: web.Request, customer_profile_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_customer_profile_evaluation

    Retrieve a list of Evaluations associated to the customer_profile resource.

    :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :type customer_profile_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
