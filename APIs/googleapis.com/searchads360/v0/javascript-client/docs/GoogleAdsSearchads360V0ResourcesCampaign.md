# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesCampaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adServingOptimizationStatus** | **String** | The ad serving optimization status of the campaign. | [optional] 
**advertisingChannelSubType** | **String** | Immutable. Optional refinement to &#x60;advertising_channel_type&#x60;. Must be a valid sub-type of the parent channel type. Can be set only when creating campaigns. After campaign is created, the field can not be changed. | [optional] 
**advertisingChannelType** | **String** | Immutable. The primary serving target for ads within the campaign. The targeting options can be refined in &#x60;network_settings&#x60;. This field is required and should not be empty when creating new campaigns. Can be set only when creating campaigns. After the campaign is created, the field can not be changed. | [optional] 
**biddingStrategy** | **String** | Portfolio bidding strategy used by campaign. | [optional] 
**biddingStrategySystemStatus** | **String** | Output only. The system status of the campaign&#39;s bidding strategy. | [optional] [readonly] 
**biddingStrategyType** | **String** | Output only. The type of bidding strategy. A bidding strategy can be created by setting either the bidding scheme to create a standard bidding strategy or the &#x60;bidding_strategy&#x60; field to create a portfolio bidding strategy. This field is read-only. | [optional] [readonly] 
**campaignBudget** | **String** | The budget of the campaign. | [optional] 
**createTime** | **String** | Output only. The timestamp when this campaign was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. create_time will be deprecated in v1. Use creation_time instead. | [optional] [readonly] 
**creationTime** | **String** | Output only. The timestamp when this campaign was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. | [optional] [readonly] 
**dynamicSearchAdsSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignDynamicSearchAdsSetting**](GoogleAdsSearchads360V0ResourcesCampaignDynamicSearchAdsSetting.md) |  | [optional] 
**endDate** | **String** | The last day of the campaign in serving customer&#39;s timezone in YYYY-MM-DD format. On create, defaults to 2037-12-30, which means the campaign will run indefinitely. To set an existing campaign to run indefinitely, set this field to 2037-12-30. | [optional] 
**engineId** | **String** | Output only. ID of the campaign in the external engine account. This field is for non-Google Ads account only, for example, Yahoo Japan, Microsoft, Baidu etc. For Google Ads entity, use \&quot;campaign.id\&quot; instead. | [optional] [readonly] 
**excludedParentAssetFieldTypes** | **[String]** | The asset field types that should be excluded from this campaign. Asset links with these field types will not be inherited by this campaign from the upper level. | [optional] 
**finalUrlSuffix** | **String** | Suffix used to append query parameters to landing pages that are served with parallel tracking. | [optional] 
**frequencyCaps** | **[Object]** | A list that limits how often each user will see this campaign&#39;s ads. | [optional] 
**geoTargetTypeSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignGeoTargetTypeSetting**](GoogleAdsSearchads360V0ResourcesCampaignGeoTargetTypeSetting.md) |  | [optional] 
**id** | **String** | Output only. The ID of the campaign. | [optional] [readonly] 
**labels** | **[String]** | Output only. The resource names of labels attached to this campaign. | [optional] [readonly] 
**lastModifiedTime** | **String** | Output only. The datetime when this campaign was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. | [optional] [readonly] 
**manualCpa** | **Object** | Manual bidding strategy that allows advertiser to set the bid per advertiser-specified action. | [optional] 
**manualCpc** | [**GoogleAdsSearchads360V0CommonManualCpc**](GoogleAdsSearchads360V0CommonManualCpc.md) |  | [optional] 
**manualCpm** | **Object** | Manual impression-based bidding where user pays per thousand impressions. | [optional] 
**maximizeConversionValue** | [**GoogleAdsSearchads360V0CommonMaximizeConversionValue**](GoogleAdsSearchads360V0CommonMaximizeConversionValue.md) |  | [optional] 
**maximizeConversions** | [**GoogleAdsSearchads360V0CommonMaximizeConversions**](GoogleAdsSearchads360V0CommonMaximizeConversions.md) |  | [optional] 
**name** | **String** | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. | [optional] 
**networkSettings** | [**GoogleAdsSearchads360V0ResourcesCampaignNetworkSettings**](GoogleAdsSearchads360V0ResourcesCampaignNetworkSettings.md) |  | [optional] 
**optimizationGoalSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignOptimizationGoalSetting**](GoogleAdsSearchads360V0ResourcesCampaignOptimizationGoalSetting.md) |  | [optional] 
**percentCpc** | [**GoogleAdsSearchads360V0CommonPercentCpc**](GoogleAdsSearchads360V0CommonPercentCpc.md) |  | [optional] 
**realTimeBiddingSetting** | [**GoogleAdsSearchads360V0CommonRealTimeBiddingSetting**](GoogleAdsSearchads360V0CommonRealTimeBiddingSetting.md) |  | [optional] 
**resourceName** | **String** | Immutable. The resource name of the campaign. Campaign resource names have the form: &#x60;customers/{customer_id}/campaigns/{campaign_id}&#x60; | [optional] 
**selectiveOptimization** | [**GoogleAdsSearchads360V0ResourcesCampaignSelectiveOptimization**](GoogleAdsSearchads360V0ResourcesCampaignSelectiveOptimization.md) |  | [optional] 
**servingStatus** | **String** | Output only. The ad serving status of the campaign. | [optional] [readonly] 
**shoppingSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignShoppingSetting**](GoogleAdsSearchads360V0ResourcesCampaignShoppingSetting.md) |  | [optional] 
**startDate** | **String** | The date when campaign started in serving customer&#39;s timezone in YYYY-MM-DD format. | [optional] 
**status** | **String** | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. | [optional] 
**targetCpa** | [**GoogleAdsSearchads360V0CommonTargetCpa**](GoogleAdsSearchads360V0CommonTargetCpa.md) |  | [optional] 
**targetCpm** | **Object** | Target CPM (cost per thousand impressions) is an automated bidding strategy that sets bids to optimize performance given the target CPM you set. | [optional] 
**targetImpressionShare** | [**GoogleAdsSearchads360V0CommonTargetImpressionShare**](GoogleAdsSearchads360V0CommonTargetImpressionShare.md) |  | [optional] 
**targetRoas** | [**GoogleAdsSearchads360V0CommonTargetRoas**](GoogleAdsSearchads360V0CommonTargetRoas.md) |  | [optional] 
**targetSpend** | [**GoogleAdsSearchads360V0CommonTargetSpend**](GoogleAdsSearchads360V0CommonTargetSpend.md) |  | [optional] 
**trackingSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignTrackingSetting**](GoogleAdsSearchads360V0ResourcesCampaignTrackingSetting.md) |  | [optional] 
**trackingUrlTemplate** | **String** | The URL template for constructing a tracking URL. | [optional] 
**urlCustomParameters** | [**[GoogleAdsSearchads360V0CommonCustomParameter]**](GoogleAdsSearchads360V0CommonCustomParameter.md) | The list of mappings used to substitute custom parameter tags in a &#x60;tracking_url_template&#x60;, &#x60;final_urls&#x60;, or &#x60;mobile_final_urls&#x60;. | [optional] 
**urlExpansionOptOut** | **Boolean** | Represents opting out of URL expansion to more targeted URLs. If opted out (true), only the final URLs in the asset group or URLs specified in the advertiser&#39;s Google Merchant Center or business data feeds are targeted. If opted in (false), the entire domain will be targeted. This field can only be set for Performance Max campaigns, where the default value is false. | [optional] 



## Enum: AdServingOptimizationStatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `OPTIMIZE` (value: `"OPTIMIZE"`)

* `CONVERSION_OPTIMIZE` (value: `"CONVERSION_OPTIMIZE"`)

* `ROTATE` (value: `"ROTATE"`)

* `ROTATE_INDEFINITELY` (value: `"ROTATE_INDEFINITELY"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)





## Enum: AdvertisingChannelSubTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `SEARCH_MOBILE_APP` (value: `"SEARCH_MOBILE_APP"`)

* `DISPLAY_MOBILE_APP` (value: `"DISPLAY_MOBILE_APP"`)

* `SEARCH_EXPRESS` (value: `"SEARCH_EXPRESS"`)

* `DISPLAY_EXPRESS` (value: `"DISPLAY_EXPRESS"`)

* `SHOPPING_SMART_ADS` (value: `"SHOPPING_SMART_ADS"`)

* `DISPLAY_GMAIL_AD` (value: `"DISPLAY_GMAIL_AD"`)

* `DISPLAY_SMART_CAMPAIGN` (value: `"DISPLAY_SMART_CAMPAIGN"`)

* `VIDEO_OUTSTREAM` (value: `"VIDEO_OUTSTREAM"`)

* `VIDEO_ACTION` (value: `"VIDEO_ACTION"`)

* `VIDEO_NON_SKIPPABLE` (value: `"VIDEO_NON_SKIPPABLE"`)

* `APP_CAMPAIGN` (value: `"APP_CAMPAIGN"`)

* `APP_CAMPAIGN_FOR_ENGAGEMENT` (value: `"APP_CAMPAIGN_FOR_ENGAGEMENT"`)

* `LOCAL_CAMPAIGN` (value: `"LOCAL_CAMPAIGN"`)

* `SHOPPING_COMPARISON_LISTING_ADS` (value: `"SHOPPING_COMPARISON_LISTING_ADS"`)

* `SMART_CAMPAIGN` (value: `"SMART_CAMPAIGN"`)

* `VIDEO_SEQUENCE` (value: `"VIDEO_SEQUENCE"`)

* `APP_CAMPAIGN_FOR_PRE_REGISTRATION` (value: `"APP_CAMPAIGN_FOR_PRE_REGISTRATION"`)

* `VIDEO_REACH_TARGET_FREQUENCY` (value: `"VIDEO_REACH_TARGET_FREQUENCY"`)

* `TRAVEL_ACTIVITIES` (value: `"TRAVEL_ACTIVITIES"`)





## Enum: AdvertisingChannelTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `SEARCH` (value: `"SEARCH"`)

* `DISPLAY` (value: `"DISPLAY"`)

* `SHOPPING` (value: `"SHOPPING"`)

* `HOTEL` (value: `"HOTEL"`)

* `VIDEO` (value: `"VIDEO"`)

* `MULTI_CHANNEL` (value: `"MULTI_CHANNEL"`)

* `LOCAL` (value: `"LOCAL"`)

* `SMART` (value: `"SMART"`)

* `PERFORMANCE_MAX` (value: `"PERFORMANCE_MAX"`)

* `LOCAL_SERVICES` (value: `"LOCAL_SERVICES"`)

* `DISCOVERY` (value: `"DISCOVERY"`)

* `TRAVEL` (value: `"TRAVEL"`)





## Enum: BiddingStrategySystemStatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `LEARNING_NEW` (value: `"LEARNING_NEW"`)

* `LEARNING_SETTING_CHANGE` (value: `"LEARNING_SETTING_CHANGE"`)

* `LEARNING_BUDGET_CHANGE` (value: `"LEARNING_BUDGET_CHANGE"`)

* `LEARNING_COMPOSITION_CHANGE` (value: `"LEARNING_COMPOSITION_CHANGE"`)

* `LEARNING_CONVERSION_TYPE_CHANGE` (value: `"LEARNING_CONVERSION_TYPE_CHANGE"`)

* `LEARNING_CONVERSION_SETTING_CHANGE` (value: `"LEARNING_CONVERSION_SETTING_CHANGE"`)

* `LIMITED_BY_CPC_BID_CEILING` (value: `"LIMITED_BY_CPC_BID_CEILING"`)

* `LIMITED_BY_CPC_BID_FLOOR` (value: `"LIMITED_BY_CPC_BID_FLOOR"`)

* `LIMITED_BY_DATA` (value: `"LIMITED_BY_DATA"`)

* `LIMITED_BY_BUDGET` (value: `"LIMITED_BY_BUDGET"`)

* `LIMITED_BY_LOW_PRIORITY_SPEND` (value: `"LIMITED_BY_LOW_PRIORITY_SPEND"`)

* `LIMITED_BY_LOW_QUALITY` (value: `"LIMITED_BY_LOW_QUALITY"`)

* `LIMITED_BY_INVENTORY` (value: `"LIMITED_BY_INVENTORY"`)

* `MISCONFIGURED_ZERO_ELIGIBILITY` (value: `"MISCONFIGURED_ZERO_ELIGIBILITY"`)

* `MISCONFIGURED_CONVERSION_TYPES` (value: `"MISCONFIGURED_CONVERSION_TYPES"`)

* `MISCONFIGURED_CONVERSION_SETTINGS` (value: `"MISCONFIGURED_CONVERSION_SETTINGS"`)

* `MISCONFIGURED_SHARED_BUDGET` (value: `"MISCONFIGURED_SHARED_BUDGET"`)

* `MISCONFIGURED_STRATEGY_TYPE` (value: `"MISCONFIGURED_STRATEGY_TYPE"`)

* `PAUSED` (value: `"PAUSED"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)

* `MULTIPLE_LEARNING` (value: `"MULTIPLE_LEARNING"`)

* `MULTIPLE_LIMITED` (value: `"MULTIPLE_LIMITED"`)

* `MULTIPLE_MISCONFIGURED` (value: `"MULTIPLE_MISCONFIGURED"`)

* `MULTIPLE` (value: `"MULTIPLE"`)





## Enum: BiddingStrategyTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `COMMISSION` (value: `"COMMISSION"`)

* `ENHANCED_CPC` (value: `"ENHANCED_CPC"`)

* `INVALID` (value: `"INVALID"`)

* `MANUAL_CPA` (value: `"MANUAL_CPA"`)

* `MANUAL_CPC` (value: `"MANUAL_CPC"`)

* `MANUAL_CPM` (value: `"MANUAL_CPM"`)

* `MANUAL_CPV` (value: `"MANUAL_CPV"`)

* `MAXIMIZE_CONVERSIONS` (value: `"MAXIMIZE_CONVERSIONS"`)

* `MAXIMIZE_CONVERSION_VALUE` (value: `"MAXIMIZE_CONVERSION_VALUE"`)

* `PAGE_ONE_PROMOTED` (value: `"PAGE_ONE_PROMOTED"`)

* `PERCENT_CPC` (value: `"PERCENT_CPC"`)

* `TARGET_CPA` (value: `"TARGET_CPA"`)

* `TARGET_CPM` (value: `"TARGET_CPM"`)

* `TARGET_IMPRESSION_SHARE` (value: `"TARGET_IMPRESSION_SHARE"`)

* `TARGET_OUTRANK_SHARE` (value: `"TARGET_OUTRANK_SHARE"`)

* `TARGET_ROAS` (value: `"TARGET_ROAS"`)

* `TARGET_SPEND` (value: `"TARGET_SPEND"`)





## Enum: [ExcludedParentAssetFieldTypesEnum]


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `HEADLINE` (value: `"HEADLINE"`)

* `DESCRIPTION` (value: `"DESCRIPTION"`)

* `MANDATORY_AD_TEXT` (value: `"MANDATORY_AD_TEXT"`)

* `MARKETING_IMAGE` (value: `"MARKETING_IMAGE"`)

* `MEDIA_BUNDLE` (value: `"MEDIA_BUNDLE"`)

* `YOUTUBE_VIDEO` (value: `"YOUTUBE_VIDEO"`)

* `BOOK_ON_GOOGLE` (value: `"BOOK_ON_GOOGLE"`)

* `LEAD_FORM` (value: `"LEAD_FORM"`)

* `PROMOTION` (value: `"PROMOTION"`)

* `CALLOUT` (value: `"CALLOUT"`)

* `STRUCTURED_SNIPPET` (value: `"STRUCTURED_SNIPPET"`)

* `SITELINK` (value: `"SITELINK"`)

* `MOBILE_APP` (value: `"MOBILE_APP"`)

* `HOTEL_CALLOUT` (value: `"HOTEL_CALLOUT"`)

* `CALL` (value: `"CALL"`)

* `PRICE` (value: `"PRICE"`)

* `LONG_HEADLINE` (value: `"LONG_HEADLINE"`)

* `BUSINESS_NAME` (value: `"BUSINESS_NAME"`)

* `SQUARE_MARKETING_IMAGE` (value: `"SQUARE_MARKETING_IMAGE"`)

* `PORTRAIT_MARKETING_IMAGE` (value: `"PORTRAIT_MARKETING_IMAGE"`)

* `LOGO` (value: `"LOGO"`)

* `LANDSCAPE_LOGO` (value: `"LANDSCAPE_LOGO"`)

* `VIDEO` (value: `"VIDEO"`)

* `CALL_TO_ACTION_SELECTION` (value: `"CALL_TO_ACTION_SELECTION"`)

* `AD_IMAGE` (value: `"AD_IMAGE"`)

* `BUSINESS_LOGO` (value: `"BUSINESS_LOGO"`)

* `HOTEL_PROPERTY` (value: `"HOTEL_PROPERTY"`)





## Enum: ServingStatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `SERVING` (value: `"SERVING"`)

* `NONE` (value: `"NONE"`)

* `ENDED` (value: `"ENDED"`)

* `PENDING` (value: `"PENDING"`)

* `SUSPENDED` (value: `"SUSPENDED"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `PAUSED` (value: `"PAUSED"`)

* `REMOVED` (value: `"REMOVED"`)




