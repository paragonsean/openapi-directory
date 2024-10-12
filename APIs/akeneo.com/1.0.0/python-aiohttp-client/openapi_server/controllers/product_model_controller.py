from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_product_models_request import PatchProductModelsRequest
from openapi_server.models.post_product_models_request import PostProductModelsRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.product_models import ProductModels
from openapi_server import util


async def delete_product_models_code(request: web.Request, code) -> web.Response:
    """Delete a product model

    This endpoint allows you to delete a given product model. All its children, product models and variant products, will be also deleted. In the Enterprise Edition, the permissions based on your connection user group are applied to the product model you try to delete.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def get_product_model_draft_code(request: web.Request, code) -> web.Response:
    """Get a draft

    This endpoint allows you to get the information about a given product model draft.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def get_product_models(request: web.Request, search=None, scope=None, locales=None, attributes=None, pagination_type=None, page=None, search_after=None, limit=None, with_count=None, with_quality_scores=None) -> web.Response:
    """Get list of product models

    This endpoint allows you to get a list of product models. Product models are paginated. In the Enterprise Edition, since the 2.0, permissions based on your user groups are applied to the set of products you request.

    :param search: Filter product models, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section
    :type search: str
    :param scope: Filter product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-channel\&quot;&gt;Filter product values via channel&lt;/a&gt; section
    :type scope: str
    :param locales: Filter product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-locale\&quot;&gt;Filter product values via locale&lt;/a&gt; section
    :type locales: str
    :param attributes: Filter product values to only return those concerning the given attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-product-values\&quot;&gt;Filter on product values&lt;/a&gt; section and the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-on-product-model-properties\&quot;&gt;Filter on product model properties&lt;/a&gt; section
    :type attributes: str
    :param pagination_type: Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type pagination_type: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool
    :param with_quality_scores: Return product model quality scores in the response. &lt;strong&gt;(Only available since the 6.0 version)&lt;/strong&gt;
    :type with_quality_scores: bool

    """
    return web.Response(status=200)


async def get_product_models_code(request: web.Request, code, with_quality_scores=None) -> web.Response:
    """Get a product model

    This endpoint allows you to get the information about a given product model. In the Entreprise Edition, since the v2.0, permissions based on your user groups are applied to the product model you request.

    :param code: Code of the resource
    :type code: str
    :param with_quality_scores: Return product model quality scores in the response. &lt;strong&gt;(Only available since the 6.0 version)&lt;/strong&gt;
    :type with_quality_scores: bool

    """
    return web.Response(status=200)


async def patch_product_models(request: web.Request, body=None) -> web.Response:
    """Update/create several product models

    This endpoint allows you to update and/or create several product models at once. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no product models exists for the given code, it creates it. In the Enterprise Edition, since the v2.3, permissions based on your user groups are applied to the product models you try to update. It may result in the creation of drafts if you only have edit rights through the product model&#39;s categories.

    :param body: 
    :type body: dict | bytes

    """
    body = PatchProductModelsRequest.from_dict(body)
    return web.Response(status=200)


async def patch_product_models_code(request: web.Request, code, body) -> web.Response:
    """Update/create a product model

    This endpoint allows you to update a given product model. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no product model exists for the given code, it creates it. In the Enterprise Edition PIM since the 2.3, permissions based on your user groups are applied to the product model you try to update. It may result in the creation of a draft if you only have edit rights through the product model&#39;s categories.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostProductModelsRequest.from_dict(body)
    return web.Response(status=200)


async def post_product_model_proposal(request: web.Request, code) -> web.Response:
    """Submit a draft for approval

    This endpoint allows you to submit a product model draft for approval.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def post_product_models(request: web.Request, body=None) -> web.Response:
    """Create a new product model

    This endpoint allows you to create a new product model. In the Enterprise Edition, since the v2.3, permissions based on your user groups are applied to the product model you try to create.

    :param body: 
    :type body: dict | bytes

    """
    body = PostProductModelsRequest.from_dict(body)
    return web.Response(status=200)
