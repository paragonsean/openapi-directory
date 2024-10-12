from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_response import ExceptionResponse
from openapi_server.models.service import Service
from openapi_server.models.services_list_result import ServicesListResult
from openapi_server import util


async def services_get(request: web.Request, service_name, api_version) -> web.Response:
    """services_get

    Gets a specific Azure service for support ticket creation.

    :param service_name: Name of Azure service
    :type service_name: str
    :param api_version: Api version
    :type api_version: str

    """
    return web.Response(status=200)


async def services_list(request: web.Request, api_version) -> web.Response:
    """services_list

    Lists all the Azure services available for support ticket creation. Here are the Service Ids for **Billing**, **Subscription Management**, and **Service and subscription limits (Quotas)** issues: &lt;br/&gt;&lt;table&gt;&lt;tr&gt;&lt;td&gt;&lt;u&gt;Issue type&lt;/u&gt;&lt;/td&gt;&lt;td&gt;&lt;u&gt;Service Id&lt;/u&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Billing&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/517f2da6-78fd-0498-4e22-ad26996b1dfc&#39;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Subscription Management&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/f3dc5421-79ef-1efa-41a5-42bf3cbb52c6&#39;&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Quota&lt;/td&gt;&lt;td&gt;&#39;/providers/Microsoft.Support/services/06bfd9d3-516b-d5c6-5802-169c800dec89&#39;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; &lt;br/&gt;&lt;br/&gt; For **Technical** issues, select the Service Id that maps to the Azure service/product as displayed in the **Services** drop-down list on the Azure portal&#39;s &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/overview&#39;&gt;New support request&lt;/a&gt; page. &lt;br/&gt;&lt;br/&gt; Always use the service and it&#39;s corresponding problem classification(s) obtained programmatically for support ticket creation. This practice ensures that you always have the most recent set of service and problem classification Ids.

    :param api_version: Api version
    :type api_version: str

    """
    return web.Response(status=200)
