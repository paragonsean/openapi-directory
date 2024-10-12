# AdExchangeBuyerApiIi.Creative

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account that this creative belongs to. Can be used to filter the response of the creatives.list method. | [optional] 
**adChoicesDestinationUrl** | **String** | The link to AdChoices destination page. | [optional] 
**adTechnologyProviders** | [**AdTechnologyProviders**](AdTechnologyProviders.md) |  | [optional] 
**advertiserName** | **String** | The name of the company being advertised in the creative. | [optional] 
**agencyId** | **String** | The agency ID for this creative. | [optional] 
**apiUpdateTime** | **String** | Output only. The last update timestamp of the creative through the API. | [optional] 
**attributes** | **[String]** | All attributes for the ads that may be shown from this creative. Can be used to filter the response of the creatives.list method. | [optional] 
**clickThroughUrls** | **[String]** | The set of destination URLs for the creative. | [optional] 
**corrections** | [**[Correction]**](Correction.md) | Output only. Shows any corrections that were applied to this creative. | [optional] 
**creativeId** | **String** | The buyer-defined creative ID of this creative. Can be used to filter the response of the creatives.list method. | [optional] 
**dealsStatus** | **String** | Output only. The top-level deals status of this creative. If disapproved, an entry for &#39;auctionType&#x3D;DIRECT_DEALS&#39; (or &#39;ALL&#39;) in serving_restrictions will also exist. Note that this may be nuanced with other contextual restrictions, in which case, it may be preferable to read from serving_restrictions directly. Can be used to filter the response of the creatives.list method. | [optional] 
**declaredClickThroughUrls** | **[String]** | The set of declared destination URLs for the creative. | [optional] 
**detectedAdvertiserIds** | **[String]** | Output only. Detected advertiser IDs, if any. | [optional] 
**detectedDomains** | **[String]** | Output only. The detected domains for this creative. | [optional] 
**detectedLanguages** | **[String]** | Output only. The detected languages for this creative. The order is arbitrary. The codes are 2 or 5 characters and are documented at https://developers.google.com/adwords/api/docs/appendix/languagecodes. | [optional] 
**detectedProductCategories** | **[Number]** | Output only. Detected product categories, if any. See the ad-product-categories.txt file in the technical documentation for a list of IDs. | [optional] 
**detectedSensitiveCategories** | **[Number]** | Output only. Detected sensitive categories, if any. See the ad-sensitive-categories.txt file in the technical documentation for a list of IDs. You should use these IDs along with the excluded-sensitive-category field in the bid request to filter your bids. | [optional] 
**html** | [**HtmlContent**](HtmlContent.md) |  | [optional] 
**impressionTrackingUrls** | **[String]** | The set of URLs to be called to record an impression. | [optional] 
**_native** | [**NativeContent**](NativeContent.md) |  | [optional] 
**openAuctionStatus** | **String** | Output only. The top-level open auction status of this creative. If disapproved, an entry for &#39;auctionType &#x3D; OPEN_AUCTION&#39; (or &#39;ALL&#39;) in serving_restrictions will also exist. Note that this may be nuanced with other contextual restrictions, in which case, it may be preferable to read from serving_restrictions directly. Can be used to filter the response of the creatives.list method. | [optional] 
**restrictedCategories** | **[String]** | All restricted categories for the ads that may be shown from this creative. | [optional] 
**servingRestrictions** | [**[ServingRestriction]**](ServingRestriction.md) | Output only. The granular status of this ad in specific contexts. A context here relates to where something ultimately serves (for example, a physical location, a platform, an HTTPS versus HTTP request, or the type of auction). | [optional] 
**vendorIds** | **[Number]** | All vendor IDs for the ads that may be shown from this creative. See https://storage.googleapis.com/adx-rtb-dictionaries/vendors.txt for possible values. | [optional] 
**version** | **Number** | Output only. The version of this creative. | [optional] 
**video** | [**VideoContent**](VideoContent.md) |  | [optional] 



## Enum: [AttributesEnum]


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





## Enum: DealsStatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `NOT_CHECKED` (value: `"NOT_CHECKED"`)

* `CONDITIONALLY_APPROVED` (value: `"CONDITIONALLY_APPROVED"`)

* `APPROVED` (value: `"APPROVED"`)

* `DISAPPROVED` (value: `"DISAPPROVED"`)

* `PENDING_REVIEW` (value: `"PENDING_REVIEW"`)

* `STATUS_TYPE_UNSPECIFIED` (value: `"STATUS_TYPE_UNSPECIFIED"`)





## Enum: OpenAuctionStatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `NOT_CHECKED` (value: `"NOT_CHECKED"`)

* `CONDITIONALLY_APPROVED` (value: `"CONDITIONALLY_APPROVED"`)

* `APPROVED` (value: `"APPROVED"`)

* `DISAPPROVED` (value: `"DISAPPROVED"`)

* `PENDING_REVIEW` (value: `"PENDING_REVIEW"`)

* `STATUS_TYPE_UNSPECIFIED` (value: `"STATUS_TYPE_UNSPECIFIED"`)





## Enum: [RestrictedCategoriesEnum]


* `NO_RESTRICTED_CATEGORIES` (value: `"NO_RESTRICTED_CATEGORIES"`)

* `ALCOHOL` (value: `"ALCOHOL"`)




