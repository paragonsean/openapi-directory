from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_info import CategoryInfo
from openapi_server.models.category_metrics import CategoryMetrics
from openapi_server.models.category_subscription_info import CategorySubscriptionInfo
from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server import util


async def categories_images_get(request: web.Request, ) -> web.Response:
    """Gets the names of all alert category images.  You can get the image by going to account.signl4.com/images/alerts/categoryImageName.svg

    


    """
    return web.Response(status=200)


async def categories_team_id_category_id_delete(request: web.Request, team_id, category_id) -> web.Response:
    """Delete an existing category

    Sample Request:                    DELETE /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e

    :param team_id: ID of the team the category belongs to
    :type team_id: str
    :param category_id: ID of the category to delete
    :type category_id: str

    """
    return web.Response(status=200)


async def categories_team_id_category_id_get(request: web.Request, team_id, category_id) -> web.Response:
    """Get a specific category

    Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e

    :param team_id: ID of the team the category belongs to
    :type team_id: str
    :param category_id: ID of the category to get
    :type category_id: str

    """
    return web.Response(status=200)


async def categories_team_id_category_id_metrics_get(request: web.Request, team_id, category_id) -> web.Response:
    """Get metrics for a specific category

    Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/metrics

    :param team_id: ID of the team the category belongs to
    :type team_id: str
    :param category_id: ID of the category to get
    :type category_id: str

    """
    return web.Response(status=200)


async def categories_team_id_category_id_put(request: web.Request, team_id, category_id, body=None) -> web.Response:
    """Update an existing category

    Sample Request:                    PUT /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e      {          \&quot;name\&quot;: \&quot;Water-Updated\&quot;,          \&quot;imageName\&quot;: \&quot;water.svg\&quot;,          \&quot;color\&quot;: \&quot;#0000cc\&quot;,          \&quot;keywordMatching\&quot;: \&quot;All\&quot;,          \&quot;keywords\&quot;: [              {                  \&quot;value\&quot;: \&quot;H2O\&quot;              },              {                  \&quot;value\&quot;: \&quot;Water\&quot;              },              {                  \&quot;value\&quot;: \&quot;Wet\&quot;              }          ]      }

    :param team_id: ID of the team the category belongs to
    :type team_id: str
    :param category_id: 
    :type category_id: str
    :param body: Category to be updated
    :type body: dict | bytes

    """
    body = CategoryInfo.from_dict(body)
    return web.Response(status=200)


async def categories_team_id_category_id_subscriptions_get(request: web.Request, team_id, category_id) -> web.Response:
    """Get category subscriptions

    Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/subscriptions      {      }

    :param team_id: ID of the team the category belongs to
    :type team_id: str
    :param category_id: Category to get subscriptions for
    :type category_id: str

    """
    return web.Response(status=200)


async def categories_team_id_category_id_subscriptions_post(request: web.Request, team_id, category_id, body=None) -> web.Response:
    """Set category subscriptions

    Sample Request:                    POST /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/subscriptions      {      }

    :param team_id: ID of the team the category belongs to
    :type team_id: str
    :param category_id: Category to be updated
    :type category_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [CategorySubscriptionInfo.from_dict(d) for d in body]
    return web.Response(status=200)


async def categories_team_id_get(request: web.Request, team_id) -> web.Response:
    """Get all categories

    Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7

    :param team_id: ID of the team the categories belong to
    :type team_id: str

    """
    return web.Response(status=200)


async def categories_team_id_metrics_get(request: web.Request, team_id) -> web.Response:
    """Get metrics for all categories

    Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/metrics

    :param team_id: ID of the team the categories belongs to
    :type team_id: str

    """
    return web.Response(status=200)


async def categories_team_id_post(request: web.Request, team_id, body=None) -> web.Response:
    """Create a new category

    Sample Request:                    POST /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7      {          \&quot;name\&quot;: \&quot;Water\&quot;,          \&quot;imageName\&quot;: \&quot;water.svg\&quot;,          \&quot;color\&quot;: \&quot;#0000cc\&quot;,          \&quot;keywordMatching\&quot;: \&quot;Any\&quot;,          \&quot;keywords\&quot;: [              {                  \&quot;value\&quot;: \&quot;H2O\&quot;              },              {                  \&quot;value\&quot;: \&quot;Water\&quot;              }          ]      }

    :param team_id: ID of the team the category belongs to
    :type team_id: str
    :param body: Category to be created
    :type body: dict | bytes

    """
    body = CategoryInfo.from_dict(body)
    return web.Response(status=200)
