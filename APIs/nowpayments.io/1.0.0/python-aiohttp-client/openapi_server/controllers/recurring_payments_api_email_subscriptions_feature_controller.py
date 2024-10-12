from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_recurring_payment200_response import DeleteRecurringPayment200Response
from openapi_server.models.get_many_plans200_response import GetManyPlans200Response
from openapi_server.models.get_many_recurring_payments200_response import GetManyRecurringPayments200Response
from openapi_server.models.get_one_plan200_response import GetOnePlan200Response
from openapi_server.models.get_one_plan404_response import GetOnePlan404Response
from openapi_server.models.get_one_recurring_payment200_response import GetOneRecurringPayment200Response
from openapi_server.models.get_one_recurring_payment404_response import GetOneRecurringPayment404Response
from openapi_server.models.update_plan_request import UpdatePlanRequest
from openapi_server import util


async def delete_recurring_payment(request: web.Request, sub_id) -> web.Response:
    """Delete recurring payment

    Completely removes a particular payment from the recurring payment plan.   You need to specify the payment plan id in the request.

    :param sub_id: 
    :type sub_id: str

    """
    return web.Response(status=200)


async def get_many_plans(request: web.Request, limit=None, offset=None, x_api_key=None) -> web.Response:
    """Get many plans

    This method allows you to obtain information about all the payment plans you’ve created.

    :param limit: Number
    :type limit: str
    :param offset: Number
    :type offset: str
    :param x_api_key: 
    :type x_api_key: str

    """
    return web.Response(status=200)


async def get_many_recurring_payments(request: web.Request, status=None, subscription_plan_id=None, is_active=None, limit=None, offset=None, x_api_key=None) -> web.Response:
    """Get many recurring payments

    The method allows you to view the entire list of recurring payments filtered by payment status and/or payment plan id

    :param status: \&quot;WAITING_PAY\&quot; / \&quot;PAID\&quot; /  \&quot;PARTIALLY_PAID\&quot; / \&quot;EXPIRED\&quot;
    :type status: str
    :param subscription_plan_id: 
    :type subscription_plan_id: str
    :param is_active: true / false
    :type is_active: str
    :param limit: 
    :type limit: str
    :param offset: 
    :type offset: str
    :param x_api_key: 
    :type x_api_key: str

    """
    return web.Response(status=200)


async def get_one_plan(request: web.Request, plan_id, x_api_key=None) -> web.Response:
    """Get one plan

    This method allows you to obtain information about your payment plan.   (you need to specify your payment plan id in the request).

    :param plan_id: 
    :type plan_id: str
    :param x_api_key: 
    :type x_api_key: str

    """
    return web.Response(status=200)


async def get_one_recurring_payment(request: web.Request, sub_id, x_api_key=None) -> web.Response:
    """Get one recurring payment

    Get information about a particular recurring payment via its ID.  Here’s the list of available statuses:   \\- WAITING_PAY   \\- PAID   \\- PARTIALLY_PAID   \\- EXPIRED

    :param sub_id: 
    :type sub_id: str
    :param x_api_key: 
    :type x_api_key: str

    """
    return web.Response(status=200)


async def update_plan(request: web.Request, plan_id, body=None) -> web.Response:
    """Update plan

    This method allows you to add necessary changes to a created plan. They won’t affect users who have already paid; however, the changes will take effect when a new payment is to be made.

    :param plan_id: 
    :type plan_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePlanRequest.from_dict(body)
    return web.Response(status=200)
