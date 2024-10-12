from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_collection_post200_response import ApiCatalogPvtCollectionPost200Response
from openapi_server.models.resquest_body import ResquestBody
from openapi_server.models.resquest_body1 import ResquestBody1
from openapi_server import util


async def api_catalog_pvt_collection_collection_id_delete(request: web.Request, content_type, accept, collection_id) -> web.Response:
    """Delete Collection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously existing Collection.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param collection_id: Collection’s unique numerical identifier.
    :type collection_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_collection_collection_id_get(request: web.Request, content_type, accept, collection_id) -> web.Response:
    """Get Collection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves general information of a Collection.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param collection_id: Collection’s unique numerical identifier.
    :type collection_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_collection_collection_id_put(request: web.Request, content_type, accept, collection_id, body=None) -> web.Response:
    """Update Collection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param collection_id: Collection’s unique numerical identifier.
    :type collection_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ResquestBody1.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_collection_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create Collection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = ResquestBody.from_dict(body)
    return web.Response(status=200)
