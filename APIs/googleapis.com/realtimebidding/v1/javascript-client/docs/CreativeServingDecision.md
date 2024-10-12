# RealTimeBiddingApi.CreativeServingDecision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adTechnologyProviders** | [**AdTechnologyProviders**](AdTechnologyProviders.md) |  | [optional] 
**chinaPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  | [optional] 
**dealsPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  | [optional] 
**detectedAdvertisers** | [**[AdvertiserAndBrand]**](AdvertiserAndBrand.md) | Detected advertisers and brands. | [optional] 
**detectedAttributes** | **[String]** | Publisher-excludable attributes that were detected for this creative. Can be used to filter the response of the creatives.list method. If the &#x60;excluded_attribute&#x60; field of a [bid request](https://developers.google.com/authorized-buyers/rtb/downloads/realtime-bidding-proto) contains one of the attributes that were declared or detected for a given creative, and a bid is submitted with that creative, the bid will be filtered before the auction. | [optional] 
**detectedClickThroughUrls** | **[String]** | The set of detected destination URLs for the creative. Can be used to filter the response of the creatives.list method. | [optional] 
**detectedDomains** | **[String]** | The detected domains for this creative. | [optional] 
**detectedLanguages** | **[String]** | The detected languages for this creative. The order is arbitrary. The codes are 2 or 5 characters and are documented at https://developers.google.com/adwords/api/docs/appendix/languagecodes. Can be used to filter the response of the creatives.list method. | [optional] 
**detectedProductCategories** | **[Number]** | Detected product categories, if any. See the ad-product-categories.txt file in the technical documentation for a list of IDs. Can be used to filter the response of the creatives.list method. | [optional] 
**detectedSensitiveCategories** | **[Number]** | Detected sensitive categories, if any. Can be used to filter the response of the creatives.list method. See the ad-sensitive-categories.txt file in the technical documentation for a list of IDs. You should use these IDs along with the excluded-sensitive-category field in the bid request to filter your bids. | [optional] 
**detectedVendorIds** | **[Number]** | IDs of the ad technology vendors that were detected to be used by this creative. See https://storage.googleapis.com/adx-rtb-dictionaries/vendors.txt for possible values. Can be used to filter the response of the creatives.list method. If the &#x60;allowed_vendor_type&#x60; field of a [bid request](https://developers.google.com/authorized-buyers/rtb/downloads/realtime-bidding-proto) does not contain one of the vendor type IDs that were declared or detected for a given creative, and a bid is submitted with that creative, the bid will be filtered before the auction. | [optional] 
**lastStatusUpdate** | **String** | The last time the creative status was updated. Can be used to filter the response of the creatives.list method. | [optional] 
**networkPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  | [optional] 
**platformPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  | [optional] 
**russiaPolicyCompliance** | [**PolicyCompliance**](PolicyCompliance.md) |  | [optional] 



## Enum: [DetectedAttributesEnum]


* `ATTRIBUTE_UNSPECIFIED` (value: `"ATTRIBUTE_UNSPECIFIED"`)

* `IMAGE_RICH_MEDIA` (value: `"IMAGE_RICH_MEDIA"`)

* `ADOBE_FLASH_FLV` (value: `"ADOBE_FLASH_FLV"`)

* `IS_TAGGED` (value: `"IS_TAGGED"`)

* `IS_COOKIE_TARGETED` (value: `"IS_COOKIE_TARGETED"`)

* `IS_USER_INTEREST_TARGETED` (value: `"IS_USER_INTEREST_TARGETED"`)

* `EXPANDING_DIRECTION_NONE` (value: `"EXPANDING_DIRECTION_NONE"`)

* `EXPANDING_DIRECTION_UP` (value: `"EXPANDING_DIRECTION_UP"`)

* `EXPANDING_DIRECTION_DOWN` (value: `"EXPANDING_DIRECTION_DOWN"`)

* `EXPANDING_DIRECTION_LEFT` (value: `"EXPANDING_DIRECTION_LEFT"`)

* `EXPANDING_DIRECTION_RIGHT` (value: `"EXPANDING_DIRECTION_RIGHT"`)

* `EXPANDING_DIRECTION_UP_LEFT` (value: `"EXPANDING_DIRECTION_UP_LEFT"`)

* `EXPANDING_DIRECTION_UP_RIGHT` (value: `"EXPANDING_DIRECTION_UP_RIGHT"`)

* `EXPANDING_DIRECTION_DOWN_LEFT` (value: `"EXPANDING_DIRECTION_DOWN_LEFT"`)

* `EXPANDING_DIRECTION_DOWN_RIGHT` (value: `"EXPANDING_DIRECTION_DOWN_RIGHT"`)

* `CREATIVE_TYPE_HTML` (value: `"CREATIVE_TYPE_HTML"`)

* `CREATIVE_TYPE_VAST_VIDEO` (value: `"CREATIVE_TYPE_VAST_VIDEO"`)

* `EXPANDING_DIRECTION_UP_OR_DOWN` (value: `"EXPANDING_DIRECTION_UP_OR_DOWN"`)

* `EXPANDING_DIRECTION_LEFT_OR_RIGHT` (value: `"EXPANDING_DIRECTION_LEFT_OR_RIGHT"`)

* `EXPANDING_DIRECTION_ANY_DIAGONAL` (value: `"EXPANDING_DIRECTION_ANY_DIAGONAL"`)

* `EXPANDING_ACTION_ROLLOVER_TO_EXPAND` (value: `"EXPANDING_ACTION_ROLLOVER_TO_EXPAND"`)

* `INSTREAM_VAST_VIDEO_TYPE_VPAID_FLASH` (value: `"INSTREAM_VAST_VIDEO_TYPE_VPAID_FLASH"`)

* `RICH_MEDIA_CAPABILITY_TYPE_MRAID` (value: `"RICH_MEDIA_CAPABILITY_TYPE_MRAID"`)

* `RICH_MEDIA_CAPABILITY_TYPE_FLASH` (value: `"RICH_MEDIA_CAPABILITY_TYPE_FLASH"`)

* `RICH_MEDIA_CAPABILITY_TYPE_HTML5` (value: `"RICH_MEDIA_CAPABILITY_TYPE_HTML5"`)

* `SKIPPABLE_INSTREAM_VIDEO` (value: `"SKIPPABLE_INSTREAM_VIDEO"`)

* `RICH_MEDIA_CAPABILITY_TYPE_SSL` (value: `"RICH_MEDIA_CAPABILITY_TYPE_SSL"`)

* `RICH_MEDIA_CAPABILITY_TYPE_NON_SSL` (value: `"RICH_MEDIA_CAPABILITY_TYPE_NON_SSL"`)

* `RICH_MEDIA_CAPABILITY_TYPE_INTERSTITIAL` (value: `"RICH_MEDIA_CAPABILITY_TYPE_INTERSTITIAL"`)

* `NON_SKIPPABLE_INSTREAM_VIDEO` (value: `"NON_SKIPPABLE_INSTREAM_VIDEO"`)

* `NATIVE_ELIGIBILITY_ELIGIBLE` (value: `"NATIVE_ELIGIBILITY_ELIGIBLE"`)

* `NON_VPAID` (value: `"NON_VPAID"`)

* `NATIVE_ELIGIBILITY_NOT_ELIGIBLE` (value: `"NATIVE_ELIGIBILITY_NOT_ELIGIBLE"`)

* `ANY_INTERSTITIAL` (value: `"ANY_INTERSTITIAL"`)

* `NON_INTERSTITIAL` (value: `"NON_INTERSTITIAL"`)

* `IN_BANNER_VIDEO` (value: `"IN_BANNER_VIDEO"`)

* `RENDERING_SIZELESS_ADX` (value: `"RENDERING_SIZELESS_ADX"`)

* `OMSDK_1_0` (value: `"OMSDK_1_0"`)

* `RENDERING_PLAYABLE` (value: `"RENDERING_PLAYABLE"`)




