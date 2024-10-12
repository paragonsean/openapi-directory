from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_regulation_response import ListRegulationResponse
from openapi_server.models.numbers_v2_regulatory_compliance_regulation import NumbersV2RegulatoryComplianceRegulation
from openapi_server.models.regulation_enum_end_user_type import RegulationEnumEndUserType
from openapi_server import util


async def fetch_regulation(request: web.Request, sid) -> web.Response:
    """fetch_regulation

    Fetch specific Regulation Instance.

    :param sid: The unique string that identifies the Regulation resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_regulation(request: web.Request, end_user_type=None, iso_country=None, number_type=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_regulation

    Retrieve a list of all Regulations.

    :param end_user_type: The type of End User the regulation requires - can be &#x60;individual&#x60; or &#x60;business&#x60;.
    :type end_user_type: str
    :param iso_country: The ISO country code of the phone number&#39;s country.
    :type iso_country: str
    :param number_type: The type of phone number that the regulatory requiremnt is restricting.
    :type number_type: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
