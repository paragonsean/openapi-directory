

# GoogleAdsSearchads360V0ResourcesCampaign

A campaign.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adServingOptimizationStatus** | [**AdServingOptimizationStatusEnum**](#AdServingOptimizationStatusEnum) | The ad serving optimization status of the campaign. |  [optional] |
|**advertisingChannelSubType** | [**AdvertisingChannelSubTypeEnum**](#AdvertisingChannelSubTypeEnum) | Immutable. Optional refinement to &#x60;advertising_channel_type&#x60;. Must be a valid sub-type of the parent channel type. Can be set only when creating campaigns. After campaign is created, the field can not be changed. |  [optional] |
|**advertisingChannelType** | [**AdvertisingChannelTypeEnum**](#AdvertisingChannelTypeEnum) | Immutable. The primary serving target for ads within the campaign. The targeting options can be refined in &#x60;network_settings&#x60;. This field is required and should not be empty when creating new campaigns. Can be set only when creating campaigns. After the campaign is created, the field can not be changed. |  [optional] |
|**biddingStrategy** | **String** | Portfolio bidding strategy used by campaign. |  [optional] |
|**biddingStrategySystemStatus** | [**BiddingStrategySystemStatusEnum**](#BiddingStrategySystemStatusEnum) | Output only. The system status of the campaign&#39;s bidding strategy. |  [optional] [readonly] |
|**biddingStrategyType** | [**BiddingStrategyTypeEnum**](#BiddingStrategyTypeEnum) | Output only. The type of bidding strategy. A bidding strategy can be created by setting either the bidding scheme to create a standard bidding strategy or the &#x60;bidding_strategy&#x60; field to create a portfolio bidding strategy. This field is read-only. |  [optional] [readonly] |
|**campaignBudget** | **String** | The budget of the campaign. |  [optional] |
|**createTime** | **String** | Output only. The timestamp when this campaign was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. create_time will be deprecated in v1. Use creation_time instead. |  [optional] [readonly] |
|**creationTime** | **String** | Output only. The timestamp when this campaign was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. |  [optional] [readonly] |
|**dynamicSearchAdsSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignDynamicSearchAdsSetting**](GoogleAdsSearchads360V0ResourcesCampaignDynamicSearchAdsSetting.md) |  |  [optional] |
|**endDate** | **String** | The last day of the campaign in serving customer&#39;s timezone in YYYY-MM-DD format. On create, defaults to 2037-12-30, which means the campaign will run indefinitely. To set an existing campaign to run indefinitely, set this field to 2037-12-30. |  [optional] |
|**engineId** | **String** | Output only. ID of the campaign in the external engine account. This field is for non-Google Ads account only, for example, Yahoo Japan, Microsoft, Baidu etc. For Google Ads entity, use \&quot;campaign.id\&quot; instead. |  [optional] [readonly] |
|**excludedParentAssetFieldTypes** | [**List&lt;ExcludedParentAssetFieldTypesEnum&gt;**](#List&lt;ExcludedParentAssetFieldTypesEnum&gt;) | The asset field types that should be excluded from this campaign. Asset links with these field types will not be inherited by this campaign from the upper level. |  [optional] |
|**finalUrlSuffix** | **String** | Suffix used to append query parameters to landing pages that are served with parallel tracking. |  [optional] |
|**frequencyCaps** | **List&lt;Object&gt;** | A list that limits how often each user will see this campaign&#39;s ads. |  [optional] |
|**geoTargetTypeSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignGeoTargetTypeSetting**](GoogleAdsSearchads360V0ResourcesCampaignGeoTargetTypeSetting.md) |  |  [optional] |
|**id** | **String** | Output only. The ID of the campaign. |  [optional] [readonly] |
|**labels** | **List&lt;String&gt;** | Output only. The resource names of labels attached to this campaign. |  [optional] [readonly] |
|**lastModifiedTime** | **String** | Output only. The datetime when this campaign was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. |  [optional] [readonly] |
|**manualCpa** | **Object** | Manual bidding strategy that allows advertiser to set the bid per advertiser-specified action. |  [optional] |
|**manualCpc** | [**GoogleAdsSearchads360V0CommonManualCpc**](GoogleAdsSearchads360V0CommonManualCpc.md) |  |  [optional] |
|**manualCpm** | **Object** | Manual impression-based bidding where user pays per thousand impressions. |  [optional] |
|**maximizeConversionValue** | [**GoogleAdsSearchads360V0CommonMaximizeConversionValue**](GoogleAdsSearchads360V0CommonMaximizeConversionValue.md) |  |  [optional] |
|**maximizeConversions** | [**GoogleAdsSearchads360V0CommonMaximizeConversions**](GoogleAdsSearchads360V0CommonMaximizeConversions.md) |  |  [optional] |
|**name** | **String** | The name of the campaign. This field is required and should not be empty when creating new campaigns. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |  [optional] |
|**networkSettings** | [**GoogleAdsSearchads360V0ResourcesCampaignNetworkSettings**](GoogleAdsSearchads360V0ResourcesCampaignNetworkSettings.md) |  |  [optional] |
|**optimizationGoalSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignOptimizationGoalSetting**](GoogleAdsSearchads360V0ResourcesCampaignOptimizationGoalSetting.md) |  |  [optional] |
|**percentCpc** | [**GoogleAdsSearchads360V0CommonPercentCpc**](GoogleAdsSearchads360V0CommonPercentCpc.md) |  |  [optional] |
|**realTimeBiddingSetting** | [**GoogleAdsSearchads360V0CommonRealTimeBiddingSetting**](GoogleAdsSearchads360V0CommonRealTimeBiddingSetting.md) |  |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the campaign. Campaign resource names have the form: &#x60;customers/{customer_id}/campaigns/{campaign_id}&#x60; |  [optional] |
|**selectiveOptimization** | [**GoogleAdsSearchads360V0ResourcesCampaignSelectiveOptimization**](GoogleAdsSearchads360V0ResourcesCampaignSelectiveOptimization.md) |  |  [optional] |
|**servingStatus** | [**ServingStatusEnum**](#ServingStatusEnum) | Output only. The ad serving status of the campaign. |  [optional] [readonly] |
|**shoppingSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignShoppingSetting**](GoogleAdsSearchads360V0ResourcesCampaignShoppingSetting.md) |  |  [optional] |
|**startDate** | **String** | The date when campaign started in serving customer&#39;s timezone in YYYY-MM-DD format. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the campaign. When a new campaign is added, the status defaults to ENABLED. |  [optional] |
|**targetCpa** | [**GoogleAdsSearchads360V0CommonTargetCpa**](GoogleAdsSearchads360V0CommonTargetCpa.md) |  |  [optional] |
|**targetCpm** | **Object** | Target CPM (cost per thousand impressions) is an automated bidding strategy that sets bids to optimize performance given the target CPM you set. |  [optional] |
|**targetImpressionShare** | [**GoogleAdsSearchads360V0CommonTargetImpressionShare**](GoogleAdsSearchads360V0CommonTargetImpressionShare.md) |  |  [optional] |
|**targetRoas** | [**GoogleAdsSearchads360V0CommonTargetRoas**](GoogleAdsSearchads360V0CommonTargetRoas.md) |  |  [optional] |
|**targetSpend** | [**GoogleAdsSearchads360V0CommonTargetSpend**](GoogleAdsSearchads360V0CommonTargetSpend.md) |  |  [optional] |
|**trackingSetting** | [**GoogleAdsSearchads360V0ResourcesCampaignTrackingSetting**](GoogleAdsSearchads360V0ResourcesCampaignTrackingSetting.md) |  |  [optional] |
|**trackingUrlTemplate** | **String** | The URL template for constructing a tracking URL. |  [optional] |
|**urlCustomParameters** | [**List&lt;GoogleAdsSearchads360V0CommonCustomParameter&gt;**](GoogleAdsSearchads360V0CommonCustomParameter.md) | The list of mappings used to substitute custom parameter tags in a &#x60;tracking_url_template&#x60;, &#x60;final_urls&#x60;, or &#x60;mobile_final_urls&#x60;. |  [optional] |
|**urlExpansionOptOut** | **Boolean** | Represents opting out of URL expansion to more targeted URLs. If opted out (true), only the final URLs in the asset group or URLs specified in the advertiser&#39;s Google Merchant Center or business data feeds are targeted. If opted in (false), the entire domain will be targeted. This field can only be set for Performance Max campaigns, where the default value is false. |  [optional] |



## Enum: AdServingOptimizationStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| OPTIMIZE | &quot;OPTIMIZE&quot; |
| CONVERSION_OPTIMIZE | &quot;CONVERSION_OPTIMIZE&quot; |
| ROTATE | &quot;ROTATE&quot; |
| ROTATE_INDEFINITELY | &quot;ROTATE_INDEFINITELY&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |



## Enum: AdvertisingChannelSubTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| SEARCH_MOBILE_APP | &quot;SEARCH_MOBILE_APP&quot; |
| DISPLAY_MOBILE_APP | &quot;DISPLAY_MOBILE_APP&quot; |
| SEARCH_EXPRESS | &quot;SEARCH_EXPRESS&quot; |
| DISPLAY_EXPRESS | &quot;DISPLAY_EXPRESS&quot; |
| SHOPPING_SMART_ADS | &quot;SHOPPING_SMART_ADS&quot; |
| DISPLAY_GMAIL_AD | &quot;DISPLAY_GMAIL_AD&quot; |
| DISPLAY_SMART_CAMPAIGN | &quot;DISPLAY_SMART_CAMPAIGN&quot; |
| VIDEO_OUTSTREAM | &quot;VIDEO_OUTSTREAM&quot; |
| VIDEO_ACTION | &quot;VIDEO_ACTION&quot; |
| VIDEO_NON_SKIPPABLE | &quot;VIDEO_NON_SKIPPABLE&quot; |
| APP_CAMPAIGN | &quot;APP_CAMPAIGN&quot; |
| APP_CAMPAIGN_FOR_ENGAGEMENT | &quot;APP_CAMPAIGN_FOR_ENGAGEMENT&quot; |
| LOCAL_CAMPAIGN | &quot;LOCAL_CAMPAIGN&quot; |
| SHOPPING_COMPARISON_LISTING_ADS | &quot;SHOPPING_COMPARISON_LISTING_ADS&quot; |
| SMART_CAMPAIGN | &quot;SMART_CAMPAIGN&quot; |
| VIDEO_SEQUENCE | &quot;VIDEO_SEQUENCE&quot; |
| APP_CAMPAIGN_FOR_PRE_REGISTRATION | &quot;APP_CAMPAIGN_FOR_PRE_REGISTRATION&quot; |
| VIDEO_REACH_TARGET_FREQUENCY | &quot;VIDEO_REACH_TARGET_FREQUENCY&quot; |
| TRAVEL_ACTIVITIES | &quot;TRAVEL_ACTIVITIES&quot; |



## Enum: AdvertisingChannelTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| SEARCH | &quot;SEARCH&quot; |
| DISPLAY | &quot;DISPLAY&quot; |
| SHOPPING | &quot;SHOPPING&quot; |
| HOTEL | &quot;HOTEL&quot; |
| VIDEO | &quot;VIDEO&quot; |
| MULTI_CHANNEL | &quot;MULTI_CHANNEL&quot; |
| LOCAL | &quot;LOCAL&quot; |
| SMART | &quot;SMART&quot; |
| PERFORMANCE_MAX | &quot;PERFORMANCE_MAX&quot; |
| LOCAL_SERVICES | &quot;LOCAL_SERVICES&quot; |
| DISCOVERY | &quot;DISCOVERY&quot; |
| TRAVEL | &quot;TRAVEL&quot; |



## Enum: BiddingStrategySystemStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| LEARNING_NEW | &quot;LEARNING_NEW&quot; |
| LEARNING_SETTING_CHANGE | &quot;LEARNING_SETTING_CHANGE&quot; |
| LEARNING_BUDGET_CHANGE | &quot;LEARNING_BUDGET_CHANGE&quot; |
| LEARNING_COMPOSITION_CHANGE | &quot;LEARNING_COMPOSITION_CHANGE&quot; |
| LEARNING_CONVERSION_TYPE_CHANGE | &quot;LEARNING_CONVERSION_TYPE_CHANGE&quot; |
| LEARNING_CONVERSION_SETTING_CHANGE | &quot;LEARNING_CONVERSION_SETTING_CHANGE&quot; |
| LIMITED_BY_CPC_BID_CEILING | &quot;LIMITED_BY_CPC_BID_CEILING&quot; |
| LIMITED_BY_CPC_BID_FLOOR | &quot;LIMITED_BY_CPC_BID_FLOOR&quot; |
| LIMITED_BY_DATA | &quot;LIMITED_BY_DATA&quot; |
| LIMITED_BY_BUDGET | &quot;LIMITED_BY_BUDGET&quot; |
| LIMITED_BY_LOW_PRIORITY_SPEND | &quot;LIMITED_BY_LOW_PRIORITY_SPEND&quot; |
| LIMITED_BY_LOW_QUALITY | &quot;LIMITED_BY_LOW_QUALITY&quot; |
| LIMITED_BY_INVENTORY | &quot;LIMITED_BY_INVENTORY&quot; |
| MISCONFIGURED_ZERO_ELIGIBILITY | &quot;MISCONFIGURED_ZERO_ELIGIBILITY&quot; |
| MISCONFIGURED_CONVERSION_TYPES | &quot;MISCONFIGURED_CONVERSION_TYPES&quot; |
| MISCONFIGURED_CONVERSION_SETTINGS | &quot;MISCONFIGURED_CONVERSION_SETTINGS&quot; |
| MISCONFIGURED_SHARED_BUDGET | &quot;MISCONFIGURED_SHARED_BUDGET&quot; |
| MISCONFIGURED_STRATEGY_TYPE | &quot;MISCONFIGURED_STRATEGY_TYPE&quot; |
| PAUSED | &quot;PAUSED&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |
| MULTIPLE_LEARNING | &quot;MULTIPLE_LEARNING&quot; |
| MULTIPLE_LIMITED | &quot;MULTIPLE_LIMITED&quot; |
| MULTIPLE_MISCONFIGURED | &quot;MULTIPLE_MISCONFIGURED&quot; |
| MULTIPLE | &quot;MULTIPLE&quot; |



## Enum: BiddingStrategyTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| COMMISSION | &quot;COMMISSION&quot; |
| ENHANCED_CPC | &quot;ENHANCED_CPC&quot; |
| INVALID | &quot;INVALID&quot; |
| MANUAL_CPA | &quot;MANUAL_CPA&quot; |
| MANUAL_CPC | &quot;MANUAL_CPC&quot; |
| MANUAL_CPM | &quot;MANUAL_CPM&quot; |
| MANUAL_CPV | &quot;MANUAL_CPV&quot; |
| MAXIMIZE_CONVERSIONS | &quot;MAXIMIZE_CONVERSIONS&quot; |
| MAXIMIZE_CONVERSION_VALUE | &quot;MAXIMIZE_CONVERSION_VALUE&quot; |
| PAGE_ONE_PROMOTED | &quot;PAGE_ONE_PROMOTED&quot; |
| PERCENT_CPC | &quot;PERCENT_CPC&quot; |
| TARGET_CPA | &quot;TARGET_CPA&quot; |
| TARGET_CPM | &quot;TARGET_CPM&quot; |
| TARGET_IMPRESSION_SHARE | &quot;TARGET_IMPRESSION_SHARE&quot; |
| TARGET_OUTRANK_SHARE | &quot;TARGET_OUTRANK_SHARE&quot; |
| TARGET_ROAS | &quot;TARGET_ROAS&quot; |
| TARGET_SPEND | &quot;TARGET_SPEND&quot; |



## Enum: List&lt;ExcludedParentAssetFieldTypesEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| HEADLINE | &quot;HEADLINE&quot; |
| DESCRIPTION | &quot;DESCRIPTION&quot; |
| MANDATORY_AD_TEXT | &quot;MANDATORY_AD_TEXT&quot; |
| MARKETING_IMAGE | &quot;MARKETING_IMAGE&quot; |
| MEDIA_BUNDLE | &quot;MEDIA_BUNDLE&quot; |
| YOUTUBE_VIDEO | &quot;YOUTUBE_VIDEO&quot; |
| BOOK_ON_GOOGLE | &quot;BOOK_ON_GOOGLE&quot; |
| LEAD_FORM | &quot;LEAD_FORM&quot; |
| PROMOTION | &quot;PROMOTION&quot; |
| CALLOUT | &quot;CALLOUT&quot; |
| STRUCTURED_SNIPPET | &quot;STRUCTURED_SNIPPET&quot; |
| SITELINK | &quot;SITELINK&quot; |
| MOBILE_APP | &quot;MOBILE_APP&quot; |
| HOTEL_CALLOUT | &quot;HOTEL_CALLOUT&quot; |
| CALL | &quot;CALL&quot; |
| PRICE | &quot;PRICE&quot; |
| LONG_HEADLINE | &quot;LONG_HEADLINE&quot; |
| BUSINESS_NAME | &quot;BUSINESS_NAME&quot; |
| SQUARE_MARKETING_IMAGE | &quot;SQUARE_MARKETING_IMAGE&quot; |
| PORTRAIT_MARKETING_IMAGE | &quot;PORTRAIT_MARKETING_IMAGE&quot; |
| LOGO | &quot;LOGO&quot; |
| LANDSCAPE_LOGO | &quot;LANDSCAPE_LOGO&quot; |
| VIDEO | &quot;VIDEO&quot; |
| CALL_TO_ACTION_SELECTION | &quot;CALL_TO_ACTION_SELECTION&quot; |
| AD_IMAGE | &quot;AD_IMAGE&quot; |
| BUSINESS_LOGO | &quot;BUSINESS_LOGO&quot; |
| HOTEL_PROPERTY | &quot;HOTEL_PROPERTY&quot; |



## Enum: ServingStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| SERVING | &quot;SERVING&quot; |
| NONE | &quot;NONE&quot; |
| ENDED | &quot;ENDED&quot; |
| PENDING | &quot;PENDING&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| PAUSED | &quot;PAUSED&quot; |
| REMOVED | &quot;REMOVED&quot; |



