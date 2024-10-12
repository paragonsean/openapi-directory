from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_evaluation_response import ListEvaluationResponse
from openapi_server.models.numbers_v2_regulatory_compliance_bundle_evaluation import NumbersV2RegulatoryComplianceBundleEvaluation
from openapi_server import util


async def create_evaluation(request: web.Request, bundle_sid) -> web.Response:
    """create_evaluation

    Creates an evaluation for a bundle

    :param bundle_sid: The unique string that identifies the Bundle resource.
    :type bundle_sid: str

    """
    return web.Response(status=200)


async def fetch_evaluation(request: web.Request, bundle_sid, sid) -> web.Response:
    """fetch_evaluation

    Fetch specific Evaluation Instance.

    :param bundle_sid: The unique string that we created to identify the Bundle resource.
    :type bundle_sid: str
    :param sid: The unique string that identifies the Evaluation resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_evaluation(request: web.Request, bundle_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_evaluation

    Retrieve a list of Evaluations associated to the Bundle resource.

    :param bundle_sid: The unique string that identifies the Bundle resource.
    :type bundle_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
