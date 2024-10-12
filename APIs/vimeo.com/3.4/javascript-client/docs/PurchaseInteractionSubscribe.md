# Vimeo.PurchaseInteractionSubscribe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drm** | **Boolean** | Whether the On Demand subscription has DRM. | [optional] 
**expiresTime** | **String** | The time in ISO 8601 format when the On Demand video will expire. | [optional] 
**link** | **String** | The URL to purchase this On Demand subscription on Vimeo. | [optional] 
**purchaseTime** | **String** | The time in ISO 8601 format when the On Demand was purchased. | [optional] 
**stream** | **String** | The user&#39;s streaming access to this On Demand subscription:  Option descriptions:  * &#x60;available&#x60; - The On Demand subscription is available for streaming.  * &#x60;purchased&#x60; - The On Demand subscription has been purchased.  * &#x60;restricted&#x60; - Streaming for the On Demand subscription is restricted.  * &#x60;unavailable&#x60; - The On Demand subscription is unavailable.  | [optional] 
**uri** | **String** | The On Demand subscription&#39;s product URI. | [optional] 



## Enum: StreamEnum


* `available` (value: `"available"`)

* `purchased` (value: `"purchased"`)

* `restricted` (value: `"restricted"`)

* `unavailable` (value: `"unavailable"`)




