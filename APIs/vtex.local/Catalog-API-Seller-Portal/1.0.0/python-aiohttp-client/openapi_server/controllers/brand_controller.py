from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_brand200_response import GetBrand200Response
from openapi_server.models.list_brand200_response import ListBrand200Response
from openapi_server.models.post_brand200_response import PostBrand200Response
from openapi_server.models.post_brand_request import PostBrandRequest
from openapi_server.models.put_brand_request import PutBrandRequest
from openapi_server import util


async def get_brand(request: web.Request, content_type, accept, brand_id) -> web.Response:
    """Get Brand by ID

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a brand by its ID.    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: \&quot;863\&quot;,    \&quot;name\&quot;: \&quot;Zwilling\&quot;,    \&quot;isActive\&quot;: false,    \&quot;createdAt\&quot;: \&quot;2021-01-18T14:41:45.696488+00:00\&quot;,    \&quot;updatedAt\&quot;: \&quot;2021-01-18T14:41:45.696488+00:00\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param brand_id: Brand unique identifier number.
    :type brand_id: str

    """
    return web.Response(status=200)


async def list_brand(request: web.Request, content_type, accept, q=None, _from=None, to=None, order_by=None, name=None) -> web.Response:
    """Get List of Brands

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about all brands of the store. It is mandatory to use at least one query parameter.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;data\&quot;: [          {              \&quot;id\&quot;: \&quot;7\&quot;,              \&quot;name\&quot;: \&quot;All For Paws\&quot;,              \&quot;isActive\&quot;: true,              \&quot;createdAt\&quot;: \&quot;2022-01-17T19:43:14.18678Z\&quot;,              \&quot;updatedAt\&quot;: \&quot;2022-01-17T19:43:14.18678Z\&quot;          },          {              \&quot;id\&quot;: \&quot;1\&quot;,              \&quot;name\&quot;: \&quot;AOC\&quot;,              \&quot;isActive\&quot;: true,              \&quot;createdAt\&quot;: \&quot;2021-08-16T21:13:40.55189Z\&quot;,              \&quot;updatedAt\&quot;: \&quot;2021-08-16T21:13:40.55189Z\&quot;          }      ],      \&quot;_metadata\&quot;: {          \&quot;total\&quot;: 18,          \&quot;from\&quot;: 1,          \&quot;to\&quot;: 2,          \&quot;orderBy\&quot;: \&quot;name,asc\&quot;      }  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param q: Search word.
    :type q: str
    :param _from: The first page of the interval of the brand list.
    :type _from: str
    :param to: The last page of the interval of the brand list.
    :type to: str
    :param order_by: The order that the list is displayed. You can select &#x60;name&#x60;, or &#x60;updated_at&#x60; to select the order criteria. Then you can add &#x60;,&#x60; , &#x60;asc&#x60; or &#x60;desc&#x60; to define the brands order.
    :type order_by: str
    :param name: Brand name.
    :type name: str

    """
    return web.Response(status=200)


async def post_brand(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create Brand

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Creates a new brand.    ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;name\&quot;: \&quot;Zwilling\&quot;,    \&quot;isActive\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: \&quot;20\&quot;,    \&quot;name\&quot;: \&quot;Zwilling\&quot;,    \&quot;isActive\&quot;: true,    \&quot;createdAt\&quot;: \&quot;2021-05-17T15:20:36.077253+00:00\&quot;,    \&quot;updatedAt\&quot;: \&quot;2021-01-18T14:41:45.696488+00:00\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostBrandRequest.from_dict(body)
    return web.Response(status=200)


async def put_brand(request: web.Request, content_type, accept, brand_id, body=None) -> web.Response:
    """Update Brand

     &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates an existing brand.     ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: \&quot;20\&quot;,    \&quot;name\&quot;: \&quot;Zwilling\&quot;,    \&quot;isActive\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param brand_id: Brand unique identifier number.
    :type brand_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutBrandRequest.from_dict(body)
    return web.Response(status=200)
