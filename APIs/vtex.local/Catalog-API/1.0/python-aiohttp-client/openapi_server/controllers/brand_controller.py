from typing import List, Dict
from aiohttp import web

from openapi_server.models.brand_create_update import BrandCreateUpdate
from openapi_server.models.brand_get import BrandGet
from openapi_server.models.brand_list_per_page200_response import BrandListPerPage200Response
from openapi_server import util


async def api_catalog_pvt_brand_brand_id_delete(request: web.Request, brand_id, content_type, accept) -> web.Response:
    """Delete Brand

    Deletes an existing Brand.

    :param brand_id: Brand’s unique numerical identifier.
    :type brand_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def api_catalog_pvt_brand_brand_id_get(request: web.Request, content_type, accept, brand_id) -> web.Response:
    """Get Brand and context

    Retrieves information about a specific Brand and its context.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param brand_id: Brand ID.
    :type brand_id: str

    """
    return web.Response(status=200)


async def api_catalog_pvt_brand_brand_id_put(request: web.Request, brand_id, content_type, accept, body=None) -> web.Response:
    """Update Brand

    Updates a previously existing Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

    :param brand_id: Brand’s unique numerical identifier.
    :type brand_id: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = BrandCreateUpdate.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_brand_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create Brand

    Creates a new Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: Request body.
    :type body: dict | bytes

    """
    body = BrandCreateUpdate.from_dict(body)
    return web.Response(status=200)


async def brand(request: web.Request, content_type, accept, brand_id) -> web.Response:
    """Get Brand

    Retrieves a specific Brand by its ID.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: 7000000,    \&quot;name\&quot;: \&quot;Pedigree\&quot;,    \&quot;isActive\&quot;: true,    \&quot;title\&quot;: \&quot;Pedigree\&quot;,    \&quot;metaTagDescription\&quot;: \&quot;Pedigree\&quot;,    \&quot;imageUrl\&quot;: null  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param brand_id: Brand ID.
    :type brand_id: str

    """
    return web.Response(status=200)


async def brand_list(request: web.Request, content_type, accept) -> web.Response:
    """Get Brand List

    Retrieves all Brands registered in the store&#39;s Catalog.   &gt;⚠️ This route&#39;s response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) endpoint instead to get a paginated response.   ## Response body example    &#x60;&#x60;&#x60;json  [    {      \&quot;id\&quot;: 9280,      \&quot;name\&quot;: \&quot;Brand\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Brand\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Brand\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000000,      \&quot;name\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000001,      \&quot;name\&quot;: \&quot;Pedigree\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Pedigree\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;\&quot;,      \&quot;imageUrl\&quot;: null    }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def brand_list_per_page(request: web.Request, content_type, accept, page_size, page) -> web.Response:
    """Get Brand List Per Page

    Retrieves all Brands registered in the store&#39;s Catalog by page number.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;items\&quot;: [      {        \&quot;id\&quot;: 2000000,        \&quot;name\&quot;: \&quot;Farm\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Farm\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Farm\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000001,        \&quot;name\&quot;: \&quot;Adidas\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000002,        \&quot;name\&quot;: \&quot;Brastemp\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Brastemp\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Brastemp\&quot;,        \&quot;imageUrl\&quot;: null      }    ],      \&quot;paging\&quot;: {        \&quot;page\&quot;: 1,          \&quot;perPage\&quot;: 3,            \&quot;total\&quot;: 6,              \&quot;pages\&quot;: 2      }  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param page_size: Quantity of brands per page.
    :type page_size: int
    :param page: Page number of the brand list.
    :type page: int

    """
    return web.Response(status=200)
