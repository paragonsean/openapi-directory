

# GoogleAdsSearchads360V0ResourcesAsset

Asset is a part of an ad which can be shared across multiple ads. It can be an image (ImageAsset), a video (YoutubeVideoAsset), etc. Assets are immutable and cannot be removed. To stop an asset from serving, remove the asset from the entity that is using it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callAsset** | [**GoogleAdsSearchads360V0CommonUnifiedCallAsset**](GoogleAdsSearchads360V0CommonUnifiedCallAsset.md) |  |  [optional] |
|**callToActionAsset** | [**GoogleAdsSearchads360V0CommonCallToActionAsset**](GoogleAdsSearchads360V0CommonCallToActionAsset.md) |  |  [optional] |
|**calloutAsset** | [**GoogleAdsSearchads360V0CommonUnifiedCalloutAsset**](GoogleAdsSearchads360V0CommonUnifiedCalloutAsset.md) |  |  [optional] |
|**creationTime** | **String** | Output only. The timestamp when this asset was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. |  [optional] [readonly] |
|**engineStatus** | [**EngineStatusEnum**](#EngineStatusEnum) | Output only. The Engine Status for an asset. |  [optional] [readonly] |
|**finalUrls** | **List&lt;String&gt;** | A list of possible final URLs after all cross domain redirects. |  [optional] |
|**id** | **String** | Output only. The ID of the asset. |  [optional] [readonly] |
|**imageAsset** | [**GoogleAdsSearchads360V0CommonImageAsset**](GoogleAdsSearchads360V0CommonImageAsset.md) |  |  [optional] |
|**lastModifiedTime** | **String** | Output only. The datetime when this asset was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. |  [optional] [readonly] |
|**locationAsset** | [**GoogleAdsSearchads360V0CommonUnifiedLocationAsset**](GoogleAdsSearchads360V0CommonUnifiedLocationAsset.md) |  |  [optional] |
|**mobileAppAsset** | [**GoogleAdsSearchads360V0CommonMobileAppAsset**](GoogleAdsSearchads360V0CommonMobileAppAsset.md) |  |  [optional] |
|**name** | **String** | Optional name of the asset. |  [optional] |
|**pageFeedAsset** | [**GoogleAdsSearchads360V0CommonUnifiedPageFeedAsset**](GoogleAdsSearchads360V0CommonUnifiedPageFeedAsset.md) |  |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the asset. Asset resource names have the form: &#x60;customers/{customer_id}/assets/{asset_id}&#x60; |  [optional] |
|**sitelinkAsset** | [**GoogleAdsSearchads360V0CommonUnifiedSitelinkAsset**](GoogleAdsSearchads360V0CommonUnifiedSitelinkAsset.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The status of the asset. |  [optional] [readonly] |
|**textAsset** | [**GoogleAdsSearchads360V0CommonTextAsset**](GoogleAdsSearchads360V0CommonTextAsset.md) |  |  [optional] |
|**trackingUrlTemplate** | **String** | URL template for constructing a tracking URL. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Type of the asset. |  [optional] [readonly] |
|**youtubeVideoAsset** | [**GoogleAdsSearchads360V0CommonYoutubeVideoAsset**](GoogleAdsSearchads360V0CommonYoutubeVideoAsset.md) |  |  [optional] |



## Enum: EngineStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| SERVING | &quot;SERVING&quot; |
| SERVING_LIMITED | &quot;SERVING_LIMITED&quot; |
| DISAPPROVED | &quot;DISAPPROVED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| PENDING_SYSTEM_GENERATED | &quot;PENDING_SYSTEM_GENERATED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| YOUTUBE_VIDEO | &quot;YOUTUBE_VIDEO&quot; |
| MEDIA_BUNDLE | &quot;MEDIA_BUNDLE&quot; |
| IMAGE | &quot;IMAGE&quot; |
| TEXT | &quot;TEXT&quot; |
| LEAD_FORM | &quot;LEAD_FORM&quot; |
| BOOK_ON_GOOGLE | &quot;BOOK_ON_GOOGLE&quot; |
| PROMOTION | &quot;PROMOTION&quot; |
| CALLOUT | &quot;CALLOUT&quot; |
| STRUCTURED_SNIPPET | &quot;STRUCTURED_SNIPPET&quot; |
| SITELINK | &quot;SITELINK&quot; |
| PAGE_FEED | &quot;PAGE_FEED&quot; |
| DYNAMIC_EDUCATION | &quot;DYNAMIC_EDUCATION&quot; |
| MOBILE_APP | &quot;MOBILE_APP&quot; |
| HOTEL_CALLOUT | &quot;HOTEL_CALLOUT&quot; |
| CALL | &quot;CALL&quot; |
| PRICE | &quot;PRICE&quot; |
| CALL_TO_ACTION | &quot;CALL_TO_ACTION&quot; |
| DYNAMIC_REAL_ESTATE | &quot;DYNAMIC_REAL_ESTATE&quot; |
| DYNAMIC_CUSTOM | &quot;DYNAMIC_CUSTOM&quot; |
| DYNAMIC_HOTELS_AND_RENTALS | &quot;DYNAMIC_HOTELS_AND_RENTALS&quot; |
| DYNAMIC_FLIGHTS | &quot;DYNAMIC_FLIGHTS&quot; |
| DISCOVERY_CAROUSEL_CARD | &quot;DISCOVERY_CAROUSEL_CARD&quot; |
| DYNAMIC_TRAVEL | &quot;DYNAMIC_TRAVEL&quot; |
| DYNAMIC_LOCAL | &quot;DYNAMIC_LOCAL&quot; |
| DYNAMIC_JOBS | &quot;DYNAMIC_JOBS&quot; |
| LOCATION | &quot;LOCATION&quot; |
| HOTEL_PROPERTY | &quot;HOTEL_PROPERTY&quot; |



