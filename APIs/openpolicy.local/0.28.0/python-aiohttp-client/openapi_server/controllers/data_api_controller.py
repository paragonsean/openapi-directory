from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_document_with_web_hook200_response import GetDocumentWithWebHook200Response
from openapi_server.models.model400 import Model400
from openapi_server.models.model404 import Model404
from openapi_server.models.patches_schema_inner import PatchesSchemaInner
from openapi_server import util


async def delete_document(request: web.Request, path) -> web.Response:
    """Delete a document

    This API endpoint deletes an existing document from the server

    :param path: A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    :type path: str

    """
    return web.Response(status=200)


async def get_document(request: web.Request, path, input=None, pretty=None, provenance=None, explain=None, metrics=None, instrument=None) -> web.Response:
    """Get a document

    This API endpoint returns the document specified by &#x60;path&#x60;.  The server will return a *bad request* (400) response if either: - The query requires an input document and you do not provide it - You provide the input document but the query has already defined it.

    :param path: A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    :type path: str
    :param input: Provide the text for an [input document](https://www.openpolicyagent.org/docs/latest/kubernetes-primer/#input-document) in JSON format
    :type input: Dict[str, ]
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool
    :param provenance: If true, response will include build and version information in addition to the result.
    :type provenance: bool
    :param explain: If set to *full*, response will include query explanations in addition to the result.
    :type explain: str
    :param metrics: If true, compiler performance metrics will be returned in the response.
    :type metrics: bool
    :param instrument: If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
    :type instrument: bool

    """
    return web.Response(status=200)


async def get_document_with_path(request: web.Request, path, body, pretty=None, provenance=None, explain=None, metrics=None, instrument=None) -> web.Response:
    """Get a document (with input)

    The server will return a *bad request* (400) response if either: - The query requires an input document and you do not provide it - You provided an input document but the query has already defined it.  If &#x60;path&#x60; indexes into an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, a *not found* response (404) will be returned.

    :param path: A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    :type path: str
    :param body: The input document (in JSON format)
    :type body: Dict[str, ]
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool
    :param provenance: If true, response will include build and version information in addition to the result.
    :type provenance: bool
    :param explain: If set to *full*, response will include query explanations in addition to the result.
    :type explain: str
    :param metrics: If true, compiler performance metrics will be returned in the response.
    :type metrics: bool
    :param instrument: If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
    :type instrument: bool

    """
    return web.Response(status=200)


async def get_document_with_web_hook(request: web.Request, path, body, pretty=None) -> web.Response:
    """Get a document (with webhook)

    The example given here assumes you have created a policy (with &#x60;PUT /v1/policies/{path}&#x60;), such as:    &#x60;&#x60;&#x60;yaml   package opa.examples   import input.example.flag   allow_request { flag &#x3D;&#x3D; true }   &#x60;&#x60;&#x60;  The server will return a *not found* (404) response if the requested document is missing or undefined. 

    :param path: A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    :type path: str
    :param body: The input document (in JSON format)
    :type body: Dict[str, ]
    :param pretty: If true, response will be in a human-readable format.
    :type pretty: bool

    """
    return web.Response(status=200)


async def patch_document(request: web.Request, path, body) -> web.Response:
    """Update a document

    This API endpoint updates an existing document on the server by describing the changes required (using [JSON patch operations](http://jsonpatch.com/))

    :param path: A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    :type path: str
    :param body: The list of JSON patch operations.
    :type body: list | bytes

    """
    body = [PatchesSchemaInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def put_document(request: web.Request, path, body, if_none_match=None) -> web.Response:
    """Create or overwrite a document

    If the path does not refer to an existing document (for example *us-west/servers*), the server will attempt to create all the necessary containing documents.  This behavior is similar to the Unix command [mkdir -p](https://en.wikipedia.org/wiki/Mkdir#Options).

    :param path: A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    :type path: str
    :param body: The JSON document to write to the specified path.
    :type body: 
    :param if_none_match: The server will respect the If-None-Match header if it is set to * (in other words, it will not overwrite an existing document located at the specified &#x60;path&#x60;).
    :type if_none_match: str

    """
    return web.Response(status=200)
