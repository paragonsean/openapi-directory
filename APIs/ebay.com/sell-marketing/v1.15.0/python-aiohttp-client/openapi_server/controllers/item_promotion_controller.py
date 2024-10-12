from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_response import BaseResponse
from openapi_server.models.item_promotion import ItemPromotion
from openapi_server.models.item_promotion_response import ItemPromotionResponse
from openapi_server import util


async def create_item_promotion(request: web.Request, body=None) -> web.Response:
    """create_item_promotion

    This method creates an &lt;b&gt;item promotion&lt;/b&gt;, where the buyer receives a discount when they meet the buying criteria that&#39;s set for the promotion. Known here as \&quot;threshold promotions\&quot;, these promotions trigger when a threshold is met.  &lt;p&gt;eBay highlights promoted items by placing teasers for the promoted items throughout the online buyer flows.&lt;/p&gt;  &lt;p&gt;&lt;i&gt;Discounts&lt;/i&gt; are specified as either a monetary amount or a percentage off the standard sales price of a listing, letting you offer deals such as \&quot;Buy 1 Get 1\&quot; and \&quot;Buy $50, get 20% off\&quot;.&lt;/p&gt; &lt;p&gt;&lt;i&gt;Volume pricing&lt;/i&gt; promotions increase the value of the discount as the buyer increases the quantity they purchase.&lt;/p&gt; &lt;p&gt;&lt;i&gt;Coded Coupons&lt;/i&gt; provide unique codes that a buyer can use during checkout to receive a discount. The seller can specify the number of times a buyer can use the coupon and the maximum amount across all purchases that can be discounted using the coupon. The coupon code can also be made public (appearing on the seller&#39;s Offer page, search pages, the item listing, and the checkout page) or private (only on the seller&#39;s Offer page, but the seller can include the code in email and social media).&lt;/p&gt; &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note&lt;/b&gt;: Coded Coupons are currently available in the US, UK, DE, FR, IT, ES, and AU marketplaces.&lt;/p&gt;&lt;p&gt;There are two ways to add items to a threshold promotion:&lt;/p&gt;  &lt;ul&gt;&lt;li&gt;&lt;b&gt;Key-based promotions&lt;/b&gt; select items using either the listing IDs or inventory reference IDs of the items you want to promote. Note that if you use inventory reference IDs, you must specify both the &lt;b&gt;inventoryReferenceId&lt;/b&gt; and the associated &lt;b&gt;inventoryReferenceType&lt;/b&gt; of the item(s) you want to include the promotion.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Rule-based promotions&lt;/b&gt; select items using a list of eBay category IDs or seller Store category IDs. Rules can further constrain items in a promotion by minimum and maximum prices, brands, and item conditions.&lt;/li&gt;&lt;/ul&gt;  &lt;p&gt;You must create a new promotion in either a &lt;code&gt;DRAFT&lt;/code&gt; or &lt;code&gt;SCHEDULED&lt;/code&gt; state. Use the DRAFT state when you are initially creating a promotion and you want to be sure it&#39;s correctly configured before scheduling it to run. When you create a promotion, the promotion ID is returned in the &lt;b&gt;Location&lt;/b&gt; response header. Use this ID to reference the promotion in subsequent requests.&lt;/p&gt;  &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Tip:&lt;/b&gt; Refer to the &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/promotions-manager.html\&quot;&gt;Selling Integration Guide&lt;/a&gt; for details and examples showing how to create and manage threshold promotions using the Promotions Manager.&lt;/p&gt;  &lt;p&gt;For information on the eBay marketplaces that support item promotions, see &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/static/overview.html#PM-requirements\&quot;&gt;Promotions Manager requirements and restrictions&lt;/a&gt;.&lt;/p&gt;

    :param body: This type defines the fields that describe an item promotion.
    :type body: dict | bytes

    """
    body = ItemPromotion.from_dict(body)
    return web.Response(status=200)


async def delete_item_promotion(request: web.Request, promotion_id) -> web.Response:
    """delete_item_promotion

    This method deletes the threshold promotion specified by the &lt;b&gt;promotion_id&lt;/b&gt; path parameter. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of a seller&#39;s promotions.  &lt;br&gt;&lt;br&gt;You can delete any promotion with the exception of those that are currently active (RUNNING). To end a running threshold promotion, call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/item_promotion/methods/updateItemPromotion\&quot;&gt;updateItemPromotion&lt;/a&gt; and adjust the &lt;b&gt;endDate&lt;/b&gt; field as appropriate.

    :param promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to delete plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt;
    :type promotion_id: str

    """
    return web.Response(status=200)


async def get_item_promotion(request: web.Request, promotion_id) -> web.Response:
    """get_item_promotion

    This method returns the complete details of the threshold promotion specified by the &lt;b&gt;promotion_id&lt;/b&gt; path parameter. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of a seller&#39;s promotions.

    :param promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to retrieve plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt;
    :type promotion_id: str

    """
    return web.Response(status=200)


async def update_item_promotion(request: web.Request, promotion_id, body=None) -> web.Response:
    """update_item_promotion

    This method updates the specified threshold promotion with the new configuration that you supply in the request. Indicate the promotion you want to update using the &lt;b&gt;promotion_id&lt;/b&gt; path parameter.  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of a seller&#39;s promotions.&lt;/p&gt;  &lt;p&gt;When updating a promotion, supply all the fields that you used to configure the original promotion (and not just the fields you are updating). eBay replaces the specified promotion with the values you supply in the update request and if you don&#39;t pass a field that currently has a value, the update request will fail.&lt;/p&gt;  &lt;p&gt;The parameters you are allowed to update with this request depend on the status of the promotion you&#39;re updating:  &lt;ul&gt;&lt;li&gt;DRAFT or SCHEDULED promotions: You can update any of the parameters in these promotions that have not yet started to run, including the &lt;b&gt;discountRules&lt;/b&gt;.&lt;/li&gt; &lt;li&gt;RUNNING or PAUSED promotions: You can change the &lt;b&gt;endDate&lt;/b&gt; and the item&#39;s inventory but you cannot change the promotional discount or the promotion&#39;s start date.&lt;/li&gt; &lt;li&gt;ENDED promotions: Nothing can be changed.&lt;/li&gt;&lt;/ul&gt; &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Tip:&lt;/b&gt; When updating a &lt;code&gt;RUNNING&lt;/code&gt; or &lt;code&gt;PAUSED&lt;/code&gt; promotion, set the &lt;b&gt;status&lt;/b&gt; field to &lt;code&gt;SCHEDULED&lt;/code&gt; for the update request. When the promotion is updated, the previous status (either &lt;code&gt;RUNNING&lt;/code&gt; or &lt;code&gt;PAUSED&lt;/code&gt;) is retained.&lt;/p&gt;

    :param promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to update plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt;
    :type promotion_id: str
    :param body: This type defines the fields that describe an item promotion.
    :type body: dict | bytes

    """
    body = ItemPromotion.from_dict(body)
    return web.Response(status=200)
