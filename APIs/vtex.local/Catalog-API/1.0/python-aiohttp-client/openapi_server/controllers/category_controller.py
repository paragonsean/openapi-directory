from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_category_category_id_put_request import ApiCatalogPvtCategoryCategoryIdPutRequest
from openapi_server.models.category import Category
from openapi_server.models.create_category_request import CreateCategoryRequest
from openapi_server.models.get_category_tree import GetCategoryTree
from openapi_server import util


async def api_catalog_pvt_category_category_id_get(request: web.Request, content_type, accept, category_id) -> web.Response:
    """Get Category by ID

    Retrieves general information about a Category.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 3367,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param category_id: Category’s unique numerical identifier.
    :type category_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_category_category_id_put(request: web.Request, content_type, accept, category_id, body=None) -> web.Response:
    """Update Category

    Updates a previously existing Category.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param category_id: Category’s unique numerical identifier.
    :type category_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtCategoryCategoryIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_category_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create Category

    Creates a new Category.    If there is a need to create a new category with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ## Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Request body example (custom ID)    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCategoryRequest.from_dict(body)
    return web.Response(status=200)


async def category_tree(request: web.Request, content_type, accept, category_levels) -> web.Response:
    """Get Category Tree

    Retrieves the Category Tree of your store. Get all the category levels registered in the Catalog or define the level up to which you want to get.    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;id\&quot;: 1,          \&quot;name\&quot;: \&quot;Alimentação\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 6,                  \&quot;name\&quot;: \&quot;Bebedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/bebedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bebedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 7,                  \&quot;name\&quot;: \&quot;Comedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/comedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Comedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 8,                  \&quot;name\&quot;: \&quot;Biscoitos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/biscoitos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Biscoitos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 9,                  \&quot;name\&quot;: \&quot;Petiscos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/petiscos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Petiscos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 10,                  \&quot;name\&quot;: \&quot;Ração Seca\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-seca\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Seca para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 11,                  \&quot;name\&quot;: \&quot;Ração Úmida\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-umida\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Úmida para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Alimentação para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      },      {          \&quot;id\&quot;: 2,          \&quot;name\&quot;: \&quot;Brinquedos\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 12,                  \&quot;name\&quot;: \&quot;Bolinhas\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/bolinhas\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bolinhas para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 13,                  \&quot;name\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/ratinhos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 19,                  \&quot;name\&quot;: \&quot;Arranhador para gato\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/arranhador-para-gato\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Brinquedo Arranhador para gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;Arranhador gatos é indispensável no lar com felinos. Ideais para afiar as unhas e garantir a diversão\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Brinquedos para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param category_levels: Value of the category level you need to retrieve.
    :type category_levels: str

    """
    return web.Response(status=200)
