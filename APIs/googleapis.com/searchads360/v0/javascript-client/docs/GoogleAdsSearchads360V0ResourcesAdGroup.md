# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesAdGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adRotationMode** | **String** | The ad rotation mode of the ad group. | [optional] 
**cpcBidMicros** | **String** | The maximum CPC (cost-per-click) bid. | [optional] 
**creationTime** | **String** | Output only. The timestamp when this ad_group was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. | [optional] [readonly] 
**endDate** | **String** | Output only. Date when the ad group ends serving ads. By default, the ad group ends on the ad group&#39;s end date. If this field is set, then the ad group ends at the end of the specified date in the customer&#39;s time zone. This field is only available for Microsoft Advertising and Facebook gateway accounts. Format: YYYY-MM-DD Example: 2019-03-14 | [optional] [readonly] 
**engineId** | **String** | Output only. ID of the ad group in the external engine account. This field is for non-Google Ads account only, for example, Yahoo Japan, Microsoft, Baidu etc. For Google Ads entity, use \&quot;ad_group.id\&quot; instead. | [optional] [readonly] 
**engineStatus** | **String** | Output only. The Engine Status for ad group. | [optional] [readonly] 
**id** | **String** | Output only. The ID of the ad group. | [optional] [readonly] 
**labels** | **[String]** | Output only. The resource names of labels attached to this ad group. | [optional] [readonly] 
**languageCode** | **String** | Output only. The language of the ads and keywords in an ad group. This field is only available for Microsoft Advertising accounts. More details: https://docs.microsoft.com/en-us/advertising/guides/ad-languages?view&#x3D;bingads-13#adlanguage | [optional] [readonly] 
**lastModifiedTime** | **String** | Output only. The datetime when this ad group was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. | [optional] [readonly] 
**name** | **String** | The name of the ad group. This field is required and should not be empty when creating new ad groups. It must contain fewer than 255 UTF-8 full-width characters. It must not contain any null (code point 0x0), NL line feed (code point 0xA) or carriage return (code point 0xD) characters. | [optional] 
**resourceName** | **String** | Immutable. The resource name of the ad group. Ad group resource names have the form: &#x60;customers/{customer_id}/adGroups/{ad_group_id}&#x60; | [optional] 
**startDate** | **String** | Output only. Date when this ad group starts serving ads. By default, the ad group starts now or the ad group&#39;s start date, whichever is later. If this field is set, then the ad group starts at the beginning of the specified date in the customer&#39;s time zone. This field is only available for Microsoft Advertising and Facebook gateway accounts. Format: YYYY-MM-DD Example: 2019-03-14 | [optional] [readonly] 
**status** | **String** | The status of the ad group. | [optional] 
**targetingSetting** | [**GoogleAdsSearchads360V0CommonTargetingSetting**](GoogleAdsSearchads360V0CommonTargetingSetting.md) |  | [optional] 
**type** | **String** | Immutable. The type of the ad group. | [optional] 



## Enum: AdRotationModeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `OPTIMIZE` (value: `"OPTIMIZE"`)

* `ROTATE_FOREVER` (value: `"ROTATE_FOREVER"`)





## Enum: EngineStatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `AD_GROUP_ELIGIBLE` (value: `"AD_GROUP_ELIGIBLE"`)

* `AD_GROUP_EXPIRED` (value: `"AD_GROUP_EXPIRED"`)

* `AD_GROUP_REMOVED` (value: `"AD_GROUP_REMOVED"`)

* `AD_GROUP_DRAFT` (value: `"AD_GROUP_DRAFT"`)

* `AD_GROUP_PAUSED` (value: `"AD_GROUP_PAUSED"`)

* `AD_GROUP_SERVING` (value: `"AD_GROUP_SERVING"`)

* `AD_GROUP_SUBMITTED` (value: `"AD_GROUP_SUBMITTED"`)

* `CAMPAIGN_PAUSED` (value: `"CAMPAIGN_PAUSED"`)

* `ACCOUNT_PAUSED` (value: `"ACCOUNT_PAUSED"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `PAUSED` (value: `"PAUSED"`)

* `REMOVED` (value: `"REMOVED"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `SEARCH_STANDARD` (value: `"SEARCH_STANDARD"`)

* `DISPLAY_STANDARD` (value: `"DISPLAY_STANDARD"`)

* `SHOPPING_PRODUCT_ADS` (value: `"SHOPPING_PRODUCT_ADS"`)

* `SHOPPING_SHOWCASE_ADS` (value: `"SHOPPING_SHOWCASE_ADS"`)

* `HOTEL_ADS` (value: `"HOTEL_ADS"`)

* `SHOPPING_SMART_ADS` (value: `"SHOPPING_SMART_ADS"`)

* `VIDEO_BUMPER` (value: `"VIDEO_BUMPER"`)

* `VIDEO_TRUE_VIEW_IN_STREAM` (value: `"VIDEO_TRUE_VIEW_IN_STREAM"`)

* `VIDEO_TRUE_VIEW_IN_DISPLAY` (value: `"VIDEO_TRUE_VIEW_IN_DISPLAY"`)

* `VIDEO_NON_SKIPPABLE_IN_STREAM` (value: `"VIDEO_NON_SKIPPABLE_IN_STREAM"`)

* `VIDEO_OUTSTREAM` (value: `"VIDEO_OUTSTREAM"`)

* `SEARCH_DYNAMIC_ADS` (value: `"SEARCH_DYNAMIC_ADS"`)

* `SHOPPING_COMPARISON_LISTING_ADS` (value: `"SHOPPING_COMPARISON_LISTING_ADS"`)

* `PROMOTED_HOTEL_ADS` (value: `"PROMOTED_HOTEL_ADS"`)

* `VIDEO_RESPONSIVE` (value: `"VIDEO_RESPONSIVE"`)

* `VIDEO_EFFICIENT_REACH` (value: `"VIDEO_EFFICIENT_REACH"`)

* `SMART_CAMPAIGN_ADS` (value: `"SMART_CAMPAIGN_ADS"`)

* `TRAVEL_ADS` (value: `"TRAVEL_ADS"`)




