from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_variation_files_channel_code_locale_code200_response import GetVariationFilesChannelCodeLocaleCode200Response
from openapi_server.models.post_reference_files_locale_code_request import PostReferenceFilesLocaleCodeRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_variation_files_channel_code_locale_code(request: web.Request, asset_code, channel_code, locale_code) -> web.Response:
    """Get a variation file

    This endpoint allows you to get the information about a variation file of a given PAM asset.

    :param asset_code: Code of the asset
    :type asset_code: str
    :param channel_code: Code of the channel
    :type channel_code: str
    :param locale_code: Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable
    :type locale_code: str

    """
    return web.Response(status=200)


async def get_variation_files_channel_code_locale_code_download(request: web.Request, asset_code, channel_code, locale_code) -> web.Response:
    """Download a variation file

    This endpoint allows you to download a given variation file.

    :param asset_code: Code of the asset
    :type asset_code: str
    :param channel_code: Code of the channel
    :type channel_code: str
    :param locale_code: Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable
    :type locale_code: str

    """
    return web.Response(status=200)


async def post_variation_files_channel_code_locale_code(request: web.Request, asset_code, channel_code, locale_code, content_type, body=None) -> web.Response:
    """Upload a new variation file

    This endpoint allows you to upload a new variation file for a given PAM asset, channel and locale.

    :param asset_code: Code of the asset
    :type asset_code: str
    :param channel_code: Code of the channel
    :type channel_code: str
    :param locale_code: Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable
    :type locale_code: str
    :param content_type: Equal to &#39;multipart/form-data&#39;, no other value allowed
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostReferenceFilesLocaleCodeRequest.from_dict(body)
    return web.Response(status=200)
