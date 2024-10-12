from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sku200_response import ListSKU200Response
from openapi_server.models.search_sku200_response import SearchSKU200Response
from openapi_server import util


async def list_sku(request: web.Request, content_type, accept, _from=None, to=None) -> web.Response:
    """Get List of SKUs

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about all SKUs.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;data\&quot;: [          \&quot;1\&quot;,          \&quot;10\&quot;,          \&quot;11\&quot;,          \&quot;12\&quot;,          \&quot;13\&quot;,          \&quot;14\&quot;,          \&quot;15\&quot;,          \&quot;16\&quot;,          \&quot;19\&quot;,          \&quot;2\&quot;,          \&quot;20\&quot;,          \&quot;21\&quot;,          \&quot;22\&quot;,          \&quot;23\&quot;,          \&quot;24\&quot;      ],      \&quot;_metadata\&quot;: {          \&quot;total\&quot;: 65,          \&quot;from\&quot;: 1,          \&quot;to\&quot;: 15      }  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param _from: The first page of the interval of the product list.
    :type _from: str
    :param to: The last page of the interval of the product list.
    :type to: str

    """
    return web.Response(status=200)


async def search_sku(request: web.Request, content_type, accept, _from=None, to=None, id=None, externalid=None) -> web.Response:
    """Search for SKU

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about an SKU taking into consideration the defined search criteria. It is mandatory to use at least one query parameter.     ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;data\&quot;: [      {        \&quot;id\&quot;: \&quot;2\&quot;,        \&quot;productId\&quot;: \&quot;2\&quot;,        \&quot;externalId\&quot;: \&quot;1909621862\&quot;      }    ],    \&quot;_metadata\&quot;: {      \&quot;total\&quot;: 1,      \&quot;from\&quot;: 1,      \&quot;to\&quot;: 15    }  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param _from: The first page of the interval of the product list.
    :type _from: str
    :param to: The last page of the interval of the product list.
    :type to: str
    :param id: SKU unique idenfier number.
    :type id: int
    :param externalid: SKU reference unique identifier number in the store.
    :type externalid: int

    """
    return web.Response(status=200)
