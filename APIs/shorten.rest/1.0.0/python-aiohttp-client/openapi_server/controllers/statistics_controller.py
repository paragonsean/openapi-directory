from typing import List, Dict
from aiohttp import web

from openapi_server.models.click_model_pg import ClickModelPg
from openapi_server.models.clicks_filter_model import ClicksFilterModel
from openapi_server import util


async def get_statistics(request: web.Request, body) -> web.Response:
    """Get clicks statistics

    Retrieve the raw click statistics for your account. Clicks are retrieved by creation date in descending order.

    :param body: Filter
    :type body: dict | bytes

    """
    body = ClicksFilterModel.from_dict(body)
    return web.Response(status=200)
