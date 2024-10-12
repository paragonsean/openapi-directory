from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_applicant_single_applicant_multi_request import PostApplicantSingleApplicantMultiRequest
from openapi_server.models.post_free_end_point_free_request import PostFreeEndPointFreeRequest
from openapi_server.models.post_partial_address_multi_partial_address_multi_request import PostPartialAddressMultiPartialAddressMultiRequest
from openapi_server.models.post_postcode_multi_postcode_multi_request import PostPostcodeMultiPostcodeMultiRequest
from openapi_server.models.post_proposal_multi_proposal_request import PostProposalMultiProposalRequest
from openapi_server import util


async def post_applicant_single_applicant_multi(request: web.Request, payload) -> web.Response:
    """post_applicant_single_applicant_multi

    Retrieve 50 planning applications for an applicant name (example: John Smith). Rate limit is 100/day;10/minute

    :param payload: 
    :type payload: dict | bytes

    """
    payload = PostApplicantSingleApplicantMultiRequest.from_dict(payload)
    return web.Response(status=200)


async def post_applicant_single_applicant_single(request: web.Request, payload) -> web.Response:
    """post_applicant_single_applicant_single

    Retrieve a single planning application for an applicant (example: John Smith). Rate limit is 100/day;10/minute

    :param payload: 
    :type payload: dict | bytes

    """
    payload = PostApplicantSingleApplicantMultiRequest.from_dict(payload)
    return web.Response(status=200)


async def post_free_end_point_free(request: web.Request, payload) -> web.Response:
    """post_free_end_point_free

    Retrieve 1 planning application for proposal key word (example: Swimming Pool). Rate limit is 100/day;10/minute

    :param payload: 
    :type payload: dict | bytes

    """
    payload = PostFreeEndPointFreeRequest.from_dict(payload)
    return web.Response(status=200)


async def post_partial_addres_single_partial_address_single(request: web.Request, payload) -> web.Response:
    """post_partial_addres_single_partial_address_single

    Retrieve a single planning application for a partial address (example: Station Road). Rate limit is 100/day;10/minute

    :param payload: 
    :type payload: dict | bytes

    """
    payload = PostPartialAddressMultiPartialAddressMultiRequest.from_dict(payload)
    return web.Response(status=200)


async def post_partial_address_multi_partial_address_multi(request: web.Request, payload) -> web.Response:
    """post_partial_address_multi_partial_address_multi

    Retrieve 50 planning applications for a partial address (example: Station Road). Rate limit is 100/day;10/minute

    :param payload: 
    :type payload: dict | bytes

    """
    payload = PostPartialAddressMultiPartialAddressMultiRequest.from_dict(payload)
    return web.Response(status=200)


async def post_postcode_multi_postcode_multi(request: web.Request, payload) -> web.Response:
    """post_postcode_multi_postcode_multi

    Retrieve 50 planning applications for a postcode. Rate limit is 100/day;10/minute

    :param payload: 
    :type payload: dict | bytes

    """
    payload = PostPostcodeMultiPostcodeMultiRequest.from_dict(payload)
    return web.Response(status=200)


async def post_postcode_single_postcode_single(request: web.Request, payload) -> web.Response:
    """post_postcode_single_postcode_single

    Retrieve a single planning application for a postcode. Rate limit is 100/day;10/minute

    :param payload: 
    :type payload: dict | bytes

    """
    payload = PostPostcodeMultiPostcodeMultiRequest.from_dict(payload)
    return web.Response(status=200)


async def post_proposal_multi_proposal(request: web.Request, payload) -> web.Response:
    """post_proposal_multi_proposal

    Retrieve 50 planning applications for proposal key word (example: Swimming Pool). Rate limit is 100/day;10/minute

    :param payload: 
    :type payload: dict | bytes

    """
    payload = PostProposalMultiProposalRequest.from_dict(payload)
    return web.Response(status=200)
