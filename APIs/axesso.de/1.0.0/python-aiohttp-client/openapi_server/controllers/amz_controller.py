from typing import List, Dict
from aiohttp import web

from openapi_server.models.buy_recommendation_response import BuyRecommendationResponse
from openapi_server.models.keyword_search_response import KeywordSearchResponse
from openapi_server.models.product_details_response import ProductDetailsResponse
from openapi_server.models.sort_option_response import SortOptionResponse
from openapi_server import util


async def keyword_search(request: web.Request, keyword, domain_code, sort_by=None, number_of_products=None) -> web.Response:
    """fetch results auf a keyword search on Amazon

    

    :param keyword: keyword to search
    :type keyword: str
    :param domain_code: domain for the search
    :type domain_code: str
    :param sort_by: sort option
    :type sort_by: str
    :param number_of_products: number of the results (max 20)
    :type number_of_products: int

    """
    return web.Response(status=200)


async def request_buy_recommendation(request: web.Request, url) -> web.Response:
    """request buy recommendations to a given product

    

    :param url: The url of the requested product.
    :type url: str

    """
    return web.Response(status=200)


async def request_product(request: web.Request, url, size=None) -> web.Response:
    """lookup product information

    

    :param url: The url of the requested product.
    :type url: str
    :param size: Size parameter if available.
    :type size: str

    """
    return web.Response(status=200)


async def sort_options(request: web.Request, ) -> web.Response:
    """request available sort options to use in keyword search

    


    """
    return web.Response(status=200)
