from typing import List, Dict
from aiohttp import web

from openapi_server.models.netlicensing import Netlicensing
from openapi_server import util


async def create_licensee(request: web.Request, active, product_number, marked_for_transfer=None, name=None, number=None) -> web.Response:
    """Create Licensee

    Creates a new Licensee

    :param active: If set to &#39;false&#39;, the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled
    :type active: bool
    :param product_number: &#39;productNumber&#39; to assign new Licensee object
    :type product_number: str
    :param marked_for_transfer: Mark Licensee for transfer.
    :type marked_for_transfer: bool
    :param name: 
    :type name: str
    :param number: Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee
    :type number: str

    """
    return web.Response(status=200)


async def delete_licensee(request: web.Request, licensee_number, force_cascade=None) -> web.Response:
    """Delete Licensee

    Delete a Licensee by &#39;number&#39;

    :param licensee_number: Unique number (across all Products of a Vendor) that identifies the Licensee.
    :type licensee_number: str
    :param force_cascade: Force object deletion and all descendants.
    :type force_cascade: bool

    """
    return web.Response(status=200)


async def get_licensee(request: web.Request, licensee_number) -> web.Response:
    """Get Licensee

    Return a Licensee by &#39;licenseeNumber&#39;

    :param licensee_number: Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee.
    :type licensee_number: str

    """
    return web.Response(status=200)


async def list_licensees(request: web.Request, ) -> web.Response:
    """List Licensees

    Return a list of all Licensees for the current Vendor


    """
    return web.Response(status=200)


async def transfer_licenses(request: web.Request, licensee_number, source_licensee_number) -> web.Response:
    """Transfer Licenses

    Licenses transfer between Licensees

    :param licensee_number: Licensee number with a maximum length of 1000 characters
    :type licensee_number: str
    :param source_licensee_number: Licensee number which Licenses to be transferred
    :type source_licensee_number: str

    """
    return web.Response(status=200)


async def update_licensee(request: web.Request, licensee_number, active=None, marked_for_transfer=None, name=None, number=None) -> web.Response:
    """Update Licensee

    Sets the provided properties to a Licensee. Return an updated Licensee

    :param licensee_number: Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee.
    :type licensee_number: str
    :param active: If set to &#39;false&#39;, the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled
    :type active: bool
    :param marked_for_transfer: Mark Licensee for transfer.
    :type marked_for_transfer: bool
    :param name: 
    :type name: str
    :param number: New Licensee number (update).
    :type number: str

    """
    return web.Response(status=200)


async def validate_licensee(request: web.Request, licensee_number, action=None, licensee_name=None, node_secret=None, product_module_number=None, product_number=None, session_id=None) -> web.Response:
    """Validate Licensee

    Validates active Licenses of the Licensee

    :param licensee_number: Licensee number with a maximum length of 1000 characters
    :type licensee_number: str
    :param action: &#39;Floating&#39; licensing model: check-out or check-in session action, to allocate or return it from/to the pool of available sessions
    :type action: str
    :param licensee_name: Human-readable name for the auto-created Licensee (will be set as custom Licensee property)
    :type licensee_name: str
    :param node_secret: &#39;Node-Locked&#39; licensing model: specifies unique secret
    :type node_secret: str
    :param product_module_number: &#39;Node-Locked&#39; licensing model: product module number
    :type product_module_number: str
    :param product_number: Product number, must be provided when &#39;Licensee auto-create&#39; is enabled (see also Product JavaDoc). Identifies the Product to which new Licensee should be added
    :type product_number: str
    :param session_id: &#39;Floating&#39; licensing model: specifies unique session identifier
    :type session_id: str

    """
    return web.Response(status=200)
