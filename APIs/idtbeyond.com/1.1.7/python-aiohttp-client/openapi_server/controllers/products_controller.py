from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def iatu_products_reports_all_csv_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key) -> web.Response:
    """Get a list of products in CSV format

    Returns a CSV of products, ranges, and their commissions percentages.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str

    """
    return web.Response(status=200)


async def iatu_products_reports_all_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key) -> web.Response:
    """Get a list of products in JSON format

    Returns a JSON list of products, ranges, and their commissions percentages.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str

    """
    return web.Response(status=200)


async def iatu_products_reports_local_value_get(request: web.Request, x_idt_beyond_app_id, x_idt_beyond_app_key, country_code, carrier_code, amount, currency_code) -> web.Response:
    """Get the estimated Local Value of a product

    Returns a CSV of products, ranges, and their commissions percentages.

    :param x_idt_beyond_app_id: Application ID you would like to use
    :type x_idt_beyond_app_id: str
    :param x_idt_beyond_app_key: Application KEY you would like to use
    :type x_idt_beyond_app_key: str
    :param country_code: 2-digit code of the country in ISO 3166 format. &#39;GT&#39;
    :type country_code: str
    :param carrier_code: Name of the mobile carrier. &#39;Claro&#39;
    :type carrier_code: str
    :param amount: This is the amount, in cents, of the product you are purchasing. &#39;500&#39; &#x3D; $5.00
    :type amount: int
    :param currency_code: The currency code (ISO 4217) on the product you are querying. &#39;USD&#39;
    :type currency_code: str

    """
    return web.Response(status=200)
