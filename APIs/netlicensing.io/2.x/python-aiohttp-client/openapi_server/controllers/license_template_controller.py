from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def create_license_template(request: web.Request, active, license_type, name, product_module_number, automatic=None, currency=None, hidden=None, hide_licenses=None, max_sessions=None, number=None, price=None, quantity=None, quota=None, time_volume=None, time_volume_period=None) -> web.Response:
    """Create License Template

    Creates a new License Template

    :param active: If set to &#39;false&#39;, the License Template is disabled. Licensee can not obtain any new Licenses off this License Template.
    :type active: bool
    :param license_type: Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY
    :type license_type: str
    :param name: License Template name to create License Template object
    :type name: str
    :param product_module_number: Number of Product Module to create License Template object
    :type product_module_number: str
    :param automatic: If set to &#39;true&#39;, every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0.
    :type automatic: bool
    :param currency: Specifies currency for the License price. Check data types to discover which currencies are supported.
    :type currency: str
    :param hidden: If set to &#39;true&#39;, this License Template is not shown in NetLicensing Shop as offered for purchase.
    :type hidden: bool
    :param hide_licenses: If set to &#39;true&#39;, Licenses from this License Template are not visible to the end customer, but participate in validation.
    :type hide_licenses: bool
    :param max_sessions: Mandatory for &#39;FLOATING&#39; License Type.
    :type max_sessions: str
    :param number: Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
    :type number: str
    :param price: Price for the License. If &gt;0, it must always be accompanied by the currency specification.
    :type price: float
    :param quantity: Mandatory for &#39;Pay-per-Use&#39; and &#39;Node-Locked&#39; License Model.
    :type quantity: str
    :param quota: Mandatory for &#39;Quota&#39; License Model.
    :type quota: str
    :param time_volume: Mandatory for &#39;TIMEVOLUME&#39; License Type.
    :type time_volume: str
    :param time_volume_period: For &#39;TIMEVOLUME&#39; License Type.
    :type time_volume_period: str

    """
    return web.Response(status=200)


async def delete_license_template(request: web.Request, license_template_number, force_cascade=None) -> web.Response:
    """Delete License Template

    Delete a License Template by &#39;number&#39;.

    :param license_template_number: Unique number (across all Products of a Vendor) that identifies the License Template.
    :type license_template_number: str
    :param force_cascade: Force object deletion and all descendants.
    :type force_cascade: bool

    """
    return web.Response(status=200)


async def get_license_template(request: web.Request, license_template_number) -> web.Response:
    """Get License Template

    Return a License Template by &#39;licenseTemplateNumber&#39;

    :param license_template_number: Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
    :type license_template_number: str

    """
    return web.Response(status=200)


async def list_license_templates(request: web.Request, ) -> web.Response:
    """List License Templates

    Return a list of all License Templates for the current Vendor


    """
    return web.Response(status=200)


async def update_license_template(request: web.Request, license_template_number, active=None, automatic=None, currency=None, hidden=None, hide_licenses=None, license_type=None, max_sessions=None, name=None, number=None, price=None, quantity=None, quota=None, time_volume=None, time_volume_period=None) -> web.Response:
    """Update License Template

    Sets the provided properties to a License Template. Return an updated License Template

    :param license_template_number: Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
    :type license_template_number: str
    :param active: If set to &#39;false&#39;, the License Template is disabled. Licensee can not obtain any new Licenses off this License Template.
    :type active: bool
    :param automatic: If set to &#39;true&#39;, every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0.
    :type automatic: bool
    :param currency: Specifies currency for the License price. Check data types to discover which currencies are supported.
    :type currency: str
    :param hidden: If set to &#39;true&#39;, this License Template is not shown in NetLicensing Shop as offered for purchase.
    :type hidden: bool
    :param hide_licenses: If set to &#39;true&#39;, Licenses from this License Template are not visible to the end customer, but participate in validation.
    :type hide_licenses: bool
    :param license_type: Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY
    :type license_type: str
    :param max_sessions: Mandatory for &#39;FLOATING&#39; License Type.
    :type max_sessions: str
    :param name: Name for the Licensed item
    :type name: str
    :param number: New License Template number (update).
    :type number: str
    :param price: Price for the License. If &gt;0, it must always be accompanied by the currency specification.
    :type price: float
    :param quantity: Mandatory for &#39;Pay-per-Use&#39; and &#39;Node-Locked&#39; License Model.
    :type quantity: str
    :param quota: Mandatory for &#39;Quota&#39; License Model.
    :type quota: str
    :param time_volume: Mandatory for &#39;TIMEVOLUME&#39; License Type.
    :type time_volume: str
    :param time_volume_period: For &#39;TIMEVOLUME&#39; License Type.
    :type time_volume_period: str

    """
    return web.Response(status=200)
