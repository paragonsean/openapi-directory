from typing import List, Dict
from aiohttp import web

from openapi_server.models.beta_app_review_submission_create_request import BetaAppReviewSubmissionCreateRequest
from openapi_server.models.beta_app_review_submission_response import BetaAppReviewSubmissionResponse
from openapi_server.models.beta_app_review_submissions_response import BetaAppReviewSubmissionsResponse
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def beta_app_review_submissions_build_get_to_one_related(request: web.Request, id, fields_builds=None) -> web.Response:
    """beta_app_review_submissions_build_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def beta_app_review_submissions_create_instance(request: web.Request, body) -> web.Response:
    """beta_app_review_submissions_create_instance

    

    :param body: BetaAppReviewSubmission representation
    :type body: dict | bytes

    """
    body = BetaAppReviewSubmissionCreateRequest.from_dict(body)
    return web.Response(status=200)


async def beta_app_review_submissions_get_collection(request: web.Request, filter_build, filter_beta_review_state=None, fields_beta_app_review_submissions=None, limit=None, include=None, fields_builds=None) -> web.Response:
    """beta_app_review_submissions_get_collection

    

    :param filter_build: filter by id(s) of related &#39;build&#39;
    :type filter_build: List[str]
    :param filter_beta_review_state: filter by attribute &#39;betaReviewState&#39;
    :type filter_beta_review_state: List[str]
    :param fields_beta_app_review_submissions: the fields to include for returned resources of type betaAppReviewSubmissions
    :type fields_beta_app_review_submissions: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def beta_app_review_submissions_get_instance(request: web.Request, id, fields_beta_app_review_submissions=None, include=None, fields_builds=None) -> web.Response:
    """beta_app_review_submissions_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_app_review_submissions: the fields to include for returned resources of type betaAppReviewSubmissions
    :type fields_beta_app_review_submissions: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)
