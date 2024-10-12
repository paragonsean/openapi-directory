from typing import List, Dict
from aiohttp import web

from openapi_server.models.saveschemabyname_request import SaveschemabynameRequest
from openapi_server import util


async def deleteschemabyname(request: web.Request, content_type, data_entity_name, schema_name) -> web.Response:
    """Delete schema by name

    Deletes an existing schema for a given data entity.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param schema_name: Name of the schema.
    :type schema_name: str

    """
    return web.Response(status=200)


async def getschemabyname(request: web.Request, data_entity_name, content_type, schema_name) -> web.Response:
    """Get schema by name

    Returns an existing schema for a given data entity.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param schema_name: Name of the schema.
    :type schema_name: str

    """
    return web.Response(status=200)


async def getschemas(request: web.Request, data_entity_name, content_type) -> web.Response:
    """Get schemas

    Return the schemas saved.

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param content_type: Type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def saveschemabyname(request: web.Request, data_entity_name, schema_name, body) -> web.Response:
    """Save schema by name

    Creates or edits a data entity schema. Learn more about [Master Data schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle)    &gt; Note that if you send a &#x60;schemaName&#x60; that does not exist for that data entity, this request will create it.    This request can also be used to [create or edit Master Data v2 triggers](https://developers.vtex.com/vtex-rest-api/docs/setting-up-triggers-in-master-data-v2).

    :param data_entity_name: Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses.
    :type data_entity_name: str
    :param schema_name: Name of the schema.
    :type schema_name: str
    :param body: Request body for saving schema
    :type body: dict | bytes

    """
    body = SaveschemabynameRequest.from_dict(body)
    return web.Response(status=200)
