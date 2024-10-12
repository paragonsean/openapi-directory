from typing import List, Dict
from aiohttp import web

from openapi_server.models.estimate_details import EstimateDetails
from openapi_server.models.estimate_list import EstimateList
from openapi_server.models.new_estimate import NewEstimate
from openapi_server import util


async def estimate_get(request: web.Request, updated_after=None, page_size=None, page_number=None, sort=None, company_idfk=None) -> web.Response:
    """Gets list of Estimates

    EstimateStatusCode values are: \&quot;Draft\&quot;, \&quot;Sent\&quot;, \&quot;Accepted\&quot;, \&quot;Converted\&quot;, \&quot;Expired\&quot;, \&quot;Rejected\&quot;

    :param updated_after: 
    :type updated_after: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param sort: 
    :type sort: str
    :param company_idfk: 
    :type company_idfk: int

    """
    updated_after = util.deserialize_datetime(updated_after)
    return web.Response(status=200)


async def estimate_get_by_id(request: web.Request, id) -> web.Response:
    """Gets Estimate by Estimate ID

    

    :param id: Estimate Estimate ID number
    :type id: int

    """
    return web.Response(status=200)


async def estimate_post(request: web.Request, model) -> web.Response:
    """Create a new draft Estimate

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewEstimate.from_dict(model)
    return web.Response(status=200)
