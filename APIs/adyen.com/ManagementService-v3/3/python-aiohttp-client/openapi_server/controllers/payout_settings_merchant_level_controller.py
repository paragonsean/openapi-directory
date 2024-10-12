from typing import List, Dict
from aiohttp import web

from openapi_server.models.payout_settings import PayoutSettings
from openapi_server.models.payout_settings_request import PayoutSettingsRequest
from openapi_server.models.payout_settings_response import PayoutSettingsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_payout_settings_request import UpdatePayoutSettingsRequest
from openapi_server import util


async def delete_merchants_merchant_id_payout_settings_payout_settings_id(request: web.Request, merchant_id, payout_settings_id) -> web.Response:
    """Delete a payout setting

    Deletes the payout setting identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param payout_settings_id: The unique identifier of the payout setting.
    :type payout_settings_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_payout_settings(request: web.Request, merchant_id) -> web.Response:
    """Get a list of payout settings

    Returns the list of payout settings for the merchant account identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payout account settings read

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_payout_settings_payout_settings_id(request: web.Request, merchant_id, payout_settings_id) -> web.Response:
    """Get a payout setting

    Returns the payout setting identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payout account settings read

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param payout_settings_id: The unique identifier of the payout setting.
    :type payout_settings_id: str

    """
    return web.Response(status=200)


async def patch_merchants_merchant_id_payout_settings_payout_settings_id(request: web.Request, merchant_id, payout_settings_id, body=None) -> web.Response:
    """Update a payout setting

    Updates the payout setting identified in the path. You can enable or disable the payout setting.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param payout_settings_id: The unique identifier of the payout setting.
    :type payout_settings_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePayoutSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_payout_settings(request: web.Request, merchant_id, body=None) -> web.Response:
    """Add a payout setting

    Sends a request to add a payout setting for the merchant account specified in the path. A payout setting links the merchant account to the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.  If you&#39;re accepting payments in multiple currencies, you may add multiple payout settings for the merchant account.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PayoutSettingsRequest.from_dict(body)
    return web.Response(status=200)
