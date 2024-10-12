from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def convert_api(request: web.Request, format, url=None) -> web.Response:
    """Transform API Descriptions from/to various formats

    Transform API Descriptions from/to various formats e.g., Swagger, API Blueprint, RAML, WADL, Google Discovery, I/O Docs.  ### INPUTS * API Blueprint * Swagger 1.0 - 1.2 * Swagger 2.0 JSON * Swagger 2.0 YAML * WADL - W3C 2009 * Google Discovery * RAML 0.8 * I/O Docs - Mashery * HAR 1.2 * Postman Collection 1.0 - 2.0 * APIMATIC Format * Mashape  ### OUTPUTS * API Blueprint * Swagger 1.2 * Swagger 2.0 JSON * Swagger 2.0 YAML * WADL - W3C 2009 * RAML 0.8 - 1.0 * APIMATIC Format

    :param format: 
    :type format: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)
