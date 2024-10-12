

# CancelBookingResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookingId** | **String** | Booking reference number for this booking, prepended with &#x60;BR-&#x60; |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | String indicating the outcome of the booking cancellation request.    * &#x60;ACCEPTED&#x60;: The cancellation was successful   * &#x60;DECLINED&#x60;: The cancellation failed  |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| ALREADY_CANCELLED | &quot;ALREADY_CANCELLED&quot; |
| NOT_CANCELLABLE | &quot;NOT_CANCELLABLE&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;ACCEPTED&quot; |
| DECLINED | &quot;DECLINED&quot; |



