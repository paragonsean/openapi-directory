from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def create_license(request: web.Request, active, license_template_number, licensee_number, currency=None, hidden=None, name=None, number=None, parentfeature=None, price=None, quantity=None, start_date=None, time_volume=None, time_volume_period=None, used_quantity=None) -> web.Response:
    """Create License

    Creates a new License

    :param active: 
    :type active: bool
    :param license_template_number: 
    :type license_template_number: str
    :param licensee_number: 
    :type licensee_number: str
    :param currency: Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation
    :type currency: str
    :param hidden: If set to &#39;true&#39;, this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly
    :type hidden: bool
    :param name: Name for the Licensed item. Set from License Template on creation, if not specified explicitly.
    :type name: str
    :param number: 
    :type number: str
    :param parentfeature: Mandatory for &#39;TIMEVOLUME&#39; License Type and &#39;RENTAL&#39; licensing model
    :type parentfeature: str
    :param price: Price for the License. If &gt;0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation
    :type price: float
    :param quantity: Mandatory for &#39;Pay-per-Use&#39; License Model.
    :type quantity: str
    :param start_date: Mandatory for &#39;TIMEVOLUME&#39; License Type.
    :type start_date: str
    :param time_volume: Mandatory for &#39;TIMEVOLUME&#39; License Type.
    :type time_volume: str
    :param time_volume_period: For &#39;TIMEVOLUME&#39; License Type.
    :type time_volume_period: str
    :param used_quantity: Mandatory for &#39;Pay-per-Use&#39; License Model.
    :type used_quantity: str

    """
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)


async def delete_license(request: web.Request, license_number) -> web.Response:
    """Delete License

    Delete License by a &#39;licenseNumber&#39;

    :param license_number: Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
    :type license_number: str

    """
    return web.Response(status=200)


async def get_license(request: web.Request, license_number) -> web.Response:
    """Get License

    Get License by a &#39;licenseNumber&#39;

    :param license_number: Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
    :type license_number: str

    """
    return web.Response(status=200)


async def list_licenses(request: web.Request, ) -> web.Response:
    """List Licenses

    Return a list of all Licenses for the current Vendor


    """
    return web.Response(status=200)


async def update_license(request: web.Request, license_number, active=None, currency=None, hidden=None, name=None, number=None, parentfeature=None, price=None, quantity=None, start_date=None, time_volume=None, time_volume_period=None, used_quantity=None) -> web.Response:
    """Update License

    Update License by a &#39;licenseNumber&#39;

    :param license_number: Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
    :type license_number: str
    :param active: 
    :type active: bool
    :param currency: Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation
    :type currency: str
    :param hidden: If set to &#39;true&#39;, this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly
    :type hidden: bool
    :param name: Name for the Licensed item. Set from License Template on creation, if not specified explicitly.
    :type name: str
    :param number: Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
    :type number: str
    :param parentfeature: 
    :type parentfeature: str
    :param price: Price for the License. If &gt; 0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation
    :type price: float
    :param quantity: Mandatory for &#39;Pay-per-Use&#39; License Model.
    :type quantity: str
    :param start_date: For &#39;TIMEVOLUME&#39; License type
    :type start_date: str
    :param time_volume: Mandatory for &#39;TIMEVOLUME&#39; License Type.
    :type time_volume: str
    :param time_volume_period: For &#39;TIMEVOLUME&#39; License Type.
    :type time_volume_period: str
    :param used_quantity: Mandatory for &#39;Pay-per-Use&#39; License Model.
    :type used_quantity: str

    """
    start_date = util.deserialize_datetime(start_date)
    return web.Response(status=200)
