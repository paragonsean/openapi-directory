from typing import List, Dict
from aiohttp import web

from openapi_server.models.items_paged_collection import ItemsPagedCollection
from openapi_server.models.promotions_paged_collection import PromotionsPagedCollection
from openapi_server import util


async def get_listing_set(request: web.Request, promotion_id, limit=None, offset=None, q=None, sort=None, status=None) -> web.Response:
    """get_listing_set

    This method returns the set of listings associated with the &lt;b&gt;promotion_id&lt;/b&gt; specified in the path parameter. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of a seller&#39;s promotions.  &lt;p&gt;The listing details are returned in a paginated set and you can control and results returned using the following query parameters: &lt;b&gt;limit&lt;/b&gt;, &lt;b&gt;offset&lt;/b&gt;, &lt;b&gt;q&lt;/b&gt;, &lt;b&gt;sort&lt;/b&gt;, and &lt;b&gt;status&lt;/b&gt;.&lt;/p&gt;  &lt;ul&gt;&lt;li&gt;&lt;b&gt;Maximum associated listings returned:&lt;/b&gt; 200&lt;/li&gt;  &lt;li&gt;&lt;b&gt;Default number of listings returned:&lt;/b&gt; 200&lt;/li&gt;&lt;/ul&gt;

    :param promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to get plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt;
    :type promotion_id: str
    :param limit: Specifies the maximum number of promotions returned on a page from the result set. &lt;br&gt;&lt;br&gt;&lt;b&gt;Default:&lt;/b&gt; 200&lt;br&gt;&lt;b&gt;Maximum:&lt;/b&gt; 200
    :type limit: str
    :param offset: Specifies the number of promotions to skip in the result set before returning the first promotion in the paginated response.  &lt;p&gt;Combine &lt;b&gt;offset&lt;/b&gt; with the &lt;b&gt;limit&lt;/b&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;b&gt;offset&lt;/b&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;b&gt;limit&lt;/b&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;b&gt;offset&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;b&gt;limit&lt;/b&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set.&lt;/p&gt; &lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 0&lt;/p&gt;
    :type offset: str
    :param q: Reserved for future use.
    :type q: str
    :param sort: Specifies the order in which to sort the associated listings in the response. If you precede the supplied value with a dash, the response is sorted in reverse order.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;code&gt;sort&#x3D;PRICE&lt;/code&gt; - Sorts the associated listings by their current price in ascending order &lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;code&gt;sort&#x3D;-TITLE&lt;/code&gt; - Sorts the associated listings by their title in descending alphabetical order (Z-Az-a)  &lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values&lt;/b&gt;:&lt;ul class&#x3D;\&quot;compact\&quot;&gt;&lt;li&gt;AVAILABLE&lt;/li&gt; &lt;li&gt;PRICE&lt;/li&gt; &lt;li&gt;TITLE&lt;/li&gt;&lt;/ul&gt; For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/csb:SortField
    :type sort: str
    :param status: This query parameter applies only to markdown promotions. It filters the response based on the indicated status of the promotion. Currently, the only supported value for this parameter is &lt;code&gt;MARKED_DOWN&lt;/code&gt;, which indicates active markdown promotions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/sme:ItemMarkdownStatusEnum
    :type status: str

    """
    return web.Response(status=200)


async def get_promotions(request: web.Request, marketplace_id, limit=None, offset=None, promotion_status=None, promotion_type=None, q=None, sort=None) -> web.Response:
    """get_promotions

    This method returns a list of a seller&#39;s undeleted promotions. &lt;p&gt;The call returns up to 200 currently-available promotions on the specified marketplace. While the response body does not include the promotion&#39;s &lt;b&gt;discountRules&lt;/b&gt; or &lt;b&gt;inventoryCriterion&lt;/b&gt; containers, it does include the &lt;b&gt;promotionHref&lt;/b&gt; (which you can use to retrieve the complete details of the promotion).&lt;/p&gt;  &lt;p&gt;Use query parameters to sort and filter the results by the number of promotions to return, the promotion state or type, and the eBay marketplace. You can also supply keywords to limit the response to the promotions that contain that keywords in the title of the promotion.&lt;/p&gt; &lt;p&gt;&lt;b&gt;Maximum returned:&lt;/b&gt; 200&lt;/p&gt;

    :param marketplace_id: The eBay marketplace ID of the site where the promotion is hosted.  &lt;p&gt;&lt;b&gt;Valid values:&lt;/b&gt;&lt;/p&gt;  &lt;ul&gt;&lt;li&gt;&lt;code&gt;EBAY_AU&lt;/code&gt; &#x3D; Australia&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_DE&lt;/code&gt; &#x3D; Germany&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_ES&lt;/code&gt; &#x3D; Spain&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_FR&lt;/code&gt; &#x3D; France&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_GB&lt;/code&gt; &#x3D; Great Britain&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_IT&lt;/code&gt; &#x3D; Italy&lt;/li&gt; &lt;li&gt;&lt;code&gt;EBAY_US&lt;/code&gt; &#x3D; United States&lt;/li&gt;&lt;/ul&gt;
    :type marketplace_id: str
    :param limit: Specifies the maximum number of promotions returned on a page from the result set.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Default:&lt;/b&gt; 200 &lt;br&gt;&lt;b&gt;Maximum:&lt;/b&gt; 200
    :type limit: str
    :param offset: Specifies the number of promotions to skip in the result set before returning the first promotion in the paginated response.  &lt;p&gt;Combine &lt;b&gt;offset&lt;/b&gt; with the &lt;b&gt;limit&lt;/b&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;b&gt;offset&lt;/b&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;b&gt;limit&lt;/b&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;b&gt;offset&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;b&gt;limit&lt;/b&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set.&lt;/p&gt; &lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 0&lt;/p&gt;
    :type offset: str
    :param promotion_status: Specifies the promotion state by which you want to filter the results. The response contains only those promotions that match the state you specify.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values:&lt;/b&gt; &lt;ul&gt;&lt;li&gt;&lt;code&gt;DRAFT&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;SCHEDULED&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;RUNNING&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;PAUSED&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;ENDED&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Maximum number of input values:&lt;/b&gt; 1
    :type promotion_status: str
    :param promotion_type: Filters the returned promotions based on their campaign promotion type. Specify one of the following values to indicate the promotion type you want returned: &lt;ul&gt;&lt;li&gt;&lt;code&gt;CODED_COUPON&lt;/code&gt; &amp;ndash; A coupon code promotion set with &lt;b&gt;createItemPromotion&lt;/b&gt;.&lt;/li&gt; &lt;li&gt;&lt;code&gt;MARKDOWN_SALE&lt;/code&gt; &amp;ndash; A markdown promotion set with &lt;b&gt;createItemPriceMarkdownPromotion&lt;/b&gt;.&lt;/li&gt; &lt;li&gt;&lt;code&gt;ORDER_DISCOUNT&lt;/code&gt; &amp;ndash; A threshold promotion set with &lt;b&gt;createItemPromotion&lt;/b&gt;.&lt;/li&gt; &lt;li&gt;&lt;code&gt;VOLUME_DISCOUNT&lt;/code&gt; &amp;ndash; A volume pricing promotion set with &lt;b&gt;createItemPromotion&lt;/b&gt;.&lt;/li&gt;&lt;/ul&gt;
    :type promotion_type: str
    :param q: A string consisting of one or more &lt;i&gt;keywords&lt;/i&gt;. eBay filters the response by returning only the promotions that contain the supplied keywords in the promotion title.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; \&quot;iPhone\&quot; or \&quot;Harry Potter.\&quot;  &lt;br&gt;&lt;br&gt;Commas that separate keywords are ignored. For example, a keyword string of \&quot;iPhone, iPad\&quot; equals \&quot;iPhone iPad\&quot;, and each results in a response that contains promotions with both \&quot;iPhone\&quot; and \&quot;iPad\&quot; in the title.
    :type q: str
    :param sort: Specifies the order for how to sort the response. If you precede the supplied value with a dash, the response is sorted in reverse order.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;code&gt;sort&#x3D;END_DATE&lt;/code&gt; &amp;nbsp; Sorts the promotions in the response by their end dates in ascending order &lt;br&gt;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;code&gt;sort&#x3D;-PROMOTION_NAME&lt;/code&gt; &amp;nbsp; Sorts the promotions by their promotion name in descending alphabetical order (Z-Az-a)  &lt;br&gt;&lt;br&gt;&lt;b&gt;Valid values&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;&lt;code&gt;START_DATE&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;END_DATE&lt;/code&gt;&lt;/li&gt; &lt;li&gt;&lt;code&gt;PROMOTION_NAME&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt; For implementation help, refer to eBay API documentation at https://developer.ebay.com/api-docs/sell/marketing/types/csb:SortField
    :type sort: str

    """
    return web.Response(status=200)


async def pause_promotion(request: web.Request, promotion_id) -> web.Response:
    """pause_promotion

    This method pauses a currently-active (RUNNING) threshold promotion and changes the state of the promotion from &lt;code&gt;RUNNING&lt;/code&gt; to &lt;code&gt;PAUSED&lt;/code&gt;. Pausing a promotion makes the promotion temporarily unavailable to buyers and any currently-incomplete transactions will not receive the promotional offer until the promotion is resumed. Also, promotion teasers are not displayed when a promotion is paused.  &lt;br&gt;&lt;br&gt;Pass the ID of the promotion you want to pause using the &lt;b&gt;promotion_id&lt;/b&gt; path parameter. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of the seller&#39;s promotions. &lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; You can only pause threshold promotions (you cannot pause markdown promotions).

    :param promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to pause plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt;
    :type promotion_id: str

    """
    return web.Response(status=200)


async def resume_promotion(request: web.Request, promotion_id) -> web.Response:
    """resume_promotion

    This method restarts a threshold promotion that was previously paused and changes the state of the promotion from &lt;code&gt;PAUSED&lt;/code&gt; to &lt;code&gt;RUNNING&lt;/code&gt;. Only promotions that have been previously paused can be resumed. Resuming a promotion reinstates the promotional teasers and any transactions that were in motion before the promotion was paused will again be eligible for the promotion.  &lt;br&gt;&lt;br&gt;Pass the ID of the promotion you want to resume using the &lt;b&gt;promotion_id&lt;/b&gt; path parameter. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/promotion/methods/getPromotions\&quot;&gt;getPromotions&lt;/a&gt; to retrieve the IDs of the seller&#39;s promotions.

    :param promotion_id: This path parameter takes a concatenation of the ID of the promotion you want to resume plus the marketplace ID on which the promotion is hosted. Concatenate the two values by separating them with an \&quot;at sign\&quot; (&lt;b&gt;@&lt;/b&gt;).  &lt;br&gt;&lt;br&gt;The ID of the promotion (&lt;b&gt;promotionId&lt;/b&gt;) is a unique eBay-assigned value that&#39;s generated when the promotion is created. The Marketplace ID is the ENUM value of eBay marketplace where the promotion is hosted. &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;1********5@EBAY_US&lt;/code&gt;
    :type promotion_id: str

    """
    return web.Response(status=200)
