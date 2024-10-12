from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def searchdocuments(request: web.Request, content_type, accept, rest_range, acronym, fields=None, where=None, _schema=None, keyword=None, sort=None) -> web.Response:
    """Search documents

    Search documents by the query parameters described below.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;503&#x60;.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    :type accept: str
    :param rest_range: Range of documents to show
    :type rest_range: str
    :param acronym: Identifies the kind of data
    :type acronym: str
    :param fields: Fields that will be returned by document
    :type fields: str
    :param where: Specification of filters. As seen below
    :type where: str
    :param _schema: Enter with the name of the schema to filter documents by compatibility of the schema.
    :type _schema: str
    :param keyword: String to search
    :type keyword: str
    :param sort: Use ASC value to sort ascending or DESC value to sort descending. 
    :type sort: str

    """
    return web.Response(status=200)
