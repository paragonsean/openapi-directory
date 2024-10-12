# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesAd

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayUrl** | **String** | The URL that appears in the ad description for some ad formats. | [optional] 
**expandedDynamicSearchAd** | [**GoogleAdsSearchads360V0CommonSearchAds360ExpandedDynamicSearchAdInfo**](GoogleAdsSearchads360V0CommonSearchAds360ExpandedDynamicSearchAdInfo.md) |  | [optional] 
**expandedTextAd** | [**GoogleAdsSearchads360V0CommonSearchAds360ExpandedTextAdInfo**](GoogleAdsSearchads360V0CommonSearchAds360ExpandedTextAdInfo.md) |  | [optional] 
**finalUrls** | **[String]** | The list of possible final URLs after all cross-domain redirects for the ad. | [optional] 
**id** | **String** | Output only. The ID of the ad. | [optional] [readonly] 
**name** | **String** | Immutable. The name of the ad. This is only used to be able to identify the ad. It does not need to be unique and does not affect the served ad. The name field is currently only supported for DisplayUploadAd, ImageAd, ShoppingComparisonListingAd and VideoAd. | [optional] 
**productAd** | **Object** | A Search Ads 360 product ad. | [optional] 
**resourceName** | **String** | Immutable. The resource name of the ad. Ad resource names have the form: &#x60;customers/{customer_id}/ads/{ad_id}&#x60; | [optional] 
**responsiveSearchAd** | [**GoogleAdsSearchads360V0CommonSearchAds360ResponsiveSearchAdInfo**](GoogleAdsSearchads360V0CommonSearchAds360ResponsiveSearchAdInfo.md) |  | [optional] 
**textAd** | [**GoogleAdsSearchads360V0CommonSearchAds360TextAdInfo**](GoogleAdsSearchads360V0CommonSearchAds360TextAdInfo.md) |  | [optional] 
**type** | **String** | Output only. The type of ad. | [optional] [readonly] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `TEXT_AD` (value: `"TEXT_AD"`)

* `EXPANDED_TEXT_AD` (value: `"EXPANDED_TEXT_AD"`)

* `CALL_ONLY_AD` (value: `"CALL_ONLY_AD"`)

* `EXPANDED_DYNAMIC_SEARCH_AD` (value: `"EXPANDED_DYNAMIC_SEARCH_AD"`)

* `HOTEL_AD` (value: `"HOTEL_AD"`)

* `SHOPPING_SMART_AD` (value: `"SHOPPING_SMART_AD"`)

* `SHOPPING_PRODUCT_AD` (value: `"SHOPPING_PRODUCT_AD"`)

* `VIDEO_AD` (value: `"VIDEO_AD"`)

* `GMAIL_AD` (value: `"GMAIL_AD"`)

* `IMAGE_AD` (value: `"IMAGE_AD"`)

* `RESPONSIVE_SEARCH_AD` (value: `"RESPONSIVE_SEARCH_AD"`)

* `LEGACY_RESPONSIVE_DISPLAY_AD` (value: `"LEGACY_RESPONSIVE_DISPLAY_AD"`)

* `APP_AD` (value: `"APP_AD"`)

* `LEGACY_APP_INSTALL_AD` (value: `"LEGACY_APP_INSTALL_AD"`)

* `RESPONSIVE_DISPLAY_AD` (value: `"RESPONSIVE_DISPLAY_AD"`)

* `LOCAL_AD` (value: `"LOCAL_AD"`)

* `HTML5_UPLOAD_AD` (value: `"HTML5_UPLOAD_AD"`)

* `DYNAMIC_HTML5_AD` (value: `"DYNAMIC_HTML5_AD"`)

* `APP_ENGAGEMENT_AD` (value: `"APP_ENGAGEMENT_AD"`)

* `SHOPPING_COMPARISON_LISTING_AD` (value: `"SHOPPING_COMPARISON_LISTING_AD"`)

* `VIDEO_BUMPER_AD` (value: `"VIDEO_BUMPER_AD"`)

* `VIDEO_NON_SKIPPABLE_IN_STREAM_AD` (value: `"VIDEO_NON_SKIPPABLE_IN_STREAM_AD"`)

* `VIDEO_OUTSTREAM_AD` (value: `"VIDEO_OUTSTREAM_AD"`)

* `VIDEO_TRUEVIEW_DISCOVERY_AD` (value: `"VIDEO_TRUEVIEW_DISCOVERY_AD"`)

* `VIDEO_TRUEVIEW_IN_STREAM_AD` (value: `"VIDEO_TRUEVIEW_IN_STREAM_AD"`)

* `VIDEO_RESPONSIVE_AD` (value: `"VIDEO_RESPONSIVE_AD"`)

* `SMART_CAMPAIGN_AD` (value: `"SMART_CAMPAIGN_AD"`)

* `APP_PRE_REGISTRATION_AD` (value: `"APP_PRE_REGISTRATION_AD"`)

* `DISCOVERY_MULTI_ASSET_AD` (value: `"DISCOVERY_MULTI_ASSET_AD"`)

* `DISCOVERY_CAROUSEL_AD` (value: `"DISCOVERY_CAROUSEL_AD"`)

* `TRAVEL_AD` (value: `"TRAVEL_AD"`)

* `DISCOVERY_VIDEO_RESPONSIVE_AD` (value: `"DISCOVERY_VIDEO_RESPONSIVE_AD"`)




