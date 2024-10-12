

# AdSlot

Ad Slot

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | Comment for this ad slot. |  [optional] |
|**compatibility** | [**CompatibilityEnum**](#CompatibilityEnum) | Ad slot compatibility. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop, mobile devices or in mobile apps for regular or interstitial ads respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. |  [optional] |
|**height** | **String** | Height of this ad slot. |  [optional] |
|**linkedPlacementId** | **String** | ID of the placement from an external platform that is linked to this ad slot. |  [optional] |
|**name** | **String** | Name of this ad slot. |  [optional] |
|**paymentSourceType** | [**PaymentSourceTypeEnum**](#PaymentSourceTypeEnum) | Payment source type of this ad slot. |  [optional] |
|**primary** | **Boolean** | Primary ad slot of a roadblock inventory item. |  [optional] |
|**width** | **String** | Width of this ad slot. |  [optional] |



## Enum: CompatibilityEnum

| Name | Value |
|---- | -----|
| DISPLAY | &quot;DISPLAY&quot; |
| DISPLAY_INTERSTITIAL | &quot;DISPLAY_INTERSTITIAL&quot; |
| APP | &quot;APP&quot; |
| APP_INTERSTITIAL | &quot;APP_INTERSTITIAL&quot; |
| IN_STREAM_VIDEO | &quot;IN_STREAM_VIDEO&quot; |
| IN_STREAM_AUDIO | &quot;IN_STREAM_AUDIO&quot; |



## Enum: PaymentSourceTypeEnum

| Name | Value |
|---- | -----|
| AGENCY_PAID | &quot;PLANNING_PAYMENT_SOURCE_TYPE_AGENCY_PAID&quot; |
| PUBLISHER_PAID | &quot;PLANNING_PAYMENT_SOURCE_TYPE_PUBLISHER_PAID&quot; |



