

# CreativeServingDecision

Top level status and detected attributes of a creative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adTechnologyProviders** | [**AdTechnologyProviders**](AdTechnologyProviders.md) |  |  [optional] |
|**chinaPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  |  [optional] |
|**dealsPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  |  [optional] |
|**detectedAdvertisers** | [**List&lt;AdvertiserAndBrand&gt;**](AdvertiserAndBrand.md) | Detected advertisers and brands. |  [optional] |
|**detectedAttributes** | [**List&lt;DetectedAttributesEnum&gt;**](#List&lt;DetectedAttributesEnum&gt;) | Publisher-excludable attributes that were detected for this creative. Can be used to filter the response of the creatives.list method. If the &#x60;excluded_attribute&#x60; field of a [bid request](https://developers.google.com/authorized-buyers/rtb/downloads/realtime-bidding-proto) contains one of the attributes that were declared or detected for a given creative, and a bid is submitted with that creative, the bid will be filtered before the auction. |  [optional] |
|**detectedClickThroughUrls** | **List&lt;String&gt;** | The set of detected destination URLs for the creative. Can be used to filter the response of the creatives.list method. |  [optional] |
|**detectedDomains** | **List&lt;String&gt;** | The detected domains for this creative. |  [optional] |
|**detectedLanguages** | **List&lt;String&gt;** | The detected languages for this creative. The order is arbitrary. The codes are 2 or 5 characters and are documented at https://developers.google.com/adwords/api/docs/appendix/languagecodes. Can be used to filter the response of the creatives.list method. |  [optional] |
|**detectedProductCategories** | **List&lt;Integer&gt;** | Detected product categories, if any. See the ad-product-categories.txt file in the technical documentation for a list of IDs. Can be used to filter the response of the creatives.list method. |  [optional] |
|**detectedSensitiveCategories** | **List&lt;Integer&gt;** | Detected sensitive categories, if any. Can be used to filter the response of the creatives.list method. See the ad-sensitive-categories.txt file in the technical documentation for a list of IDs. You should use these IDs along with the excluded-sensitive-category field in the bid request to filter your bids. |  [optional] |
|**detectedVendorIds** | **List&lt;Integer&gt;** | IDs of the ad technology vendors that were detected to be used by this creative. See https://storage.googleapis.com/adx-rtb-dictionaries/vendors.txt for possible values. Can be used to filter the response of the creatives.list method. If the &#x60;allowed_vendor_type&#x60; field of a [bid request](https://developers.google.com/authorized-buyers/rtb/downloads/realtime-bidding-proto) does not contain one of the vendor type IDs that were declared or detected for a given creative, and a bid is submitted with that creative, the bid will be filtered before the auction. |  [optional] |
|**lastStatusUpdate** | **String** | The last time the creative status was updated. Can be used to filter the response of the creatives.list method. |  [optional] |
|**networkPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  |  [optional] |
|**platformPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  |  [optional] |
|**russiaPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  |  [optional] |



## Enum: List&lt;DetectedAttributesEnum&gt;

| Name | Value |
|---- | -----|
| ATTRIBUTE_UNSPECIFIED | &quot;ATTRIBUTE_UNSPECIFIED&quot; |
| IMAGE_RICH_MEDIA | &quot;IMAGE_RICH_MEDIA&quot; |
| ADOBE_FLASH_FLV | &quot;ADOBE_FLASH_FLV&quot; |
| IS_TAGGED | &quot;IS_TAGGED&quot; |
| IS_COOKIE_TARGETED | &quot;IS_COOKIE_TARGETED&quot; |
| IS_USER_INTEREST_TARGETED | &quot;IS_USER_INTEREST_TARGETED&quot; |
| EXPANDING_DIRECTION_NONE | &quot;EXPANDING_DIRECTION_NONE&quot; |
| EXPANDING_DIRECTION_UP | &quot;EXPANDING_DIRECTION_UP&quot; |
| EXPANDING_DIRECTION_DOWN | &quot;EXPANDING_DIRECTION_DOWN&quot; |
| EXPANDING_DIRECTION_LEFT | &quot;EXPANDING_DIRECTION_LEFT&quot; |
| EXPANDING_DIRECTION_RIGHT | &quot;EXPANDING_DIRECTION_RIGHT&quot; |
| EXPANDING_DIRECTION_UP_LEFT | &quot;EXPANDING_DIRECTION_UP_LEFT&quot; |
| EXPANDING_DIRECTION_UP_RIGHT | &quot;EXPANDING_DIRECTION_UP_RIGHT&quot; |
| EXPANDING_DIRECTION_DOWN_LEFT | &quot;EXPANDING_DIRECTION_DOWN_LEFT&quot; |
| EXPANDING_DIRECTION_DOWN_RIGHT | &quot;EXPANDING_DIRECTION_DOWN_RIGHT&quot; |
| CREATIVE_TYPE_HTML | &quot;CREATIVE_TYPE_HTML&quot; |
| CREATIVE_TYPE_VAST_VIDEO | &quot;CREATIVE_TYPE_VAST_VIDEO&quot; |
| EXPANDING_DIRECTION_UP_OR_DOWN | &quot;EXPANDING_DIRECTION_UP_OR_DOWN&quot; |
| EXPANDING_DIRECTION_LEFT_OR_RIGHT | &quot;EXPANDING_DIRECTION_LEFT_OR_RIGHT&quot; |
| EXPANDING_DIRECTION_ANY_DIAGONAL | &quot;EXPANDING_DIRECTION_ANY_DIAGONAL&quot; |
| EXPANDING_ACTION_ROLLOVER_TO_EXPAND | &quot;EXPANDING_ACTION_ROLLOVER_TO_EXPAND&quot; |
| INSTREAM_VAST_VIDEO_TYPE_VPAID_FLASH | &quot;INSTREAM_VAST_VIDEO_TYPE_VPAID_FLASH&quot; |
| RICH_MEDIA_CAPABILITY_TYPE_MRAID | &quot;RICH_MEDIA_CAPABILITY_TYPE_MRAID&quot; |
| RICH_MEDIA_CAPABILITY_TYPE_FLASH | &quot;RICH_MEDIA_CAPABILITY_TYPE_FLASH&quot; |
| RICH_MEDIA_CAPABILITY_TYPE_HTML5 | &quot;RICH_MEDIA_CAPABILITY_TYPE_HTML5&quot; |
| SKIPPABLE_INSTREAM_VIDEO | &quot;SKIPPABLE_INSTREAM_VIDEO&quot; |
| RICH_MEDIA_CAPABILITY_TYPE_SSL | &quot;RICH_MEDIA_CAPABILITY_TYPE_SSL&quot; |
| RICH_MEDIA_CAPABILITY_TYPE_NON_SSL | &quot;RICH_MEDIA_CAPABILITY_TYPE_NON_SSL&quot; |
| RICH_MEDIA_CAPABILITY_TYPE_INTERSTITIAL | &quot;RICH_MEDIA_CAPABILITY_TYPE_INTERSTITIAL&quot; |
| NON_SKIPPABLE_INSTREAM_VIDEO | &quot;NON_SKIPPABLE_INSTREAM_VIDEO&quot; |
| NATIVE_ELIGIBILITY_ELIGIBLE | &quot;NATIVE_ELIGIBILITY_ELIGIBLE&quot; |
| NON_VPAID | &quot;NON_VPAID&quot; |
| NATIVE_ELIGIBILITY_NOT_ELIGIBLE | &quot;NATIVE_ELIGIBILITY_NOT_ELIGIBLE&quot; |
| ANY_INTERSTITIAL | &quot;ANY_INTERSTITIAL&quot; |
| NON_INTERSTITIAL | &quot;NON_INTERSTITIAL&quot; |
| IN_BANNER_VIDEO | &quot;IN_BANNER_VIDEO&quot; |
| RENDERING_SIZELESS_ADX | &quot;RENDERING_SIZELESS_ADX&quot; |
| OMSDK_1_0 | &quot;OMSDK_1_0&quot; |
| RENDERING_PLAYABLE | &quot;RENDERING_PLAYABLE&quot; |



