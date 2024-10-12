from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_config_update200_response import AccountConfigUpdate200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.cart_config_update200_response import CartConfigUpdate200Response
from openapi_server.models.cart_validate200_response import CartValidate200Response
from openapi_server.models.model_response_product_attribute_list import ModelResponseProductAttributeList
from openapi_server.models.model_response_product_child_item_list import ModelResponseProductChildItemList
from openapi_server.models.model_response_product_list import ModelResponseProductList
from openapi_server.models.product_add import ProductAdd
from openapi_server.models.product_add200_response import ProductAdd200Response
from openapi_server.models.product_attribute_value_set200_response import ProductAttributeValueSet200Response
from openapi_server.models.product_attribute_value_unset200_response import ProductAttributeValueUnset200Response
from openapi_server.models.product_brand_list200_response import ProductBrandList200Response
from openapi_server.models.product_child_item_find200_response import ProductChildItemFind200Response
from openapi_server.models.product_child_item_info200_response import ProductChildItemInfo200Response
from openapi_server.models.product_count200_response import ProductCount200Response
from openapi_server.models.product_currency_add200_response import ProductCurrencyAdd200Response
from openapi_server.models.product_currency_list200_response import ProductCurrencyList200Response
from openapi_server.models.product_delete200_response import ProductDelete200Response
from openapi_server.models.product_find200_response import ProductFind200Response
from openapi_server.models.product_image_add import ProductImageAdd
from openapi_server.models.product_image_add200_response import ProductImageAdd200Response
from openapi_server.models.product_image_update200_response import ProductImageUpdate200Response
from openapi_server.models.product_info200_response import ProductInfo200Response
from openapi_server.models.product_manufacturer_add200_response import ProductManufacturerAdd200Response
from openapi_server.models.product_option_add200_response import ProductOptionAdd200Response
from openapi_server.models.product_option_assign200_response import ProductOptionAssign200Response
from openapi_server.models.product_option_list200_response import ProductOptionList200Response
from openapi_server.models.product_option_value_add200_response import ProductOptionValueAdd200Response
from openapi_server.models.product_option_value_assign200_response import ProductOptionValueAssign200Response
from openapi_server.models.product_price_add import ProductPriceAdd
from openapi_server.models.product_price_update import ProductPriceUpdate
from openapi_server.models.product_review_list200_response import ProductReviewList200Response
from openapi_server.models.product_tax_add import ProductTaxAdd
from openapi_server.models.product_tax_add200_response import ProductTaxAdd200Response
from openapi_server.models.product_update import ProductUpdate
from openapi_server.models.product_variant_add import ProductVariantAdd
from openapi_server.models.product_variant_add200_response import ProductVariantAdd200Response
from openapi_server.models.product_variant_count200_response import ProductVariantCount200Response
from openapi_server.models.product_variant_image_add import ProductVariantImageAdd
from openapi_server.models.product_variant_list200_response import ProductVariantList200Response
from openapi_server.models.product_variant_price_add import ProductVariantPriceAdd
from openapi_server.models.product_variant_price_update import ProductVariantPriceUpdate
from openapi_server.models.product_variant_update import ProductVariantUpdate
from openapi_server import util


async def product_add(request: web.Request, body) -> web.Response:
    """product_add

    Add new product to store.

    :param body: 
    :type body: dict | bytes

    """
    body = ProductAdd.from_dict(body)
    return web.Response(status=200)


async def product_attribute_list(request: web.Request, product_id, attribute_id=None, variant_id=None, page_cursor=None, start=None, count=None, attribute_group_id=None, set_name=None, lang_id=None, store_id=None, sort_by=None, sort_direction=None, params=None, response_fields=None, exclude=None) -> web.Response:
    """product_attribute_list

    Get list of attributes and values.

    :param product_id: Retrieves attributes specified by product id
    :type product_id: str
    :param attribute_id: Retrieves info for specified attribute_id
    :type attribute_id: str
    :param variant_id: Defines product&#39;s variants specified by variant id
    :type variant_id: str
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param attribute_group_id: Filter by attribute_group_id
    :type attribute_group_id: str
    :param set_name: Retrieves attributes specified by set_name in Magento
    :type set_name: str
    :param lang_id: Retrieves attributes specified by language id
    :type lang_id: str
    :param store_id: Retrieves attributes specified by store id
    :type store_id: str
    :param sort_by: Set field to sort by
    :type sort_by: str
    :param sort_direction: Set sorting direction
    :type sort_direction: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str

    """
    return web.Response(status=200)


async def product_attribute_value_set(request: web.Request, product_id, attribute_id=None, attribute_group_id=None, attribute_name=None, value=None, value_id=None, lang_id=None, store_id=None) -> web.Response:
    """product_attribute_value_set

    Set attribute value to product.

    :param product_id: Defines product id where the attribute should be added
    :type product_id: str
    :param attribute_id: Filter by attribute_id
    :type attribute_id: str
    :param attribute_group_id: Filter by attribute_group_id
    :type attribute_group_id: str
    :param attribute_name: Define attribute name
    :type attribute_name: str
    :param value: Define attribute value
    :type value: str
    :param value_id: Define attribute value id
    :type value_id: int
    :param lang_id: Language id
    :type lang_id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_attribute_value_unset(request: web.Request, product_id, attribute_id, store_id=None, include_default=None, reindex=None, clear_cache=None) -> web.Response:
    """product_attribute_value_unset

    Removes attribute value for a product.

    :param product_id: Product id
    :type product_id: str
    :param attribute_id: Attribute Id
    :type attribute_id: str
    :param store_id: Store Id
    :type store_id: str
    :param include_default: Boolean, whether or not to unset default value of the attribute, if applicable
    :type include_default: bool
    :param reindex: Is reindex required
    :type reindex: bool
    :param clear_cache: Is cache clear required
    :type clear_cache: bool

    """
    return web.Response(status=200)


async def product_brand_list(request: web.Request, start=None, count=None, params=None, brand_ids=None, exclude=None, store_id=None, lang_id=None, created_from=None, created_to=None, modified_from=None, modified_to=None, response_fields=None) -> web.Response:
    """product_brand_list

    Get list of brands from your store.

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param brand_ids: Retrieves brands specified by brand ids
    :type brand_ids: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)


async def product_child_item_find(request: web.Request, find_value, find_where=None, find_params=None, store_id=None) -> web.Response:
    """product_child_item_find

    Search product child item (bundled item or configurable product variant) in store catalog.

    :param find_value: Entity search that is specified by some value
    :type find_value: str
    :param find_where: Entity search that is specified by the comma-separated unique fields
    :type find_where: str
    :param find_params: Entity search that is specified by comma-separated parameters
    :type find_params: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_child_item_info(request: web.Request, product_id, id, params=None, response_fields=None, exclude=None, store_id=None, lang_id=None, currency_id=None) -> web.Response:
    """product_child_item_info

    Get child for specific product.

    :param product_id: Filter by parent product id
    :type product_id: str
    :param id: Entity id
    :type id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param currency_id: Currency Id
    :type currency_id: str

    """
    return web.Response(status=200)


async def product_child_item_list(request: web.Request, page_cursor=None, start=None, count=None, params=None, response_fields=None, exclude=None, created_from=None, created_to=None, modified_from=None, modified_to=None, product_id=None, product_ids=None, store_id=None, lang_id=None, currency_id=None, avail_sale=None, report_request_id=None, disable_report_cache=None) -> web.Response:
    """product_child_item_list

    Get child items list of specific product(s).

    :param page_cursor: Used to retrieve products child items via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param product_id: Filter by parent product id
    :type product_id: str
    :param product_ids: Filter by parent product ids
    :type product_ids: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param currency_id: Currency Id
    :type currency_id: str
    :param avail_sale: Specifies the set of available/not available products for sale
    :type avail_sale: bool
    :param report_request_id: Report request id
    :type report_request_id: str
    :param disable_report_cache: Disable report cache for current request
    :type disable_report_cache: bool

    """
    return web.Response(status=200)


async def product_count(request: web.Request, category_id=None, created_from=None, created_to=None, modified_from=None, modified_to=None, avail_view=None, avail_sale=None, store_id=None, lang_id=None, product_ids=None, report_request_id=None, disable_report_cache=None, brand_name=None, product_attributes=None, status=None, type=None) -> web.Response:
    """product_count

    Count products in store.

    :param category_id: Counts products specified by category id
    :type category_id: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param avail_view: Specifies the set of visible/invisible products
    :type avail_view: bool
    :param avail_sale: Specifies the set of available/not available products for sale
    :type avail_sale: bool
    :param store_id: Counts products specified by store id
    :type store_id: str
    :param lang_id: Counts products specified by language id
    :type lang_id: str
    :param product_ids: Counts products specified by product ids
    :type product_ids: str
    :param report_request_id: Report request id
    :type report_request_id: str
    :param disable_report_cache: Disable report cache for current request
    :type disable_report_cache: bool
    :param brand_name: Retrieves brands specified by brand name
    :type brand_name: str
    :param product_attributes: Defines product attributes
    :type product_attributes: List[str]
    :param status: Defines product&#39;s status
    :type status: str
    :param type: Defines products&#39;s type
    :type type: str

    """
    return web.Response(status=200)


async def product_currency_add(request: web.Request, iso3, rate, name=None, avail=None, symbol_left=None, symbol_right=None, default=None) -> web.Response:
    """product_currency_add

    Add currency and/or set default in store

    :param iso3: Specifies standardized currency code
    :type iso3: str
    :param rate: Defines the numerical identifier against to the major currency
    :type rate: 
    :param name: Defines currency&#39;s name
    :type name: str
    :param avail: Specifies whether the currency is available
    :type avail: bool
    :param symbol_left: Defines the symbol that is located before the currency
    :type symbol_left: str
    :param symbol_right: Defines the symbol that is located after the currency
    :type symbol_right: str
    :param default: Specifies currency&#39;s default meaning
    :type default: bool

    """
    return web.Response(status=200)


async def product_currency_list(request: web.Request, start=None, count=None, params=None, page_cursor=None, exclude=None, response_fields=None, default=None, avail=None) -> web.Response:
    """product_currency_list

    Get list of currencies

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param default: Specifies the set of default/not default currencies
    :type default: bool
    :param avail: Specifies the set of available/not available currencies
    :type avail: bool

    """
    return web.Response(status=200)


async def product_delete(request: web.Request, id) -> web.Response:
    """product_delete

    Product delete

    :param id: Product id that will be removed
    :type id: str

    """
    return web.Response(status=200)


async def product_fields(request: web.Request, ) -> web.Response:
    """product_fields

    Retrieve all available fields for product item in store.


    """
    return web.Response(status=200)


async def product_find(request: web.Request, find_value, find_where=None, find_params=None, find_what=None, lang_id=None, store_id=None) -> web.Response:
    """product_find

    Search product in store catalog. \&quot;Apple\&quot; is specified here by default.

    :param find_value: Entity search that is specified by some value
    :type find_value: str
    :param find_where: Entity search that is specified by the comma-separated unique fields
    :type find_where: str
    :param find_params: Entity search that is specified by comma-separated parameters
    :type find_params: str
    :param find_what: Parameter&#39;s value specifies the entity that has to be found
    :type find_what: str
    :param lang_id: Search products specified by language id
    :type lang_id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_image_add(request: web.Request, body) -> web.Response:
    """product_image_add

    Add image to product

    :param body: 
    :type body: dict | bytes

    """
    body = ProductImageAdd.from_dict(body)
    return web.Response(status=200)


async def product_image_delete(request: web.Request, product_id, id, store_id=None) -> web.Response:
    """product_image_delete

    Delete image

    :param product_id: Defines product id where the image should be deleted
    :type product_id: str
    :param id: Entity id
    :type id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_image_update(request: web.Request, product_id, id, variant_ids=None, image_name=None, type=None, label=None, position=None, store_id=None, lang_id=None, hidden=None) -> web.Response:
    """product_image_update

    Update details of image

    :param product_id: Defines product id where the image should be updated
    :type product_id: str
    :param id: Defines image update specified by image id
    :type id: str
    :param variant_ids: Defines product&#39;s variants ids
    :type variant_ids: str
    :param image_name: Defines image&#39;s name
    :type image_name: str
    :param type: Defines image&#39;s types that are specified by comma-separated list
    :type type: str
    :param label: Defines alternative text that has to be attached to the picture
    :type label: str
    :param position: Defines image’s position in the list
    :type position: int
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param hidden: Define is hide image
    :type hidden: bool

    """
    return web.Response(status=200)


async def product_info(request: web.Request, id, params=None, response_fields=None, exclude=None, store_id=None, lang_id=None, currency_id=None, report_request_id=None, disable_report_cache=None) -> web.Response:
    """product_info

    Get product info about product ID *** or specify other product ID.

    :param id: Retrieves product&#39;s info specified by product id
    :type id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Retrieves product info specified by store id
    :type store_id: str
    :param lang_id: Retrieves product info specified by language id
    :type lang_id: str
    :param currency_id: Currency Id
    :type currency_id: str
    :param report_request_id: Report request id
    :type report_request_id: str
    :param disable_report_cache: Disable report cache for current request
    :type disable_report_cache: bool

    """
    return web.Response(status=200)


async def product_list(request: web.Request, page_cursor=None, start=None, count=None, params=None, response_fields=None, exclude=None, category_id=None, created_from=None, created_to=None, modified_from=None, modified_to=None, avail_view=None, avail_sale=None, store_id=None, lang_id=None, currency_id=None, product_ids=None, since_id=None, report_request_id=None, disable_report_cache=None, sort_by=None, sort_direction=None, sku=None, disable_cache=None, brand_name=None, product_attributes=None, status=None, type=None) -> web.Response:
    """product_list

    Get list of products from your store. Returns 10 products by default.

    :param page_cursor: Used to retrieve products via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param category_id: Retrieves products specified by category id
    :type category_id: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param avail_view: Specifies the set of visible/invisible products
    :type avail_view: bool
    :param avail_sale: Specifies the set of available/not available products for sale
    :type avail_sale: bool
    :param store_id: Retrieves products specified by store id
    :type store_id: str
    :param lang_id: Retrieves products specified by language id
    :type lang_id: str
    :param currency_id: Currency Id
    :type currency_id: str
    :param product_ids: Retrieves products specified by product ids
    :type product_ids: str
    :param since_id: Retrieve entities starting from the specified id.
    :type since_id: int
    :param report_request_id: Report request id
    :type report_request_id: str
    :param disable_report_cache: Disable report cache for current request
    :type disable_report_cache: bool
    :param sort_by: Set field to sort by
    :type sort_by: str
    :param sort_direction: Set sorting direction
    :type sort_direction: str
    :param sku: Filter by product&#39;s sku
    :type sku: str
    :param disable_cache: Disable cache for current request
    :type disable_cache: bool
    :param brand_name: Retrieves brands specified by brand name
    :type brand_name: str
    :param product_attributes: Defines product attributes
    :type product_attributes: List[str]
    :param status: Defines product&#39;s status
    :type status: str
    :param type: Defines products&#39;s type
    :type type: str

    """
    return web.Response(status=200)


async def product_manufacturer_add(request: web.Request, product_id, manufacturer) -> web.Response:
    """product_manufacturer_add

    Add manufacturer to store and assign to product

    :param product_id: Defines products specified by product id
    :type product_id: str
    :param manufacturer: Defines product’s manufacturer&#39;s name
    :type manufacturer: str

    """
    return web.Response(status=200)


async def product_option_add(request: web.Request, name, type, product_id=None, default_option_value=None, option_values=None, description=None, avail=None, sort_order=None, required=None, clear_cache=None) -> web.Response:
    """product_option_add

    Add product option from store.

    :param name: Defines option&#39;s name
    :type name: str
    :param type: Defines option&#39;s type that has to be added
    :type type: str
    :param product_id: Defines product id where the option should be added
    :type product_id: str
    :param default_option_value: Defines default option value that has to be added
    :type default_option_value: str
    :param option_values: Defines option values that has to be added
    :type option_values: str
    :param description: Defines option&#39;s description
    :type description: str
    :param avail: Defines whether the option is available
    :type avail: bool
    :param sort_order: Sort number in the list
    :type sort_order: int
    :param required: Defines if the option is required
    :type required: bool
    :param clear_cache: Is cache clear required
    :type clear_cache: bool

    """
    return web.Response(status=200)


async def product_option_assign(request: web.Request, product_id, option_id, required=None, sort_order=None, option_values=None, clear_cache=None) -> web.Response:
    """product_option_assign

    Assign option from product.

    :param product_id: Defines product id where the option should be assigned
    :type product_id: str
    :param option_id: Defines option id which has to be assigned
    :type option_id: str
    :param required: Defines if the option is required
    :type required: bool
    :param sort_order: Sort number in the list
    :type sort_order: int
    :param option_values: Defines option values that has to be assigned
    :type option_values: str
    :param clear_cache: Is cache clear required
    :type clear_cache: bool

    """
    return web.Response(status=200)


async def product_option_list(request: web.Request, start=None, count=None, params=None, exclude=None, response_fields=None, product_id=None, lang_id=None, store_id=None) -> web.Response:
    """product_option_list

    Get list of options.

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param product_id: Retrieves products&#39; options specified by product id
    :type product_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_option_value_add(request: web.Request, product_id, option_id, option_value, sort_order=None, clear_cache=None) -> web.Response:
    """product_option_value_add

    Add product option item from option.

    :param product_id: Defines product id where the option value should be added
    :type product_id: str
    :param option_id: Defines option id where the value has to be added
    :type option_id: str
    :param option_value: Defines option value that has to be added
    :type option_value: str
    :param sort_order: Sort number in the list
    :type sort_order: int
    :param clear_cache: Is cache clear required
    :type clear_cache: bool

    """
    return web.Response(status=200)


async def product_option_value_assign(request: web.Request, product_option_id, option_value_id, clear_cache=None) -> web.Response:
    """product_option_value_assign

    Assign product option item from product.

    :param product_option_id: Defines product&#39;s option id where the value has to be assigned
    :type product_option_id: int
    :param option_value_id: Defines value id that has to be assigned
    :type option_value_id: int
    :param clear_cache: Is cache clear required
    :type clear_cache: bool

    """
    return web.Response(status=200)


async def product_option_value_update(request: web.Request, product_id, option_id, option_value_id, option_value, price=None, quantity=None, clear_cache=None) -> web.Response:
    """product_option_value_update

    Update product option item from option.

    :param product_id: Defines product id where the option value should be updated
    :type product_id: str
    :param option_id: Defines option id where the value has to be updated
    :type option_id: str
    :param option_value_id: Defines value id that has to be assigned
    :type option_value_id: int
    :param option_value: Defines option value that has to be added
    :type option_value: str
    :param price: Defines new product option price
    :type price: 
    :param quantity: Defines new products&#39; options quantity
    :type quantity: 
    :param clear_cache: Is cache clear required
    :type clear_cache: bool

    """
    return web.Response(status=200)


async def product_price_add(request: web.Request, body) -> web.Response:
    """product_price_add

    Add some prices to the product.

    :param body: 
    :type body: dict | bytes

    """
    body = ProductPriceAdd.from_dict(body)
    return web.Response(status=200)


async def product_price_delete(request: web.Request, product_id, group_prices=None) -> web.Response:
    """product_price_delete

    Delete some prices of the product

    :param product_id: Defines the product where the price has to be deleted
    :type product_id: str
    :param group_prices: Defines product&#39;s group prices
    :type group_prices: str

    """
    return web.Response(status=200)


async def product_price_update(request: web.Request, body) -> web.Response:
    """product_price_update

    Update some prices of the product.

    :param body: 
    :type body: dict | bytes

    """
    body = ProductPriceUpdate.from_dict(body)
    return web.Response(status=200)


async def product_review_list(request: web.Request, product_id, start=None, page_cursor=None, count=None, ids=None, store_id=None, status=None, params=None, exclude=None, response_fields=None) -> web.Response:
    """product_review_list

    Get reviews of a specific product.

    :param product_id: Product id
    :type product_id: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param ids: Retrieves reviews specified by ids
    :type ids: str
    :param store_id: Store Id
    :type store_id: str
    :param status: Defines status
    :type status: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)


async def product_store_assign(request: web.Request, product_id, store_id) -> web.Response:
    """product_store_assign

    Assign product to store

    :param product_id: Defines id of the product which should be assigned to a store
    :type product_id: str
    :param store_id: Defines id of the store product should be assigned to
    :type store_id: str

    """
    return web.Response(status=200)


async def product_tax_add(request: web.Request, body) -> web.Response:
    """product_tax_add

    Add tax class and tax rate to store and assign to product.

    :param body: 
    :type body: dict | bytes

    """
    body = ProductTaxAdd.from_dict(body)
    return web.Response(status=200)


async def product_update(request: web.Request, body) -> web.Response:
    """product_update

    Update price and quantity for a specific product

    :param body: 
    :type body: dict | bytes

    """
    body = ProductUpdate.from_dict(body)
    return web.Response(status=200)


async def product_variant_add(request: web.Request, body) -> web.Response:
    """product_variant_add

    Add variant to product.

    :param body: 
    :type body: dict | bytes

    """
    body = ProductVariantAdd.from_dict(body)
    return web.Response(status=200)


async def product_variant_count(request: web.Request, product_id, created_from=None, created_to=None, modified_from=None, modified_to=None, category_id=None, store_id=None) -> web.Response:
    """product_variant_count

    Get count variants.

    :param product_id: Retrieves products&#39; variants specified by product id
    :type product_id: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param category_id: Counts products’ variants specified by category id
    :type category_id: str
    :param store_id: Retrieves variants specified by store id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_variant_delete(request: web.Request, id, product_id) -> web.Response:
    """product_variant_delete

    Delete variant.

    :param id: Defines variant removal, specified by variant id
    :type id: str
    :param product_id: Defines product&#39;s id where the variant has to be deleted
    :type product_id: str

    """
    return web.Response(status=200)


async def product_variant_image_add(request: web.Request, body) -> web.Response:
    """product_variant_image_add

    Add image to product

    :param body: 
    :type body: dict | bytes

    """
    body = ProductVariantImageAdd.from_dict(body)
    return web.Response(status=200)


async def product_variant_image_delete(request: web.Request, product_id, product_variant_id, id, store_id=None) -> web.Response:
    """product_variant_image_delete

    Delete  image to product

    :param product_id: Defines product id where the variant image should be deleted
    :type product_id: str
    :param product_variant_id: Defines product&#39;s variants specified by variant id
    :type product_variant_id: int
    :param id: Entity id
    :type id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_variant_info(request: web.Request, id, params=None, exclude=None, store_id=None) -> web.Response:
    """product_variant_info

    Get variant info. This method is deprecated, and its development is stopped. Please use \&quot;product.child_item.info\&quot; instead.

    :param id: Retrieves variant&#39;s info specified by variant id
    :type id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Retrieves variant info specified by store id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_variant_list(request: web.Request, start=None, count=None, params=None, exclude=None, created_from=None, created_to=None, modified_from=None, modified_to=None, category_id=None, product_id=None, store_id=None) -> web.Response:
    """product_variant_list

    Get a list of variants. This method is deprecated, and its development is stopped. Please use \&quot;product.child_item.list\&quot; instead.

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param category_id: Retrieves products’ variants specified by category id
    :type category_id: str
    :param product_id: Retrieves products&#39; variants specified by product id
    :type product_id: str
    :param store_id: Retrieves variants specified by store id
    :type store_id: str

    """
    return web.Response(status=200)


async def product_variant_price_add(request: web.Request, body) -> web.Response:
    """product_variant_price_add

    Add some prices to the product variant.

    :param body: 
    :type body: dict | bytes

    """
    body = ProductVariantPriceAdd.from_dict(body)
    return web.Response(status=200)


async def product_variant_price_delete(request: web.Request, id, product_id, group_prices) -> web.Response:
    """product_variant_price_delete

    Delete some prices of the product variant.

    :param id: Defines the variant where the price has to be deleted
    :type id: str
    :param product_id: Product id
    :type product_id: str
    :param group_prices: Defines variants&#39;s group prices
    :type group_prices: str

    """
    return web.Response(status=200)


async def product_variant_price_update(request: web.Request, body) -> web.Response:
    """product_variant_price_update

    Update some prices of the product variant.

    :param body: 
    :type body: dict | bytes

    """
    body = ProductVariantPriceUpdate.from_dict(body)
    return web.Response(status=200)


async def product_variant_update(request: web.Request, body) -> web.Response:
    """product_variant_update

    Update variant.

    :param body: 
    :type body: dict | bytes

    """
    body = ProductVariantUpdate.from_dict(body)
    return web.Response(status=200)
