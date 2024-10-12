from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def list_users_subscription_group_sms_0(request: web.Request, external_id=None, limit=None, offset=None, phone=None) -> web.Response:
    """List User&#39;s Subscription Group - SMS

    Use the endpoint below to list and get the subscription groups of a certain user.  &gt; If there are multiple users (multiple external ids) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).

    :param external_id: (Required*) String  The external_id of the user. Must include at least one and at most 50 &#x60;external_ids&#x60;.
    :type external_id: str
    :param limit: (Optional) Integer  The limit on the maximum number of results returned. Default (and max) limit is 100.
    :type limit: str
    :param offset: (Optional) Integer  Number of templates to skip before returning rest of the templates that fit the search criteria.
    :type offset: str
    :param phone: (Required*) String  The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format. 
    :type phone: str

    """
    return web.Response(status=200)


async def list_users_subscription_group_status_sms_0(request: web.Request, subscription_group_id=None, external_id=None, phone=None) -> web.Response:
    """List User&#39;s  Subscription Group Status - SMS

    Use the endpoint below to get the subscription state of a user in a subscription group. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.  &gt; *Either &#x60;external_id&#x60; or &#x60;email&#x60; are required.  ## Response  All successful responses will return &#x60;subscribed&#x60;, &#x60;unsubscribed&#x60;, or &#x60;unknown&#x60; depending on status and user history with the subscription group.  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;status\&quot;: {     \&quot;1\&quot;: \&quot;Unsubscribed\&quot;,     \&quot;2\&quot;: \&quot;Subscribed\&quot;   },   \&quot;message\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;

    :param subscription_group_id: (Required) String  The &#x60;id&#x60; of your subscription group.
    :type subscription_group_id: str
    :param external_id: (Required*) String  The &#x60;external_id&#x60; of the user (must include at least one and at most 50 &#x60;external_ids&#x60;).  Only external_id or phone is accepted for SMS subscription groups 
    :type external_id: str
    :param phone: (Required*) String  The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format.  Only external_id or phone is accepted for SMS subscription groups 
    :type phone: str

    """
    return web.Response(status=200)
