# DisplayVideo360Api.YoutubeAndPartnersSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentCategory** | **String** | The kind of content on which the YouTube and Partners ads will be shown. | [optional] 
**effectiveContentCategory** | **String** | Output only. The content category which takes effect when serving the line item. When content category is set in both line item and advertiser, the stricter one will take effect when serving the line item. | [optional] [readonly] 
**inventorySourceSettings** | [**YoutubeAndPartnersInventorySourceConfig**](YoutubeAndPartnersInventorySourceConfig.md) |  | [optional] 
**leadFormId** | **String** | Optional. The ID of the form to generate leads. | [optional] 
**linkedMerchantId** | **String** | Optional. The ID of the merchant which is linked to the line item for product feed. | [optional] 
**relatedVideoIds** | **[String]** | Optional. The IDs of the videos appear below the primary video ad when the ad is playing in the YouTube app on mobile devices. | [optional] 
**targetFrequency** | [**TargetFrequency**](TargetFrequency.md) |  | [optional] 
**thirdPartyMeasurementConfigs** | [**ThirdPartyMeasurementConfigs**](ThirdPartyMeasurementConfigs.md) |  | [optional] 
**videoAdSequenceSettings** | [**VideoAdSequenceSettings**](VideoAdSequenceSettings.md) |  | [optional] 
**viewFrequencyCap** | [**FrequencyCap**](FrequencyCap.md) |  | [optional] 



## Enum: ContentCategoryEnum


* `UNSPECIFIED` (value: `"YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_UNSPECIFIED"`)

* `STANDARD` (value: `"YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_STANDARD"`)

* `EXPANDED` (value: `"YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_EXPANDED"`)

* `LIMITED` (value: `"YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_LIMITED"`)





## Enum: EffectiveContentCategoryEnum


* `UNSPECIFIED` (value: `"YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_UNSPECIFIED"`)

* `STANDARD` (value: `"YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_STANDARD"`)

* `EXPANDED` (value: `"YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_EXPANDED"`)

* `LIMITED` (value: `"YOUTUBE_AND_PARTNERS_CONTENT_CATEGORY_LIMITED"`)




