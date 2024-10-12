from typing import List, Dict
from aiohttp import web

from openapi_server.models.campaign import Campaign
from openapi_server.models.campaign_paged_collection_response import CampaignPagedCollectionResponse
from openapi_server.models.campaigns import Campaigns
from openapi_server.models.clone_campaign_request import CloneCampaignRequest
from openapi_server.models.create_campaign_request import CreateCampaignRequest
from openapi_server.models.targeted_ads_paged_collection import TargetedAdsPagedCollection
from openapi_server.models.update_adrate_strategy_request import UpdateAdrateStrategyRequest
from openapi_server.models.update_campaign_budget_request import UpdateCampaignBudgetRequest
from openapi_server.models.update_campaign_identification_request import UpdateCampaignIdentificationRequest
from openapi_server import util


async def clone_campaign(request: web.Request, campaign_id, body) -> web.Response:
    """clone_campaign

    This method clones (makes a copy of) the specified campaign&#39;s &lt;b&gt;campaign criterion&lt;/b&gt;. The &lt;b&gt;campaign criterion&lt;/b&gt; is a container for the fields that define the criteria for a rule-based campaign.&lt;p&gt;To clone a campaign, supply the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter in your call. There is no request payload.&lt;/p&gt;  &lt;p&gt;The ID of the newly-cloned campaign is returned in the &lt;b&gt;Location&lt;/b&gt; response header.&lt;/p&gt;&lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve a seller&#39;s current campaign IDs.&lt;/p&gt;  &lt;p&gt;&lt;b&gt;Requirement: &lt;/b&gt;In order to clone a campaign, the &lt;b&gt;campaignStatus&lt;/b&gt; must be &lt;code&gt;ENDED&lt;/code&gt; and the campaign must define a set of selection rules (it must be a rules-based campaign).&lt;/p&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created. This ID is the campaign ID of the campaign being cloned.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This type defines the fields for a clone campaign request.
    :type body: dict | bytes

    """
    body = CloneCampaignRequest.from_dict(body)
    return web.Response(status=200)


async def create_campaign(request: web.Request, body) -> web.Response:
    """create_campaign

    This method creates a Promoted Listings ad campaign. &lt;p&gt;A Promoted Listings &lt;i&gt;campaign&lt;/i&gt; is the structure into which you place the ads or ad group for the listings you want to promote.&lt;/p&gt;  &lt;p&gt;Identify the items you want to place into a campaign either by \&quot;key\&quot; or by \&quot;rule\&quot; as follows:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;b&gt;Rules-based campaigns&lt;/b&gt; &amp;ndash; A rules-based campaign adds items to the campaign according to the &lt;i&gt;criteria&lt;/i&gt; you specify in your call to &lt;b&gt;createCampaign&lt;/b&gt;. You can set the &lt;b&gt;autoSelectFutureInventory&lt;/b&gt; request field to &lt;code&gt;true&lt;/code&gt; so that after your campaign launches, eBay will regularly assess your new, revised, or newly-eligible listings to determine whether any should be added or removed from your campaign according to the rules you set. If there are, eBay will add or remove them automatically on a daily basis.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Key-based campaigns&lt;/b&gt; &amp;ndash; Add items to an existing campaign using either listing ID values or Inventory Reference values: &lt;ul&gt;&lt;li&gt;Add &lt;b&gt;listingId&lt;/b&gt; values to an existing campaign by calling either &lt;b&gt;createAdByListingID&lt;/b&gt; or &lt;b&gt;bulkCreateAdsByListingId&lt;/b&gt;.&lt;/li&gt;  &lt;li&gt;Add &lt;b&gt;inventoryReference&lt;/b&gt; values to an existing campaign by calling either &lt;b&gt;createAdByInventoryReference&lt;/b&gt; or &lt;b&gt;bulkCreateAdsByInventoryReference&lt;/b&gt;.&lt;/li&gt;&lt;li&gt;Add an &lt;b&gt;ad group&lt;/b&gt; to an existing campaign by calling &lt;b&gt;createAdGroup&lt;/b&gt;.&lt;/li&gt;&lt;/ul&gt;&lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; No matter how you add items to a Promoted Listings campaign, each campaign can contain ads for a maximum of 50,000 items. &lt;br&gt;&lt;br&gt;If a rules-based campaign identifies more than 50,000 items, ads are created for only the first 50,000 items identified by the specified criteria, and ads are not created for the remaining items.&lt;/p&gt;  &lt;p&gt;&lt;b&gt;Creating a campaign&lt;/b&gt;&lt;/p&gt; &lt;p&gt;To create a basic campaign, supply:&lt;/p&gt;  &lt;ul&gt;&lt;li&gt;The user-defined campaign name&lt;/li&gt; &lt;li&gt;The start date (and optionally the end date) of the campaign&lt;/li&gt; &lt;li&gt;The eBay marketplace on which the campaign is hosted&lt;/li&gt; &lt;li&gt;Details on the campaign funding model&lt;/li&gt;&lt;/ul&gt;  &lt;p&gt;The campaign funding model specifies how the Promoted Listings fee is calculated. Currently, the supported funding models are &lt;code&gt;COST_PER_SALE&lt;/code&gt; and &lt;code&gt;COST_PER_CLICK&lt;/code&gt;. For complete information on how the fee is calculated and when it applies, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#pl-fees\&quot;&gt;Promoted Listings fees&lt;/a&gt;.&lt;/p&gt;   &lt;p&gt;If you populate the &lt;b&gt;campaignCriterion&lt;/b&gt; object in your &lt;b&gt;createCampaign&lt;/b&gt; request, campaign \&quot;ads\&quot; are created by \&quot;rule\&quot; for the listings that meet the criteria you specify, and these ads are associated with the newly created campaign.&lt;/p&gt;  &lt;p&gt;For details on creating Promoted Listings campaigns and how to select the items to be included in your campaigns, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-create-campaign.html\&quot;&gt;Promoted Listings campaign creation&lt;/a&gt;.&lt;/p&gt;  &lt;p&gt;For recommendations on which listings are prime for a Promoted Listings ad campaign and to get guidance on how to set the &lt;b&gt;bidPercentage&lt;/b&gt; field, see &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-reco-api.html\&quot;&gt;Using the Recommendation API to help configure campaigns&lt;/a&gt;.&lt;/p&gt;  &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Tip:&lt;/b&gt; See &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/static/overview.html#PL-requirements\&quot;&gt;Promoted Listings requirements and restrictions&lt;/a&gt; for the details on the marketplaces that support Promoted Listings via the API. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-restrictions\&quot;&gt;Promoted Listings restrictions&lt;/a&gt; for details about campaign limitations and restrictions.&lt;/p&gt;

    :param body: This type defines the fields for the create campaign request.
    :type body: dict | bytes

    """
    body = CreateCampaignRequest.from_dict(body)
    return web.Response(status=200)


async def delete_campaign(request: web.Request, campaign_id) -> web.Response:
    """delete_campaign

    This method deletes the campaign specified by the &lt;code&gt;campaign_id&lt;/code&gt; query parameter.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note: &lt;/b&gt; You can only delete campaigns that have ended.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve the &lt;b&gt;campaign_id&lt;/b&gt; and the campaign status (&lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;PAUSED&lt;/code&gt;, &lt;code&gt;ENDED&lt;/code&gt;, and so on) for all the seller&#39;s campaigns.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str

    """
    return web.Response(status=200)


async def end_campaign(request: web.Request, campaign_id) -> web.Response:
    """end_campaign

    This method ends an active (&lt;code&gt;RUNNING&lt;/code&gt;) or paused campaign. Specify the campaign you want to end by supplying its campaign ID in a query parameter.  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve the &lt;b&gt;campaign_id&lt;/b&gt; and the campaign status (&lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;PAUSED&lt;/code&gt;, &lt;code&gt;ENDED&lt;/code&gt;, and so on) for all the seller&#39;s campaigns.&lt;/p&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str

    """
    return web.Response(status=200)


async def find_campaign_by_ad_reference(request: web.Request, inventory_reference_id=None, inventory_reference_type=None, listing_id=None) -> web.Response:
    """find_campaign_by_ad_reference

    This method retrieves the campaigns containing the listing that is specified using either a listing ID, or an inventory reference ID and inventory reference type pair. The request accepts either a &lt;b&gt;listing_id&lt;/b&gt;, &lt;i&gt;or&lt;/i&gt; an &lt;b&gt;inventory_reference_id&lt;/b&gt; and &lt;b&gt;inventory_reference_type&lt;/b&gt; pair, as used in the Inventory API.&lt;br /&gt;&lt;br /&gt;eBay &lt;i&gt;listing IDs&lt;/i&gt; are generated by either the &lt;a href&#x3D;\&quot;/Devzone/XML/docs/Reference/eBay/index.html\&quot; title&#x3D;\&quot;Trading API Reference\&quot;&gt;Trading API&lt;/a&gt; or the &lt;a href&#x3D;\&quot;/api-docs/sell/inventory/resources/methods\&quot;&gt;Inventory API&lt;/a&gt; when you create a listing.&lt;br /&gt;&lt;br /&gt;An &lt;i&gt;inventory reference ID&lt;/i&gt; can be either a seller-defined &lt;b&gt;SKU&lt;/b&gt; or &lt;b&gt;inventoryItemGroupKey&lt;/b&gt;, as specified in the Inventory API.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the Cost Per Sale (CPS) funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;

    :param inventory_reference_id: The seller&#39;s inventory reference ID of the listing to be used to find the campaign in which it is associated.  This will either be a seller-defined &lt;b&gt;SKU&lt;/b&gt; value or inventory item group ID, depending on the reference type specified. You must always pass in both  &lt;b&gt;inventory_reference_id&lt;/b&gt; and &lt;b&gt;inventory_reference_type&lt;/b&gt;.
    :type inventory_reference_id: str
    :param inventory_reference_type: The type of the seller&#39;s inventory reference ID, which is a listing or group of items. You must always pass in both &lt;b&gt;inventory_reference_id&lt;/b&gt; and &lt;b&gt;inventory_reference_type&lt;/b&gt;.
    :type inventory_reference_type: str
    :param listing_id: Identifier of the eBay listing associated with the ad.
    :type listing_id: str

    """
    return web.Response(status=200)


async def get_campaign(request: web.Request, campaign_id) -> web.Response:
    """get_campaign

    This method retrieves the details of a single campaign, as specified with the &lt;b&gt;campaign_id&lt;/b&gt; query parameter.  &lt;p&gt;This method returns all the details of a campaign (including the campaign&#39;s the selection rules), except the for the listing IDs or inventory reference IDs included in the campaign. These IDs are returned by &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/ad/methods/getAds\&quot;&gt;getAds&lt;/a&gt;.&lt;/p&gt;  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve a list of the seller&#39;s campaign IDs.&lt;/p&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str

    """
    return web.Response(status=200)


async def get_campaign_by_name(request: web.Request, campaign_name) -> web.Response:
    """get_campaign_by_name

    This method retrieves the details of a single campaign, as specified with the &lt;b&gt;campaign_name&lt;/b&gt; query parameter. Note that the campaign name you specify must be an exact, case-sensitive match of the name of the campaign you want to retrieve.&lt;/p&gt;&lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve a list of the seller&#39;s campaign names.&lt;/p&gt;

    :param campaign_name: The name of the campaign.
    :type campaign_name: str

    """
    return web.Response(status=200)


async def get_campaigns(request: web.Request, campaign_name=None, campaign_status=None, end_date_range=None, funding_strategy=None, limit=None, offset=None, start_date_range=None) -> web.Response:
    """get_campaigns

    This method retrieves the details for all of the seller&#39;s defined campaigns. Request parameters can be used to retrieve a specific campaign, such as the campaign&#39;s name, the start and end date, the status, and the funding model (Cost Per Sale (CPS) or Cost Per Click (CPC). &lt;p&gt;You can filter the result set by a campaign name, end date range, start date range, or campaign status. You can also paginate the records returned from the result set using the &lt;b&gt;limit&lt;/b&gt; query parameter, and control which records to return using the  &lt;b&gt;offset&lt;/b&gt; parameter.&lt;/p&gt;

    :param campaign_name: Specifies the campaign name. The results are filtered to include only the campaign by the specified name.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Note: &lt;/b&gt;The results might be null if other filters exclude the campaign with this name. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum: &lt;/b&gt; 1 campaign name
    :type campaign_name: str
    :param campaign_status: Include this filter and input a specific campaign status to retrieve campaigns currently in that state. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Note: &lt;/b&gt;The results might not include all the campaigns with this status if other filters exclude them. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid values:&lt;/b&gt; See &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/types/pls:CampaignStatusEnum\&quot;&gt;CampaignStatusEnum&lt;/a&gt; &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum: &lt;/b&gt; 1 status
    :type campaign_status: str
    :param end_date_range: Specifies the range of a campaign&#39;s end date. The results are filtered to include only campaigns with an end date that is within specified range. &lt;br&gt;&lt;br&gt;&lt;b&gt;Valid format (UTC)&lt;/b&gt;: &lt;ul&gt;&lt;li&gt;&lt;code&gt; yyyy-MM-ddThh:mm:ssZ..yyyy-MM-ddThh:mm:ssZ &lt;/code&gt;  (campaign ends within this range)&lt;/li&gt;&lt;li&gt;&lt;code&gt;yyyy-MM-ddThh:mm:ssZ..&lt;/code&gt; (campaign ends on or after this date)&lt;/li&gt;&lt;li&gt;&lt;code&gt;..yyyy-MM-ddThh:mm:ssZ &lt;/code&gt; (campaign ends on or before this date)&lt;/li&gt;&lt;li&gt;&lt;code&gt;2016-09-08T00:00.00.000Z..2016-09-09T00:00:00Z&lt;/code&gt; (campaign ends on September 08, 2016)&lt;/li&gt;&lt;/ul&gt; &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Note: &lt;/b&gt;The results might not include all the campaigns ending on this date if other filters exclude them.
    :type end_date_range: str
    :param funding_strategy: Specifies the funding strategy for the campaign.&lt;br /&gt;&lt;br /&gt;The results will be filtered to only include campaigns with the specified funding model. If not specified, all campaigns matching the other filter parameters will be returned. The results might not include these campaigns if other search conditions exclude them.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt;&lt;ul&gt;&lt;li&gt;&lt;code&gt;COST_PER_SALE&lt;/code&gt;&lt;/li&gt;&lt;li&gt;&lt;code&gt;COST_PER_CLICK&lt;/code&gt;&lt;/li&gt;&lt;/ul&gt;
    :type funding_strategy: str
    :param limit: &lt;p&gt;Specifies the maximum number of campaigns to return on a page in the paginated response.&lt;/p&gt;  &lt;b&gt;Default: &lt;/b&gt;10 &lt;br&gt;&lt;b&gt;Maximum: &lt;/b&gt; 500
    :type limit: str
    :param offset: Specifies the number of campaigns to skip in the result set before returning the first report in the paginated response.  &lt;p&gt;Combine &lt;b&gt;offset&lt;/b&gt; with the &lt;b&gt;limit&lt;/b&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;b&gt;offset&lt;/b&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;b&gt;limit&lt;/b&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;b&gt;offset&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;b&gt;limit&lt;/b&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set.&lt;/p&gt; &lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 0&lt;/p&gt;
    :type offset: str
    :param start_date_range: Specifies the range of a campaign&#39;s start date in which to filter the results. The results are filtered to include only campaigns with a start date that is equal to this date or is within specified range.&lt;br&gt;&lt;br&gt;&lt;b&gt;Valid format (UTC): &lt;/b&gt; &lt;ul&gt;&lt;li&gt;&lt;code&gt;yyyy-MM-ddThh:mm:ssZ..yyyy-MM-ddThh:mm:ssZ&lt;/code&gt; (starts within this range)&lt;/li&gt;&lt;li&gt;&lt;code&gt;yyyy-MM-ddThh:mm:ssZ&lt;/code&gt; (campaign starts on or after this date)&lt;/li&gt;&lt;li&gt;&lt;code&gt;..yyyy-MM-ddThh:mm:ssZ &lt;/code&gt;(campaign starts on or before this date)&lt;/li&gt;&lt;li&gt;&lt;code&gt;2016-09-08T00:00.00.000Z..2016-09-09T00:00:00Z&lt;/code&gt; (campaign starts on September 08, 2016)&lt;/li&gt;&lt;/ul&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Note: &lt;/b&gt;The results might not include all the campaigns with this start date if other filters exclude them.
    :type start_date_range: str

    """
    return web.Response(status=200)


async def pause_campaign(request: web.Request, campaign_id) -> web.Response:
    """pause_campaign

    This method pauses an active (RUNNING) campaign.  &lt;p&gt;You can restart the campaign by calling &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/resumeCampaign\&quot;&gt;resumeCampaign&lt;/a&gt;, as long as the campaign&#39;s end date is in the future.&lt;/p&gt;  &lt;p&gt;&lt;b&gt;Note: &lt;/b&gt; The listings associated with a paused campaign cannot be added into another campaign.&lt;/p&gt;  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve the &lt;b&gt;campaign_id&lt;/b&gt; and the campaign status (&lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;PAUSED&lt;/code&gt;, &lt;code&gt;ENDED&lt;/code&gt;, and so on) for all the seller&#39;s campaigns.&lt;/p&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str

    """
    return web.Response(status=200)


async def resume_campaign(request: web.Request, campaign_id) -> web.Response:
    """resume_campaign

    This method resumes a paused campaign, as long as its end date is in the future. Supply the &lt;b&gt;campaign_id&lt;/b&gt; for the campaign you want to restart as a query parameter in the request.  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve the &lt;b&gt;campaign_id&lt;/b&gt; and the campaign status (&lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;PAUSED&lt;/code&gt;, &lt;code&gt;ENDED&lt;/code&gt;, and so on) for all the seller&#39;s campaigns.&lt;/p&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str

    """
    return web.Response(status=200)


async def suggest_items(request: web.Request, campaign_id, category_ids=None, limit=None, offset=None) -> web.Response:
    """suggest_items

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method allows sellers to obtain ideas for listings, which can be targeted for Promoted Listings campaigns.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param category_ids: Specifies the category ID that is used to limit the results. This refers to an exact leaf category (the lowest level in that category and has no children). This field can have one category ID, or a comma-separated list of IDs. To return all category IDs, set to &lt;code&gt;null&lt;/code&gt;. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum: &lt;/b&gt; 10 
    :type category_ids: str
    :param limit: Specifies the maximum number of campaigns to return on a page in the paginated response. If no value is specified, the default value is used. &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default: &lt;/b&gt;10 &lt;br /&gt;&lt;br /&gt;&lt;b&gt;Minimum: &lt;/b&gt; 1&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum: &lt;/b&gt; 1000
    :type limit: str
    :param offset: Specifies the number of campaigns to skip in the result set before returning the first report in the paginated response.  &lt;p&gt;Combine &lt;b&gt;offset&lt;/b&gt; with the &lt;b&gt;limit&lt;/b&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;b&gt;offset&lt;/b&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;b&gt;limit&lt;/b&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;b&gt;offset&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;b&gt;limit&lt;/b&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set.&lt;/p&gt; &lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 0&lt;/p&gt;
    :type offset: str

    """
    return web.Response(status=200)


async def update_ad_rate_strategy(request: web.Request, campaign_id, body) -> web.Response:
    """update_ad_rate_strategy

    This method updates the ad rate strategy for an existing Promoted Listings Standard (PLS) rules-based ad campaign that uses the Cost Per Sale (CPS) funding model.&lt;br /&gt;&lt;br /&gt;Specify the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter. You can retrieve the campaign IDs for a seller by calling the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method only applies to the CPS funding model; it does not apply to the Cost Per Click (CPC) funding model. See &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-overview.html#funding-model\&quot;&gt;Funding Models&lt;/a&gt; in the &lt;i&gt;Promoted Listings Playbook&lt;/i&gt; for more information.&lt;/span&gt;

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This type defines the request fields for the ad rate strategy that shall be updated.
    :type body: dict | bytes

    """
    body = UpdateAdrateStrategyRequest.from_dict(body)
    return web.Response(status=200)


async def update_campaign_budget(request: web.Request, campaign_id, body) -> web.Response:
    """update_campaign_budget

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method updates the daily budget for a PLA campaign that uses the Cost Per Click (CPC) funding model.&lt;br /&gt;&lt;br /&gt;A click occurs when an eBay user finds and clicks on the seller’s listing (within the search results) after using a keyword that the seller has created for the campaign. For each ad in an ad group in the campaign, each click triggers a cost, which gets subtracted from the campaign’s daily budget. If the cost of the clicks exceeds the daily budget, the Promoted Listings campaign will be paused until the next day.&lt;br /&gt;&lt;br /&gt;Specify the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter. You can retrieve the campaign IDs for a seller by calling the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This type defines the request fields for the budget details that shall be updated.
    :type body: dict | bytes

    """
    body = UpdateCampaignBudgetRequest.from_dict(body)
    return web.Response(status=200)


async def update_campaign_identification(request: web.Request, campaign_id, body) -> web.Response:
    """update_campaign_identification

    This method can be used to change the name of a campaign, as well as modify the start or end dates. &lt;p&gt;Specify the &lt;b&gt;campaign_id&lt;/b&gt; you want to update as a URI parameter, and configure the &lt;b&gt;campaignName&lt;/b&gt; and &lt;b&gt;startDate&lt;/b&gt; in the request payload.  &lt;p&gt;If you want to change only the end date of the campaign, specify the current campaign name, set &lt;b&gt;endDate&lt;/b&gt; as desired, and set &lt;b&gt;startDate&lt;/b&gt; to the actual start date of the campaign. This applies if the campaign status is &lt;code&gt;RUNNING&lt;/code&gt; or &lt;code&gt;PAUSED&lt;/code&gt;. You can retrieve the &lt;b&gt;startDate&lt;/b&gt; using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaign#response.startDate\&quot;&gt;getCampaign&lt;/a&gt; method.&lt;/p&gt; &lt;p&gt;Note that if you do not set a new end date in this call, any current &lt;b&gt;endDate&lt;/b&gt; value will be set to &lt;code&gt;null&lt;/code&gt;. To preserve the currently-set end date, you must specify the value again in your request.&lt;/p&gt;  &lt;p&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve a seller&#39;s campaign details, including the campaign ID, campaign name, and the start and end dates of the campaign.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This type defines the fields to update the campaign name and start and end dates.
    :type body: dict | bytes

    """
    body = UpdateCampaignIdentificationRequest.from_dict(body)
    return web.Response(status=200)
