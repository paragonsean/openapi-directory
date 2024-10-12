from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def create_product(request: web.Request, active, name, version, description=None, licensee_auto_create=None, licensing_info=None, number=None, vat_mode=None) -> web.Response:
    """Create Product

    Creates a new Product

    :param active: If set to &#39;false&#39;, the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses.
    :type active: bool
    :param name: Product name. Together with the version identifies the Product for the end customer.
    :type name: str
    :param version: Product version. Convenience parameter, additional to the Product name.
    :type version: str
    :param description: Product description.
    :type description: str
    :param licensee_auto_create: If set to &#39;true&#39;, non-existing Licensees will be created at first validation attempt.
    :type licensee_auto_create: bool
    :param licensing_info: Licensing information.
    :type licensing_info: str
    :param number: Unique number that identifies the Product. Vendor can assign this number when creating a Product or let NetLicensing generate one.
    :type number: str
    :param vat_mode: Vat mode for Product. Supported types: GROSS, NET
    :type vat_mode: str

    """
    return web.Response(status=200)


async def delete_product(request: web.Request, product_number, force_cascade=None) -> web.Response:
    """Delete Product

    Delete a Product by &#39;number&#39;

    :param product_number: Unique number that identifies the Product.
    :type product_number: str
    :param force_cascade: Force object deletion and all descendants.
    :type force_cascade: bool

    """
    return web.Response(status=200)


async def list_products(request: web.Request, ) -> web.Response:
    """List Products

    Return a list of all configured Products for the current Vendor


    """
    return web.Response(status=200)


async def product_number(request: web.Request, product_number) -> web.Response:
    """Get Product

    Return a Product by &#39;productNumber&#39;

    :param product_number: Unique number that identifies the Product.
    :type product_number: str

    """
    return web.Response(status=200)


async def update_product(request: web.Request, product_number, active=None, description=None, licensee_auto_create=None, licensing_info=None, name=None, number=None, vat_mode=None, version=None) -> web.Response:
    """Update Product

    Sets the provided properties to a Product. Return an updated Product

    :param product_number: Unique number that identifies the Product.
    :type product_number: str
    :param active: If set to &#39;false&#39;, the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses.
    :type active: bool
    :param description: Product description.
    :type description: str
    :param licensee_auto_create: If set to &#39;true&#39;, non-existing Licensees will be created at first validation attempt.
    :type licensee_auto_create: bool
    :param licensing_info: Licensing information.
    :type licensing_info: str
    :param name: Product name. Together with the version identifies the Product for the end customer.
    :type name: str
    :param number: New Product number (update)
    :type number: str
    :param vat_mode: Vat mode for Product. Supported types: GROSS, NET
    :type vat_mode: str
    :param version: Product version. Convenience parameter, additional to the Product name.
    :type version: str

    """
    return web.Response(status=200)
