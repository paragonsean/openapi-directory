from typing import List, Dict
from aiohttp import web

from openapi_server.models.automotive_parts_compatibility_policy_response import AutomotivePartsCompatibilityPolicyResponse
from openapi_server.models.extended_producer_responsibility_policy_response import ExtendedProducerResponsibilityPolicyResponse
from openapi_server.models.hazardous_material_details_response import HazardousMaterialDetailsResponse
from openapi_server.models.item_condition_policy_response import ItemConditionPolicyResponse
from openapi_server.models.listing_structure_policy_response import ListingStructurePolicyResponse
from openapi_server.models.negotiated_price_policy_response import NegotiatedPricePolicyResponse
from openapi_server.models.return_policy_response import ReturnPolicyResponse
from openapi_server import util


async def get_automotive_parts_compatibility_policies(request: web.Request, marketplace_id, filter=None) -> web.Response:
    """get_automotive_parts_compatibility_policies

    This method returns the eBay policies that define how to list automotive-parts-compatibility items in the categories of a specific marketplace.  &lt;br&gt;&lt;br&gt;By default, this method returns the entire category tree for the specified marketplace. You can limit the size of the result set by using the &lt;b&gt;filter&lt;/b&gt; query parameter to specify only the category IDs you want to review.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt;&lt;/span&gt; This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the &lt;b&gt;Accept-Encoding&lt;/b&gt; request header and setting the value to &lt;code&gt;application/gzip&lt;/code&gt;.&lt;/span&gt;

    :param marketplace_id: This path parameter specifies the eBay marketplace for which policy information is retrieved.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; Only the following eBay marketplaces support automotive parts compatibility: &lt;ul&gt; &lt;li&gt;EBAY_US&lt;/li&gt; &lt;li&gt;EBAY_AU&lt;/li&gt; &lt;li&gt;EBAY_CA&lt;/li&gt; &lt;li&gt;EBAY_DE&lt;/li&gt; &lt;li&gt;EBAY_ES&lt;/li&gt; &lt;li&gt;EBAY_FR&lt;/li&gt; &lt;li&gt;EBAY_GB&lt;/li&gt; &lt;li&gt;EBAY_IT&lt;/li&gt;&lt;ul&gt;
    :type marketplace_id: str
    :param filter: This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt;
    :type filter: str

    """
    return web.Response(status=200)


async def get_extended_producer_responsibility_policies(request: web.Request, marketplace_id, filter=None) -> web.Response:
    """get_extended_producer_responsibility_policies

    This method returns the Extended Producer Responsibility policies for one, multiple, or all eBay categories in an eBay marketplace.&lt;br /&gt;&lt;br /&gt;The identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay category IDs are passed in through the filter query parameter, this method will return metadata on every applicable category for the specified marketplace.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#004680\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt;&lt;/span&gt; Currently, the Extended Producer Responsibility policies are only applicable to a limited number of categories, and only in the EBAY_FR marketplace.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt;&lt;/span&gt; This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the &lt;b&gt;Accept-Encoding&lt;/b&gt; request header and setting the value to &lt;code&gt;application/gzip&lt;/code&gt;.&lt;/span&gt;

    :param marketplace_id: A path parameter that specifies the eBay marketplace for which policy information shall be retrieved.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt;&lt;/span&gt; See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Request components&lt;/a&gt; for a list of valid eBay marketplace IDs.&lt;/span&gt;
    :type marketplace_id: str
    :param filter: A query parameter that can be used to limit the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree that should be returned.&lt;br /&gt;&lt;br /&gt;When a &lt;b&gt;categoryId&lt;/b&gt; value is specified, the returned category tree includes the policies for that parent node, as well as the policies for any child nodes below that parent node.&lt;br /&gt;&lt;br /&gt;Pass in the &lt;b&gt;categoryId&lt;/b&gt; values using a URL-encoded, pipe-separated (&#39;|&#39;) list. For example:&lt;br /&gt;&lt;br /&gt;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum:&lt;/b&gt; 50
    :type filter: str

    """
    return web.Response(status=200)


async def get_hazardous_materials_labels(request: web.Request, marketplace_id) -> web.Response:
    """get_hazardous_materials_labels

    This method returns hazardous materials label information for the specified eBay marketplace. The information includes IDs, descriptions, and URLs (as applicable) for the available signal words, statements, and pictograms. The returned statements are localized for the default langauge of the marketplace. If a marketplace does not support hazardous materials label information, an error is returned.&lt;p&gt;This information is used by the seller to add hazardous materials label related information to their listings (see &lt;a href&#x3D;&#39;/api-docs/sell/static/metadata/feature-regulatorhazmatcontainer.html&#39;&gt;Specifying hazardous material related information&lt;/a&gt;).&lt;/p&gt;

    :param marketplace_id: A path parameter that specifies the eBay marketplace for which hazardous materials label information shall be retrieved.&lt;p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt; See &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; &gt;Request components&lt;/a&gt; for a list of valid eBay marketplace IDs.&lt;/span&gt;&lt;/p&gt;
    :type marketplace_id: str

    """
    return web.Response(status=200)


async def get_item_condition_policies(request: web.Request, marketplace_id, filter=None) -> web.Response:
    """get_item_condition_policies

    This method returns item condition metadata on one, multiple, or all eBay categories on an eBay marketplace. This metadata consists of the different item conditions (with IDs) that an eBay category supports, and a boolean to indicate if an eBay category requires an item condition. &lt;br&gt;&lt;br&gt;The identifier of the eBay marketplace is passed in as a path parameter, and unless one or more eBay category IDs are passed in through the &lt;b&gt;filter&lt;/b&gt; query parameter, this method will return metadata on every single category for the specified marketplace. If you only want to view item condition metadata for one eBay category or a select group of eBay categories, you can pass in up to 50 eBay category ID through the &lt;b&gt;filter&lt;/b&gt; query parameter.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#FF0000\&quot;&gt;&lt;strong&gt;Important:&lt;/strong&gt;&lt;/span&gt; &lt;b&gt;Certified - Refurbished&lt;/b&gt;-eligible sellers, and sellers who are eligible to list with the new values (EXCELLENT_REFURBISHED, VERY_GOOD_REFURBISHED, and GOOD_REFURBISHED) must use an OAuth token created with the &lt;a href&#x3D;\&quot;/api-docs/static/oauth-authorization-code-grant.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;authorization code grant flow&lt;/a&gt; and &lt;b&gt;https://api.ebay.com/oauth/api_scope/sell.inventory&lt;/b&gt; scope in order to retrieve the refurbished conditions for the relevant categories.&lt;br/&gt;&lt;br/&gt;See the &lt;a href&#x3D;\&quot;/api-docs/sell/static/metadata/condition-id-values.html#Category \&quot; target&#x3D;\&quot;_blank\&quot;&gt;eBay Refurbished Program - Category and marketplace support&lt;/a&gt; topic for the categories and marketplaces that support these refurbished conditions&lt;br/&gt;&lt;br/&gt;These restricted item conditions will not be returned if an OAuth token created with the &lt;a href&#x3D;\&quot;/api-docs/static/oauth-client-credentials-grant.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;client credentials grant flow&lt;/a&gt; and &lt;b&gt;https://api.ebay.com/oauth/api_scope&lt;/b&gt; scope is used, or if any seller is not eligible to list with that item condition. &lt;br/&gt;&lt;br/&gt; See the &lt;a href&#x3D;\&quot;/api-docs/static/oauth-scopes.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Specifying OAuth scopes&lt;/a&gt; topic for more information about specifying scopes.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt;&lt;/span&gt; This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the &lt;b&gt;Accept-Encoding&lt;/b&gt; request header and setting the value to &lt;code&gt;application/gzip&lt;/code&gt;.&lt;/span&gt;

    :param marketplace_id: This path parameter specifies the eBay marketplace for which policy information is retrieved. See the following page for a list of valid eBay marketplace IDs: &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Request components&lt;/a&gt;.
    :type marketplace_id: str
    :param filter: This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt;
    :type filter: str

    """
    return web.Response(status=200)


async def get_listing_structure_policies(request: web.Request, marketplace_id, filter=None) -> web.Response:
    """get_listing_structure_policies

    This method returns the eBay policies that define the allowed listing structures for the categories of a specific marketplace. The listing-structure policies currently pertain to whether or not you can list items with variations.  &lt;br&gt;&lt;br&gt;By default, this method returns the entire category tree for the specified marketplace. You can limit the size of the result set by using the &lt;b&gt;filter&lt;/b&gt; query parameter to specify only the category IDs you want to review.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt;&lt;/span&gt; This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the &lt;b&gt;Accept-Encoding&lt;/b&gt; request header and setting the value to &lt;code&gt;application/gzip&lt;/code&gt;.&lt;/span&gt;

    :param marketplace_id: This path parameter specifies the eBay marketplace for which policy information is retrieved. See the following page for a list of valid eBay marketplace IDs: &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Request components&lt;/a&gt;.
    :type marketplace_id: str
    :param filter: This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt;
    :type filter: str

    """
    return web.Response(status=200)


async def get_negotiated_price_policies(request: web.Request, marketplace_id, filter=None) -> web.Response:
    """get_negotiated_price_policies

    This method returns the eBay policies that define the supported negotiated price features (like \&quot;best offer\&quot;) for the categories of a specific marketplace.  &lt;br&gt;&lt;br&gt;By default, this method returns the entire category tree for the specified marketplace. You can limit the size of the result set by using the &lt;b&gt;filter&lt;/b&gt; query parameter to specify only the category IDs you want to review.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt;&lt;/span&gt; This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the &lt;b&gt;Accept-Encoding&lt;/b&gt; request header and setting the value to &lt;code&gt;application/gzip&lt;/code&gt;.&lt;/span&gt;

    :param marketplace_id: This path parameter specifies the eBay marketplace for which policy information is retrieved. See the following page for a list of valid eBay marketplace IDs: &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Request components&lt;/a&gt;.
    :type marketplace_id: str
    :param filter: This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt;
    :type filter: str

    """
    return web.Response(status=200)


async def get_return_policies(request: web.Request, marketplace_id, filter=None) -> web.Response:
    """get_return_policies

    This method returns the eBay policies that define whether or not you must include a return policy for the items you list in the categories of a specific marketplace, plus the guidelines for creating domestic and international return policies in the different eBay categories.  &lt;br&gt;&lt;br&gt;By default, this method returns the entire category tree for the specified marketplace. You can limit the size of the result set by using the &lt;b&gt;filter&lt;/b&gt; query parameter to specify only the category IDs you want to review.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;span style&#x3D;\&quot;color:#478415\&quot;&gt;&lt;strong&gt;Tip:&lt;/strong&gt;&lt;/span&gt; This method can potentially return a very large response payload. eBay recommends that the response payload be compressed by passing in the &lt;b&gt;Accept-Encoding&lt;/b&gt; request header and setting the value to &lt;code&gt;application/gzip&lt;/code&gt;.&lt;/span&gt;

    :param marketplace_id: This path parameter specifies the eBay marketplace for which policy information is retrieved. See the following page for a list of valid eBay marketplace IDs: &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Request components&lt;/a&gt;.
    :type marketplace_id: str
    :param filter: This query parameter limits the response by returning policy information for only the selected sections of the category tree. Supply &lt;b&gt;categoryId&lt;/b&gt; values for the sections of the tree you want returned.  &lt;br&gt;&lt;br&gt;When you specify a &lt;b&gt;categoryId&lt;/b&gt; value, the returned category tree includes the policies for that parent node, plus the policies for any leaf nodes below that parent node.  &lt;br&gt;&lt;br&gt;The parameter takes a list of &lt;b&gt;categoryId&lt;/b&gt; values and you can specify up to 50 separate category IDs. Separate multiple values with a pipe character (&#39;|&#39;). If you specify more than 50 &lt;code&gt;categoryId&lt;/code&gt; values, eBay returns the policies for the first 50 IDs and a warning that not all categories were returned.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Example:&lt;/b&gt; &lt;code&gt;filter&#x3D;categoryIds:{100|101|102}&lt;/code&gt;  &lt;br&gt;&lt;br&gt;Note that you must URL-encode the parameter list, which results in the following filter for the above example: &lt;br&gt;&lt;br&gt; &amp;nbsp;&amp;nbsp;&lt;code&gt;filter&#x3D;categoryIds%3A%7B100%7C101%7C102%7D&lt;/code&gt;
    :type filter: str

    """
    return web.Response(status=200)
