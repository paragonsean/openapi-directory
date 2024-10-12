from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_customer_service_metric_response import GetCustomerServiceMetricResponse
from openapi_server import util


async def get_customer_service_metric(request: web.Request, customer_service_metric_type, evaluation_marketplace_id, evaluation_type) -> web.Response:
    """get_customer_service_metric

    Use this method to retrieve a seller&#39;s performance and rating for the customer service metric. Control the response from the getCustomerServiceMetric method using the following path and query parameters: customer_service_metric_type controls the type of customer service transactions evaluated for the metric rating. evaluation_type controls the period you want to review. evaluation_marketplace_id specifies the target marketplace for the evaluation. Currently, metric data is returned for only peer benchmarking. For more detail on the workings of peer benchmarking, see Service metrics policy.

    :param customer_service_metric_type: Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are: ITEM_NOT_AS_DESCRIBED ITEM_NOT_RECEIVED
    :type customer_service_metric_type: str
    :param evaluation_marketplace_id: Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data. For the list of supported marketplaces, see Analytics API requirements and restrictions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/devzone/rest/api-ref/analytics/types/MarketplaceIdEnum.html
    :type evaluation_marketplace_id: str
    :param evaluation_type: Use this path parameter to specify the type of the seller evaluation you want returned, either: CURRENT &amp;ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &amp;ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period.
    :type evaluation_type: str

    """
    return web.Response(status=200)
