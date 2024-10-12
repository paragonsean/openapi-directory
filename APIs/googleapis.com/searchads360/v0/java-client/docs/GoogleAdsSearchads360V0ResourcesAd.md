

# GoogleAdsSearchads360V0ResourcesAd

An ad.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayUrl** | **String** | The URL that appears in the ad description for some ad formats. |  [optional] |
|**expandedDynamicSearchAd** | [**GoogleAdsSearchads360V0CommonSearchAds360ExpandedDynamicSearchAdInfo**](GoogleAdsSearchads360V0CommonSearchAds360ExpandedDynamicSearchAdInfo.md) |  |  [optional] |
|**expandedTextAd** | [**GoogleAdsSearchads360V0CommonSearchAds360ExpandedTextAdInfo**](GoogleAdsSearchads360V0CommonSearchAds360ExpandedTextAdInfo.md) |  |  [optional] |
|**finalUrls** | **List&lt;String&gt;** | The list of possible final URLs after all cross-domain redirects for the ad. |  [optional] |
|**id** | **String** | Output only. The ID of the ad. |  [optional] [readonly] |
|**name** | **String** | Immutable. The name of the ad. This is only used to be able to identify the ad. It does not need to be unique and does not affect the served ad. The name field is currently only supported for DisplayUploadAd, ImageAd, ShoppingComparisonListingAd and VideoAd. |  [optional] |
|**productAd** | **Object** | A Search Ads 360 product ad. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the ad. Ad resource names have the form: &#x60;customers/{customer_id}/ads/{ad_id}&#x60; |  [optional] |
|**responsiveSearchAd** | [**GoogleAdsSearchads360V0CommonSearchAds360ResponsiveSearchAdInfo**](GoogleAdsSearchads360V0CommonSearchAds360ResponsiveSearchAdInfo.md) |  |  [optional] |
|**textAd** | [**GoogleAdsSearchads360V0CommonSearchAds360TextAdInfo**](GoogleAdsSearchads360V0CommonSearchAds360TextAdInfo.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of ad. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| TEXT_AD | &quot;TEXT_AD&quot; |
| EXPANDED_TEXT_AD | &quot;EXPANDED_TEXT_AD&quot; |
| CALL_ONLY_AD | &quot;CALL_ONLY_AD&quot; |
| EXPANDED_DYNAMIC_SEARCH_AD | &quot;EXPANDED_DYNAMIC_SEARCH_AD&quot; |
| HOTEL_AD | &quot;HOTEL_AD&quot; |
| SHOPPING_SMART_AD | &quot;SHOPPING_SMART_AD&quot; |
| SHOPPING_PRODUCT_AD | &quot;SHOPPING_PRODUCT_AD&quot; |
| VIDEO_AD | &quot;VIDEO_AD&quot; |
| GMAIL_AD | &quot;GMAIL_AD&quot; |
| IMAGE_AD | &quot;IMAGE_AD&quot; |
| RESPONSIVE_SEARCH_AD | &quot;RESPONSIVE_SEARCH_AD&quot; |
| LEGACY_RESPONSIVE_DISPLAY_AD | &quot;LEGACY_RESPONSIVE_DISPLAY_AD&quot; |
| APP_AD | &quot;APP_AD&quot; |
| LEGACY_APP_INSTALL_AD | &quot;LEGACY_APP_INSTALL_AD&quot; |
| RESPONSIVE_DISPLAY_AD | &quot;RESPONSIVE_DISPLAY_AD&quot; |
| LOCAL_AD | &quot;LOCAL_AD&quot; |
| HTML5_UPLOAD_AD | &quot;HTML5_UPLOAD_AD&quot; |
| DYNAMIC_HTML5_AD | &quot;DYNAMIC_HTML5_AD&quot; |
| APP_ENGAGEMENT_AD | &quot;APP_ENGAGEMENT_AD&quot; |
| SHOPPING_COMPARISON_LISTING_AD | &quot;SHOPPING_COMPARISON_LISTING_AD&quot; |
| VIDEO_BUMPER_AD | &quot;VIDEO_BUMPER_AD&quot; |
| VIDEO_NON_SKIPPABLE_IN_STREAM_AD | &quot;VIDEO_NON_SKIPPABLE_IN_STREAM_AD&quot; |
| VIDEO_OUTSTREAM_AD | &quot;VIDEO_OUTSTREAM_AD&quot; |
| VIDEO_TRUEVIEW_DISCOVERY_AD | &quot;VIDEO_TRUEVIEW_DISCOVERY_AD&quot; |
| VIDEO_TRUEVIEW_IN_STREAM_AD | &quot;VIDEO_TRUEVIEW_IN_STREAM_AD&quot; |
| VIDEO_RESPONSIVE_AD | &quot;VIDEO_RESPONSIVE_AD&quot; |
| SMART_CAMPAIGN_AD | &quot;SMART_CAMPAIGN_AD&quot; |
| APP_PRE_REGISTRATION_AD | &quot;APP_PRE_REGISTRATION_AD&quot; |
| DISCOVERY_MULTI_ASSET_AD | &quot;DISCOVERY_MULTI_ASSET_AD&quot; |
| DISCOVERY_CAROUSEL_AD | &quot;DISCOVERY_CAROUSEL_AD&quot; |
| TRAVEL_AD | &quot;TRAVEL_AD&quot; |
| DISCOVERY_VIDEO_RESPONSIVE_AD | &quot;DISCOVERY_VIDEO_RESPONSIVE_AD&quot; |



