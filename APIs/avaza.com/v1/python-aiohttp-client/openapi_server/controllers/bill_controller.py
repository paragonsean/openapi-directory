from typing import List, Dict
from aiohttp import web

from openapi_server.models.bill import Bill
from openapi_server.models.bill_list import BillList
from openapi_server.models.new_bill import NewBill
from openapi_server import util


async def bill_get(request: web.Request, updated_after=None, page_size=None, page_number=None, sort=None, company_idfk=None) -> web.Response:
    """Gets list of Bills

    TransactionStatusCode values are: \&quot;Draft\&quot;, \&quot;Verified\&quot;, \&quot;Late\&quot;, \&quot;Paid\&quot;, \&quot;Partial\&quot;, \&quot;Void\&quot;

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


async def bill_get_by_id(request: web.Request, id) -> web.Response:
    """Gets a Bill by Bill ID

    

    :param id: Bill Transaction ID number
    :type id: int

    """
    return web.Response(status=200)


async def bill_post(request: web.Request, model) -> web.Response:
    """Create a new draft Bill

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewBill.from_dict(model)
    return web.Response(status=200)
