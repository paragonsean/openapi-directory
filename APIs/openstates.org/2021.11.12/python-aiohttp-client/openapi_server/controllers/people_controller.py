from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.org_classification import OrgClassification
from openapi_server.models.person_include import PersonInclude
from openapi_server.models.person_list import PersonList
from openapi_server import util


async def people_geo_people_geo_get(request: web.Request, lat, lng, include=None, apikey=None, x_api_key=None) -> web.Response:
    """People Geo

    Get list of people currently representing a given location.  **Note:** Currently limited to state legislators and US Congress.  Governors &amp; mayors are not included.

    :param lat: Latitude of point.
    :type lat: 
    :param lng: Longitude of point.
    :type lng: 
    :param include: Additional information to include in the response.
    :type include: list | bytes
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    include = [PersonInclude.from_dict(d) for d in include]
    return web.Response(status=200)


async def people_search_people_get(request: web.Request, jurisdiction=None, name=None, id=None, org_classification=None, district=None, include=None, page=None, per_page=None, apikey=None, x_api_key=None) -> web.Response:
    """People Search

    Get list of people matching selected criteria.  Must provide either **jurisdiction**, **name**, or one or more **id** parameters.

    :param jurisdiction: Filter by jurisdiction name or id.
    :type jurisdiction: str
    :param name: Filter by name, case-insensitive match.
    :type name: str
    :param id: Filter by id, can be specified multiple times for multiple people.
    :type id: List[str]
    :param org_classification: Filter by current role.
    :type org_classification: dict | bytes
    :param district: Filter by district name.
    :type district: str
    :param include: Additional information to include in response.
    :type include: list | bytes
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param apikey: 
    :type apikey: str
    :param x_api_key: 
    :type x_api_key: str

    """
    org_classification = .from_dict(org_classification)
    include = [PersonInclude.from_dict(d) for d in include]
    return web.Response(status=200)
