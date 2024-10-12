from typing import List, Dict
from aiohttp import web

from openapi_server.models.ad import Ad
from openapi_server.models.ad_ids import AdIds
from openapi_server.models.ad_paged_collection_response import AdPagedCollectionResponse
from openapi_server.models.ad_references import AdReferences
from openapi_server.models.ads import Ads
from openapi_server.models.bulk_ad_response import BulkAdResponse
from openapi_server.models.bulk_ad_update_response import BulkAdUpdateResponse
from openapi_server.models.bulk_ad_update_status_by_listing_id_response import BulkAdUpdateStatusByListingIdResponse
from openapi_server.models.bulk_ad_update_status_response import BulkAdUpdateStatusResponse
from openapi_server.models.bulk_create_ad_request import BulkCreateAdRequest
from openapi_server.models.bulk_create_ads_by_inventory_reference_request import BulkCreateAdsByInventoryReferenceRequest
from openapi_server.models.bulk_create_ads_by_inventory_reference_response import BulkCreateAdsByInventoryReferenceResponse
from openapi_server.models.bulk_delete_ad_request import BulkDeleteAdRequest
from openapi_server.models.bulk_delete_ad_response import BulkDeleteAdResponse
from openapi_server.models.bulk_delete_ads_by_inventory_reference_request import BulkDeleteAdsByInventoryReferenceRequest
from openapi_server.models.bulk_delete_ads_by_inventory_reference_response import BulkDeleteAdsByInventoryReferenceResponse
from openapi_server.models.bulk_update_ad_status_by_listing_id_request import BulkUpdateAdStatusByListingIdRequest
from openapi_server.models.bulk_update_ad_status_request import BulkUpdateAdStatusRequest
from openapi_server.models.bulk_update_ads_by_inventory_reference_response import BulkUpdateAdsByInventoryReferenceResponse
from openapi_server.models.create_ad_request import CreateAdRequest
from openapi_server.models.create_ads_by_inventory_reference_request import CreateAdsByInventoryReferenceRequest
from openapi_server.models.delete_ads_by_inventory_reference_request import DeleteAdsByInventoryReferenceRequest
from openapi_server.models.update_bid_percentage_request import UpdateBidPercentageRequest
from openapi_server import util


async def bulk_create_ads_by_inventory_reference(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_create_ads_by_inventory_reference

    This method adds multiple listings that are managed with the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt; to an existing Promoted Listings campaign.&lt;br /&gt;&lt;br /&gt;For Promoted Listings Standard (PLS) campaigns using the Cost Per Sale (CPS) model, bulk ads may be directly created for the listing.&lt;br /&gt;&lt;br /&gt;For each listing specified in the request, this method:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Creates an ad for the listing.&lt;/li&gt; &lt;li&gt;Sets the bid percentage (also known as the &lt;i&gt;ad rate&lt;/i&gt;) for the ads created.&lt;/li&gt; &lt;li&gt;Associates the ads created with the specified campaign.&lt;/li&gt;&lt;/ul&gt;&lt;br /&gt;To create ads for a listing, specify their &lt;b&gt;inventoryReferenceId&lt;/b&gt; and &lt;b&gt;inventoryReferenceType&lt;/b&gt;, plus the &lt;b&gt;bidPercentage&lt;/b&gt; for the ad in the payload of the request. Specify the campaign to which you want to associate the ads using the &lt;b&gt;campaign_id&lt;/b&gt; path parameter.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;Use &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/createCampaign\&quot;&gt;createCampaign&lt;/a&gt; to create a new campaign and use &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to get a list of existing campaigns.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created. Get a seller&#39;s campaign IDs by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt;.
    :type campaign_id: str
    :param body: The container for the bulk request to create ads for eBay inventory reference IDs. eBay inventory reference IDs are seller-defined IDs used by theInventory API.
    :type body: dict | bytes

    """
    body = BulkCreateAdsByInventoryReferenceRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_create_ads_by_listing_id(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_create_ads_by_listing_id

    This method adds multiple listings to an existing Promoted Listings campaign using &lt;b&gt;listingId&lt;/b&gt; values generated by the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot; title&#x3D;\&quot;Trading API Reference\&quot;&gt;Trading API&lt;/a&gt; or &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt;, or using values generated by an ad group ID.&lt;p&gt;For Promoted Listings Standard (PLS) campaigns using the Cost Per Sale (CPS) funding model, bulk ads may be directly created for the listing.&lt;/p&gt;&lt;p&gt;For each listing ID specified in the request, this method:&lt;/p&gt;  &lt;ul&gt;&lt;li&gt;Creates an ad for the listing.&lt;/li&gt; &lt;li&gt;Sets the bid percentage (also known as the &lt;i&gt;ad rate&lt;/i&gt;) for the ad.&lt;/li&gt; &lt;li&gt;Associates the ad with the specified campaign.&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;To create an ad for a listing, specify its &lt;b&gt;listingId&lt;/b&gt;, plus the &lt;b&gt;bidPercentage&lt;/b&gt; for the ad in the payload of the request. Specify the campaign to associate the ads with using the &lt;b&gt;campaign_id&lt;/b&gt; path parameter. Listing IDs are generated by eBay when a seller creates listings with the Trading API.&lt;/p&gt;&lt;p&gt;You can specify a maximum of &lt;b&gt;500 listings per call&lt;/b&gt; and each campaign can have ads for a maximum of 50,000 items. Be aware when using this call that each variation in a multiple-variation listing creates an individual ad.&lt;/p&gt;&lt;p&gt;For Promoted Listings Advanced (PLA) campaigns using the Cost Per Click (CPC) funding model, an ad group must be created first. If no ad group has been created for the campaign, ads cannot be created.&lt;/p&gt;&lt;p&gt;For the ad group specified in the request, this method associates the ad with the specified ad group.&lt;/p&gt;&lt;p&gt;To create an ad for an ad group, specify the name of the ad group plus the &lt;b&gt;defaultBid&lt;/b&gt; for the ad in the payload of the request. Specify the campaign to associate the ads with using the &lt;b&gt;campaign_id&lt;/b&gt; path parameter. Ad groups are generated using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/adgroup/methods/createAdGroup\&quot;&gt;createAdGroup&lt;/a&gt;  method.&lt;/p&gt; &lt;p&gt;You can specify one or more ad groups per campaign.&lt;/p&gt;&lt;p&gt;Use &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/createCampaign\&quot;&gt;createCampaign&lt;/a&gt; to create a new campaign and use &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to get a list of existing campaigns.&lt;/p&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that&#39;s generated when a campaign is created. Get a seller&#39;s campaign IDs by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt;.
    :type campaign_id: str
    :param body: The container for the bulk request to create ads for eBay listing IDs. eBay listing IDs are generated by the Trading API and Inventory API when the listing is created on eBay.
    :type body: dict | bytes

    """
    body = BulkCreateAdRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_delete_ads_by_inventory_reference(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_delete_ads_by_inventory_reference

    This method works with listings created with the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt;.&lt;br /&gt;&lt;br /&gt;The method deletes a set of ads, as specified by a list of inventory reference IDs, from the specified campaign. &lt;i&gt;Inventory reference IDs&lt;/i&gt; are seller-defined IDs that are used with the Inventory API&lt;/a&gt;.&lt;br /&gt;&lt;br /&gt;Pass the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter and populate the payload with a list of &lt;b&gt;inventoryReferenceId&lt;/b&gt; and &lt;b&gt;inventoryReferenceType&lt;/b&gt; pairs that you want to delete.&lt;br /&gt;&lt;br /&gt;Get the campaign IDs for a seller by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; and call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAds\&quot;&gt;getAds&lt;/a&gt; to get a list of the seller&#39;s inventory reference IDs.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that&#39;s generated when a campaign is created. Get a seller&#39;s campaign IDs by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt;.
    :type campaign_id: str
    :param body: This request works with listings created via the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot;&gt;Inventory API&lt;/a&gt;.&lt;br /&gt;&lt;br /&gt;The request is to delete a set of ads in bulk, as specified by a list of inventory reference IDs from the specified campaign.
    :type body: dict | bytes

    """
    body = BulkDeleteAdsByInventoryReferenceRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_delete_ads_by_listing_id(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_delete_ads_by_listing_id

    This method works with listing IDs created with either the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot; title&#x3D;\&quot;Trading API Reference\&quot;&gt;Trading API&lt;/a&gt; or the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt;.&lt;br /&gt;&lt;br /&gt;The method deletes a set of ads, as specified by a list of &lt;b&gt;listingID&lt;/b&gt; values from a Promoted Listings campaign. A listing ID value is generated by eBay when a seller creates a listing with either the Trading API and Inventory API.&lt;br /&gt;&lt;br /&gt;Pass the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter and populate the payload with the set of listing IDs that you want to delete.&lt;br /&gt;&lt;br /&gt;Get the campaign IDs for a seller by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; and call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAds\&quot;&gt;getAds&lt;/a&gt; to get a list of the seller&#39;s inventory reference IDs.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;When using the CPC funding model, use the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/bulkUpdateAdsStatusByListingId\&quot;&gt;bulkUpdateAdsStatusByListingId&lt;/a&gt; method to change the status of ads to ARCHIVED.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that&#39;s generated when a campaign is created. Get a seller&#39;s campaign IDs by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt;.
    :type campaign_id: str
    :param body: This request object defines the fields for the &lt;b&gt;bulkDeleteAdsByListingId&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = BulkDeleteAdRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_update_ads_bid_by_inventory_reference(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_update_ads_bid_by_inventory_reference

    This method works with listings created with either the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot; title&#x3D;\&quot;Trading API Reference\&quot;&gt;Trading API&lt;/a&gt; or the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt;.  &lt;p&gt;The method updates the &lt;b&gt;bidPercentage&lt;/b&gt; values for a set of ads associated with the specified campaign.&lt;/p&gt;  &lt;p&gt;Specify the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter and supply a set of listing IDs with their associated updated &lt;b&gt;bidPercentage&lt;/b&gt; values in the request body. An eBay listing ID is generated when a listing is created with the Trading API.&lt;/p&gt;  &lt;p&gt;Get the campaign IDs for a seller by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; and call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAds\&quot;&gt;getAds&lt;/a&gt; to get a list of the seller&#39;s inventory reference IDs.&lt;/p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that&#39;s generated when a campaign is created. Get a seller&#39;s campaign IDs by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt;.
    :type campaign_id: str
    :param body: This request object defines the fields for the &lt;b&gt;BulkCreateAdsByInventoryReference&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = BulkCreateAdsByInventoryReferenceRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_update_ads_bid_by_listing_id(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_update_ads_bid_by_listing_id

    This method works with listings created with either the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot; title&#x3D;\&quot;Trading API Reference\&quot;&gt;Trading API&lt;/a&gt; or the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt;.  &lt;p&gt;The method updates the &lt;b&gt;bidPercentage&lt;/b&gt; values for a set of ads associated with the specified campaign.&lt;/p&gt;  &lt;p&gt;Specify the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter and supply a set of listing IDs with their associated updated &lt;b&gt;bidPercentage&lt;/b&gt; values in the request body. An eBay listing ID is generated when a listing is created with the Trading API.&lt;/p&gt;  &lt;p&gt;Get the campaign IDs for a seller by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; and call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAds\&quot;&gt;getAds&lt;/a&gt; to get a list of the seller&#39;s inventory reference IDs.&lt;/p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that&#39;s generated when a campaign is created. Get a seller&#39;s campaign IDs by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt;.
    :type campaign_id: str
    :param body: This request object defines the fields for the &lt;b&gt;BulkCreateAdsByListingId&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = BulkCreateAdRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_update_ads_status(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_update_ads_status

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method works with listings created with either the &lt;a href&#x3D; \&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot;&gt;Trading API&lt;/a&gt; or the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot;&gt;Inventory API&lt;/a&gt;.&lt;br /&gt;&lt;br /&gt;This method updates the status of ads in bulk.&lt;br /&gt;&lt;br /&gt;Specify the &lt;b&gt;campaign_id&lt;/b&gt; you want to update as a URI parameter, and configure the &lt;b&gt;adGroupStatus&lt;/b&gt; in the request payload.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: The bulk request to update the ads.
    :type body: dict | bytes

    """
    body = BulkUpdateAdStatusRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_update_ads_status_by_listing_id(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_update_ads_status_by_listing_id

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method works with listings created with either the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot;&gt;Trading API&lt;/a&gt; or the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot;&gt;Inventory API&lt;/a&gt;.&lt;br /&gt;&lt;br /&gt;The method updates the status of ads in bulk, based on listing ID values.&lt;br /&gt;&lt;br /&gt;Specify the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter and supply a set of listing IDs with their updated &lt;b&gt;adStatus&lt;/b&gt; values in the request body. An eBay listing ID is generated when a listing is created with the Trading API.&lt;br /&gt;&lt;br /&gt;Get the campaign IDs for a seller by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; and call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAds\&quot;&gt;getAds&lt;/a&gt; to retrieve a list of seller inventory reference IDs.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: The bulk request to update ads.
    :type body: dict | bytes

    """
    body = BulkUpdateAdStatusByListingIdRequest.from_dict(body)
    return web.Response(status=200)


async def create_ad_by_listing_id(request: web.Request, campaign_id, body) -> web.Response:
    """create_ad_by_listing_id

    This method adds a listing to an existing Promoted Listings campaign using a &lt;b&gt;listingId&lt;/b&gt; value generated by the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot; title&#x3D;\&quot;Trading API Reference\&quot;&gt;Trading API&lt;/a&gt; or &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt;, or using a value generated by an ad group ID. &lt;p&gt;For Promoted Listings Standard (PLS) campaigns using the Cost Per Sale (CPS) funding model, an ad may be directly created for the listing.&lt;/p&gt;&lt;p&gt;For the listing ID specified in the request, this method:&lt;/p&gt;  &lt;ul&gt;&lt;li&gt;Creates an ad for the listing.&lt;/li&gt; &lt;li&gt;Sets the bid percentage (also known as the &lt;i&gt;ad rate&lt;/i&gt;) for the ad.&lt;/li&gt; &lt;li&gt;Associates the ad with the specified campaign.&lt;/li&gt;&lt;/ul&gt;  &lt;p&gt;To create an ad for a listing, specify its &lt;b&gt;listingId&lt;/b&gt;, plus the &lt;b&gt;bidPercentage&lt;/b&gt; for the ad in the payload of the request. Specify the campaign to associate the ad with using the &lt;b&gt;campaign_id&lt;/b&gt; path parameter. Listing IDs are generated by eBay when a seller creates listings with the Trading API.&lt;/p&gt;&lt;p&gt;For Promoted Listings Advanced (PLA) campaigns using the Cost Per Click (CPC) funding model, an ad group must be created first. If no ad group has been created for the campaign, an ad cannot be created.&lt;/p&gt;&lt;p&gt;For the ad group specified in the request, this method associates the ad with the specified ad group.&lt;/p&gt;&lt;p&gt;To create an ad for an ad group, specify the name of the ad group in the payload of the request. Specify the campaign to associate the ads with using the &lt;b&gt;campaign_id&lt;/b&gt; path parameter. Ad groups are generated using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/adgroup/methods/createAdGroup\&quot;&gt;createAdGroup&lt;/a&gt; method.&lt;/p&gt; &lt;p&gt;You can specify one or more ad groups per campaign.&lt;/p&gt;&lt;p&gt;Use &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/createCampaign\&quot;&gt;createCampaign&lt;/a&gt; to create a new campaign and use &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to get a list of existing campaigns.&lt;/p&gt;&lt;p&gt;This call has no response payload. If the ad is successfully created, a &lt;code&gt;201 Created&lt;/code&gt; HTTP status code and the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAd\&quot;&gt;getAd&lt;/a&gt; URI of the ad are returned in the location header.&lt;/p&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This request object defines the fields used in the &lt;b&gt;createAdByListingId&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = CreateAdRequest.from_dict(body)
    return web.Response(status=200)


async def create_ads_by_inventory_reference(request: web.Request, campaign_id, body) -> web.Response:
    """create_ads_by_inventory_reference

    This method adds a listing that is managed with the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt; to an existing Promoted Listings campaign.&lt;br /&gt;&lt;br /&gt;For Promoted Listings Standard (PLS) campaigns using the Cost Per Sale (CPS) funding model, an ad may be directly created for the listing.&lt;br /&gt;&lt;br /&gt;For each listing specified in the request, this method:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Creates an ad for the listing.&lt;/li&gt; &lt;li&gt;Sets the bid percentage (also known as the &lt;i&gt;ad rate&lt;/i&gt;) for the ads created.&lt;/li&gt; &lt;li&gt;Associates the created ad with the specified campaign.&lt;/li&gt;&lt;/ul&gt;&lt;br /&gt;To create an ad for a listing, specify its &lt;b&gt;inventoryReferenceId&lt;/b&gt; and &lt;b&gt;inventoryReferenceType&lt;/b&gt;, plus the &lt;b&gt;bidPercentage&lt;/b&gt; for the ad in the payload of the request. Specify the campaign to associate the ad with using the &lt;b&gt;campaign_id&lt;/b&gt; path parameter.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;Use &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/createCampaign\&quot;&gt;createCampaign&lt;/a&gt; to create a new campaign and use &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to get a list of existing campaigns.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This request object defines the fields used in the &lt;b&gt;createAdsByInventoryReference&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = CreateAdsByInventoryReferenceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_ad(request: web.Request, ad_id, campaign_id) -> web.Response:
    """delete_ad

    This method removes the specified ad from the specified campaign.&lt;br /&gt;&lt;br /&gt;Pass the ID of the ad to delete with the ID of the campaign associated with the ad as path parameters to the call.&lt;br /&gt;&lt;br /&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to get the current list of the seller&#39;s campaign IDs.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;When using the CPC funding model, use the &lt;b&gt;bulkUpdateAdsStatusByListingId&lt;/b&gt; method to change the status of ads to ARCHIVED.

    :param ad_id: Identifier of an ad. This ID was generated when the ad was created.
    :type ad_id: str
    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str

    """
    return web.Response(status=200)


async def delete_ads_by_inventory_reference(request: web.Request, campaign_id, body) -> web.Response:
    """delete_ads_by_inventory_reference

    This method works with listings that are managed with the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt;.  &lt;p&gt;The method deletes ads using a list of seller-defined inventory reference IDs, used with the Inventory API, that are associated with the specified campaign ID.&lt;/p&gt; &lt;p&gt;Specify the campaign ID (as a path parameter) and a list of &lt;b&gt;inventoryReferenceId&lt;/b&gt; and &lt;b&gt;inventoryReferenceType&lt;/b&gt; pairs to be deleted.&lt;/p&gt;  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to get a list of the seller&#39;s current campaign IDs.&lt;/p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;When using the CPC funding model, use the bulkUpdateAdsStatusByInventoryReference method to change the status of ads to ARCHIVED.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This request object defines the fields for the &lt;b&gt;deleteAdsByInventoryReference&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = DeleteAdsByInventoryReferenceRequest.from_dict(body)
    return web.Response(status=200)


async def get_ad(request: web.Request, ad_id, campaign_id) -> web.Response:
    """get_ad

    This method retrieves the specified ad from the specified campaign.  &lt;p&gt;In the request, supply the &lt;b&gt;campaign_id&lt;/b&gt; and &lt;b&gt;ad_id&lt;/b&gt; as path parameters.&lt;/p&gt; &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve a list of the seller&#39;s current campaign IDs and call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAds\&quot;&gt;getAds&lt;/a&gt; to retrieve their current ad IDs.&lt;/p&gt;

    :param ad_id: A unique identifier for an ad. This ID is generated when the ad is created.
    :type ad_id: str
    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str

    """
    return web.Response(status=200)


async def get_ads(request: web.Request, campaign_id, ad_group_ids=None, ad_status=None, limit=None, listing_ids=None, offset=None) -> web.Response:
    """get_ads

    This method retrieves Promoted Listings ads that are associated with listings created with either the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot; title&#x3D;\&quot;Trading API Reference\&quot;&gt;Trading API&lt;/a&gt; or the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt;. &lt;p&gt;The method retrieves ads related to the specified campaign. Specify the Promoted Listings campaign to target with the &lt;b&gt;campaign_id&lt;/b&gt; path parameter.&lt;/p&gt;  &lt;p&gt;Because of the large number of possible results, you can use query parameters to paginate the result set by specifying a &lt;b&gt;limit&lt;/b&gt;, which dictates how many ads to return on each page of the response. You can also specify how many ads to skip in the result set before returning the first result using the &lt;b&gt;offset&lt;/b&gt; path parameter.&lt;/p&gt;  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve the current campaign IDs for the seller.&lt;/p&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param ad_group_ids: A comma-separated list of ad group IDs. The results will be filtered to only include active ads for these ad groups. Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\&quot;&gt;getAdGroups&lt;/a&gt; to retrieve the ad group ID for the ad group.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This field only applies to the Cost Per Click (CPC) funding model; it does not apply to the Cost Per Sale (CPS) funding model.&lt;/span&gt;
    :type ad_group_ids: str
    :param ad_status: A comma-separated list of ad statuses. The results will be filtered to only include the given statuses of the ad. If none are provided, all ads are returned.
    :type ad_status: str
    :param limit: Specifies the maximum number of ads to return on a page in the paginated response. &lt;p&gt;&lt;b&gt;Default: &lt;/b&gt;10 &lt;br&gt;&lt;b&gt;Maximum:&lt;/b&gt; 500&lt;/p&gt;
    :type limit: str
    :param listing_ids: A comma-separated list of listing IDs. The response includes only active ads (ads associated with a RUNNING campaign). The results do not include listing IDs that are excluded by other conditions.
    :type listing_ids: str
    :param offset: Specifies the number of ads to skip in the result set before returning the first ad in the paginated response.  &lt;p&gt;Combine &lt;b&gt;offset&lt;/b&gt; with the &lt;b&gt;limit&lt;/b&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;b&gt;offset&lt;/b&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;b&gt;limit&lt;/b&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;b&gt;offset&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;b&gt;limit&lt;/b&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set.&lt;/p&gt; &lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 0&lt;/p&gt;
    :type offset: str

    """
    return web.Response(status=200)


async def get_ads_by_inventory_reference(request: web.Request, campaign_id, inventory_reference_id, inventory_reference_type) -> web.Response:
    """get_ads_by_inventory_reference

    This method retrieves Promoted Listings ads associated with listings that are managed with the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot; title&#x3D;\&quot;Inventory API Reference\&quot;&gt;Inventory API&lt;/a&gt; from the specified campaign.&lt;br /&gt;&lt;br /&gt;Supply the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter and use query parameters to specify the &lt;b&gt;inventory_reference_id&lt;/b&gt; and &lt;b&gt;inventory_reference_type&lt;/b&gt; pairs.&lt;br /&gt;&lt;br /&gt;In the Inventory API, an &lt;i&gt;inventory reference ID&lt;/i&gt; is either a seller-defined &lt;b&gt;SKU&lt;/b&gt; value or an &lt;b&gt;inventoryItemGroupKey&lt;/b&gt; (a seller-defined ID for an inventory item group, which is an entity that&#39;s used in the Inventory API to create a multiple-variation listing). To indicate a listing managed by the Inventory API, you must always specify both an &lt;b&gt;inventory_reference_id&lt;/b&gt; and the associated &lt;b&gt;inventory_reference_type&lt;/b&gt;.&lt;br /&gt;&lt;br /&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve all of the seller&#39;s the current campaign IDs.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param inventory_reference_id: The inventory reference ID associated with the ad you want returned. A seller&#39;s inventory reference ID is the ID of either a listing or the ID of an inventory item group (the parent of a multi-variation listing, such as a shirt that is available in multiple sizes and colors). You must always supply in both an &lt;b&gt;inventory_reference_id&lt;/b&gt; and an &lt;b&gt;inventory_reference_type&lt;/b&gt;.
    :type inventory_reference_id: str
    :param inventory_reference_type: The type of the inventory reference ID. Set this value to either &lt;code&gt;INVENTORY_ITEM&lt;/CODE&gt; (a single listing) or &lt;code&gt;INVENTORY_ITEM_GROUP&lt;/CODE&gt; (a multi-variation listing). You must always pass in both an &lt;b&gt;inventory_reference_id&lt;/b&gt; and an &lt;b&gt;inventory_reference_type&lt;/b&gt;. 
    :type inventory_reference_type: str

    """
    return web.Response(status=200)


async def update_bid(request: web.Request, ad_id, campaign_id, body) -> web.Response:
    """update_bid

    This method updates the bid percentage (also known as the \&quot;ad rate\&quot;) for the specified ad in the specified campaign. &lt;p&gt;In the request, supply the &lt;b&gt;campaign_id&lt;/b&gt; and &lt;b&gt;ad_id&lt;/b&gt; as path parameters, and supply the new &lt;b&gt;bidPercentage&lt;/b&gt; value in the payload of the call.&lt;/p&gt;  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve a seller&#39;s current campaign IDs and call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAds\&quot;&gt;getAds&lt;/a&gt; to get their ad IDs.&lt;/p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;

    :param ad_id: A unique eBay-assigned ID for an ad that&#39;s generated when an ad is created.
    :type ad_id: str
    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This type defines the fields for the &lt;b&gt;updateBid&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = UpdateBidPercentageRequest.from_dict(body)
    return web.Response(status=200)
