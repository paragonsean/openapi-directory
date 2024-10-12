from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def create_product_module(request: web.Request, active, licensing_model, name, product_number, license_template=None, max_checkout_validity=None, node_secret_mode=None, number=None, red_threshold=None, yellow_threshold=None) -> web.Response:
    """Create Product Module

    Creates a new Product Module

    :param active: If set to &#39;false&#39;, the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module.
    :type active: bool
    :param licensing_model: Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation.
    :type licensing_model: str
    :param name: Product Module name that is visible to the end customers in NetLicensing Shop.
    :type name: str
    :param product_number: Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
    :type product_number: str
    :param license_template: License Template. Mandatory for &#39;Try &amp;amp; Buy&#39; licensing model.
    :type license_template: List[str]
    :param max_checkout_validity: Maximum checkout validity (days). Mandatory for &#39;Floating&#39; licensing model.
    :type max_checkout_validity: int
    :param node_secret_mode: Secret Mode. Mandatory for &#39;Node-Locked&#39; licensing model.
    :type node_secret_mode: List[str]
    :param number: Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
    :type number: str
    :param red_threshold: Remaining time volume for red level. Mandatory for &#39;Rental&#39; licensing model.
    :type red_threshold: int
    :param yellow_threshold: Remaining time volume for yellow level. Mandatory for &#39;Rental&#39; licensing model.
    :type yellow_threshold: int

    """
    return web.Response(status=200)


async def delete_product_module(request: web.Request, product_module_number, force_cascade=None) -> web.Response:
    """Delete Product Module

    Delete a Product Module by &#39;number&#39;

    :param product_module_number: Unique number (across all Products of a Vendor) that identifies the Product Module.
    :type product_module_number: str
    :param force_cascade: Force object deletion and all descendants.
    :type force_cascade: bool

    """
    return web.Response(status=200)


async def get_product_module(request: web.Request, product_module_number) -> web.Response:
    """Get Product Module

    Return a Product Module by &#39;productModuleNumber&#39;

    :param product_module_number: Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
    :type product_module_number: str

    """
    return web.Response(status=200)


async def list_product_modules(request: web.Request, ) -> web.Response:
    """List Product Modules

    Return a list of all Product Modules for the current Vendor


    """
    return web.Response(status=200)


async def update_product_module(request: web.Request, product_module_number, active=None, license_template=None, licensing_model=None, max_checkout_validity=None, name=None, node_secret_mode=None, number=None, red_threshold=None, yellow_threshold=None) -> web.Response:
    """Update Product Module

    Sets the provided properties to a Product Module. Return an updated Product Module

    :param product_module_number: Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
    :type product_module_number: str
    :param active: If set to &#39;false&#39;, the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module.
    :type active: bool
    :param license_template: License Template. Mandatory for &#39;Try &amp;amp; Buy&#39; licensing model.
    :type license_template: List[str]
    :param licensing_model: Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation.
    :type licensing_model: str
    :param max_checkout_validity: Maximum checkout validity (days). Mandatory for &#39;Floating&#39; licensing model.
    :type max_checkout_validity: int
    :param name: Product Module name that is visible to the end customers in NetLicensing Shop.
    :type name: str
    :param node_secret_mode: Secret Mode. Mandatory for &#39;Node-Locked&#39; licensing model.
    :type node_secret_mode: List[str]
    :param number: New Product Module number (update).
    :type number: str
    :param red_threshold: Remaining time volume for red level. Mandatory for &#39;Rental&#39; licensing model.
    :type red_threshold: int
    :param yellow_threshold: Remaining time volume for yellow level. Mandatory for &#39;Rental&#39; licensing model.
    :type yellow_threshold: int

    """
    return web.Response(status=200)
