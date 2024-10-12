

# Creative

A creative and its classification data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Output only. ID of the buyer account that this creative is owned by. Can be used to filter the response of the creatives.list method with equality and inequality check. |  [optional] [readonly] |
|**adChoicesDestinationUrl** | **String** | The link to AdChoices destination page. This is only supported for native ads. |  [optional] |
|**advertiserName** | **String** | The name of the company being advertised in the creative. Can be used to filter the response of the creatives.list method. |  [optional] |
|**agencyId** | **String** | The agency ID for this creative. |  [optional] |
|**apiUpdateTime** | **String** | Output only. The last update timestamp of the creative through the API. |  [optional] [readonly] |
|**creativeFormat** | [**CreativeFormatEnum**](#CreativeFormatEnum) | Output only. The format of this creative. Can be used to filter the response of the creatives.list method. |  [optional] [readonly] |
|**creativeId** | **String** | Buyer-specific creative ID that references this creative in bid responses. This field is Ignored in update operations. Can be used to filter the response of the creatives.list method. The maximum length of the creative ID is 128 bytes. |  [optional] |
|**creativeServingDecision** | [**CreativeServingDecision**](CreativeServingDecision.md) |  |  [optional] |
|**dealIds** | **List&lt;String&gt;** | Output only. IDs of all of the deals with which this creative has been used in bidding. Can be used to filter the response of the creatives.list method. |  [optional] [readonly] |
|**declaredAttributes** | [**List&lt;DeclaredAttributesEnum&gt;**](#List&lt;DeclaredAttributesEnum&gt;) | All declared attributes for the ads that may be shown from this creative. Can be used to filter the response of the creatives.list method. If the &#x60;excluded_attribute&#x60; field of a [bid request](https://developers.google.com/authorized-buyers/rtb/downloads/realtime-bidding-proto\&quot;) contains one of the attributes that were declared or detected for a given creative, and a bid is submitted with that creative, the bid will be filtered before the auction. |  [optional] |
|**declaredClickThroughUrls** | **List&lt;String&gt;** | The set of declared destination URLs for the creative. Can be used to filter the response of the creatives.list method. |  [optional] |
|**declaredRestrictedCategories** | [**List&lt;DeclaredRestrictedCategoriesEnum&gt;**](#List&lt;DeclaredRestrictedCategoriesEnum&gt;) | All declared restricted categories for the ads that may be shown from this creative. Can be used to filter the response of the creatives.list method. |  [optional] |
|**declaredVendorIds** | **List&lt;Integer&gt;** | IDs for the declared ad technology vendors that may be used by this creative. See https://storage.googleapis.com/adx-rtb-dictionaries/vendors.txt for possible values. Can be used to filter the response of the creatives.list method. |  [optional] |
|**html** | [**HtmlContent**](HtmlContent.md) |  |  [optional] |
|**impressionTrackingUrls** | **List&lt;String&gt;** | The set of URLs to be called to record an impression. |  [optional] |
|**name** | **String** | Output only. Name of the creative. Follows the pattern &#x60;buyers/{buyer}/creatives/{creative}&#x60;, where &#x60;{buyer}&#x60; represents the account ID of the buyer who owns the creative, and &#x60;{creative}&#x60; is the buyer-specific creative ID that references this creative in the bid response. |  [optional] [readonly] |
|**_native** | [**NativeContent**](NativeContent.md) |  |  [optional] |
|**renderUrl** | **String** | Experimental field that can be used during the [FLEDGE Origin Trial](/authorized-buyers/rtb/fledge-origin-trial). The URL to fetch an interest group ad used in [TURTLEDOVE on-device auction](https://github.com/WICG/turtledove/blob/main/FLEDGE.md#1-browsers-record-interest-groups\&quot;). This should be unique among all creatives for a given &#x60;accountId&#x60;. This URL should be the same as the URL returned by [generateBid()](https://github.com/WICG/turtledove/blob/main/FLEDGE.md#32-on-device-bidding). |  [optional] |
|**restrictedCategories** | [**List&lt;RestrictedCategoriesEnum&gt;**](#List&lt;RestrictedCategoriesEnum&gt;) | All restricted categories for the ads that may be shown from this creative. |  [optional] |
|**version** | **Integer** | Output only. The version of the creative. Version for a new creative is 1 and it increments during subsequent creative updates. |  [optional] [readonly] |
|**video** | [**VideoContent**](VideoContent.md) |  |  [optional] |



## Enum: CreativeFormatEnum

| Name | Value |
|---- | -----|
| CREATIVE_FORMAT_UNSPECIFIED | &quot;CREATIVE_FORMAT_UNSPECIFIED&quot; |
| HTML | &quot;HTML&quot; |
| VIDEO | &quot;VIDEO&quot; |
| NATIVE | &quot;NATIVE&quot; |



## Enum: List&lt;DeclaredAttributesEnum&gt;

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



## Enum: List&lt;DeclaredRestrictedCategoriesEnum&gt;

| Name | Value |
|---- | -----|
| RESTRICTED_CATEGORY_UNSPECIFIED | &quot;RESTRICTED_CATEGORY_UNSPECIFIED&quot; |
| ALCOHOL | &quot;ALCOHOL&quot; |



## Enum: List&lt;RestrictedCategoriesEnum&gt;

| Name | Value |
|---- | -----|
| RESTRICTED_CATEGORY_UNSPECIFIED | &quot;RESTRICTED_CATEGORY_UNSPECIFIED&quot; |
| ALCOHOL | &quot;ALCOHOL&quot; |



