# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesAsset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callAsset** | [**GoogleAdsSearchads360V0CommonUnifiedCallAsset**](GoogleAdsSearchads360V0CommonUnifiedCallAsset.md) |  | [optional] 
**callToActionAsset** | [**GoogleAdsSearchads360V0CommonCallToActionAsset**](GoogleAdsSearchads360V0CommonCallToActionAsset.md) |  | [optional] 
**calloutAsset** | [**GoogleAdsSearchads360V0CommonUnifiedCalloutAsset**](GoogleAdsSearchads360V0CommonUnifiedCalloutAsset.md) |  | [optional] 
**creationTime** | **String** | Output only. The timestamp when this asset was created. The timestamp is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss\&quot; format. | [optional] [readonly] 
**engineStatus** | **String** | Output only. The Engine Status for an asset. | [optional] [readonly] 
**finalUrls** | **[String]** | A list of possible final URLs after all cross domain redirects. | [optional] 
**id** | **String** | Output only. The ID of the asset. | [optional] [readonly] 
**imageAsset** | [**GoogleAdsSearchads360V0CommonImageAsset**](GoogleAdsSearchads360V0CommonImageAsset.md) |  | [optional] 
**lastModifiedTime** | **String** | Output only. The datetime when this asset was last modified. The datetime is in the customer&#39;s time zone and in \&quot;yyyy-MM-dd HH:mm:ss.ssssss\&quot; format. | [optional] [readonly] 
**locationAsset** | [**GoogleAdsSearchads360V0CommonUnifiedLocationAsset**](GoogleAdsSearchads360V0CommonUnifiedLocationAsset.md) |  | [optional] 
**mobileAppAsset** | [**GoogleAdsSearchads360V0CommonMobileAppAsset**](GoogleAdsSearchads360V0CommonMobileAppAsset.md) |  | [optional] 
**name** | **String** | Optional name of the asset. | [optional] 
**pageFeedAsset** | [**GoogleAdsSearchads360V0CommonUnifiedPageFeedAsset**](GoogleAdsSearchads360V0CommonUnifiedPageFeedAsset.md) |  | [optional] 
**resourceName** | **String** | Immutable. The resource name of the asset. Asset resource names have the form: &#x60;customers/{customer_id}/assets/{asset_id}&#x60; | [optional] 
**sitelinkAsset** | [**GoogleAdsSearchads360V0CommonUnifiedSitelinkAsset**](GoogleAdsSearchads360V0CommonUnifiedSitelinkAsset.md) |  | [optional] 
**status** | **String** | Output only. The status of the asset. | [optional] [readonly] 
**textAsset** | [**GoogleAdsSearchads360V0CommonTextAsset**](GoogleAdsSearchads360V0CommonTextAsset.md) |  | [optional] 
**trackingUrlTemplate** | **String** | URL template for constructing a tracking URL. | [optional] 
**type** | **String** | Output only. Type of the asset. | [optional] [readonly] 
**youtubeVideoAsset** | [**GoogleAdsSearchads360V0CommonYoutubeVideoAsset**](GoogleAdsSearchads360V0CommonYoutubeVideoAsset.md) |  | [optional] 



## Enum: EngineStatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `SERVING` (value: `"SERVING"`)

* `SERVING_LIMITED` (value: `"SERVING_LIMITED"`)

* `DISAPPROVED` (value: `"DISAPPROVED"`)

* `DISABLED` (value: `"DISABLED"`)

* `REMOVED` (value: `"REMOVED"`)





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `REMOVED` (value: `"REMOVED"`)

* `ARCHIVED` (value: `"ARCHIVED"`)

* `PENDING_SYSTEM_GENERATED` (value: `"PENDING_SYSTEM_GENERATED"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `YOUTUBE_VIDEO` (value: `"YOUTUBE_VIDEO"`)

* `MEDIA_BUNDLE` (value: `"MEDIA_BUNDLE"`)

* `IMAGE` (value: `"IMAGE"`)

* `TEXT` (value: `"TEXT"`)

* `LEAD_FORM` (value: `"LEAD_FORM"`)

* `BOOK_ON_GOOGLE` (value: `"BOOK_ON_GOOGLE"`)

* `PROMOTION` (value: `"PROMOTION"`)

* `CALLOUT` (value: `"CALLOUT"`)

* `STRUCTURED_SNIPPET` (value: `"STRUCTURED_SNIPPET"`)

* `SITELINK` (value: `"SITELINK"`)

* `PAGE_FEED` (value: `"PAGE_FEED"`)

* `DYNAMIC_EDUCATION` (value: `"DYNAMIC_EDUCATION"`)

* `MOBILE_APP` (value: `"MOBILE_APP"`)

* `HOTEL_CALLOUT` (value: `"HOTEL_CALLOUT"`)

* `CALL` (value: `"CALL"`)

* `PRICE` (value: `"PRICE"`)

* `CALL_TO_ACTION` (value: `"CALL_TO_ACTION"`)

* `DYNAMIC_REAL_ESTATE` (value: `"DYNAMIC_REAL_ESTATE"`)

* `DYNAMIC_CUSTOM` (value: `"DYNAMIC_CUSTOM"`)

* `DYNAMIC_HOTELS_AND_RENTALS` (value: `"DYNAMIC_HOTELS_AND_RENTALS"`)

* `DYNAMIC_FLIGHTS` (value: `"DYNAMIC_FLIGHTS"`)

* `DISCOVERY_CAROUSEL_CARD` (value: `"DISCOVERY_CAROUSEL_CARD"`)

* `DYNAMIC_TRAVEL` (value: `"DYNAMIC_TRAVEL"`)

* `DYNAMIC_LOCAL` (value: `"DYNAMIC_LOCAL"`)

* `DYNAMIC_JOBS` (value: `"DYNAMIC_JOBS"`)

* `LOCATION` (value: `"LOCATION"`)

* `HOTEL_PROPERTY` (value: `"HOTEL_PROPERTY"`)




