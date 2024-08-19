from typing import List, Dict
from aiohttp import web

from openapi_server.models.accountregistration167_wrapper import Accountregistration167Wrapper
from openapi_server.models.accountregistration168_wrapper import Accountregistration168Wrapper
from openapi_server.models.accountregistration169_wrapper import Accountregistration169Wrapper
from openapi_server.models.accountregistration170_wrapper import Accountregistration170Wrapper
from openapi_server.models.accountregistration171_wrapper import Accountregistration171Wrapper
from openapi_server.models.accountregistration172_wrapper import Accountregistration172Wrapper
from openapi_server import util


async def create_transfer_notification_registration(request: web.Request, partner_id, accountregistration=None) -> web.Response:
    """This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction.

    This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction.

    :param partner_id: Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
    :type partner_id: str
    :param accountregistration: Contains the details of the request message.
    :type accountregistration: dict | bytes

    """
    accountregistration = Accountregistration167Wrapper.from_dict(accountregistration)
    return web.Response(status=200)


async def delete_transfer_notification_registration(request: web.Request, partner_id, account_reg_ref) -> web.Response:
    """This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications. 

    This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications. 

    :param partner_id: Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
    :type partner_id: str
    :param account_reg_ref: Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40
    :type account_reg_ref: str

    """
    return web.Response(status=200)


async def notification_registration_api_read_by(request: web.Request, partner_id, account_reg_ref) -> web.Response:
    """This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider&#39;s information for a registered PAN for notifications. 

    This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider&#39;s information for a registered PAN for notifications. 

    :param partner_id: Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
    :type partner_id: str
    :param account_reg_ref: Path Param - System generated unique account registration identifier. Type: Alphanumberic Special Length: 40
    :type account_reg_ref: str

    """
    return web.Response(status=200)


async def notification_registration_api_update(request: web.Request, partner_id, account_reg_ref, accountregistration=None) -> web.Response:
    """This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN.

    This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN.

    :param partner_id: Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
    :type partner_id: str
    :param account_reg_ref: Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40
    :type account_reg_ref: str
    :param accountregistration: Contains the details of the request message.
    :type accountregistration: dict | bytes

    """
    accountregistration = Accountregistration169Wrapper.from_dict(accountregistration)
    return web.Response(status=200)
