

# YoutubeAndPartnersSettings

Settings for YouTube and Partners line items.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**biddingStrategy** | [**YoutubeAndPartnersBiddingStrategy**](YoutubeAndPartnersBiddingStrategy.md) |  |  [optional] |
|**contentCategory** | [**ContentCategoryEnum**](#ContentCategoryEnum) | The kind of content on which the YouTube and Partners ads will be shown. |  [optional] |
|**effectiveContentCategory** | [**EffectiveContentCategoryEnum**](#EffectiveContentCategoryEnum) | Output only. The content category which takes effect when serving the line item. When content category is set in both line item and advertiser, the stricter one will take effect when serving the line item. |  [optional] [readonly] |
|**inventorySourceSettings** | [**YoutubeAndPartnersInventorySourceConfig**](YoutubeAndPartnersInventorySourceConfig.md) |  |  [optional] |
|**leadFormId** | **String** | Optional. The ID of the form to generate leads. |  [optional] |
|**linkedMerchantId** | **String** | Optional. The ID of the merchant which is linked to the line item for product feed. |  [optional] |
|**relatedVideoIds** | **List&lt;String&gt;** | Optional. The IDs of the videos appear below the primary video ad when the ad is playing in the YouTube app on mobile devices. |  [optional] |
|**targetFrequency** | [**TargetFrequency**](TargetFrequency.md) |  |  [optional] |
|**thirdPartyMeasurementSettings** | [**YoutubeAndPartnersThirdPartyMeasurementSettings**](YoutubeAndPartnersThirdPartyMeasurementSettings.md) |  |  [optional] |
|**videoAdSequenceSettings** | [**VideoAdSequenceSettings**](VideoAdSequenceSettings.md) |  |  [optional] |
|**viewFrequencyCap** | [**FrequencyCap**](FrequencyCap.md) |  |  [optional] |



## Enum: ContentCategoryEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_UNSPECIFIED&quot; |
| STANDARD | &quot;YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_STANDARD&quot; |
| EXPANDED | &quot;YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_EXPANDED&quot; |
| LIMITED | &quot;YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_LIMITED&quot; |



## Enum: EffectiveContentCategoryEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_UNSPECIFIED&quot; |
| STANDARD | &quot;YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_STANDARD&quot; |
| EXPANDED | &quot;YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_EXPANDED&quot; |
| LIMITED | &quot;YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_LIMITED&quot; |



