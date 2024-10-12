from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.subscription_plan_request import SubscriptionPlanRequest
from openapi_server.models.subscription_plan_response import SubscriptionPlanResponse
from openapi_server import util


async def internal_request_subscription_plan(request: web.Request, x_sds_service_token) -> web.Response:
    """Request subscription plan

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description: Get the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 

    :param x_sds_service_token: Service Authentication token
    :type x_sds_service_token: str

    """
    return web.Response(status=200)


async def internal_set_subscription_plan(request: web.Request, x_sds_service_token, body) -> web.Response:
    """Set subscription plan

    &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.36.0&lt;/h3&gt;  ### Description:  Change the subscription plan id of the current tenant  ### Precondition: Valid &#x60;X-SDS-Service-Token&#x60; Header  ### Postcondition: The subscription plan of the current tenant is set to the given value.   Returns SubscriptionPlanResponse model that includes subscription plan id.  ### Further Information: None. 

    :param x_sds_service_token: Service Authentication token
    :type x_sds_service_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionPlanRequest.from_dict(body)
    return web.Response(status=200)
