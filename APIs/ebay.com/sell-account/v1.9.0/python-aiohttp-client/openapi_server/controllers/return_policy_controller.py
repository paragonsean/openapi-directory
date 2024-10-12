from typing import List, Dict
from aiohttp import web

from openapi_server.models.return_policy import ReturnPolicy
from openapi_server.models.return_policy_request import ReturnPolicyRequest
from openapi_server.models.return_policy_response import ReturnPolicyResponse
from openapi_server.models.set_return_policy_response import SetReturnPolicyResponse
from openapi_server import util


async def create_return_policy(request: web.Request, body) -> web.Response:
    """create_return_policy

    This method creates a new return policy where the policy encapsulates seller&#39;s terms for returning items.  &lt;br/&gt;&lt;br/&gt;Each policy targets a specific marketplace, and you can create multiple policies for each marketplace. Return policies are not applicable to motor-vehicle listings.&lt;br/&gt;&lt;br/&gt;A successful request returns the &lt;b&gt;getReturnPolicy&lt;/b&gt; URI to the new policy in the &lt;b&gt;Location&lt;/b&gt; response header and the ID for the new policy is returned in the response payload.  &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Tip:&lt;/b&gt; For details on creating and using the business policies supported by the Account API, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/seller-accounts/business-policies.html\&quot;&gt;eBay business policies&lt;/a&gt;.&lt;/p&gt;

    :param body: Return policy request
    :type body: dict | bytes

    """
    body = ReturnPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_return_policy(request: web.Request, return_policy_id) -> web.Response:
    """delete_return_policy

    This method deletes a return policy. Supply the ID of the policy you want to delete in the &lt;b&gt;returnPolicyId&lt;/b&gt; path parameter.

    :param return_policy_id: This path parameter specifies the ID of the return policy you want to delete.
    :type return_policy_id: str

    """
    return web.Response(status=200)


async def get_return_policies(request: web.Request, marketplace_id) -> web.Response:
    """get_return_policies

    This method retrieves all the return policies configured for the marketplace you specify using the &lt;code&gt;marketplace_id&lt;/code&gt; query parameter.  &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Marketplaces and locales&lt;/b&gt;  &lt;br/&gt;&lt;br/&gt;Get the correct policies for a marketplace that supports multiple locales using the &lt;code&gt;Content-Language&lt;/code&gt; request header. For example, get the policies for the French locale of the Canadian marketplace by specifying &lt;code&gt;fr-CA&lt;/code&gt; for the &lt;code&gt;Content-Language&lt;/code&gt; header. Likewise, target the Dutch locale of the Belgium marketplace by setting &lt;code&gt;Content-Language: nl-BE&lt;/code&gt;. For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HTTP request headers&lt;/a&gt;.

    :param marketplace_id: This query parameter specifies the ID of the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum
    :type marketplace_id: str

    """
    return web.Response(status=200)


async def get_return_policy(request: web.Request, return_policy_id) -> web.Response:
    """get_return_policy

    This method retrieves the complete details of the return policy specified by the &lt;b&gt;returnPolicyId&lt;/b&gt; path parameter.

    :param return_policy_id: This path parameter specifies the of the return policy you want to retrieve.
    :type return_policy_id: str

    """
    return web.Response(status=200)


async def get_return_policy_by_name(request: web.Request, marketplace_id, name) -> web.Response:
    """get_return_policy_by_name

    This method retrieves the details of a specific return policy. Supply both the policy &lt;code&gt;name&lt;/code&gt; and its associated &lt;code&gt;marketplace_id&lt;/code&gt; in the request query parameters.   &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Marketplaces and locales&lt;/b&gt;  &lt;br/&gt;&lt;br/&gt;Get the correct policy for a marketplace that supports multiple locales using the &lt;code&gt;Content-Language&lt;/code&gt; request header. For example, get a policy for the French locale of the Canadian marketplace by specifying &lt;code&gt;fr-CA&lt;/code&gt; for the &lt;code&gt;Content-Language&lt;/code&gt; header. Likewise, target the Dutch locale of the Belgium marketplace by setting &lt;code&gt;Content-Language: nl-BE&lt;/code&gt;. For details on header values, see &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#HTTP\&quot;&gt;HTTP request headers&lt;/a&gt;.

    :param marketplace_id: This query parameter specifies the ID of the eBay marketplace of the policy you want to retrieve. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/account/types/ba:MarketplaceIdEnum
    :type marketplace_id: str
    :param name: This query parameter specifies the seller-defined name of the return policy you want to retrieve.
    :type name: str

    """
    return web.Response(status=200)


async def update_return_policy(request: web.Request, return_policy_id, body) -> web.Response:
    """update_return_policy

    This method updates an existing return policy. Specify the policy you want to update using the &lt;b&gt;return_policy_id&lt;/b&gt; path parameter. Supply a complete policy payload with the updates you want to make; this call overwrites the existing policy with the new details specified in the payload.

    :param return_policy_id: This path parameter specifies the ID of the return policy you want to update.
    :type return_policy_id: str
    :param body: Container for a return policy request.
    :type body: dict | bytes

    """
    body = ReturnPolicyRequest.from_dict(body)
    return web.Response(status=200)
