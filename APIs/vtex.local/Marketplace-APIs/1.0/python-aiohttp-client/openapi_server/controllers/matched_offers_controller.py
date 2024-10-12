from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_matched_offers_response import GetMatchedOffersResponse
from openapi_server import util


async def get_productoffers(request: web.Request, account_name, environment, content_type, accept, product_id) -> web.Response:
    """Get Matched Offer&#39;s Data by Product ID

    Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.   This endpoint retrieves the available offers for a speciic Product ID in the marketplace&#39;s catalog. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace operator, and are currently active in its catalog.   The call returns a list of offers for that ID, that contain the following data:   - Seller that sells the SKU   - Correspondent SKU ID   - SKU&#39;s price value   - Inventory level   - Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) that it is available at.

    :param account_name: Name of the VTEX account. Used as part of the URL.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: A string that identifies the seller&#39;s product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications.
    :type product_id: str

    """
    return web.Response(status=200)


async def get_sk_uoffers(request: web.Request, account_name, environment, content_type, accept, product_id, sku_id) -> web.Response:
    """Get Matched Offer&#39;s Data by SKU ID

    Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.   This endpoint retrieves the available offers for a speciic SKU ID in the marketplace&#39;s catalog. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace operator, and are currently active in its catalog.   The call returns a list of offers for that ID, that contain the following data:   - Seller that sells the SKU   - Correspondent SKU ID   - SKU&#39;s price value   - Inventory level   - Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) that it is available at.

    :param account_name: Name of the VTEX account. Used as part of the URL.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: A string that identifies the seller&#39;s product. This is the ID that the marketplace will use for all references to this product, such as price and inventory notifications.
    :type product_id: str
    :param sku_id: A string that identifies the seller&#39;s SKU. This is the ID that the marketplace will use for all references to this SKU, such as price and inventory notifications.
    :type sku_id: str

    """
    return web.Response(status=200)


async def getofferslist(request: web.Request, account_name, content_type, environment, accept, sort=None, rows=None, start=None, fq=None) -> web.Response:
    """Get Matched Offers List

    Offers are seller&#39;s products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.    This endpoint retrieves the available offers in a marketplace. It differs from the Get Suggestions endpoints, since it retrieves products that were already matched by the marketplace, and are currently in its catalog.   It is possible to filter the search through the following parameters:   - rows  - sort   - start   - fq

    :param account_name: Name of the VTEX account. Used as part of the URL
    :type account_name: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sort: Criteria used to sort the list of offers. For sorting values in ascending order, use &#x60;asc&#x60;, while for descending order, use &#x60;desc&#x60;. To fill in the field, insert the sorting criteria, followed by &#39;asc&#39;, or &#39;desc&#39;, separated by a comma. You can sort by the following criteria:   - **price:** sorts offers by price. *Ascending* goes from lowest to highest price, while *Descending* goes from highest to lowest price.   - **name:** sorts offers by *productName*, in alphabetical order. *Ascending* goes from *A* to *Z*, while *Descending* goes from *Z* to *A*.   - **availability:** availability in the sales channel (sc). The default value is 1.   Ex. sort&#x3D;availability,desc   Ex. sort&#x3D;name,asc   Ex. price,desc
    :type sort: str
    :param rows: Number of rows included in the response. Each row corresponds to a single offer. The default amount of rows in the response is 1, and the maximum amount is 50. To have more than one offer listed in the response, please add the &#x60;rows&#x60; parameter with a number greater than 1.
    :type rows: int
    :param start: Number corresponding to the row from which the offer list will begin, used for pagination. Filters the list of offers by retrieving the offers starting from the row defined. The default value is 0, if the param is not included in the call.
    :type start: int
    :param fq: This filter query can be used to filter offers by the criteria described below. It should be filled in by following the format: &#x60;fq&#x3D;{{criteriaName}}:{{criteriaValue}}&#x60;.   - **productId:** integer of the product ID   - **productName:** string of the product&#39;s name   - **skuId:** integer of the SKU ID   - **eanId:** string of the EAN ID   - **refId:** string of the Ref ID   - **categoryId:** integer of the category ID   - **brandId:** integer of the brand ID   - **sellerId:** string of the seller ID   - **sc:** integer of the sales channel&#39;s ID (trade policy in VTEX)   Ex: skuId:172   Ex: categoryId:13   Ex. productName:Product example-123
    :type fq: str

    """
    return web.Response(status=200)
