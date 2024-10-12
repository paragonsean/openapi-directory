# CampaignManager360Api.AdSlot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | Comment for this ad slot. | [optional] 
**compatibility** | **String** | Ad slot compatibility. DISPLAY and DISPLAY_INTERSTITIAL refer to rendering either on desktop, mobile devices or in mobile apps for regular or interstitial ads respectively. APP and APP_INTERSTITIAL are for rendering in mobile apps. IN_STREAM_VIDEO refers to rendering in in-stream video ads developed with the VAST standard. | [optional] 
**height** | **String** | Height of this ad slot. | [optional] 
**linkedPlacementId** | **String** | ID of the placement from an external platform that is linked to this ad slot. | [optional] 
**name** | **String** | Name of this ad slot. | [optional] 
**paymentSourceType** | **String** | Payment source type of this ad slot. | [optional] 
**primary** | **Boolean** | Primary ad slot of a roadblock inventory item. | [optional] 
**width** | **String** | Width of this ad slot. | [optional] 



## Enum: CompatibilityEnum


* `DISPLAY` (value: `"DISPLAY"`)

* `DISPLAY_INTERSTITIAL` (value: `"DISPLAY_INTERSTITIAL"`)

* `APP` (value: `"APP"`)

* `APP_INTERSTITIAL` (value: `"APP_INTERSTITIAL"`)

* `IN_STREAM_VIDEO` (value: `"IN_STREAM_VIDEO"`)

* `IN_STREAM_AUDIO` (value: `"IN_STREAM_AUDIO"`)





## Enum: PaymentSourceTypeEnum


* `AGENCY_PAID` (value: `"PLANNING_PAYMENT_SOURCE_TYPE_AGENCY_PAID"`)

* `PUBLISHER_PAID` (value: `"PLANNING_PAYMENT_SOURCE_TYPE_PUBLISHER_PAID"`)




