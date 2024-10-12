from typing import List, Dict
from aiohttp import web

from openapi_server.models.committee import Committee
from openapi_server.models.committee_classification import CommitteeClassification
from openapi_server.models.committee_include import CommitteeInclude
from openapi_server.models.committee_list import CommitteeList
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.org_classification import OrgClassification
from openapi_server import util


async def committee_detail_committees_committee_id_get(request: web.Request, committee_id, include=None, apikey=None, x_api_key=None) -> web.Response:
    """Committee Detail

    Get details on a single committee by ID.

    :param committee_id: 
    :type committee_id: str
    :param include: Additional includes for the Committee response.
    :type include: list | bytes
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    include = [CommitteeInclude.from_dict(d) for d in include]
    return web.Response(status=200)


async def committee_list_committees_get(request: web.Request, jurisdiction=None, classification=None, parent=None, chamber=None, include=None, apikey=None, page=None, per_page=None, x_api_key=None) -> web.Response:
    """Committee List

    

    :param jurisdiction: Filter by jurisdiction name or ID.
    :type jurisdiction: str
    :param classification: 
    :type classification: dict | bytes
    :param parent: ocd-organization ID of parent committee.
    :type parent: str
    :param chamber: Chamber of committee, generally upper or lower.
    :type chamber: dict | bytes
    :param include: Additional includes for the Committee response.
    :type include: list | bytes
    :param apikey: 
    :type apikey: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param x_api_key: 
    :type x_api_key: str

    """
    classification = .from_dict(classification)
    chamber = .from_dict(chamber)
    include = [CommitteeInclude.from_dict(d) for d in include]
    return web.Response(status=200)
