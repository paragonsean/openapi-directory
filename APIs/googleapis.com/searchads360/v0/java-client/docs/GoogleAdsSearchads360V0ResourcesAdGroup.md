

# GoogleAdsSearchads360V0ResourcesAdGroup

An ad group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adRotationMode** | [**AdRotationModeEnum**](#AdRotationModeEnum) | The ad rotation mode of the ad group. |  [optional] |
|**cpcBidMicros** | **String** | The maximum CPC (cost-per-click) bid. |  [optional] |
|**creationTime** | **String** | Output only. The timestamp when this ad_group was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. |  [optional] [readonly] |
|**endDate** | **String** | Output only. Date when the ad group ends serving ads. By default, the ad group ends on the ad group&#39;s end date. If this field is set, then the ad group ends at the end of the specified date in the customer&#39;s time zone. This field is only available for Microsoft Advertising and Facebook gateway accounts. Format: YYYY-MM-DD Example: 2019-03-14 |  [optional] [readonly] |
|**engineId** | **String** | Output only. ID of the ad group in the external engine account. This field is for non-Google Ads account only, for example, Yahoo Japan, Microsoft, Baidu etc. For Google Ads entity, use \&quot;ad_group.id\&quot; instead. |  [optional] [readonly] |
|**engineStatus** | [**EngineStatusEnum**](#EngineStatusEnum) | Output only. The Engine Status for ad group. |  [optional] [readonly] |
|**id** | **String** | Output only. The ID of the ad group. |  [optional] [readonly] |
|**labels** | **List&lt;String&gt;** | Output only. The resource names of labels attached to this ad group. |  [optional] [readonly] |
|**languageCode** | **String** | Output only. The language of the ads and keywords in an ad group. This field is only available for Microsoft Advertising accounts. More details: https://docs.microsoft.com/en-us/advertising/guides/ad-languages?view&#x3D;bingads-13#adlanguage |  [optional] [readonly] |
|**lastModifiedTime** | **String** | Output only. The datetime when this ad group was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. |  [optional] [readonly] |
|**name** | **String** | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the ad group. Ad group resource names have the form: &#x60;customers/{customer_id}/adGroups/{ad_group_id}&#x60; |  [optional] |
|**startDate** | **String** | Output only. Date when this ad group starts serving ads. By default, the ad group starts now or the ad group&#39;s start date, whichever is later. If this field is set, then the ad group starts at the beginning of the specified date in the customer&#39;s time zone. This field is only available for Microsoft Advertising and Facebook gateway accounts. Format: YYYY-MM-DD Example: 2019-03-14 |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the ad group. |  [optional] |
|**targetingSetting** | [**GoogleAdsSearchads360V0CommonTargetingSetting**](GoogleAdsSearchads360V0CommonTargetingSetting.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Immutable. The type of the ad group. |  [optional] |



## Enum: AdRotationModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| OPTIMIZE | &quot;OPTIMIZE&quot; |
| ROTATE_FOREVER | &quot;ROTATE_FOREVER&quot; |



## Enum: EngineStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| AD_GROUP_ELIGIBLE | &quot;AD_GROUP_ELIGIBLE&quot; |
| AD_GROUP_EXPIRED | &quot;AD_GROUP_EXPIRED&quot; |
| AD_GROUP_REMOVED | &quot;AD_GROUP_REMOVED&quot; |
| AD_GROUP_DRAFT | &quot;AD_GROUP_DRAFT&quot; |
| AD_GROUP_PAUSED | &quot;AD_GROUP_PAUSED&quot; |
| AD_GROUP_SERVING | &quot;AD_GROUP_SERVING&quot; |
| AD_GROUP_SUBMITTED | &quot;AD_GROUP_SUBMITTED&quot; |
| CAMPAIGN_PAUSED | &quot;CAMPAIGN_PAUSED&quot; |
| ACCOUNT_PAUSED | &quot;ACCOUNT_PAUSED&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| PAUSED | &quot;PAUSED&quot; |
| REMOVED | &quot;REMOVED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| SEARCH_STANDARD | &quot;SEARCH_STANDARD&quot; |
| DISPLAY_STANDARD | &quot;DISPLAY_STANDARD&quot; |
| SHOPPING_PRODUCT_ADS | &quot;SHOPPING_PRODUCT_ADS&quot; |
| SHOPPING_SHOWCASE_ADS | &quot;SHOPPING_SHOWCASE_ADS&quot; |
| HOTEL_ADS | &quot;HOTEL_ADS&quot; |
| SHOPPING_SMART_ADS | &quot;SHOPPING_SMART_ADS&quot; |
| VIDEO_BUMPER | &quot;VIDEO_BUMPER&quot; |
| VIDEO_TRUE_VIEW_IN_STREAM | &quot;VIDEO_TRUE_VIEW_IN_STREAM&quot; |
| VIDEO_TRUE_VIEW_IN_DISPLAY | &quot;VIDEO_TRUE_VIEW_IN_DISPLAY&quot; |
| VIDEO_NON_SKIPPABLE_IN_STREAM | &quot;VIDEO_NON_SKIPPABLE_IN_STREAM&quot; |
| VIDEO_OUTSTREAM | &quot;VIDEO_OUTSTREAM&quot; |
| SEARCH_DYNAMIC_ADS | &quot;SEARCH_DYNAMIC_ADS&quot; |
| SHOPPING_COMPARISON_LISTING_ADS | &quot;SHOPPING_COMPARISON_LISTING_ADS&quot; |
| PROMOTED_HOTEL_ADS | &quot;PROMOTED_HOTEL_ADS&quot; |
| VIDEO_RESPONSIVE | &quot;VIDEO_RESPONSIVE&quot; |
| VIDEO_EFFICIENT_REACH | &quot;VIDEO_EFFICIENT_REACH&quot; |
| SMART_CAMPAIGN_ADS | &quot;SMART_CAMPAIGN_ADS&quot; |
| TRAVEL_ADS | &quot;TRAVEL_ADS&quot; |



