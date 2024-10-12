from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def retrieveattachment(request: web.Request, acronym, id, _field, file_name) -> web.Response:
    """Retrieve attachment

    Use this API to retrieve a file.    Be sure to include the file extension in the name. Like in this example:  &#x60;&#x60;&#x60;  /dataentities/CL/documents/123/file/attachments/image.png  &#x60;&#x60;&#x60;

    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param _field: Field to attach the file to, as described in admin
    :type _field: str
    :param file_name: 
    :type file_name: str

    """
    return web.Response(status=200)


async def saveattachment(request: web.Request, acronym, id, _field, file) -> web.Response:
    """Save attachment

    This API allows you to save a file in a field of type &#x60;File&#x60;.    When using in javascript, you must add the header &#x60;content-type&#x60; with value &#x60;multipart/form-data;&#x60;    You can upload more than one file. Just add a new field in the &#x60;form-data&#x60; with type &#x60;File&#x60;.

    :param acronym: Two letter word that identifies the data structure
    :type acronym: str
    :param id: Id of the document
    :type id: str
    :param _field: Field to attach the file to, as described in admin
    :type _field: str
    :param file: 
    :type file: List[str]

    """
    return web.Response(status=200)
