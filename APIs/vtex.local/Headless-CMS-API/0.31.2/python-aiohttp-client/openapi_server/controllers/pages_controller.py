from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_all_content_types200_response import GetAllContentTypes200Response
from openapi_server.models.get_cm_spage200_response import GetCMSpage200Response
from openapi_server.models.get_pagesby_content_type200_response import GetPagesbyContentType200Response
from openapi_server import util


async def get_all_content_types(request: web.Request, builder_id) -> web.Response:
    """Get all Content Types

    Gets data from all Content Types.

    :param builder_id: Builder ID specified in the settings of the CMS app.
    :type builder_id: str

    """
    return web.Response(status=200)


async def get_cm_spage(request: web.Request, builder_id, content_type, document_id, version_id=None, release_id=None) -> web.Response:
    """Get CMS page

    Gets all data from a given page.

    :param builder_id: Builder ID specified in the settings of the CMS app.
    :type builder_id: str
    :param content_type: Content Type ID defined in the FastStore project.
    :type content_type: str
    :param document_id: Document ID presented in the URL path of a CMS preview.
    :type document_id: str
    :param version_id: Version ID presented in the URL path of a CMS preview.
    :type version_id: str
    :param release_id: Release ID presented in the URL path of a CMS preview.
    :type release_id: str

    """
    return web.Response(status=200)


async def get_pagesby_content_type(request: web.Request, builder_id, content_type, version_id=None, release_id=None, filters_field=None) -> web.Response:
    """Get all CMS pages by Content Type

    Gets data from all pages of a given Content Type.

    :param builder_id: Builder ID specified in the settings of the CMS app.
    :type builder_id: str
    :param content_type: Content Type identifier defined in the FastStore project.
    :type content_type: str
    :param version_id: Version ID presented in the URL path of a CMS preview.
    :type version_id: str
    :param release_id: Release ID presented in the URL path of a CMS preview.
    :type release_id: str
    :param filters_field: Filter results by a property of the page (e.g., &#x60;filters[status]&#x60;) or by a nested custom field of the &#x60;parameters&#x60; object (e.g., &#x60;filters[parameters.collection.sort]&#x60;). *Replace {field} with the desired property.*
    :type filters_field: str

    """
    return web.Response(status=200)
