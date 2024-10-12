from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_trust_product_evaluation_response import ListTrustProductEvaluationResponse
from openapi_server.models.trusthub_v1_trust_product_trust_product_evaluation import TrusthubV1TrustProductTrustProductEvaluation
from openapi_server import util


async def create_trust_product_evaluation(request: web.Request, trust_product_sid, policy_sid) -> web.Response:
    """create_trust_product_evaluation

    Create a new Evaluation

    :param trust_product_sid: The unique string that we created to identify the trust_product resource.
    :type trust_product_sid: str
    :param policy_sid: The unique string of a policy that is associated to the customer_profile resource.
    :type policy_sid: str

    """
    return web.Response(status=200)


async def fetch_trust_product_evaluation(request: web.Request, trust_product_sid, sid) -> web.Response:
    """fetch_trust_product_evaluation

    Fetch specific Evaluation Instance.

    :param trust_product_sid: The unique string that we created to identify the trust_product resource.
    :type trust_product_sid: str
    :param sid: The unique string that identifies the Evaluation resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_trust_product_evaluation(request: web.Request, trust_product_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_trust_product_evaluation

    Retrieve a list of Evaluations associated to the trust_product resource.

    :param trust_product_sid: The unique string that we created to identify the trust_product resource.
    :type trust_product_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
