

# CreativeNativeAd

If nativeAd is set, HTMLSnippet, videoVastXML, and the videoURL outside of nativeAd should not be set. (The videoURL inside nativeAd can be set.)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiser** | **String** |  |  [optional] |
|**appIcon** | [**CreativeNativeAdAppIcon**](CreativeNativeAdAppIcon.md) |  |  [optional] |
|**body** | **String** | A long description of the ad. |  [optional] |
|**callToAction** | **String** | A label for the button that the user is supposed to click. |  [optional] |
|**clickLinkUrl** | **String** | The URL that the browser/SDK will load when the user clicks the ad. |  [optional] |
|**clickTrackingUrl** | **String** | The URL to use for click tracking. |  [optional] |
|**headline** | **String** | A short title for the ad. |  [optional] |
|**image** | [**CreativeNativeAdImage**](CreativeNativeAdImage.md) |  |  [optional] |
|**impressionTrackingUrl** | **List&lt;String&gt;** | The URLs are called when the impression is rendered. |  [optional] |
|**logo** | [**CreativeNativeAdLogo**](CreativeNativeAdLogo.md) |  |  [optional] |
|**price** | **String** | The price of the promoted app including the currency info. |  [optional] |
|**starRating** | **Double** | The app rating in the app store. Must be in the range [0-5]. |  [optional] |
|**videoURL** | **String** | The URL of the XML VAST for a native ad. Note this is a separate field from resource.video_url. |  [optional] |



