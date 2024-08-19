from typing import List, Dict
from aiohttp import web

from openapi_server.models.object import Object
from openapi_server import util


async def create_by_object_name(request: web.Request, authorization, object_name, body) -> web.Response:
    """Create an {objectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param body: The {objectName}
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def create_object_name_by_child_object_name(request: web.Request, authorization, object_name, object_id, child_object_name, body) -> web.Response:
    """Create an {objectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str
    :param child_object_name: The name of the object
    :type child_object_name: str
    :param body: The {childObjectName}
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def delete_object_name_by_child_object_id(request: web.Request, authorization, object_name, child_object_name, object_id, child_object_id) -> web.Response:
    """Delete an {childObjectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param child_object_name: The name of the childObjectName
    :type child_object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str
    :param child_object_id: The {childObjectName} ID
    :type child_object_id: str

    """
    return web.Response(status=200)


async def delete_object_name_by_object_id(request: web.Request, authorization, object_name, object_id) -> web.Response:
    """Delete an {objectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str

    """
    return web.Response(status=200)


async def get_by_object_name(request: web.Request, authorization, object_name, where=None, page_size=None, next_page=None, fields=None) -> web.Response:
    """Search for {objectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param where: The CEQL search expression.
    :type where: str
    :param page_size: The page size. Defaults to 200 if not provided. Maximum of 5000.
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def get_object_name_by_child_object_id(request: web.Request, authorization, object_name, child_object_name, object_id, child_object_id) -> web.Response:
    """Retrieve an {childObjectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param child_object_name: The name of the childObjectName
    :type child_object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str
    :param child_object_id: The {childObjectName} ID
    :type child_object_id: str

    """
    return web.Response(status=200)


async def get_object_name_by_child_object_name(request: web.Request, authorization, object_name, object_id, child_object_name, where=None, page_size=None, next_page=None, fields=None) -> web.Response:
    """Search for {childObjectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str
    :param child_object_name: The name of the childObjectName
    :type child_object_name: str
    :param where: The CEQL search expression.
    :type where: str
    :param page_size: The page size. Defaults to 200 if not provided. Maximum of 5000.
    :type page_size: int
    :param next_page: The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60;
    :type next_page: str
    :param fields: The fields to return on the response. Can be a single field or a comma-separated list of fields
    :type fields: str

    """
    return web.Response(status=200)


async def get_object_name_by_object_id(request: web.Request, authorization, object_name, object_id) -> web.Response:
    """Retrieve an {objectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str

    """
    return web.Response(status=200)


async def replace_object_name_by_child_object_id(request: web.Request, authorization, object_name, child_object_name, object_id, child_object_id, body) -> web.Response:
    """Update an {childObjectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param child_object_name: The name of the childObjectName
    :type child_object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str
    :param child_object_id: The {childObjectName} ID
    :type child_object_id: str
    :param body: The {objectName}
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def replace_object_name_by_object_id(request: web.Request, authorization, object_name, object_id, body) -> web.Response:
    """Update an {objectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str
    :param body: The {objectName}
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def update_object_name_by_child_object_id(request: web.Request, authorization, object_name, child_object_name, object_id, child_object_id, body) -> web.Response:
    """Update an {childObjectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param child_object_name: The name of the childObjectName
    :type child_object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str
    :param child_object_id: The {childObjectName} ID
    :type child_object_id: str
    :param body: The {objectName}
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)


async def update_object_name_by_object_id(request: web.Request, authorization, object_name, object_id, body) -> web.Response:
    """Update an {objectName}

    

    :param authorization: The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39;
    :type authorization: str
    :param object_name: The name of the object
    :type object_name: str
    :param object_id: The {objectName} ID
    :type object_id: str
    :param body: The {objectName}
    :type body: dict | bytes

    """
    body = Object.from_dict(body)
    return web.Response(status=200)
