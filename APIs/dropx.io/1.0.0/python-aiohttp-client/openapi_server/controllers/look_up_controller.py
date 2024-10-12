from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def products_link_search_get(request: web.Request, url, providers=None) -> web.Response:
    """Search for similar products by providing a link to any e-commerce product.

    Returns list of e-commerce product that are close to the one provided -- one from each provider

    :param url: URL must be a url encoded value
    :type url: str
    :param providers: A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers
    :type providers: str

    """
    return web.Response(status=200)


async def products_link_search_v2_get(request: web.Request, url, providers=None) -> web.Response:
    """Search for similar products by providing a link to any e-commerce product.

    Returns list of e-commerce product that are close to the one provided -- one from each provider

    :param url: URL must be a url encoded value
    :type url: str
    :param providers: A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers
    :type providers: str

    """
    return web.Response(status=200)


async def products_search_get(request: web.Request, term, providers=None) -> web.Response:
    """Search for any product using title

    Returns one unique result from every provider that dropx.io tracks

    :param term: search terms giving any title of products that are sold online
    :type term: str
    :param providers: A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers
    :type providers: str

    """
    return web.Response(status=200)


async def products_search_v2_get(request: web.Request, term, providers=None) -> web.Response:
    """Search for any product using title

    Returns one unique result from every provider that dropx.io tracks

    :param term: search terms giving any title of products that are sold online
    :type term: str
    :param providers: A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers
    :type providers: str

    """
    return web.Response(status=200)


async def products_title_search_get(request: web.Request, term) -> web.Response:
    """Search for any product using title

    Returns list of product ids

    :param term: search terms giving any title of products that are sold online
    :type term: str

    """
    return web.Response(status=200)
