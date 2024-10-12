from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.model9 import Model9
from openapi_server import util


async def delete_api_validation_v1_campaign_settings_delete_campaignid(request: web.Request, apikey, campaign_id) -> web.Response:
    """delete campaign settings for a client

    

    :param apikey: API authentication key.
    :type apikey: str
    :param campaign_id: Remove campaign settings with a campaign ID
    :type campaign_id: str

    """
    return web.Response(status=200)


async def get_api_validation_v1_campaign_settings_campaignid(request: web.Request, apikey, campaign_id) -> web.Response:
    """get campaign settings for a client

    

    :param apikey: API authentication key.
    :type apikey: str
    :param campaign_id: The ID of the campaign to validate the receipt
    :type campaign_id: str

    """
    return web.Response(status=200)


async def get_api_validation_v1_campaign_settings_list(request: web.Request, apikey) -> web.Response:
    """list all campaign setting IDs for a client

    

    :param apikey: API authentication key.
    :type apikey: str

    """
    return web.Response(status=200)


async def post_api_validation_v1_campaign_file(request: web.Request, apikey, campaign_id, file=None, incognito=None, ip_address=None, near=None, reference_id=None) -> web.Response:
    """validate and match a receipt against a campaign validation settings by uploading an image file

    

    :param apikey: API authentication key.
    :type apikey: str
    :param campaign_id: The ID of the campaign to validate the receipt
    :type campaign_id: str
    :param file: file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
    :type file: str
    :param incognito: Set true to avoid saving the receipt in storage
    :type incognito: bool
    :param ip_address: IP Address of the end user
    :type ip_address: str
    :param near: A geo location to search for merchant. Typically in the format of city, state, country.
    :type near: str
    :param reference_id: Tag a request with a unique reference ID for feedback and training purposes
    :type reference_id: str

    """
    return web.Response(status=200)


async def post_api_validation_v1_campaign_productvalidation_file(request: web.Request, apikey, product_verification_number, file=None, incognito=None, sub_account_id=None, reference_id=None) -> web.Response:
    """validate if user-submitted info like serial number are detected an image file

    

    :param apikey: API authentication key.
    :type apikey: str
    :param product_verification_number: The number of the product to validate the receipt
    :type product_verification_number: str
    :param file: file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
    :type file: str
    :param incognito: Set true to avoid saving the receipt in storage
    :type incognito: bool
    :param sub_account_id: Tag a request with sub-account ID for billing purposes
    :type sub_account_id: str
    :param reference_id: Tag a request with a unique reference ID for feedback and training purposes
    :type reference_id: str

    """
    return web.Response(status=200)


async def post_api_validation_v1_campaign_settings_create_campaignid(request: web.Request, apikey, campaign_id, body=None) -> web.Response:
    """create campaign settings for a client

    

    :param apikey: API authentication key.
    :type apikey: str
    :param campaign_id: The ID of the campaign to validate the receipt
    :type campaign_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Model9.from_dict(body)
    return web.Response(status=200)


async def put_api_validation_v1_campaign_settings_update_campaignid(request: web.Request, apikey, campaign_id, body=None) -> web.Response:
    """update campaign settings for a client

    

    :param apikey: API authentication key.
    :type apikey: str
    :param campaign_id: The ID of the campaign to validate the receipt
    :type campaign_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Model9.from_dict(body)
    return web.Response(status=200)
