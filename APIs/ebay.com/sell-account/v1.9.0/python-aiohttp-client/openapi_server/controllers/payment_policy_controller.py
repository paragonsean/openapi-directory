from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_policy import PaymentPolicy
from openapi_server.models.payment_policy_request import PaymentPolicyRequest
from openapi_server.models.payment_policy_response import PaymentPolicyResponse
from openapi_server.models.set_payment_policy_response import SetPaymentPolicyResponse
from openapi_server import util


async def create_payment_policy(request: web.Request, body) -> web.Response:
    """create_payment_policy

    This method creates a new payment policy where the policy encapsulates seller&#39;s terms for order payments.  &lt;br/&gt;&lt;br/&gt;Each policy targets a specific eBay marketplace and category group, and you can create multiple policies for each combination.  &lt;br/&gt;&lt;br/&gt;A successful request returns the &lt;b&gt;getPaymentPolicy&lt;/b&gt; URI to the new policy in the &lt;b&gt;Location&lt;/b&gt; response header and the ID for the new policy is returned in the response payload.  &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Tip:&lt;/b&gt; For details on creating and using the business policies supported by the Account API, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/seller-accounts/business-policies.html\&quot;&gt;eBay business policies&lt;/a&gt;.&lt;/p&gt;

    :param body: Payment policy request
    :type body: dict | bytes

    """
    body = PaymentPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_payment_policy(request: web.Request, payment_policy_id) -> web.Response:
    """delete_payment_policy

    This method deletes a payment policy. Supply the ID of the policy you want to delete in the &lt;b&gt;paymentPolicyId&lt;/b&gt; path parameter. 

    :param payment_policy_id: This path parameter specifies the ID of the payment policy you want to delete.
    :type payment_policy_id: str

    """
    return web.Response(status=200)


async def get_payment_policies(request: web.Request, marketplace_id) -> web.Response:
    """get_payment_policies

    This method retrieves all the payment policies configured for the marketplace you specify using the &lt;code&gt;marketplace_id&lt;/code&gt; query parameter.  &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Marketplaces and locales&lt;/b&gt;  &lt;br/&gt;&lt;br/&gt;Get the correct policies for a marketplace that supports multiple locales using the &lt;code&gt;Content-Language&lt;/code&gt; request header. For example, get the policies for the French locale of the Canadian marketplace by specifying &lt;code&gt;fr-CA&lt;/code&gt; for the &lt;code&gt;Content-Language&lt;/code&gt; header. Likewise, target the Dutch locale of the Belgium marketplace by setting &lt;code&gt;Content-Language: nl-BE&lt;/code&gt;. For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP request headers&lt;/a&gt;.

    :param marketplace_id: This query parameter specifies the eBay marketplace of the policies you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum
    :type marketplace_id: str

    """
    return web.Response(status=200)


async def get_payment_policy(request: web.Request, payment_policy_id) -> web.Response:
    """get_payment_policy

    This method retrieves the complete details of a payment policy. Supply the ID of the policy you want to retrieve using the &lt;b&gt;paymentPolicyId&lt;/b&gt; path parameter.

    :param payment_policy_id: This path parameter specifies the ID of the payment policy you want to retrieve.
    :type payment_policy_id: str

    """
    return web.Response(status=200)


async def get_payment_policy_by_name(request: web.Request, marketplace_id, name) -> web.Response:
    """get_payment_policy_by_name

    This method retrieves the details of a specific payment policy. Supply both the policy &lt;code&gt;name&lt;/code&gt; and its associated &lt;code&gt;marketplace_id&lt;/code&gt; in the request query parameters.   &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Marketplaces and locales&lt;/b&gt;  &lt;br/&gt;&lt;br/&gt;Get the correct policy for a marketplace that supports multiple locales using the &lt;code&gt;Content-Language&lt;/code&gt; request header. For example, get a policy for the French locale of the Canadian marketplace by specifying &lt;code&gt;fr-CA&lt;/code&gt; for the &lt;code&gt;Content-Language&lt;/code&gt; header. Likewise, target the Dutch locale of the Belgium marketplace by setting &lt;code&gt;Content-Language: nl-BE&lt;/code&gt;. For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot;&gt;HTTP request headers&lt;/a&gt;.

    :param marketplace_id: This query parameter specifies the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum
    :type marketplace_id: str
    :param name: This query parameter specifies the seller-defined name of the payment policy you want to retrieve.
    :type name: str

    """
    return web.Response(status=200)


async def update_payment_policy(request: web.Request, payment_policy_id, body) -> web.Response:
    """update_payment_policy

    This method updates an existing payment policy. Specify the policy you want to update using the &lt;b&gt;payment_policy_id&lt;/b&gt; path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.

    :param payment_policy_id: This path parameter specifies the ID of the payment policy you want to update.
    :type payment_policy_id: str
    :param body: Payment policy request
    :type body: dict | bytes

    """
    body = PaymentPolicyRequest.from_dict(body)
    return web.Response(status=200)
