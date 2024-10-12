from typing import List, Dict
from aiohttp import web

from openapi_server.models.summary_report_response import SummaryReportResponse
from openapi_server import util


async def get_promotion_summary_report(request: web.Request, marketplace_id) -> web.Response:
    """get_promotion_summary_report

    This method generates a report that summarizes the seller&#39;s promotions for the specified eBay marketplace. The report returns information on &lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;PAUSED&lt;/code&gt;, and &lt;code&gt;ENDED&lt;/code&gt; promotions (deleted reports are not returned) and summarizes the seller&#39;s campaign performance for all promotions on a given site.  &lt;br&gt;&lt;br&gt;For information about summary reports, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pm-summary-report.html\&quot;&gt;Reading the item promotion Summary report&lt;/a&gt;.

    :param marketplace_id: The eBay marketplace ID of the site you for which you want a promotion summary report.  &lt;p&gt;&lt;b&gt;Valid values:&lt;/b&gt;&lt;/p&gt;  &lt;ul&gt;&lt;li&gt;&lt;code&gt;EBAY_AU&lt;/code&gt; &#x3D; Australia&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_DE&lt;/code&gt; &#x3D; Germany&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_ES&lt;/code&gt; &#x3D; Spain&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_FR&lt;/code&gt; &#x3D; France&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_GB&lt;/code&gt; &#x3D; Great Britain&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_IT&lt;/code&gt; &#x3D; Italy&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_US&lt;/code&gt; &#x3D; United States&lt;/li&gt;&lt;/ul&gt;
    :type marketplace_id: str

    """
    return web.Response(status=200)
