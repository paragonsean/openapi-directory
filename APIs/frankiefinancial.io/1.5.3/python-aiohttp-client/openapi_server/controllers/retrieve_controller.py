from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_object import ErrorObject
from openapi_server.models.retrieved_response_object import RetrievedResponseObject
from openapi_server import util


async def retrieve_result(request: web.Request, x_frankie_customer_id, request_id, x_frankie_customer_child_id=None, payload=None) -> web.Response:
    """(Re)retrieve Response Result.

    If you&#39;ve received a notification that you previously backgrounded transaction has completed, or you wish to re-retrive a result from an earlier transaction, then you can simply request the result from our encrypted cache  The response will return the original HTTP code, along with the payload that would have been returned in the original request. 

    :param x_frankie_customer_id: Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    :type x_frankie_customer_id: str
    :type x_frankie_customer_id: str
    :param request_id: This will be the same RequestId that was sent in the 202 acceptance response. 
    :type request_id: str
    :param x_frankie_customer_child_id: If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children. 
    :type x_frankie_customer_child_id: str
    :type x_frankie_customer_child_id: str
    :param payload: Specifies the type of the payload field in the retrieved response. Default is &#39;string&#39;. 
    :type payload: str

    """
    return web.Response(status=200)
