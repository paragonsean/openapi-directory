from typing import List, Dict
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_article_api_model import BillbeeInterfacesBillbeeAPIModelArticleApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_article_image_relation_api_model import BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_update_stock_api_model import BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_update_stock_code_api_model import BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_article_api_custom_field_definition_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_article_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_article_api_custom_field_definition_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_article_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_article_image_relation_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_deleted_images_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_get_reserved_amount_response_data import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_update_stock_code_response_data import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_update_stock_response_data import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_search_controller_search_results_model import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_article_image_relation_api_model import RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_stock_response_data import RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData
from openapi_server.models.rechnungsdruck_web_app_controllers_api_search_controller_search_model import RechnungsdruckWebAppControllersApiSearchControllerSearchModel
from openapi_server import util


async def article_create_article(request: web.Request, body) -> web.Response:
    """Creates a new product

    

    :param body: 
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelArticleApiModel.from_dict(body)
    return web.Response(status=200)


async def article_delete_article(request: web.Request, id) -> web.Response:
    """Deletes a product

    

    :param id: The id of the Product
    :type id: int

    """
    return web.Response(status=200)


async def article_delete_image(request: web.Request, image_id) -> web.Response:
    """Deletes a single image by id

    

    :param image_id: The image id
    :type image_id: int

    """
    return web.Response(status=200)


async def article_delete_image_from_product(request: web.Request, product_id, image_id) -> web.Response:
    """Deletes a single image from a product

    

    :param product_id: The product id
    :type product_id: int
    :param image_id: The image id
    :type image_id: int

    """
    return web.Response(status=200)


async def article_delete_images(request: web.Request, body) -> web.Response:
    """Delete multiple images by id

    

    :param body: 
    :type body: List[int]

    """
    return web.Response(status=200)


async def article_get_article(request: web.Request, id, lookup_by=None) -> web.Response:
    """Queries a single article by id or by sku

    

    :param id: The id or the sku of the article to query
    :type id: str
    :param lookup_by: Either the value id, ean or the value sku to specify the meaning of the id parameter.
    :type lookup_by: str

    """
    return web.Response(status=200)


async def article_get_category(request: web.Request, ) -> web.Response:
    """GEts a list of all defined categories

    


    """
    return web.Response(status=200)


async def article_get_custom_field(request: web.Request, id) -> web.Response:
    """Queries a single custom field

    

    :param id: The id of the custom field to query
    :type id: int

    """
    return web.Response(status=200)


async def article_get_custom_fields(request: web.Request, page=None, page_size=None) -> web.Response:
    """Queries a list of all custom fields

    

    :param page: 
    :type page: int
    :param page_size: 
    :type page_size: int

    """
    return web.Response(status=200)


async def article_get_image(request: web.Request, image_id) -> web.Response:
    """Returns a single image by id

    

    :param image_id: The Id of the image
    :type image_id: int

    """
    return web.Response(status=200)


async def article_get_image_from_product(request: web.Request, product_id, image_id) -> web.Response:
    """Returns a single image by id

    

    :param product_id: The Id of the product
    :type product_id: int
    :param image_id: The Id of the image
    :type image_id: int

    """
    return web.Response(status=200)


async def article_get_images(request: web.Request, product_id) -> web.Response:
    """Returns a list of all images of the product

    

    :param product_id: The Id of the product
    :type product_id: int

    """
    return web.Response(status=200)


async def article_get_list(request: web.Request, page=None, page_size=None, min_created_at=None, minimum_bill_bee_article_id=None, maximum_bill_bee_article_id=None) -> web.Response:
    """Get a list of all products

    

    :param page: The current page to request starting with 1
    :type page: int
    :param page_size: The pagesize for the result list. Values between 1 and 250 are allowed
    :type page_size: int
    :param min_created_at: Optional the oldest create date of the articles to be returned
    :type min_created_at: str
    :param minimum_bill_bee_article_id: 
    :type minimum_bill_bee_article_id: int
    :param maximum_bill_bee_article_id: 
    :type maximum_bill_bee_article_id: int

    """
    min_created_at = util.deserialize_datetime(min_created_at)
    return web.Response(status=200)


async def article_get_patchable_fields(request: web.Request, ) -> web.Response:
    """Returns a list of fields which can be updated with the patch call

    


    """
    return web.Response(status=200)


async def article_get_reserved_amount(request: web.Request, id, lookup_by=None, stock_id=None) -> web.Response:
    """Queries the reserved amount for a single article by id or by sku

    

    :param id: The id or the sku of the article to query
    :type id: str
    :param lookup_by: Either the value id or the value sku to specify the meaning of the id parameter
    :type lookup_by: str
    :param stock_id: Optional the stock id if the multi stock feature is enabled
    :type stock_id: int

    """
    return web.Response(status=200)


async def article_get_stocks(request: web.Request, ) -> web.Response:
    """Query all defined stock locations

    


    """
    return web.Response(status=200)


async def article_patch_article(request: web.Request, id, body) -> web.Response:
    """Updates one or more fields of a product

    

    :param id: The id of the Product
    :type id: int
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def article_put_image(request: web.Request, product_id, image_id, body) -> web.Response:
    """Add or update an existing image of a product

    

    :param product_id: The product id
    :type product_id: int
    :param image_id: The image id. If you pass 0, the image will be added
    :type image_id: int
    :param body: The ArticleApiImageModel
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.from_dict(body)
    return web.Response(status=200)


async def article_put_images(request: web.Request, product_id, body, replace=None) -> web.Response:
    """Add multiple images to a product or replace the product images by the given images

    

    :param product_id: The id of the product
    :type product_id: int
    :param body: An array of ArticleApiImageModel
    :type body: list | bytes
    :param replace: If you pass true, the images will be replaced by the passed images. Otherwise the passed images will be appended to the product.
    :type replace: bool

    """
    body = [BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.from_dict(d) for d in body]
    return web.Response(status=200)


async def article_update_stock(request: web.Request, body) -> web.Response:
    """Update the stock qty of an article

    The article is specified by sku. You have to send the absolute value for the current stock

    :param body: 
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel.from_dict(body)
    return web.Response(status=200)


async def article_update_stock_code(request: web.Request, body) -> web.Response:
    """Update the stock code of an article

    

    :param body: 
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel.from_dict(body)
    return web.Response(status=200)


async def article_update_stock_multiple(request: web.Request, body) -> web.Response:
    """Update the stock qty for multiple articles at once

    

    :param body: 
    :type body: list | bytes

    """
    body = [BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel.from_dict(d) for d in body]
    return web.Response(status=200)


async def search_search(request: web.Request, body) -> web.Response:
    """Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

    

    :param body: 
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiSearchControllerSearchModel.from_dict(body)
    return web.Response(status=200)
