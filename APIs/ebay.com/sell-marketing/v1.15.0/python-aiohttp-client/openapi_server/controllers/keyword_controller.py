from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_create_keyword_request import BulkCreateKeywordRequest
from openapi_server.models.bulk_create_keyword_response import BulkCreateKeywordResponse
from openapi_server.models.bulk_update_keyword_request import BulkUpdateKeywordRequest
from openapi_server.models.bulk_update_keyword_response import BulkUpdateKeywordResponse
from openapi_server.models.create_keyword_request import CreateKeywordRequest
from openapi_server.models.keyword import Keyword
from openapi_server.models.keyword_paged_collection_response import KeywordPagedCollectionResponse
from openapi_server.models.update_keyword_request import UpdateKeywordRequest
from openapi_server import util


async def bulk_create_keyword(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_create_keyword

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method adds keywords, in bulk, to an existing PLA ad group in a campaign that uses the Cost Per Click (CPC) funding model.&lt;br /&gt;&lt;br /&gt;This method also sets the CPC rate for each keyword.&lt;br /&gt;&lt;br /&gt;In the request, supply the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a specified seller.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: A type that defines the fields for the bulk request to create keywords.
    :type body: dict | bytes

    """
    body = BulkCreateKeywordRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_update_keyword(request: web.Request, campaign_id, body) -> web.Response:
    """bulk_update_keyword

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method updates the bids and statuses of keywords, in bulk, for an existing PLA campaign.&lt;br /&gt;&lt;br /&gt;In the request, supply the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a specified seller.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: A type that defines the fields for the bulk request to update keywords.
    :type body: dict | bytes

    """
    body = BulkUpdateKeywordRequest.from_dict(body)
    return web.Response(status=200)


async def create_keyword(request: web.Request, campaign_id, body) -> web.Response:
    """create_keyword

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method creates keywords using a specified campaign ID for an existing PLA campaign.&lt;br /&gt;&lt;br /&gt;In the request, supply the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/suggestKeywords\&quot;&gt;suggestKeywords&lt;/a&gt; method to retrieve a list of keyword ideas to be targeted for PLA campaigns, and call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a seller.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param body: A type that defines the fields for the request to create a keyword.
    :type body: dict | bytes

    """
    body = CreateKeywordRequest.from_dict(body)
    return web.Response(status=200)


async def get_keyword(request: web.Request, campaign_id, keyword_id) -> web.Response:
    """get_keyword

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method retrieves details on a specific keyword from an ad group within a PLA campaign that uses the Cost Per Click (CPC) funding model.&lt;br /&gt;&lt;br /&gt;In the request, specify the &lt;b&gt;campaign_id&lt;/b&gt; and &lt;b&gt;keyword_id&lt;/b&gt; as path parameters.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a seller and call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/keyword/methods/getKeywords\&quot;&gt;getKeywords&lt;/a&gt; method to retrieve their keyword IDs.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param keyword_id: This path parameter is used to identify the keyword to retrieve.
    :type keyword_id: str

    """
    return web.Response(status=200)


async def get_keywords(request: web.Request, campaign_id, ad_group_ids=None, keyword_status=None, limit=None, offset=None) -> web.Response:
    """get_keywords

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method can be used to retrieve all of the keywords for ad groups in PLA campaigns that use the Cost Per Click (CPC) funding model.&lt;br /&gt;&lt;br /&gt;In the request, specify the &lt;b&gt;campaign_id&lt;/b&gt; as a path parameter. If one or more &lt;b&gt;ad_group_ids&lt;/b&gt; are passed in the request body, the keywords for those ad groups will be returned. If &lt;b&gt;ad_group_ids&lt;/b&gt; are not passed in the response body, the call will return all the keywords in the campaign.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a seller.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param ad_group_ids: A comma-separated list of ad group IDs. This query parameter is used if the seller wants to retrieve keywords from one or more specific ad groups. If this query parameter is not used, all keywords that are part of the CPC campaign are returned.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;You can call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/adgroup/methods/getAdGroups\&quot;&gt;getAdGroups&lt;/a&gt;  method to retrieve the ad group IDs for a seller.&lt;/span&gt;
    :type ad_group_ids: str
    :param keyword_status: A comma-separated list of keyword statuses. The results will be filtered to only include the given statuses of the keyword. If none are provided, all keywords are returned.
    :type keyword_status: str
    :param limit: &lt;p&gt;Specifies the maximum number of results to return on a page in the paginated response.&lt;/p&gt;  &lt;b&gt;Default: &lt;/b&gt;10 &lt;br&gt;&lt;b&gt;Maximum: &lt;/b&gt; 500
    :type limit: str
    :param offset: Specifies the number of results to skip in the result set before returning the first report in the paginated response.  &lt;p&gt;Combine &lt;b&gt;offset&lt;/b&gt; with the &lt;b&gt;limit&lt;/b&gt; query parameter to control the items returned in the response. For example, if you supply an &lt;b&gt;offset&lt;/b&gt; of &lt;code&gt;0&lt;/code&gt; and a &lt;b&gt;limit&lt;/b&gt; of &lt;code&gt;10&lt;/code&gt;, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If &lt;b&gt;offset&lt;/b&gt; is &lt;code&gt;10&lt;/code&gt; and &lt;b&gt;limit&lt;/b&gt; is &lt;code&gt;20&lt;/code&gt;, the first page of the response contains items 11-30 from the complete result set.&lt;/p&gt; &lt;p&gt;&lt;b&gt;Default:&lt;/b&gt; 0&lt;/p&gt;
    :type offset: str

    """
    return web.Response(status=200)


async def update_keyword(request: web.Request, campaign_id, keyword_id, body) -> web.Response:
    """update_keyword

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is only available for select partners who have been approved for the eBay Promoted Listings Advanced (PLA) program. For information about how to request access to this program, refer to &lt;a href&#x3D;\&quot;/api-docs/sell/static/marketing/pl-verify-eligibility.html#access-requests \&quot; target&#x3D;\&quot;_blank \&quot;&gt; Promoted Listings Advanced Access Requests&lt;/a&gt; in the Promoted Listings Playbook. To determine if a seller qualifies for PLA, use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/advertising_eligibility/methods/getAdvertisingEligibility \&quot; target&#x3D;\&quot;_blank \&quot;&gt;getAdvertisingEligibility&lt;/a&gt; method in Account API.&lt;/span&gt;&lt;br /&gt;This method updates keywords using a campaign ID and keyword ID for an existing PLA campaign.&lt;br /&gt;&lt;br /&gt;In the request, specify the &lt;b&gt;campaign_id&lt;/b&gt; and &lt;b&gt;keyword_id&lt;/b&gt; as path parameters.&lt;br /&gt;&lt;br /&gt;Call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method to retrieve a list of current campaign IDs for a seller and call the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/keyword/methods/getKeywords\&quot;&gt;getKeywords&lt;/a&gt; method to retrieve their keyword IDs.

    :param campaign_id: A unique eBay-assigned ID for an ad campaign that is generated when a campaign is created.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; You can retrieve the campaign IDs for a specified seller using the &lt;a href&#x3D;\&quot;/api-docs/sell/marketing/resources/campaign/methods/getCampaigns\&quot;&gt;getCampaigns&lt;/a&gt; method.&lt;/span&gt;
    :type campaign_id: str
    :param keyword_id: A unique eBay-assigned ID that is generated when a keyword is created.
    :type keyword_id: str
    :param body: A type that defines the fields for the request to update a keyword.
    :type body: dict | bytes

    """
    body = UpdateKeywordRequest.from_dict(body)
    return web.Response(status=200)
