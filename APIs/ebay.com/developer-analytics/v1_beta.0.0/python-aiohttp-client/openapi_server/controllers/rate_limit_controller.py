from typing import List, Dict
from aiohttp import web

from openapi_server.models.rate_limits_response import RateLimitsResponse
from openapi_server import util


async def get_rate_limits(request: web.Request, api_context=None, api_name=None) -> web.Response:
    """get_rate_limits

    This method retrieves the call limit and utilization data for an application. The data is retrieved for all RESTful APIs and the legacy Trading API.  &lt;br&gt;&lt;br&gt;The response from &lt;b&gt;getRateLimits&lt;/b&gt; includes a list of the applicable resources and the \&quot;call limit\&quot;, or quota, that is set for each resource. In addition to quota information, the response also includes the number of remaining calls available before the limit is reached, the time remaining before the quota resets, and the length of the \&quot;time window\&quot; to which the quota applies.  &lt;br&gt;&lt;br&gt;By default, this method returns utilization data for all RESTful API and the legacy Trading API resources. Use the &lt;b&gt;api_name&lt;/b&gt; and &lt;b&gt;api_context&lt;/b&gt; query parameters to filter the response to only the desired APIs.  &lt;br&gt;&lt;br&gt;For more on call limits, see &lt;a href&#x3D;\&quot;https://developer.ebay.com/support/app-check \&quot; target&#x3D;\&quot;_blank\&quot;&gt;Compatible Application Check&lt;/a&gt;.

    :param api_context: This optional query parameter filters the result to include only the specified API context. &lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt; &lt;ul&gt;&lt;li&gt;&lt;code&gt;buy&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;sell&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;commerce&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;developer&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;tradingapi&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;
    :type api_context: str
    :param api_name: This optional query parameter filters the result to include only the APIs specified. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example values:&lt;/b&gt; &lt;ul&gt; &lt;li&gt;&lt;code&gt;browse&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/buy-apis#buy-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Buy APIs&lt;/a&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;inventory&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/sell-apis#sell-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Sell APIs&lt;/a&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;taxonomy&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../develop/apis/restful-apis/commerce-apis#commerce-apis\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Commerce APIs&lt;/a&gt;&lt;/li&gt;  &lt;li&gt;&lt;code&gt;tradingapi&lt;/code&gt; for the &lt;a href&#x3D;\&quot;/../Devzone/XML/docs/Reference/eBay/index.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Trading APIs&lt;/a&gt;&lt;/li&gt;&lt;/ul&gt;
    :type api_name: str

    """
    return web.Response(status=200)
