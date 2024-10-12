from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def list_contracts_get(request: web.Request, duns, naics=None, sort=None, direction=None, page=None) -> web.Response:
    """This endpoint returns contract history from FPDS for a specific vendor

    &lt;p&gt;This endpoint returns contract history from FPDS for a specific vendor. The vendor&#39;s DUNS number is a required parameter. You can also filter contracts by their NAICS code to find contracts relevant to a particular category.&lt;/p&gt;

    :param duns: A 9-digit DUNS number that uniquely identifies a vendor (required).
    :type duns: str
    :param naics: a six digit NAICS code used to filter by contracts with a certain NAICS
    :type naics: str
    :param sort: a field to sort on. Choices are date, status, agency, and amount
    :type sort: str
    :param direction: The sort direction of the results. Choices are asc or desc.
    :type direction: str
    :param page: the page to start on. Results are paginated in increments of 100. Begins at page&#x3D;1.
    :type page: str

    """
    return web.Response(status=200)
