from typing import List, Dict
from aiohttp import web

from openapi_server.models.crawl200_response import Crawl200Response
from openapi_server.models.get_the_status_of_the_api_service200_response import GetTheStatusOfTheAPIService200Response
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.images200_response import Images200Response
from openapi_server.models.news200_response import News200Response
from openapi_server.models.search200_response import Search200Response
from openapi_server.models.serp200_response import Serp200Response
from openapi_server.models.serp_data import SerpData
from openapi_server import util


async def crawl(request: web.Request, query) -> web.Response:
    """Crawl

    Perform Google Search   Parameters ---------- query : the string query to perform search. supports advance queries. Check out https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters guide for formating  Returns ------- json: a the html source of the results page

    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def get_the_status_of_the_api_service(request: web.Request, ) -> web.Response:
    """Status

    It \&quot;status\&quot; &#x3D;&#x3D; true then API is up, else the API is down


    """
    return web.Response(status=200)


async def images(request: web.Request, query) -> web.Response:
    """Images

    Perform Google Image Search  Parameters ---------- query : the string query to perform search. supports advance queries.  Returns ------- json: a list of results with the link, description, and title for each result

    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def news(request: web.Request, query) -> web.Response:
    """News

    Perform Google News Search   Parameters ---------- query : the string query to perform search for Google news. A simple query for &#x60;president&#x60; will be &#x60;q&#x3D;president&#x60;. An example of multiple keyword would be &#x60;q&#x3D;news+about+presdient+trump&#x60;. News can also be filtered by country and language. For &#x60;US&#x60; news and in English the query will be &#x60;q&#x3D;trump&amp;ceid&#x3D;US:en&#x60; for news in Great Britian the query will be &#x60;q&#x3D;trump&amp;ceid&#x3D;GB:en&#x60;  Returns ------- json: {\&quot;feed\&quot;: { \&quot;title\&quot; : \&quot;trump\&quot; ...} , \&quot;entites\&quot;: [ {\&quot;title\&quot; : \&quot;Trump doubles down on divisive messaging in speech to honor Independence Day - CNN\&quot;, \&quot;links\&quot;: []} ...]}

    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def search(request: web.Request, query) -> web.Response:
    """Search

    Perform Google Search  Parameters ---------- query : the string query to perform search. supports advance queries. Check out https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters guide for formating  Returns ------- json: a list of results with the link, description, and title for each result

    :param query: 
    :type query: str

    """
    return web.Response(status=200)


async def serp(request: web.Request, body) -> web.Response:
    """SERP

    Perform Google Search and search for website in Search Engine Results Pages (SERP)  Parameters ---------- query : the string query to perform search. supports advance queries. Check out https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters guide for formatting, it is recommended to set the query &#x60;&amp;num&#x3D;100&#x60;  Returns ------- json: a list of results with the query, website, searched_results, and position. json[\&quot;position\&quot;] will be set to -1 if website is not found in results

    :param body: 
    :type body: dict | bytes

    """
    body = SerpData.from_dict(body)
    return web.Response(status=200)
