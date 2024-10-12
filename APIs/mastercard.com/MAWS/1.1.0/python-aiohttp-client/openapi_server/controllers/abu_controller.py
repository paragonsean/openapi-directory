from typing import List, Dict
from aiohttp import web

from openapi_server.models.abu import ABU
from openapi_server.models.abu_response import AbuResponse
from openapi_server import util


async def abu_post(request: web.Request, abu_request) -> web.Response:
    """Access methods for merchants to ABU program.

    &lt;ul&gt;   &lt;li&gt;&lt;p&gt;&lt;b&gt;Pull model:&lt;/b&gt;&lt;/p&gt;     &lt;br&gt;     &lt;p&gt;To receive information for a given PAN, the customer sends a request and will receive a response with the most up to date information.&lt;/p&gt;     &lt;p&gt;In this page, customers can execute samples of requests to explore the pattern of the API responses. However, once the customer decides to start using the SDK, it is necessary to be fully onboarded to ABU API Pull model.&lt;/p&gt;   &lt;/li&gt;   &lt;br&gt;   &lt;li&gt;&lt;p&gt;&lt;b&gt;Push model:&lt;/b&gt;&lt;/p&gt;     &lt;br&gt;     &lt;p&gt;Customers can choose to automatically receive ABU account update notifications on a designated endpoint. This means that a customer can subscribe to each PAN in order to receive updates, so that when these PANs have any changes, the customer will receive the updates via notifications on the designated endpoint.&lt;/p&gt;     &lt;p&gt;Different fields on the API are mandatory to use this model.&lt;/p&gt;&lt;p&gt;In order to complete a full end-to-end test scenario (including the notifications), it is necessary to be fully onboarded on ABU API Push model:&lt;/p&gt;     &lt;p&gt;- An endpoint provided by the customer must be registered with Mastercard so that notifications can be pro-actively sent out to the customer.&lt;/p&gt;     &lt;p&gt;- A certificate provided by Mastercard representative must be used by the customer to receive notifications on the designated endpoint.&lt;/p&gt;     &lt;br&gt;     &lt;p&gt;&lt;b&gt;* For customers who are already enrolled to ABU API Pull model and want to start using ABU API Push model, it is necessary to perform a technical enrollment that involves a certificate exchange and must be registered as an ABU API Push model user.&lt;/b&gt;&lt;/p&gt;     &lt;br&gt;     &lt;p&gt;For more details on how to proceed with onboarding for ABU API push model contact abu_push_onboarding@mastercard.com.&lt;/p&gt;&lt;p&gt;Note: This email is for ABU API push onboarding only. For general ABU API inquiry questions contact api_support@mastercard.com and for general ABU questions contact abu_helpdesk@mastercard.com.&lt;/p&gt;   &lt;/li&gt; &lt;/ul&gt;

    :param abu_request: Request for ABU API
    :type abu_request: dict | bytes

    """
    abu_request = ABU.from_dict(abu_request)
    return web.Response(status=200)
