from typing import List, Dict
from aiohttp import web

from openapi_server.models.ad_group import AdGroup
from openapi_server.models.ad_group_paged_collection_response import AdGroupPagedCollectionResponse
from openapi_server.models.create_ad_group_request import CreateAdGroupRequest
from openapi_server.models.targeted_bid_request import TargetedBidRequest
from openapi_server.models.targeted_bids_paged_collection import TargetedBidsPagedCollection
from openapi_server.models.targeted_keyword_request import TargetedKeywordRequest
from openapi_server.models.targeted_keywords_paged_collection import TargetedKeywordsPagedCollection
from openapi_server.models.update_ad_group_request import UpdateAdGroupRequest
from openapi_server import util


async def create_ad_group(request: web.Request, campaign_id, body) -> web.Response:
    """create_ad_group

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method adds an ad group to an existing PLA campaign that uses the Cost Per Click (CPC) funding model.&lt;br /&gt;&lt;br /&gt;To create an ad group for a campaign, specify the &lt;b&gt;defaultBid&lt;/b&gt; for the ad group in the payload of the request. Then specify the campaign to which the ad group should be associated using the &lt;b&gt;campaign_id&lt;/b&gt; path parameter.&lt;br /&gt;&lt;br /&gt;Each campaign can have one or more associated ad groups.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This type defines the fields for the &lt;b&gt;createAdGroup&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = CreateAdGroupRequest.from_dict(body)
    return web.Response(status=200)


async def get_ad_group(request: web.Request, ad_group_id, campaign_id) -> web.Response:
    """get_ad_group

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method retrieves the details of a specified ad group, such as the ad group’s default bid and status.&lt;br /&gt;&lt;br /&gt;In the request, specify the &lt;b&gt;campaign_id&lt;/b&gt; and &lt;b&gt;ad_group_id&lt;/b&gt; as path parameters.&lt;br /&gt;&lt;br /&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve a list of the current campaign IDs for a seller and call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\&quot;&gt;getAdGroups&lt;/a&gt; for the ad group ID of the ad group you wish to retrieve.

    :param ad_group_id: The ID of the ad group that shall be retrieved.
    :type ad_group_id: str
    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str

    """
    return web.Response(status=200)


async def get_ad_groups(request: web.Request, campaign_id, ad_group_status=None, limit=None, offset=None) -> web.Response:
    """get_ad_groups

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method retrieves ad groups for the specified campaigns.&lt;br /&gt;&lt;br /&gt;Each campaign can only have &lt;b&gt;one&lt;/b&gt; ad group.&lt;br /&gt;&lt;br /&gt;In the request, supply the &lt;b&gt;campaign_ids&lt;/b&gt; as path parameters.&lt;br /&gt;&lt;br /&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; to retrieve a list of the current campaign IDs for a seller.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param ad_group_status: A comma-separated list of ad group statuses. The results will be filtered to only include the given statuses of the ad group.&lt;br /&gt;&lt;br /&gt;The results might not include these ad groups if other search conditions exclude them.
    :type ad_group_status: str
    :param limit: The number of results, from the current result set, to be returned in a single page.
    :type limit: str
    :param offset: The number of results that will be skipped in the result set. This is used with the &lt;b&gt;limit&lt;/b&gt; field to control the pagination of the output.&lt;br /&gt;&lt;br /&gt;For example, if the &lt;b&gt;offset&lt;/b&gt; is set to &lt;code&gt;0&lt;/code&gt; and the &lt;b&gt;limit&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt;, the method will retrieve items 1 through 10 from the list of items returned. If the &lt;b&gt;offset&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt; and the &lt;b&gt;limit&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt;, the method will retrieve items 11 through 20 from the list of items returned.&lt;br&gt;&lt;br&gt;&lt;b&gt;Default&lt;/b&gt;: &lt;code&gt;0&lt;/code&gt;
    :type offset: str

    """
    return web.Response(status=200)


async def suggest_bids(request: web.Request, ad_group_id, campaign_id, body) -> web.Response:
    """suggest_bids

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method allows sellers to retrieve the suggested bids for input keywords and match type.

    :param ad_group_id: The ID of the ad group containing the keywords for which the bid suggestions will be provided.
    :type ad_group_id: str
    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: The data requested to retrieve the suggested bids.
    :type body: dict | bytes

    """
    body = TargetedBidRequest.from_dict(body)
    return web.Response(status=200)


async def suggest_keywords(request: web.Request, ad_group_id, campaign_id, body=None) -> web.Response:
    """suggest_keywords

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method allows sellers to retrieve a list of keyword ideas to be targeted for Promoted Listings campaigns.

    :param ad_group_id: The ID of the ad group for which the keyword suggestions will be provided.
    :type ad_group_id: str
    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: The required data to retrieve suggested keywords.
    :type body: dict | bytes

    """
    body = TargetedKeywordRequest.from_dict(body)
    return web.Response(status=200)


async def update_ad_group(request: web.Request, ad_group_id, campaign_id, body) -> web.Response:
    """update_ad_group

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method updates the ad group associated with a campaign.&lt;br /&gt;&lt;br /&gt;With this method, you can modify the &lt;b&gt;default bid&lt;/b&gt; for the ad group, change the state of the ad group, or change the name of the ad group. Pass the &lt;b&gt;ad_group_id&lt;/b&gt; you want to update as a URI parameter, and configure the &lt;b&gt;adGroupStatus&lt;/b&gt; and &lt;b&gt;defaultBid&lt;/b&gt; in the request payload.&lt;br /&gt;&lt;br /&gt;Call &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/adgroup/methods/getAdGroup\&quot;&gt;getAdGroup&lt;/a&gt; to retrieve the current default bid and status of the ad group that you would like to update.

    :param ad_group_id: The ID of the ad group that shall be updated.
    :type ad_group_id: str
    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: This type defines the fields for the &lt;b&gt;UpdateAdGroup&lt;/b&gt; request.
    :type body: dict | bytes

    """
    body = UpdateAdGroupRequest.from_dict(body)
    return web.Response(status=200)
