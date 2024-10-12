

# Creative

A creative and its classification data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The account that this creative belongs to. Can be used to filter the response of the creatives.list method. |  [optional] |
|**adChoicesDestinationUrl** | **String** | The link to AdChoices destination page. |  [optional] |
|**adTechnologyProviders** | [**AdTechnologyProviders**](AdTechnologyProviders.md) |  |  [optional] |
|**advertiserName** | **String** | The name of the company being advertised in the creative. |  [optional] |
|**agencyId** | **String** | The agency ID for this creative. |  [optional] |
|**apiUpdateTime** | **String** | Output only. The last update timestamp of the creative through the API. |  [optional] |
|**attributes** | [**List&lt;AttributesEnum&gt;**](#List&lt;AttributesEnum&gt;) | All attributes for the ads that may be shown from this creative. Can be used to filter the response of the creatives.list method. |  [optional] |
|**clickThroughUrls** | **List&lt;String&gt;** | The set of destination URLs for the creative. |  [optional] |
|**corrections** | [**List&lt;Correction&gt;**](Correction.md) | Output only. Shows any corrections that were applied to this creative. |  [optional] |
|**creativeId** | **String** | The buyer-defined creative ID of this creative. Can be used to filter the response of the creatives.list method. |  [optional] |
|**dealsStatus** | [**DealsStatusEnum**](#DealsStatusEnum) | Output only. The top-level deals status of this creative. If disapproved, an entry for &#39;auctionType&#x3D;DIRECT_DEALS&#39; (or &#39;ALL&#39;) in serving_restrictions will also exist. Note that this may be nuanced with other contextual restrictions, in which case, it may be preferable to read from serving_restrictions directly. Can be used to filter the response of the creatives.list method. |  [optional] |
|**declaredClickThroughUrls** | **List&lt;String&gt;** | The set of declared destination URLs for the creative. |  [optional] |
|**detectedAdvertiserIds** | **List&lt;String&gt;** | Output only. Detected advertiser IDs, if any. |  [optional] |
|**detectedDomains** | **List&lt;String&gt;** | Output only. The detected domains for this creative. |  [optional] |
|**detectedLanguages** | **List&lt;String&gt;** | Output only. The detected languages for this creative. The order is arbitrary. The codes are 2 or 5 characters and are documented at https://developers.google.com/adwords/api/docs/appendix/languagecodes. |  [optional] |
|**detectedProductCategories** | **List&lt;Integer&gt;** | Output only. Detected product categories, if any. See the ad-product-categories.txt file in the technical documentation for a list of IDs. |  [optional] |
|**detectedSensitiveCategories** | **List&lt;Integer&gt;** | Output only. Detected sensitive categories, if any. See the ad-sensitive-categories.txt file in the technical documentation for a list of IDs. You should use these IDs along with the excluded-sensitive-category field in the bid request to filter your bids. |  [optional] |
|**html** | [**HtmlContent**](HtmlContent.md) |  |  [optional] |
|**impressionTrackingUrls** | **List&lt;String&gt;** | The set of URLs to be called to record an impression. |  [optional] |
|**_native** | [**NativeContent**](NativeContent.md) |  |  [optional] |
|**openAuctionStatus** | [**OpenAuctionStatusEnum**](#OpenAuctionStatusEnum) | Output only. The top-level open auction status of this creative. If disapproved, an entry for &#39;auctionType &#x3D; OPEN_AUCTION&#39; (or &#39;ALL&#39;) in serving_restrictions will also exist. Note that this may be nuanced with other contextual restrictions, in which case, it may be preferable to read from serving_restrictions directly. Can be used to filter the response of the creatives.list method. |  [optional] |
|**restrictedCategories** | [**List&lt;RestrictedCategoriesEnum&gt;**](#List&lt;RestrictedCategoriesEnum&gt;) | All restricted categories for the ads that may be shown from this creative. |  [optional] |
|**servingRestrictions** | [**List&lt;ServingRestriction&gt;**](ServingRestriction.md) | Output only. The granular status of this ad in specific contexts. A context here relates to where something ultimately serves (for example, a physical location, a platform, an HTTPS versus HTTP request, or the type of auction). |  [optional] |
|**vendorIds** | **List&lt;Integer&gt;** | All vendor IDs for the ads that may be shown from this creative. See https://storage.googleapis.com/adx-rtb-dictionaries/vendors.txt for possible values. |  [optional] |
|**version** | **Integer** | Output only. The version of this creative. |  [optional] |
|**video** | [**VideoContent**](VideoContent.md) |  |  [optional] |



## Enum: List&lt;AttributesEnum&gt;

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



## Enum: DealsStatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| NOT_CHECKED | &quot;NOT_CHECKED&quot; |
| CONDITIONALLY_APPROVED | &quot;CONDITIONALLY_APPROVED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| DISAPPROVED | &quot;DISAPPROVED&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| STATUS_TYPE_UNSPECIFIED | &quot;STATUS_TYPE_UNSPECIFIED&quot; |



## Enum: OpenAuctionStatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| NOT_CHECKED | &quot;NOT_CHECKED&quot; |
| CONDITIONALLY_APPROVED | &quot;CONDITIONALLY_APPROVED&quot; |
| APPROVED | &quot;APPROVED&quot; |
| DISAPPROVED | &quot;DISAPPROVED&quot; |
| PENDING_REVIEW | &quot;PENDING_REVIEW&quot; |
| STATUS_TYPE_UNSPECIFIED | &quot;STATUS_TYPE_UNSPECIFIED&quot; |



## Enum: List&lt;RestrictedCategoriesEnum&gt;

| Name | Value |
|---- | -----|
| NO_RESTRICTED_CATEGORIES | &quot;NO_RESTRICTED_CATEGORIES&quot; |
| ALCOHOL | &quot;ALCOHOL&quot; |



