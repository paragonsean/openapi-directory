from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_preview_sets_response import AppPreviewSetsResponse
from openapi_server.models.app_screenshot_sets_response import AppScreenshotSetsResponse
from openapi_server.models.app_store_version_localization_create_request import AppStoreVersionLocalizationCreateRequest
from openapi_server.models.app_store_version_localization_response import AppStoreVersionLocalizationResponse
from openapi_server.models.app_store_version_localization_update_request import AppStoreVersionLocalizationUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_store_version_localizations_app_preview_sets_get_to_many_related(request: web.Request, id, filter_preview_type=None, fields_app_store_version_localizations=None, fields_app_previews=None, fields_app_preview_sets=None, limit=None, include=None) -> web.Response:
    """app_store_version_localizations_app_preview_sets_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_preview_type: filter by attribute &#39;previewType&#39;
    :type filter_preview_type: List[str]
    :param fields_app_store_version_localizations: the fields to include for returned resources of type appStoreVersionLocalizations
    :type fields_app_store_version_localizations: List[str]
    :param fields_app_previews: the fields to include for returned resources of type appPreviews
    :type fields_app_previews: List[str]
    :param fields_app_preview_sets: the fields to include for returned resources of type appPreviewSets
    :type fields_app_preview_sets: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_store_version_localizations_app_screenshot_sets_get_to_many_related(request: web.Request, id, filter_screenshot_display_type=None, fields_app_store_version_localizations=None, fields_app_screenshot_sets=None, fields_app_screenshots=None, limit=None, include=None) -> web.Response:
    """app_store_version_localizations_app_screenshot_sets_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_screenshot_display_type: filter by attribute &#39;screenshotDisplayType&#39;
    :type filter_screenshot_display_type: List[str]
    :param fields_app_store_version_localizations: the fields to include for returned resources of type appStoreVersionLocalizations
    :type fields_app_store_version_localizations: List[str]
    :param fields_app_screenshot_sets: the fields to include for returned resources of type appScreenshotSets
    :type fields_app_screenshot_sets: List[str]
    :param fields_app_screenshots: the fields to include for returned resources of type appScreenshots
    :type fields_app_screenshots: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_store_version_localizations_create_instance(request: web.Request, body) -> web.Response:
    """app_store_version_localizations_create_instance

    

    :param body: AppStoreVersionLocalization representation
    :type body: dict | bytes

    """
    body = AppStoreVersionLocalizationCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_store_version_localizations_delete_instance(request: web.Request, id) -> web.Response:
    """app_store_version_localizations_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_store_version_localizations_get_instance(request: web.Request, id, fields_app_store_version_localizations=None, include=None, fields_app_screenshot_sets=None, fields_app_preview_sets=None, limit_app_preview_sets=None, limit_app_screenshot_sets=None) -> web.Response:
    """app_store_version_localizations_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_store_version_localizations: the fields to include for returned resources of type appStoreVersionLocalizations
    :type fields_app_store_version_localizations: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_screenshot_sets: the fields to include for returned resources of type appScreenshotSets
    :type fields_app_screenshot_sets: List[str]
    :param fields_app_preview_sets: the fields to include for returned resources of type appPreviewSets
    :type fields_app_preview_sets: List[str]
    :param limit_app_preview_sets: maximum number of related appPreviewSets returned (when they are included)
    :type limit_app_preview_sets: int
    :param limit_app_screenshot_sets: maximum number of related appScreenshotSets returned (when they are included)
    :type limit_app_screenshot_sets: int

    """
    return web.Response(status=200)


async def app_store_version_localizations_update_instance(request: web.Request, id, body) -> web.Response:
    """app_store_version_localizations_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppStoreVersionLocalization representation
    :type body: dict | bytes

    """
    body = AppStoreVersionLocalizationUpdateRequest.from_dict(body)
    return web.Response(status=200)
