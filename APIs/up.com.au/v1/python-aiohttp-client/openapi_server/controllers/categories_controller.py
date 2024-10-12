from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_category_response import GetCategoryResponse
from openapi_server.models.list_categories_response import ListCategoriesResponse
from openapi_server.models.update_transaction_category_request import UpdateTransactionCategoryRequest
from openapi_server import util


async def categories_get(request: web.Request, filter_parent=None) -> web.Response:
    """List categories

    Retrieve a list of all categories and their ancestry. The returned list is not paginated. 

    :param filter_parent: The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a &#x60;404&#x60; response. 
    :type filter_parent: str

    """
    return web.Response(status=200)


async def categories_id_get(request: web.Request, id) -> web.Response:
    """Retrieve category

    Retrieve a specific category by providing its unique identifier. 

    :param id: The unique identifier for the category. 
    :type id: str

    """
    return web.Response(status=200)


async def transactions_transaction_id_relationships_category_patch(request: web.Request, transaction_id, body=None) -> web.Response:
    """Categorize transaction

    Updates the category associated with a transaction. Only transactions for which &#x60;isCategorizable&#x60; is set to true support this operation. The &#x60;id&#x60; is taken from the list exposed on &#x60;/categories&#x60; and cannot be one of the top-level (parent) categories. To de-categorize a transaction, set the entire &#x60;data&#x60; key to &#x60;null&#x60;. An HTTP &#x60;204&#x60; is returned on success. The associated category, along with its request URL is also exposed via the &#x60;category&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

    :param transaction_id: The unique identifier for the transaction. 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTransactionCategoryRequest.from_dict(body)
    return web.Response(status=200)
