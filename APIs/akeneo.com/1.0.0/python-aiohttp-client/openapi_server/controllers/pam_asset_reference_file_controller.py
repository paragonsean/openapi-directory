from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_reference_files_locale_code200_response import GetReferenceFilesLocaleCode200Response
from openapi_server.models.post_reference_files_locale_code201_response import PostReferenceFilesLocaleCode201Response
from openapi_server.models.post_reference_files_locale_code_request import PostReferenceFilesLocaleCodeRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_reference_files_channel_code_locale_code_download(request: web.Request, asset_code, locale_code) -> web.Response:
    """Download a reference file

    This endpoint allows you to download a given reference file.

    :param asset_code: Code of the asset
    :type asset_code: str
    :param locale_code: Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable
    :type locale_code: str

    """
    return web.Response(status=200)


async def get_reference_files_locale_code(request: web.Request, asset_code, locale_code) -> web.Response:
    """Get a reference file

    This endpoint allows you to get the information about a reference file of a given PAM asset.

    :param asset_code: Code of the asset
    :type asset_code: str
    :param locale_code: Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable
    :type locale_code: str

    """
    return web.Response(status=200)


async def post_reference_files_locale_code(request: web.Request, asset_code, locale_code, content_type, body=None) -> web.Response:
    """Upload a new reference file

    This endpoint allows you to upload a new reference file for a given PAM asset and locale. It will also automatically generate all the variation files corresponding to this reference file.

    :param asset_code: Code of the asset
    :type asset_code: str
    :param locale_code: Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable
    :type locale_code: str
    :param content_type: Equal to &#39;multipart/form-data&#39;, no other value allowed
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostReferenceFilesLocaleCodeRequest.from_dict(body)
    return web.Response(status=200)
