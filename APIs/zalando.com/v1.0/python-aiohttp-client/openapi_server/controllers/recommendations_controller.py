from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.recommendations_article import RecommendationsArticle
from openapi_server import util


async def recommendations_article_ids_get(request: web.Request, article_ids, max_results=None, accept_language=None, fields=None) -> web.Response:
    """Get Recommendations by articleId

    Zalando API Recommendations Schema

    :param article_ids: To get Recommendations by articleIds.
    :type article_ids: List[str]
    :param max_results: To get maximum results of Recommendations by articleId.
    :type max_results: str
    :param accept_language: Specify which Shop to use.  A standard &#x60;Accept-Language&#x60; header which specifies the shop that should be used. E.g. &#x60;de-DE&#x60; will use the German shop (as does [https://www.zalando.de](https://www/zalando.de) and &#x60;de-AT&#x60; will use the Austrian one.  The shop choosen will e.g. define the currency used for prices as well as the language for product names and descriptions. Furthermore it will impact which articles are available as they might differ between countries.
    :type accept_language: str
    :param fields: Comma separated list of fields that should be returned. Fields of subobjects are specified with dots as separator. Fields of objects within lists are specified in the same way.  Example: id,name,brand.key,brand.name, units.id,units.size,units.price.formatted
    :type fields: List[str]

    """
    return web.Response(status=200)
