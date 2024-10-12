# RealTimeBiddingApi.Creative

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Output only. ID of the buyer account that this creative is owned by. Can be used to filter the response of the creatives.list method with equality and inequality check. | [optional] [readonly] 
**adChoicesDestinationUrl** | **String** | The link to AdChoices destination page. This is only supported for native ads. | [optional] 
**advertiserName** | **String** | The name of the company being advertised in the creative. Can be used to filter the response of the creatives.list method. | [optional] 
**agencyId** | **String** | The agency ID for this creative. | [optional] 
**apiUpdateTime** | **String** | Output only. The last update timestamp of the creative through the API. | [optional] [readonly] 
**creativeFormat** | **String** | Output only. The format of this creative. Can be used to filter the response of the creatives.list method. | [optional] [readonly] 
**creativeId** | **String** | Buyer-specific creative ID that references this creative in bid responses. This field is Ignored in update operations. Can be used to filter the response of the creatives.list method. The maximum length of the creative ID is 128 bytes. | [optional] 
**creativeServingDecision** | [**CreativeServingDecision**](CreativeServingDecision.md) |  | [optional] 
**dealIds** | **[String]** | Output only. IDs of all of the deals with which this creative has been used in bidding. Can be used to filter the response of the creatives.list method. | [optional] [readonly] 
**declaredAttributes** | **[String]** | All declared attributes for the ads that may be shown from this creative. Can be used to filter the response of the creatives.list method. If the &#x60;excluded_attribute&#x60; field of a [bid request](https://developers.google.com/authorized-buyers/rtb/downloads/realtime-bidding-proto\&quot;) contains one of the attributes that were declared or detected for a given creative, and a bid is submitted with that creative, the bid will be filtered before the auction. | [optional] 
**declaredClickThroughUrls** | **[String]** | The set of declared destination URLs for the creative. Can be used to filter the response of the creatives.list method. | [optional] 
**declaredRestrictedCategories** | **[String]** | All declared restricted categories for the ads that may be shown from this creative. Can be used to filter the response of the creatives.list method. | [optional] 
**declaredVendorIds** | **[Number]** | IDs for the declared ad technology vendors that may be used by this creative. See https://storage.googleapis.com/adx-rtb-dictionaries/vendors.txt for possible values. Can be used to filter the response of the creatives.list method. | [optional] 
**html** | [**HtmlContent**](HtmlContent.md) |  | [optional] 
**impressionTrackingUrls** | **[String]** | The set of URLs to be called to record an impression. | [optional] 
**name** | **String** | Output only. Name of the creative. Follows the pattern &#x60;buyers/{buyer}/creatives/{creative}&#x60;, where &#x60;{buyer}&#x60; represents the account ID of the buyer who owns the creative, and &#x60;{creative}&#x60; is the buyer-specific creative ID that references this creative in the bid response. | [optional] [readonly] 
**_native** | [**NativeContent**](NativeContent.md) |  | [optional] 
**renderUrl** | **String** | Experimental field that can be used during the [FLEDGE Origin Trial](/authorized-buyers/rtb/fledge-origin-trial). The URL to fetch an interest group ad used in [TURTLEDOVE on-device auction](https://github.com/WICG/turtledove/blob/main/FLEDGE.md#1-browsers-record-interest-groups\&quot;). This should be unique among all creatives for a given &#x60;accountId&#x60;. This URL should be the same as the URL returned by [generateBid()](https://github.com/WICG/turtledove/blob/main/FLEDGE.md#32-on-device-bidding). | [optional] 
**restrictedCategories** | **[String]** | All restricted categories for the ads that may be shown from this creative. | [optional] 
**version** | **Number** | Output only. The version of the creative. Version for a new creative is 1 and it increments during subsequent creative updates. | [optional] [readonly] 
**video** | [**VideoContent**](VideoContent.md) |  | [optional] 



## Enum: CreativeFormatEnum


* `CREATIVE_FORMAT_UNSPECIFIED` (value: `"CREATIVE_FORMAT_UNSPECIFIED"`)

* `HTML` (value: `"HTML"`)

* `VIDEO` (value: `"VIDEO"`)

* `NATIVE` (value: `"NATIVE"`)





## Enum: [DeclaredAttributesEnum]


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





## Enum: [DeclaredRestrictedCategoriesEnum]


* `RESTRICTED_CATEGORY_UNSPECIFIED` (value: `"RESTRICTED_CATEGORY_UNSPECIFIED"`)

* `ALCOHOL` (value: `"ALCOHOL"`)





## Enum: [RestrictedCategoriesEnum]


* `RESTRICTED_CATEGORY_UNSPECIFIED` (value: `"RESTRICTED_CATEGORY_UNSPECIFIED"`)

* `ALCOHOL` (value: `"ALCOHOL"`)




