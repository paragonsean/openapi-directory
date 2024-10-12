# ViatorApiDocumentationAmpSpecificationMerchantPartners.CancelBookingQuoteResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookingId** | **String** | The booking reference number, prepended with &#x60;BR-&#x60; | [optional] 
**refundDetails** | [**RefundDetails**](RefundDetails.md) |  | [optional] 
**status** | **String** | String indicating the cancellation status of this itinerary item:    * &#x60;CANCELLABLE&#x60; - this booking is available to be cancelled   * &#x60;CANCELLED&#x60; - this booking has already been cancelled   * &#x60;NOT_CANCELLABLE&#x60; - this booking cannot be cancelled (because the product&#39;s operation date is now in the past)  | [optional] 



## Enum: StatusEnum


* `CANCELLABLE` (value: `"CANCELLABLE"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `NOT_CANCELLABLE` (value: `"NOT_CANCELLABLE"`)




