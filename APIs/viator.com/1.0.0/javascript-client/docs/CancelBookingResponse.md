# ViatorApiDocumentationAmpSpecificationMerchantPartners.CancelBookingResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookingId** | **String** | Booking reference number for this booking, prepended with &#x60;BR-&#x60; | [optional] 
**reason** | **String** |  | [optional] 
**status** | **String** | String indicating the outcome of the booking cancellation request.    * &#x60;ACCEPTED&#x60;: The cancellation was successful   * &#x60;DECLINED&#x60;: The cancellation failed  | [optional] 



## Enum: ReasonEnum


* `ALREADY_CANCELLED` (value: `"ALREADY_CANCELLED"`)

* `NOT_CANCELLABLE` (value: `"NOT_CANCELLABLE"`)





## Enum: StatusEnum


* `ACCEPTED` (value: `"ACCEPTED"`)

* `DECLINED` (value: `"DECLINED"`)




