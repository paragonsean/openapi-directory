from typing import List, Dict
from aiohttp import web

from openapi_server.models.objects_metadata import ObjectsMetadata
from openapi_server.models.swagger_docs import SwaggerDocs
from openapi_server import util


async def get_objects(request: web.Request, authorization, elements_version=None) -> web.Response:
    """Get a list of all the available objects.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param elements_version: Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen
    :type elements_version: str

    """
    return web.Response(status=200)


async def get_objects_object_name_docs(request: web.Request, authorization, object_name, discovery=None, resolve_references=None, basic=None, version=None) -> web.Response:
    """Get swagger docs for an object.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param discovery: Include discovery metadata in definitions
    :type discovery: bool
    :param resolve_references: Optionally resolve swagger references for an inline object definition
    :type resolve_references: bool
    :param basic: Include only OpenAPI / Swagger properties in definitions
    :type basic: bool
    :param version: The element swagger version to get the corresponding element swagger, Passing in \&quot;-1\&quot; gives latest element swagger
    :type version: str

    """
    return web.Response(status=200)


async def get_objects_object_name_metadata(request: web.Request, authorization, object_name, elements_version=None) -> web.Response:
    """Get a list of all the field for an object.

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param elements_version: Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen
    :type elements_version: str

    """
    return web.Response(status=200)
