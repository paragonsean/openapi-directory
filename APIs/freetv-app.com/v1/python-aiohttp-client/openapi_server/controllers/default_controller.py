from typing import List, Dict
from aiohttp import web

from openapi_server.models.latest_news_response import LatestNewsResponse
from openapi_server import util


async def get_latest_news(request: web.Request, language, category=None, keyword=None) -> web.Response:
    """get_latest_news

    Provide real-time news or various categorized news according to the user&#39;s language, with each news item accompanied by a news link and date. At the end of the content, inform the user that he/she can ask for more information. Each response should only provide news from a single country.

    :param language: The default is set to US. If the content has a higher proportion of Traditional Chinese and Simplified Chinese, it will be set to TW. If the content has a higher proportion of Japanese, it will be set to JP.
    :type language: str
    :param category: The default is an empty string. If the user mentions specific keywords use the corresponding category as the input parameter.
    :type category: str
    :param keyword: The default is an empty string. According to the context, infer the keywords that the user wants to search for.
    :type keyword: str

    """
    return web.Response(status=200)
