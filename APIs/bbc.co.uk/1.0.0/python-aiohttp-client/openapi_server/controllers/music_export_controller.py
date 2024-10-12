from typing import List, Dict
from aiohttp import web

from openapi_server.models.music_export_error_response import MusicExportErrorResponse
from openapi_server.models.music_export_job import MusicExportJob
from openapi_server.models.music_export_preferences import MusicExportPreferences
from openapi_server.models.music_export_preferences_response import MusicExportPreferencesResponse
from openapi_server.models.music_export_success import MusicExportSuccess
from openapi_server import util


async def delete_music_preferences_export(request: web.Request, authorization, x_authentication_provider, x_api_key) -> web.Response:
    """Music Export Preferences

    Remove export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str

    """
    return web.Response(status=200)


async def delete_music_preferences_export_vendor(request: web.Request, authorization, x_authentication_provider, x_api_key, vendor) -> web.Response:
    """Music Export Vendor Preferences

    Remove Vendor specific export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param vendor: Supported 3rd Party Vendor
    :type vendor: str

    """
    return web.Response(status=200)


async def get_music_export(request: web.Request, authorization, x_authentication_provider, x_api_key, offset=None, limit=None) -> web.Response:
    """Music Exports

    Returns status of all previous third party export actions for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_music_export_jobs(request: web.Request, authorization, x_authentication_provider, x_api_key, over16, vendor=None) -> web.Response:
    """Music Export Jobs

    All items associated to a users export request 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param over16: Boolean age check
    :type over16: bool
    :param vendor: Specify Vendor Jobs
    :type vendor: str

    """
    return web.Response(status=200)


async def get_music_export_tracks(request: web.Request, authorization, x_authentication_provider, x_api_key, over16, offset=None, limit=None, vendor=None, status=None) -> web.Response:
    """Music Export Tracks

    Retrieves vendor and status specific tracks 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param over16: Boolean age check
    :type over16: bool
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param vendor: Specify Vendor Tracks
    :type vendor: str
    :param status: Specify Track status
    :type status: str

    """
    return web.Response(status=200)


async def get_music_preferences_export(request: web.Request, authorization, x_authentication_provider, x_api_key) -> web.Response:
    """Music Export Preferences

    Returns export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str

    """
    return web.Response(status=200)


async def get_music_preferences_export_vendor(request: web.Request, authorization, x_authentication_provider, x_api_key, vendor) -> web.Response:
    """Music Export Vendor Preferences

    Returns vendor specific export preferences for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param vendor: Supported 3rd Party Vendor
    :type vendor: str

    """
    return web.Response(status=200)


async def post_music_export_job(request: web.Request, authorization, x_authentication_provider, x_api_key, over16, body, vendor=None) -> web.Response:
    """Music Export Jobs

    Create Export Job for a user 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param over16: Boolean age check
    :type over16: bool
    :param body: 
    :type body: list | bytes
    :param vendor: Specify Vendor Jobs
    :type vendor: str

    """
    body = [MusicExportJob.from_dict(d) for d in body]
    return web.Response(status=200)


async def post_music_preferences_export(request: web.Request, authorization, x_authentication_provider, x_api_key, body) -> web.Response:
    """Music Export Preferences

    Create export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = MusicExportPreferences.from_dict(body)
    return web.Response(status=200)


async def post_music_preferences_export_vendor(request: web.Request, authorization, x_authentication_provider, x_api_key, vendor, body) -> web.Response:
    """Music Export Vendor Preferences

    Create Vendor specific export preferences (e.g. 3rd party vendors, partner id&#39;s) for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param vendor: Supported 3rd Party Vendor
    :type vendor: str
    :param body: 
    :type body: dict | bytes

    """
    body = MusicExportPreferences.from_dict(body)
    return web.Response(status=200)


async def put_music_preferences_export_vendor(request: web.Request, authorization, x_authentication_provider, x_api_key, vendor, body) -> web.Response:
    """Music Export Vendor Preferences

    Update vendor specific export preferences for a given BBC Music user. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param vendor: Supported 3rd Party Vendor
    :type vendor: str
    :param body: 
    :type body: dict | bytes

    """
    body = MusicExportPreferences.from_dict(body)
    return web.Response(status=200)
